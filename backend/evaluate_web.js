const { JSDOM, VirtualConsole } = require('jsdom');
const fs = require('fs');

async function evaluate() {
    let payloadStr = '';
    for await (const chunk of process.stdin) {
        payloadStr += chunk;
    }
    
    if (!payloadStr) {
        console.error("No input provided.");
        process.exit(1);
    }

    const payload = JSON.parse(payloadStr);
    const { language, code, test_cases } = payload;
    const results = [];

    // Setup virtual console to capture student output
    const virtualConsole = new VirtualConsole();
    let actualStdout = '';
    let actualStderr = '';
    virtualConsole.on("log", (...args) => { actualStdout += args.join(' ') + '\n'; });
    virtualConsole.on("info", (...args) => { actualStdout += args.join(' ') + '\n'; });
    virtualConsole.on("warn", (...args) => { actualStderr += args.join(' ') + '\n'; });
    virtualConsole.on("error", (...args) => { actualStderr += args.join(' ') + '\n'; });
    virtualConsole.on("jsdomError", (e) => { actualStderr += e.message + '\n'; });

    let dom;
    
    try {
        if (language === 'html' || language === 'css') {
            let htmlContent = code;
            if (language === 'css') {
                htmlContent = `<!DOCTYPE html><html><head><style>${code}</style></head><body></body></html>`;
            }
            dom = new JSDOM(htmlContent, {
                runScripts: "outside-only",
                virtualConsole
            });
        } else if (language === 'javascript') {
            // For JavaScript, we need a basic DOM to run it in
            const htmlContent = `<!DOCTYPE html><html><head></head><body><div id="app"></div></body></html>`;
            dom = new JSDOM(htmlContent, {
                runScripts: "dangerously",
                virtualConsole,
                beforeParse(window) {
                    // Mock basic browser APIs if needed, though jsdom provides most
                    window.fetch = async () => ({
                        json: async () => ({ mock: "data" }),
                        text: async () => "mock data"
                    });
                }
            });
            
            // Execute student code
            try {
                const scriptEl = dom.window.document.createElement("script");
                scriptEl.textContent = code;
                dom.window.document.body.appendChild(scriptEl);
            } catch (e) {
                actualStderr += e.toString();
            }
        }
    } catch (e) {
        // If DOM creation fails, we fail all tests
        console.log(JSON.stringify(test_cases.map(tc => ({
            id: tc.id,
            passed: false,
            status: 'runtime_error',
            actual_stderr: e.message
        }))));
        process.exit(0);
    }

    // Now evaluate each test case
    for (const tc of test_cases) {
        const start = Date.now();
        let passed = false;
        let status = 'wrong_answer';
        let tcStderr = '';
        
        try {
            // The test logic is a JS function string returning boolean or throwing.
            // Example input_data: "return document.querySelectorAll('h1').length > 0;"
            // Or for JS console checks: "return actualStdout.includes('Hello');"
            
            // We run the test logic in the context of the DOM (or with access to it)
            // It's safer to run it outside the JSDOM context but passing the window object, 
            // so the test has full Node.js privileges (since we write the tests).
            const testFunc = new Function('window', 'document', 'actualStdout', 'actualStderr', tc.input_data);
            passed = testFunc(dom.window, dom.window.document, actualStdout, actualStderr);
            
            if (passed) {
                status = 'success';
            }
        } catch (e) {
            tcStderr = e.message;
            status = 'runtime_error';
            passed = false;
        }
        
        const execTime = Date.now() - start;
        results.push({
            id: tc.id,
            passed: passed,
            status: status,
            execution_time_ms: execTime,
            actual_stdout: actualStdout,
            actual_stderr: tcStderr || actualStderr
        });
    }

    console.log(JSON.stringify(results));
}

evaluate().catch(e => {
    console.error(e);
    process.exit(1);
});

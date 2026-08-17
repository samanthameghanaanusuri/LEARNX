// code-editor.js - LEARNX Phase 4 Secure Sandbox Frontend

class CodeEditor {
    constructor(containerId, options = {}) {
        this.container = document.getElementById(containerId);
        this.exercise = options.exercise || null;
        this.exerciseIndex = options.exerciseIndex !== undefined ? options.exerciseIndex : 0;
        this.totalExercises = options.totalExercises || 1;
        this.draftCode = options.draftCode;
        this.language = (this.exercise && this.exercise.language) || options.language || 'python';
        this.onCodeChange = options.onCodeChange || (() => {});
        this.onNavigate = options.onNavigate || (() => {});
        this.onComplete = options.onComplete || (() => {});
        
        this.render();
        this.attachEvents();
    }

    render() {
        if (!this.exercise) {
            this.container.innerHTML = `<div class="glass-panel text-center"><p>No exercise loaded.</p></div>`;
            return;
        }

        const diff = this.exercise.difficulty || 'Easy';
        let badgeColor = '#00c8ff';
        let badgeBg = 'rgba(0, 200, 255, 0.15)';
        if (diff.toLowerCase() === 'medium') {
            badgeColor = '#ffb703';
            badgeBg = 'rgba(255, 183, 3, 0.15)';
        } else if (diff.toLowerCase().includes('hard')) {
            badgeColor = '#ff4d6d';
            badgeBg = 'rgba(255, 77, 109, 0.15)';
        }

        const currentCode = this.draftCode !== undefined ? this.draftCode : (
            (this.exercise.user_submission && this.exercise.user_submission.code) 
            ? this.exercise.user_submission.code 
            : (this.exercise.starter_code || '')
        );

        // Build Public Test Cases Display
        let sampleCasesHtml = '';
        if (this.exercise.test_cases && this.exercise.test_cases.length > 0) {
            const publicCases = this.exercise.test_cases.filter(tc => !tc.is_hidden);
            if (publicCases.length > 0) {
                sampleCasesHtml = `
                    <div style="margin-top: 1.25rem; background: rgba(0,0,0,0.25); padding: 1rem; border-radius: 8px; border-left: 3px solid var(--color-primary);">
                        <h5 style="margin-top: 0; margin-bottom: 0.5rem; color: #fff; font-size: 14px;">Example Input & Expected Output:</h5>
                        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 0.75rem;">
                            ${publicCases.map((tc, idx) => `
                                <div style="background: rgba(0,0,0,0.3); padding: 0.5rem 0.75rem; border-radius: 6px; font-size: 13px;">
                                    <div style="color: var(--text-secondary); margin-bottom: 0.25rem;">Sample ${idx + 1}</div>
                                    ${tc.input_data ? `<div><strong>Input:</strong> <code style="color: #00c8ff;">${escapeHtml(tc.input_data.trim())}</code></div>` : ''}
                                    <div><strong>Expected:</strong> <code style="color: #00ff88;">${escapeHtml(tc.expected_output.trim())}</code></div>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                `;
            }
        }

        this.container.innerHTML = `
            <div class="code-editor-wrapper">
                <div class="editor-header flex-between" style="align-items: flex-start; margin-bottom: 1rem;">
                    <div>
                        <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.5rem;">
                            <span style="font-size: 13px; font-weight: 600; color: var(--text-secondary);">Exercise ${this.exerciseIndex + 1} of ${this.totalExercises}</span>
                            <span class="badge" style="background: ${badgeBg}; color: ${badgeColor}; font-size: 12px; font-weight: 600;">${diff.toUpperCase()}</span>
                        </div>
                        <h3 style="margin: 0; color: #fff;">${escapeHtml(this.exercise.title)}</h3>
                    </div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span style="font-size: 13px; color: var(--text-secondary);">Language:</span>
                        <select id="lang-select" class="form-input" disabled style="width: auto; background: rgba(0,0,0,0.5); cursor: not-allowed; font-weight: 600; text-transform: uppercase; padding: 0.3rem 0.6rem;">
                            <option value="${this.language}" selected>${this.language.toUpperCase()}</option>
                        </select>
                    </div>
                </div>
                
                <p class="exercise-desc" style="font-size: 15px; line-height: 1.6; color: var(--text-primary); margin-bottom: 1rem;">${this.exercise.description}</p>
                
                ${sampleCasesHtml}

                <div style="margin-top: 1.5rem;">
                    <textarea id="code-textarea" class="code-input form-input" spellcheck="false" rows="12" style="font-family: 'Fira Code', monospace; font-size: 14px; background: #0f172a; color: #f8fafc; border: 1px solid var(--border-card); border-radius: 8px; padding: 1rem; width: 100%; box-sizing: border-box;">${escapeHtml(currentCode)}</textarea>
                </div>
                
                <div class="editor-controls flex-between" style="margin-top: 1rem; gap: 0.5rem; flex-wrap: wrap;">
                    <div style="display: flex; gap: 0.5rem;">
                        <button class="btn btn-secondary" id="btn-run" style="font-weight: 600;">▶ Run Code</button>
                        <button class="btn btn-primary" id="btn-submit" style="font-weight: 600;">🚀 Submit Solution</button>
                        <button class="btn btn-secondary" id="btn-ai-review" style="font-weight: 600; color: #00ff88; border-color: rgba(0, 255, 136, 0.5);">🤖 AI Code Review</button>
                    </div>
                    <div style="display: flex; gap: 0.5rem;">
                        <button class="btn btn-secondary" id="btn-reset" style="font-size: 13px;">Reset</button>
                        <button class="btn btn-secondary" id="btn-clear" style="font-size: 13px;">Clear Output</button>
                    </div>
                </div>
                <div class="editor-panels" style="margin-top: 1.5rem; display: grid; grid-template-columns: 1fr; gap: 1rem;">
                    ${['html', 'css', 'javascript'].includes(this.language) ? `
                    <div class="panel glass-panel" style="padding: 1rem;">
                        <h4 style="margin-top: 0; margin-bottom: 0.5rem; color: #fff; font-size: 14px;">Live Preview</h4>
                        <div style="background: #fff; border-radius: 4px; overflow: hidden; border: 1px solid var(--border-card);">
                            <iframe id="web-preview-frame" style="width: 100%; height: 300px; border: none; background: white;" sandbox="allow-scripts allow-modals"></iframe>
                        </div>
                    </div>
                    ` : `
                    <div class="panel glass-panel" style="padding: 1rem;">
                        <h4 style="margin-top: 0; margin-bottom: 0.5rem; color: #fff; font-size: 14px;">Custom Input (stdin)</h4>
                        <textarea id="code-stdin" class="form-input" rows="3" placeholder="Enter custom input values to test with 'Run Code'..." style="font-family: monospace; font-size: 13px; width: 100%; box-sizing: border-box;"></textarea>
                    </div>
                    `}
                    
                    <div class="panel glass-panel" style="padding: 1rem;">
                        <h4 style="margin-top: 0; margin-bottom: 0.5rem; color: #fff; font-size: 14px;">Output Console</h4>
                        <div id="code-status" class="execution-status" style="margin-top: 0.25rem;"></div>
                        <pre id="code-stdout" class="terminal-output stdout" style="margin-top: 0.5rem; min-height: 40px;"></pre>
                        <pre id="code-stderr" class="terminal-output stderr" style="margin-top: 0.5rem; display: none;"></pre>
                        <div id="test-results" class="test-results-container" style="margin-top: 1rem;"></div>
                    </div>
                </div>

                <div class="navigation-footer flex-between" style="margin-top: 1.5rem; border-top: 1px solid var(--border-card); padding-top: 1.25rem;">
                    <button class="btn btn-secondary" id="btn-prev-ex" ${this.exerciseIndex === 0 ? 'disabled' : ''}>← Previous Exercise</button>
                    <span style="font-size: 13px; color: var(--text-secondary);">Progress: Exercise ${this.exerciseIndex + 1} / ${this.totalExercises}</span>
                    <button class="btn btn-secondary" id="btn-next-ex" ${this.exerciseIndex === this.totalExercises - 1 ? 'disabled' : ''}>Next Exercise →</button>
                </div>
            </div>
        `;
    }

    attachEvents() {
        if (!this.exercise) return;

        const textarea = document.getElementById('code-textarea');
        if (textarea) {
            textarea.addEventListener('keydown', (e) => {
                if (e.key === 'Tab') {
                    e.preventDefault();
                    const start = textarea.selectionStart;
                    const end = textarea.selectionEnd;
                    textarea.value = textarea.value.substring(0, start) + "    " + textarea.value.substring(end);
                    textarea.selectionStart = textarea.selectionEnd = start + 4;
                    this.onCodeChange(textarea.value);
                }
            });

            textarea.addEventListener('input', () => {
                this.onCodeChange(textarea.value);
            });

            textarea.addEventListener('paste', (e) => {
                e.preventDefault();
                alert("Copy/Paste is disabled to encourage active learning and typing.");
            });
            textarea.addEventListener('copy', (e) => {
                const selectedText = textarea.value.substring(textarea.selectionStart, textarea.selectionEnd);
                if (selectedText.length > 50) {
                     console.log("Large copy detected - deterrence active.");
                }
            });
        }

        const btnPrev = document.getElementById('btn-prev-ex');
        if (btnPrev) {
            btnPrev.addEventListener('click', () => {
                if (this.exerciseIndex > 0) {
                    this.onNavigate(this.exerciseIndex - 1);
                }
            });
        }

        const btnNext = document.getElementById('btn-next-ex');
        if (btnNext) {
            btnNext.addEventListener('click', () => {
                if (this.exerciseIndex < this.totalExercises - 1) {
                    this.onNavigate(this.exerciseIndex + 1);
                }
            });
        }

        const btnReset = document.getElementById('btn-reset');
        if (btnReset) {
            btnReset.addEventListener('click', () => {
                if (confirm('Are you sure you want to reset the code to the starter template?')) {
                    const starter = this.exercise ? this.exercise.starter_code : '';
                    textarea.value = starter;
                    this.onCodeChange(starter);
                    this.clearOutput();
                }
            });
        }

        const btnClear = document.getElementById('btn-clear');
        if (btnClear) {
            btnClear.addEventListener('click', () => {
                this.clearOutput();
            });
        }

        const btnAiReview = document.getElementById('btn-ai-review');
        if (btnAiReview) {
            btnAiReview.addEventListener('click', () => {
                if (typeof requestAICodeReview === 'function') {
                    const code = document.getElementById('code-textarea').value;
                    requestAICodeReview(this.language, code, this.exercise ? this.exercise.description : "Code problem");
                } else {
                    alert("AI Assistant script is not loaded properly.");
                }
            });
        }

        const btnRun = document.getElementById('btn-run');
        if (btnRun) {
            btnRun.addEventListener('click', async () => {
                const code = textarea.value;
                const lang = this.language;
                
                if (['html', 'css', 'javascript'].includes(lang)) {
                    this.setStatus('Preview updated', 'success');
                    this.clearOutput(false);
                    const iframe = document.getElementById('web-preview-frame');
                    if (iframe) {
                        const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
                        iframeDoc.open();
                        if (lang === 'html') {
                            iframeDoc.write(code);
                        } else if (lang === 'css') {
                            iframeDoc.write(`<style>${code}</style><div style="padding: 20px; font-family: sans-serif;"><h2>CSS Preview Active</h2><p>Your CSS is applied to this document. In a real project, this would style your HTML.</p><div class="preview-target" id="preview-target" style="padding: 20px; background: #eee; border-radius: 8px;">Preview Target Element</div></div>`);
                        } else if (lang === 'javascript') {
                            iframeDoc.write(`
                                <html><body>
                                <h2>JavaScript Output</h2>
                                <pre id="console-out" style="background: #111; color: #0f0; padding: 10px; border-radius: 5px; font-family: monospace;"></pre>
                                <script>
                                    (function(){
                                        var oldLog = console.log;
                                        console.log = function (message) {
                                            if (typeof message == 'object') {
                                                document.getElementById('console-out').innerHTML += (JSON && JSON.stringify ? JSON.stringify(message) : message) + '<br />';
                                            } else {
                                                document.getElementById('console-out').innerHTML += message + '<br />';
                                            }
                                            oldLog.apply(console, arguments);
                                        };
                                    })();
                                </script>
                                <script>${code}</script>
                                </body></html>
                            `);
                        }
                        iframeDoc.close();
                    }
                    return;
                }

                this.setStatus('Executing in sandbox...', 'neutral');
                this.clearOutput(false);
                
                const stdinInput = document.getElementById('code-stdin');
                const stdin = stdinInput ? stdinInput.value : '';
                
                try {
                    const res = await LEARNX_API.runCode(lang, code, stdin);
                    
                    if (res.status === 'success') {
                        this.setStatus(`✓ SUCCESS (${res.execution_time_ms} ms)`, 'success');
                    } else if (res.status === 'compile_error' || res.error_type === 'compile_error') {
                        const compileMsg = lang === 'java' 
                            ? 'Your Java code could not be compiled.' 
                            : 'Your code could not be compiled.';
                        this.setStatus(`COMPILE ERROR: ${compileMsg} (${res.execution_time_ms} ms)`, 'error');
                    } else if (res.status === 'runtime_error') {
                        this.setStatus(`RUNTIME ERROR: Your program compiled but failed during execution. (${res.execution_time_ms} ms)`, 'error');
                    } else if (res.status === 'timeout') {
                        this.setStatus(`TIMEOUT: Your program exceeded the execution time limit. (${res.execution_time_ms} ms)`, 'error');
                    } else {
                        this.setStatus(`Execution Error (${res.execution_time_ms} ms)`, 'error');
                    }
                    
                    const stdoutEl = document.getElementById('code-stdout');
                    const stderrEl = document.getElementById('code-stderr');
                    
                    stdoutEl.textContent = res.stdout || '';
                    if (res.stderr) {
                        stderrEl.style.display = 'block';
                        stderrEl.textContent = res.stderr;
                    } else {
                        stderrEl.style.display = 'none';
                        stderrEl.textContent = '';
                    }
                    
                } catch (error) {
                    this.setStatus('Network/API Error: Unable to execute your code. Please try again.', 'error');
                }
            });
        }

        const btnSubmit = document.getElementById('btn-submit');
        if (btnSubmit) {
            btnSubmit.addEventListener('click', async () => {
                if (!this.exercise) return;
                
                this.setStatus('Evaluating against test suite...', 'neutral');
                this.clearOutput(false);
                
                const code = textarea.value;
                
                try {
                    const res = await LEARNX_API.submitExercise(this.exercise.id, code);
                    
                    if (res.error) {
                        throw new Error(res.error);
                    }

                    const isFullyPassed = res.passed === res.total;
                    let statusLabel = isFullyPassed ? '✓ SUCCESS - ALL TESTS PASSED!' : '✗ TEST EVALUATION COMPLETED';
                    if (res.status === 'compile_error' || res.error_type === 'compile_error') {
                        statusLabel = 'COMPILE ERROR: Your code could not be compiled.';
                    } else if (res.status === 'runtime_error') {
                        statusLabel = 'RUNTIME ERROR: Your program compiled but failed during execution.';
                    } else if (res.status === 'wrong_answer') {
                        statusLabel = 'WRONG ANSWER: Your output does not match expected output.';
                    } else if (res.status === 'timeout') {
                        statusLabel = 'TIMEOUT: Execution time limit exceeded.';
                    }

                    const scorePct = Math.round(res.score * 100);
                    this.setStatus(`${statusLabel} | Score: ${res.passed}/${res.total} (${scorePct}%) - ${res.execution_time_ms} ms`, isFullyPassed ? 'success' : 'error');
                    
                    const resultsContainer = document.getElementById('test-results');
                    resultsContainer.innerHTML = '';

                    if (res.results && res.results.length > 0) {
                        res.results.forEach((tc, index) => {
                            const div = document.createElement('div');
                            div.className = `test-case-item ${tc.passed ? 'pass' : 'fail'}`;
                            
                            const isHidden = tc.is_hidden;
                            const tcName = isHidden ? `Hidden Test ${index + 1}` : `Test Case ${index + 1}`;
                            
                            let html = `
                                <div class="flex-between">
                                    <strong>${tcName}: ${tc.passed ? '✓ Passed' : '✗ Failed'}</strong>
                                    <span style="font-size: 12px; color: var(--text-secondary);">${tc.execution_time_ms} ms</span>
                                </div>
                            `;

                            if (!tc.passed && !isHidden) {
                                html += `
                                    <div class="tc-details" style="margin-top: 0.5rem; font-size: 13px;">
                                        ${tc.input !== undefined && tc.input !== null ? `<div><strong>Input:</strong> <pre>${escapeHtml(tc.input)}</pre></div>` : ''}
                                        ${tc.expected !== undefined ? `<div><strong>Expected Output:</strong> <pre>${escapeHtml(tc.expected)}</pre></div>` : ''}
                                        ${tc.actual_stdout !== undefined ? `<div><strong>Actual Output:</strong> <pre>${escapeHtml(tc.actual_stdout)}</pre></div>` : ''}
                                        ${tc.actual_stderr ? `<div><strong>Stderr:</strong> <pre>${escapeHtml(tc.actual_stderr)}</pre></div>` : ''}
                                    </div>
                                `;
                            } else if (!tc.passed && isHidden) {
                                html += `
                                    <div style="font-size: 12px; color: var(--color-danger); margin-top: 0.25rem;">
                                        Hidden test failed. (Inputs & Expected outputs are hidden for test integrity).
                                    </div>
                                `;
                            }

                            div.innerHTML = html;
                            resultsContainer.appendChild(div);
                        });
                    }

                    this.onComplete(res.score, res);
                    
                } catch (error) {
                    this.setStatus(`Network/API Error: ${error.message || 'Unable to submit your solution. Please try again.'}`, 'error');
                }
            });
        }
    }

    setStatus(text, type) {
        const el = document.getElementById('code-status');
        if (!el) return;
        el.textContent = text;
        el.className = `execution-status ${type}`;
    }

    clearOutput(clearStatus = true) {
        const stdoutEl = document.getElementById('code-stdout');
        const stderrEl = document.getElementById('code-stderr');
        const resultsContainer = document.getElementById('test-results');
        
        if (stdoutEl) stdoutEl.textContent = '';
        if (stderrEl) {
            stderrEl.textContent = '';
            stderrEl.style.display = 'none';
        }
        if (resultsContainer) resultsContainer.innerHTML = '';
        if (clearStatus) this.setStatus('', 'neutral');
    }
}

function escapeHtml(str) {
    if (typeof str !== 'string') return '';
    return str
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
}

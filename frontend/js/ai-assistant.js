/**
 * AI Learning Assistant Integration
 */

const aiCache = {}; // Simple in-memory cache
let isAiRequestRunning = false;
let aiAbortController = null;

function setAiLoadingState(isLoading) {
    isAiRequestRunning = isLoading;
    const buttons = document.querySelectorAll('#ai-assistant-panel button');
    buttons.forEach(btn => {
        // don't disable minimize/close buttons
        if (btn.id === 'ai-minimize-btn' || btn.id === 'ai-close-btn') return;
        
        btn.disabled = isLoading;
        if (isLoading) {
            btn.style.opacity = '0.5';
            btn.style.cursor = 'not-allowed';
        } else {
            btn.style.opacity = '1';
            btn.style.cursor = 'pointer';
        }
    });
    
    const inputField = document.getElementById('ai-custom-question');
    if (inputField) {
        inputField.disabled = isLoading;
    }
}

function scrollToBottom() {
    const responseArea = document.getElementById('ai-response-area');
    if (responseArea) {
        responseArea.scrollTo({
            top: responseArea.scrollHeight,
            behavior: 'smooth'
        });
    }
}

async function requestAI(actionType) {
    if (isAiRequestRunning) return; // Prevent duplicate requests
    
    const urlParams = new URLSearchParams(window.location.search);
    const courseId = urlParams.get('course_id') || urlParams.get('id');
    const lessonId = window.currentLessonId || null;
    const conceptName = window.currentConceptName || "Current Lesson Concept";
    
    const responseArea = document.getElementById('ai-response-area');
    
    let endpoint = `/ai/${actionType}`;
    let method = 'POST';
    let body = {
        course_id: courseId,
        lesson_id: lessonId
    };
    
    if (actionType === 'ask') {
        const inputField = document.getElementById('ai-custom-question');
        const question = inputField.value.trim();
        if (!question) {
            responseArea.innerHTML += '<div style="color: var(--color-warning); margin-bottom: 1rem; padding: 10px;">Please type a question first.</div>';
            scrollToBottom();
            return;
        }
        body.question = question;
        inputField.value = ''; // clear input
    } else if (actionType === 'explain') {
        body.concept = conceptName;
    } else if (actionType === 'hint') {
        if (!window.currentHintLevel) window.currentHintLevel = 1;
        if (window.currentHintLevel > 5) {
            responseArea.innerHTML += '<div style="color: var(--color-warning); margin-bottom: 1rem; padding: 10px;">Maximum hint level reached. Please try your best!</div>';
            scrollToBottom();
            return;
        }
        body.hint_level = window.currentHintLevel;
        window.currentHintLevel++;
    } else if (actionType === 'weaknesses' || actionType === 'recommendation' || actionType === 'learning-plan') {
        method = 'GET';
        body = null;
    }

    // Check cache for stateless requests
    const cacheKey = `${actionType}_${lessonId}_${conceptName}`;
    if (['explain', 'weaknesses', 'recommendation'].includes(actionType)) {
        if (aiCache[cacheKey] && (Date.now() - aiCache[cacheKey].timestamp < 300000)) {
            // Cache hit (5 min expiry)
            renderAIResponse(actionType, aiCache[cacheKey].data, responseArea);
            return;
        }
    }

    // Set loading state
    setAiLoadingState(true);
    const loadingId = 'loading-' + Date.now();
    responseArea.innerHTML += `<div id="${loadingId}" class="loading" style="margin-bottom: 1rem; padding: 10px; background: rgba(0,255,136,0.1); border-radius: 6px;">🧠 AI is analyzing your learning progress...</div>`;
    scrollToBottom();

    const t_request_start = performance.now();
    console.log(`[LATENCY] Frontend request start: 0ms`);

    aiAbortController = new AbortController();
    const timeoutId = setTimeout(() => aiAbortController.abort(), 30000); // 30 second timeout

    try {
        let fetchOptions = {
            method: method,
            headers: {
                'Content-Type': 'application/json',
                'X-Student-ID': localStorage.getItem('student_id') || ''
            },
            signal: aiAbortController.signal
        };
        
        if (body) {
            fetchOptions.body = JSON.stringify(body);
        }

        const response = await fetch(API_BASE + endpoint, fetchOptions);
        const t_backend_response = performance.now();
        console.log(`[LATENCY] Backend response received at: ${(t_backend_response - t_request_start).toFixed(2)}ms`);
        
        clearTimeout(timeoutId);
        
        const data = await response.json();
        const t_json_parsed = performance.now();
        console.log(`[LATENCY] JSON parsed at: ${(t_json_parsed - t_request_start).toFixed(2)}ms`);
        
        // Remove loading indicator
        const loadingEl = document.getElementById(loadingId);
        if (loadingEl) loadingEl.remove();

        if (!response.ok || data.success === false || data.available === false) {
            const errorMsg = data.message || data.error || 'AI is temporarily unavailable. Your learning progress is safe.';
            responseArea.innerHTML += `<div class="execution-status error" style="padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">${DOMPurify.sanitize(errorMsg)}</div>`;
        } else {
            // Cache the result if eligible
            if (['explain', 'weaknesses', 'recommendation'].includes(actionType)) {
                aiCache[cacheKey] = {
                    timestamp: Date.now(),
                    data: data
                };
            }
            renderAIResponse(actionType, data, responseArea);
            const t_rendered = performance.now();
            console.log(`[LATENCY] Frontend response rendered at: ${(t_rendered - t_request_start).toFixed(2)}ms`);
            if (data._debug_latency) {
                console.log(`[LATENCY BACKEND METRICS]`, data._debug_latency);
            }
        }
        
    } catch (error) {
        clearTimeout(timeoutId);
        const loadingEl = document.getElementById(loadingId);
        if (loadingEl) loadingEl.remove();
        
        let errMsg = error.message;
        if (error.name === 'AbortError') {
            errMsg = 'AI is taking too long to respond. Please try again.';
        } else {
            errMsg = 'AI is temporarily unavailable. Your learning progress is safe.';
        }
        
        responseArea.innerHTML += `<div class="execution-status error" style="padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">${DOMPurify.sanitize(errMsg)}</div>`;
    } finally {
        setAiLoadingState(false);
        aiAbortController = null;
        scrollToBottom();
    }
}

function renderAIResponse(actionType, data, container) {
    let markdownText = "";
    
    if (actionType === 'ask') {
        markdownText = `**Answer:**\n${data.answer}\n\n*Concepts:* ${data.concepts ? data.concepts.join(', ') : 'None'} (${data.difficulty})\n\n**Next Action:** *${data.next_action}*`;
    } else if (actionType === 'explain') {
        markdownText = `**What it is:**\n${data.what}\n\n**Why it matters:**\n${data.why}\n\n**How it works:**\n${data.how}\n\n**Examples:**\n${data.examples ? data.examples.map(e => '- ' + e).join('\n') : ''}\n\n**Common Mistake:**\n${data.mistake}\n\n**Quick Check:**\n*${data.check_question}*`;
    } else if (actionType === 'hint') {
        if (data.hint) {
            markdownText = "**Hint:**\n" + data.hint;
        } else {
            markdownText = "No hints available.";
        }
    } else if (actionType === 'weaknesses') {
        if (data.weaknesses && data.weaknesses.length > 0) {
            markdownText = "**Weaknesses:**\n" + data.weaknesses.join(', ') + `\n\n**Analysis:**\n${data.analysis}\n\n**Priority:**\n${data.priority ? data.priority.join(', ') : ''}\n\n**Practice Plan:**\n${data.practice_plan ? data.practice_plan.join('\n') : ''}`;
        } else {
            markdownText = "Great job! We haven't identified any major weak concepts right now.";
        }
    } else if (actionType === 'recommendation') {
        markdownText = `**Recommended Lesson:** ${data.recommended_lesson ? data.recommended_lesson.title : 'None'}\n\n**Why?** ${data.reason}\n\n*Prerequisites:* ${data.prerequisite_concepts ? data.prerequisite_concepts.join(', ') : 'None'}\n*Estimated Focus:* ${data.estimated_focus}`;
    } else if (actionType === 'learning-plan') {
        markdownText = `**Today:**\n${data.today ? data.today.map(i => '- ' + i).join('\n') : 'None'}\n\n**Practice:**\n${data.practice ? data.practice.map(i => '- ' + i).join('\n') : 'None'}\n\n**Revision:**\n${data.revision ? data.revision.map(i => '- ' + i).join('\n') : 'None'}\n\n**Next:**\n${data.next ? data.next.map(i => '- ' + i).join('\n') : 'None'}`;
    } else if (actionType === 'code-review') {
        markdownText = `**Score:** ${data.score}/100\n\n**Bugs:**\n${data.bugs ? data.bugs.map(i => `- ${i}`).join('\n') : 'None'}\n\n**Strengths:**\n${data.strengths ? data.strengths.map(h => `- ${h}`).join('\n') : 'None'}\n\n**Improvements:**\n${data.improvements ? data.improvements.map(i => `- ${i}`).join('\n') : 'None'}\n\n**Concepts to Review:** ${data.concepts_to_review ? data.concepts_to_review.join(', ') : 'None'}`;
        if (data.corrected_code) {
            markdownText += `\n\n**Corrected Code:**\n\`\`\`\n${data.corrected_code}\n\`\`\``;
        }
    }

    // Render securely
    const rawHtml = marked.parse(markdownText);
    const cleanHtml = DOMPurify.sanitize(rawHtml);
    
    let providerIndicator = "";
    if (data._provider_used) {
        let providerText = data._provider_used === 'gemini' ? 'AI powered by Gemini' : 'AI fallback provider active';
        providerIndicator = `<div style="text-align: right; font-size: 0.8rem; color: var(--text-muted); margin-top: 0.5rem; font-style: italic;">${providerText}</div>`;
    }
    
    // Append instead of overwrite
    const wrapper = document.createElement('div');
    wrapper.style.marginBottom = '1.5rem';
    wrapper.style.padding = '10px';
    wrapper.style.background = 'rgba(0,0,0,0.4)';
    wrapper.style.borderRadius = '8px';
    wrapper.innerHTML = `<div class="markdown-body">${cleanHtml}</div>${providerIndicator}`;
    container.appendChild(wrapper);
    
    scrollToBottom();
}

// Support hitting 'Enter' in custom question box
document.addEventListener('DOMContentLoaded', () => {
    const inputField = document.getElementById('ai-custom-question');
    if (inputField) {
        inputField.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                document.getElementById('ai-ask-btn').click();
            }
        });
    }
});

// Panel toggle logic
window.toggleAIPanel = function() {
    const panel = document.getElementById('ai-assistant-panel');
    const floatingBtn = document.getElementById('ai-floating-btn');
    
    if (panel.classList.contains('minimized')) {
        panel.classList.remove('minimized');
        if(floatingBtn) floatingBtn.style.display = 'none';
        localStorage.setItem('learnx_ai_panel_state', 'expanded');
    } else {
        panel.classList.add('minimized');
        if(floatingBtn) floatingBtn.style.display = 'flex';
        localStorage.setItem('learnx_ai_panel_state', 'minimized');
    }
}

window.closeAIPanel = function() {
    const panel = document.getElementById('ai-assistant-panel');
    const floatingBtn = document.getElementById('ai-floating-btn');
    
    if(panel) panel.style.display = 'none';
    if(floatingBtn) floatingBtn.style.display = 'flex';
    localStorage.setItem('learnx_ai_panel_state', 'closed');
}

function initAIPanel() {
    const state = localStorage.getItem('learnx_ai_panel_state') || 'expanded';
    const panel = document.getElementById('ai-assistant-panel');
    const floatingBtn = document.getElementById('ai-floating-btn');
    
    if (!panel) return;
    
    if (state === 'minimized') {
        panel.classList.add('minimized');
        panel.style.display = 'flex';
        if(floatingBtn) floatingBtn.style.display = 'flex';
    } else if (state === 'closed') {
        panel.style.display = 'none';
        if(floatingBtn) floatingBtn.style.display = 'flex';
    } else {
        panel.classList.remove('minimized');
        panel.style.display = 'flex';
        if(floatingBtn) floatingBtn.style.display = 'none';
    }
    
    if(floatingBtn) {
        floatingBtn.addEventListener('click', () => {
            panel.style.display = 'flex';
            panel.classList.remove('minimized');
            floatingBtn.style.display = 'none';
            localStorage.setItem('learnx_ai_panel_state', 'expanded');
        });
    }
}

document.addEventListener('DOMContentLoaded', initAIPanel);

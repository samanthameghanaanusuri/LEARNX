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

function escapeHtml(str) {
    if (typeof str !== 'string') return '';
    return str
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
}

async function requestAI(actionType) {
    if (isAiRequestRunning) return; // Prevent duplicate requests
    
    const urlParams = new URLSearchParams(window.location.search);
    const lessonId = urlParams.get('id') || urlParams.get('lesson_id') || window.currentLessonId || (window.lessonData && window.lessonData.id) || null;
    const courseId = urlParams.get('course_id') || (window.lessonData && window.lessonData.course_id) || null;
    const conceptName = window.currentConceptName || (window.lessonData && window.lessonData.title) || "Current Lesson Concept";
    
    const responseArea = document.getElementById('ai-response-area');
    if (!responseArea) return;

    let endpoint = `/ai/${actionType}`;
    let method = 'POST';
    let body = {
        course_id: courseId,
        lesson_id: lessonId
    };
    
    let userPromptText = "";

    if (actionType === 'ask') {
        const inputField = document.getElementById('ai-custom-question');
        const question = inputField ? inputField.value.trim() : "";
        if (!question) {
            const warningEl = document.createElement('div');
            warningEl.style.color = 'var(--color-warning)';
            warningEl.style.padding = '8px';
            warningEl.style.fontSize = '13px';
            warningEl.textContent = 'Please type a question first.';
            responseArea.appendChild(warningEl);
            scrollToBottom();
            return;
        }
        body.question = question;
        userPromptText = question;
        if (inputField) {
            inputField.value = ''; // clear input
            inputField.style.height = 'auto'; // reset height
            inputField.focus(); // focus again
        }
    } else if (actionType === 'explain') {
        body.concept = conceptName;
        userPromptText = `Explain concept: ${conceptName}`;
    } else if (actionType === 'hint') {
        if (!window.currentHintLevel) window.currentHintLevel = 1;
        if (window.currentHintLevel > 5) {
            const warn = document.createElement('div');
            warn.style.color = 'var(--color-warning)';
            warn.style.padding = '8px';
            warn.style.fontSize = '13px';
            warn.textContent = 'Maximum hint level reached. Please try your best!';
            responseArea.appendChild(warn);
            scrollToBottom();
            return;
        }
        body.hint_level = window.currentHintLevel;
        userPromptText = `Give me a hint (Level ${window.currentHintLevel})`;
        window.currentHintLevel++;
    } else if (actionType === 'weaknesses') {
        method = 'GET';
        body = null;
        userPromptText = "What am I weak at?";
    } else if (actionType === 'recommendation') {
        method = 'GET';
        body = null;
        userPromptText = "What should I learn next?";
    } else if (actionType === 'learning-plan') {
        method = 'GET';
        body = null;
        userPromptText = "Make Me a Learning Plan";
    }

    // 1. Immediately Render User Question Bubble in Chat History
    const userBubble = document.createElement('div');
    userBubble.className = 'chat-bubble user-bubble';
    userBubble.innerHTML = `
        <div class="bubble-sender" style="color: #6366f1;">YOU</div>
        <div style="font-size: 14px; color: var(--text-primary); white-space: pre-wrap;">${escapeHtml(userPromptText)}</div>
    `;
    responseArea.appendChild(userBubble);

    // 2. Immediately Render Temporary AI Loading Bubble
    const loadingId = 'loading-' + Date.now();
    const aiLoadingBubble = document.createElement('div');
    aiLoadingBubble.id = loadingId;
    aiLoadingBubble.className = 'chat-bubble ai-bubble loading-bubble';
    aiLoadingBubble.innerHTML = `
        <div class="bubble-sender" style="color: #00ff88;">LEARNX AI</div>
        <div style="font-size: 13px; color: var(--text-secondary); font-style: italic;">Thinking...</div>
    `;
    responseArea.appendChild(aiLoadingBubble);
    scrollToBottom();

    // Check cache for stateless requests if available
    const cacheKey = `${actionType}_${lessonId}_${conceptName}`;
    if (['explain', 'weaknesses', 'recommendation'].includes(actionType)) {
        if (aiCache[cacheKey] && (Date.now() - aiCache[cacheKey].timestamp < 300000)) {
            renderAIResponseIntoBubble(actionType, aiCache[cacheKey].data, loadingId);
            return;
        }
    }

    setAiLoadingState(true);
    aiAbortController = new AbortController();
    const timeoutId = setTimeout(() => aiAbortController.abort(), 30000);

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
        clearTimeout(timeoutId);
        
        const data = await response.json();

        if (!response.ok || data.success === false || data.available === false) {
            const errorMsg = data.message || data.error || "I couldn't process that request right now. Please try again.";
            renderErrorIntoBubble(loadingId, errorMsg);
        } else {
            if (['explain', 'weaknesses', 'recommendation'].includes(actionType)) {
                aiCache[cacheKey] = {
                    timestamp: Date.now(),
                    data: data
                };
            }
            renderAIResponseIntoBubble(actionType, data, loadingId);
        }
    } catch (error) {
        clearTimeout(timeoutId);
        let errMsg = "I couldn't process that request right now. Please try again.";
        if (error.name === 'AbortError') {
            errMsg = 'AI response timed out. Please try again.';
        }
        renderErrorIntoBubble(loadingId, errMsg);
    } finally {
        setAiLoadingState(false);
        aiAbortController = null;
        scrollToBottom();
    }
}

function renderAIResponseIntoBubble(actionType, data, loadingId) {
    const bubble = document.getElementById(loadingId);
    if (!bubble) return;

    let markdownText = "";
    
    if (actionType === 'ask') {
        markdownText = data.answer || "No answer provided.";
        if (data.concepts && data.concepts.length > 0 && data.concepts[0] !== "Course Scope") {
            markdownText += `\n\n*Concepts:* ${data.concepts.join(', ')}`;
        }
    } else if (actionType === 'explain') {
        markdownText = `**What it is:**\n${data.what}\n\n**Why it matters:**\n${data.why}\n\n**How it works:**\n${data.how}\n\n**Examples:**\n${data.examples ? data.examples.map(e => '- ' + e).join('\n') : ''}\n\n**Common Mistake:**\n${data.mistake}\n\n**Quick Check:**\n*${data.check_question}*`;
    } else if (actionType === 'hint') {
        markdownText = data.hint ? "**Hint:**\n" + data.hint : "No hints available.";
    } else if (actionType === 'weaknesses') {
        if (data.weaknesses && data.weaknesses.length > 0) {
            markdownText = "**Weaknesses:**\n" + data.weaknesses.join(', ') + `\n\n**Analysis:**\n${data.analysis}\n\n**Practice Plan:**\n${data.practice_plan ? data.practice_plan.join('\n') : ''}`;
        } else {
            markdownText = "Great job! We haven't identified any major weak concepts right now.";
        }
    } else if (actionType === 'recommendation') {
        markdownText = `**Recommended Lesson:** ${data.recommended_lesson ? data.recommended_lesson.title : 'None'}\n\n**Reason:** ${data.reason}`;
    } else if (actionType === 'learning-plan') {
        markdownText = `**Today:**\n${data.today ? data.today.map(i => '- ' + i).join('\n') : 'None'}\n\n**Practice:**\n${data.practice ? data.practice.map(i => '- ' + i).join('\n') : 'None'}\n\n**Next:**\n${data.next ? data.next.map(i => '- ' + i).join('\n') : 'None'}`;
    }

    const rawHtml = typeof marked !== 'undefined' ? marked.parse(markdownText) : markdownText;
    const cleanHtml = typeof DOMPurify !== 'undefined' ? DOMPurify.sanitize(rawHtml) : rawHtml;
    
    let providerIndicator = "";
    if (data._provider_used) {
        let providerText = data._provider_used === 'gemini' ? 'AI powered by Gemini' : 'AI powered by OpenRouter';
        providerIndicator = `<div style="text-align: right; font-size: 0.75rem; color: var(--text-muted); margin-top: 0.5rem; font-style: italic;">${providerText}</div>`;
    }
    
    bubble.classList.remove('loading-bubble');
    bubble.innerHTML = `
        <div class="bubble-sender" style="color: #00ff88;">LEARNX AI</div>
        <div class="markdown-body" style="font-size: 14px; color: var(--text-primary);">${cleanHtml}</div>
        ${providerIndicator}
    `;
    scrollToBottom();
}

function renderErrorIntoBubble(loadingId, errorMsg) {
    const bubble = document.getElementById(loadingId);
    if (!bubble) return;

    const cleanMsg = typeof DOMPurify !== 'undefined' ? DOMPurify.sanitize(errorMsg) : errorMsg;
    bubble.classList.remove('loading-bubble');
    bubble.innerHTML = `
        <div class="bubble-sender" style="color: var(--color-danger);">LEARNX AI</div>
        <div style="color: var(--color-danger); font-size: 14px;">${cleanMsg}</div>
    `;
    scrollToBottom();
}

// Auto-grow for custom question textarea
document.addEventListener('DOMContentLoaded', () => {
    const inputField = document.getElementById('ai-custom-question');
    if (inputField) {
        inputField.addEventListener('input', function () {
            this.style.height = 'auto';
            this.style.height = (this.scrollHeight) + 'px';
        });
    }
});

// Panel toggle logic
window.toggleAIPanel = function() {
    const panel = document.getElementById('ai-assistant-panel');
    const floatingBtn = document.getElementById('ai-floating-btn');
    if (!panel) return;
    
    if (panel.classList.contains('minimized')) {
        panel.classList.remove('minimized');
        if (floatingBtn) floatingBtn.style.display = 'none';
        localStorage.setItem('learnx_ai_panel_state', 'expanded');
    } else {
        panel.classList.add('minimized');
        if (floatingBtn) floatingBtn.style.display = 'flex';
        localStorage.setItem('learnx_ai_panel_state', 'minimized');
    }
};

window.closeAIPanel = function() {
    const panel = document.getElementById('ai-assistant-panel');
    const floatingBtn = document.getElementById('ai-floating-btn');
    
    if (panel) panel.style.display = 'none';
    if (floatingBtn) floatingBtn.style.display = 'flex';
    localStorage.setItem('learnx_ai_panel_state', 'closed');
};

function initAIPanel() {
    const state = localStorage.getItem('learnx_ai_panel_state') || 'expanded';
    const panel = document.getElementById('ai-assistant-panel');
    const floatingBtn = document.getElementById('ai-floating-btn');
    
    if (!panel) return;
    
    if (state === 'minimized') {
        panel.classList.add('minimized');
        panel.style.display = 'flex';
        if (floatingBtn) floatingBtn.style.display = 'flex';
    } else if (state === 'closed') {
        panel.style.display = 'none';
        if (floatingBtn) floatingBtn.style.display = 'flex';
    } else {
        panel.classList.remove('minimized');
        panel.style.display = 'flex';
        if (floatingBtn) floatingBtn.style.display = 'none';
    }
    
    if (floatingBtn) {
        floatingBtn.addEventListener('click', () => {
            panel.style.display = 'flex';
            panel.classList.remove('minimized');
            floatingBtn.style.display = 'none';
            localStorage.setItem('learnx_ai_panel_state', 'expanded');
        });
    }
}

document.addEventListener('DOMContentLoaded', initAIPanel);

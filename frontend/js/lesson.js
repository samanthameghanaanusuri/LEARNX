const urlParams = new URLSearchParams(window.location.search);
const lessonId = urlParams.get('id');

let lessonData = null;
let codeEditor = null;
let projectEditor = null;
let activeExerciseIndex = 0;
let exerciseScores = {}; // { exerciseId: score }
let currentQuizPage = 0;
let selectedAnswers = {}; // { question_id: answer }
let quizResults = null;
let projectSubmission = null;

document.addEventListener('DOMContentLoaded', async () => {
    checkAuth();
    if (!lessonId) {
        window.location.href = '/courses.html';
        return;
    }
    await loadLesson();
});

async function loadLesson() {
    try {
        lessonData = await LEARNX_API.getLesson(lessonId);
        renderHeaderAndSidebar();
        renderTheory();
        setupPracticeLab();
        setupKnowledgeCheck();
        setupMiniProject();
        setupMasterySection();
        updateIntelligenceSidebar();
    } catch (error) {
        document.getElementById('header-lesson-title').textContent = 'Error Loading Lesson';
        document.getElementById('lesson-sidebar-nav').innerHTML = `<h4>Lesson Outline</h4><p style="color: var(--color-danger);">Failed to load.</p>`;
        document.getElementById('intelligence-status').textContent = 'Error';
        document.getElementById('intelligence-status').style.color = 'var(--color-danger)';
        
        document.getElementById('theory-content').innerHTML = `
            <div class="glass-panel" style="border-left: 4px solid var(--color-danger);">
                <h2 style="color: var(--color-danger); margin-top: 0;">Unable to load this lesson.</h2>
                <p>Reason: ${error.message}</p>
                <button class="btn btn-secondary" onclick="window.location.reload()" style="margin-top: 1rem;">Retry</button>
            </div>
        `;
    }
}

function renderHeaderAndSidebar() {
    document.getElementById('header-lesson-title').textContent = lessonData.title;
    document.getElementById('header-progress-fill').style.width = '20%';
    
    const nav = document.getElementById('lesson-sidebar-nav');
    nav.innerHTML = `<h4>Lesson Outline</h4><ul class="lesson-nav-list">
        <li class="active" onclick="scrollToSection('theory-content')">1. Theory & Examples</li>
        <li class="${lessonData.exercises && lessonData.exercises.length > 0 ? '' : 'disabled'}" onclick="scrollToSection('practice-lab-container')">2. Practice Lab (${lessonData.exercises ? lessonData.exercises.length : 0})</li>
        <li class="${lessonData.quizzes && lessonData.quizzes.length > 0 ? '' : 'disabled'}" onclick="scrollToSection('quiz-container')">3. Knowledge Check (${lessonData.quizzes ? lessonData.quizzes.length : 0})</li>
        <li class="${lessonData.projects && lessonData.projects.length > 0 ? '' : 'disabled'}" onclick="scrollToSection('project-container')">4. Mini Project</li>
        <li onclick="scrollToSection('mastery-container')">5. Mastery & Progress</li>
    </ul>`;
}

window.scrollToSection = function(sectionId) {
    const el = document.getElementById(sectionId);
    if (el) el.scrollIntoView({ behavior: 'smooth' });
}

function renderTheory() {
    const theoryCol = document.getElementById('theory-content');
    
    // Parse markdown if marked is available, otherwise fallback to raw HTML
    const parsedContent = typeof marked !== 'undefined' ? marked.parse(lessonData.content) : lessonData.content;
    
    let html = `<div class="glass-panel markdown-body" style="margin-bottom: 2rem;">
        ${parsedContent}
    </div>`;

    if (lessonData.examples && lessonData.examples.length > 0) {
        html += `<h3 style="margin-top: 2rem;">Worked Examples</h3>`;
        lessonData.examples.forEach((ex, idx) => {
            html += `
                <div class="glass-panel" style="margin-bottom: 1.5rem; position: relative;">
                    <h4 style="margin-top:0; color: #fff;">Example ${idx + 1}: ${ex.title}</h4>
                    <p style="color: var(--text-secondary); font-size: 14px;">${ex.explanation}</p>
                    <button class="btn btn-secondary" style="position: absolute; right: 1rem; top: 1rem; padding: 0.25rem 0.5rem; font-size: 12px;" onclick="navigator.clipboard.writeText(decodeURIComponent('${encodeURIComponent(ex.code)}'))">Copy Code</button>
                    <pre class="terminal-output" style="background: rgba(0,0,0,0.4); font-family: monospace;">${ex.code}</pre>
                </div>
            `;
        });
    }
    
    theoryCol.innerHTML = html;
}

let userCodeDrafts = {}; // { exerciseId: string }

function setupPracticeLab() {
    if (!lessonData.exercises || lessonData.exercises.length === 0) return;
    
    // Initialize scores & draft code from user submissions
    lessonData.exercises.forEach(ex => {
        if (ex.user_submission) {
            exerciseScores[ex.id] = ex.user_submission.score;
            userCodeDrafts[ex.id] = ex.user_submission.code;
        } else if (exerciseScores[ex.id] === undefined) {
            exerciseScores[ex.id] = 0.0;
        }
    });

    document.getElementById('practice-lab-container').style.display = 'block';
    renderPracticeLab();
    loadExerciseEditor(0);
}

function renderPracticeLab() {
    const container = document.getElementById('editor-container');
    const totalEx = lessonData.exercises.length;
    const passedEx = Object.values(exerciseScores).filter(s => s === 1.0).length;
    const remainingEx = totalEx - passedEx;
    const progressPct = totalEx > 0 ? Math.round((passedEx / totalEx) * 100) : 0;
    
    let maxScore = 0;
    Object.values(exerciseScores).forEach(s => {
        if (s > maxScore) maxScore = s;
    });
    const bestScorePct = Math.round(maxScore * 100);

    let tabsHtml = '';
    lessonData.exercises.forEach((ex, idx) => {
        const isPassed = exerciseScores[ex.id] === 1.0;
        const isActive = idx === activeExerciseIndex;
        tabsHtml += `
            <button class="btn ${isActive ? 'btn-primary' : 'btn-secondary'}" style="font-size: 13px; padding: 0.4rem 0.8rem; border-radius: 6px; font-weight: 500;" onclick="switchExercise(${idx})">
                ${isPassed ? '<span style="color: #00ff88; margin-right: 4px;">✓</span>' : ''}Ex ${idx + 1}: ${escapeHtml(ex.title.substring(0, 20))}
            </button>
        `;
    });

    container.innerHTML = `
        <div class="practice-progress-header glass-panel" style="padding: 1rem 1.25rem; margin-bottom: 1.25rem; border-left: 4px solid var(--color-primary); background: rgba(15, 23, 42, 0.6);">
            <div class="flex-between" style="margin-bottom: 0.5rem;">
                <h4 style="margin: 0; color: #fff; font-size: 15px;">Practice Progress</h4>
                <span style="font-weight: 700; font-size: 15px; color: var(--color-primary);">${passedEx} / ${totalEx} Completed (${progressPct}%)</span>
            </div>
            <div class="progress-bar-container" style="height: 8px; margin-bottom: 0.75rem; background: rgba(255,255,255,0.08); border-radius: 4px; overflow: hidden;">
                <div class="progress-bar-fill" style="width: ${progressPct}%; background: linear-gradient(90deg, var(--color-primary), #00c8ff); height: 100%; transition: width 0.3s ease;"></div>
            </div>
            <div style="display: flex; gap: 1.5rem; font-size: 13px; color: var(--text-secondary);">
                <div>Passed: <strong style="color: var(--color-success);">${passedEx}</strong></div>
                <div>Remaining: <strong style="color: var(--color-warning);">${remainingEx}</strong></div>
                <div>Best Score: <strong style="color: #00c8ff;">${bestScorePct}%</strong></div>
            </div>
        </div>

        <div class="exercise-tabs-bar" style="display: flex; gap: 0.5rem; margin-bottom: 1.25rem; flex-wrap: wrap;">
            ${tabsHtml}
        </div>
        
        <div id="active-exercise-widget"></div>
    `;
}

window.switchExercise = function(index) {
    if (index < 0 || index >= lessonData.exercises.length) return;
    activeExerciseIndex = index;
    renderPracticeLab();
    loadExerciseEditor(index);
}

function loadExerciseEditor(index) {
    const targetEx = lessonData.exercises[index];
    codeEditor = new CodeEditor('active-exercise-widget', {
        exercise: targetEx,
        exerciseIndex: index,
        totalExercises: lessonData.exercises.length,
        draftCode: userCodeDrafts[targetEx.id],
        language: targetEx.language || 'java',
        onCodeChange: (code) => {
            userCodeDrafts[targetEx.id] = code;
        },
        onNavigate: (newIndex) => {
            switchExercise(newIndex);
        },
        onComplete: (score, res) => {
            exerciseScores[targetEx.id] = score;
            renderPracticeLab();
            updateIntelligenceSidebar();
            renderMasterySummary();
        }
    });
}

function setupKnowledgeCheck() {
    if (!lessonData.quizzes || lessonData.quizzes.length === 0) return;
    document.getElementById('quiz-container').style.display = 'block';
    renderQuizPage();
}

function renderQuizPage() {
    const wrapper = document.getElementById('quiz-questions-wrapper');
    const total = lessonData.quizzes.length;
    
    if (currentQuizPage >= total) {
        wrapper.innerHTML = `<div class="glass-panel text-center"><p>Evaluating Quiz Responses...</p></div>`;
        submitQuizBulk();
        return;
    }
    
    const q = lessonData.quizzes[currentQuizPage];
    let optionsHtml = '';
    
    q.options.forEach((opt) => {
        const isSelected = selectedAnswers[q.id] === opt;
        optionsHtml += `
            <label class="quiz-option-label ${isSelected ? 'selected' : ''}" onclick="selectQuizOption(${q.id}, '${opt.replace(/'/g, "\\'")}', this)" style="display: block; padding: 1rem; margin-bottom: 0.5rem; background: rgba(255,255,255,0.03); border: 1px solid var(--border-card); border-radius: 8px; cursor: pointer;">
                <input type="radio" name="q_${q.id}" value="${opt}" ${isSelected ? 'checked' : ''} style="margin-right: 0.5rem;">
                <span>${opt}</span>
            </label>
        `;
    });

    wrapper.innerHTML = `
        <div class="glass-panel" style="margin-bottom: 2rem;">
            <div class="flex-between" style="margin-bottom: 1rem;">
                <h3 style="margin: 0; color: var(--color-primary);">Question ${currentQuizPage + 1} of ${total}</h3>
                <span class="badge" style="background: rgba(255,255,255,0.1); padding: 0.25rem 0.5rem; font-size: 12px;">${q.difficulty || 'Intermediate'}</span>
            </div>
            <p style="font-size: 18px; font-weight: 500; color: #fff; margin-bottom: 1.5rem;">${q.question_text}</p>
            <div>${optionsHtml}</div>
            
            <div class="flex-between" style="margin-top: 2rem; border-top: 1px solid var(--border-card); padding-top: 1.5rem;">
                <button class="btn btn-secondary" onclick="prevQuizPage()" ${currentQuizPage === 0 ? 'disabled' : ''}>← Previous</button>
                <button class="btn btn-primary" onclick="nextQuizPage()" id="btn-next-quiz" ${!selectedAnswers[q.id] ? 'disabled' : ''}>
                    ${currentQuizPage === total - 1 ? 'Submit Knowledge Check' : 'Next →'}
                </button>
            </div>
        </div>
    `;
}

window.selectQuizOption = function(qId, answer, element) {
    selectedAnswers[qId] = answer;
    const siblings = element.parentElement.querySelectorAll('.quiz-option-label');
    siblings.forEach(el => el.classList.remove('selected'));
    element.classList.add('selected');
    const btnNext = document.getElementById('btn-next-quiz');
    if(btnNext) btnNext.disabled = false;
}

window.prevQuizPage = function() {
    if (currentQuizPage > 0) {
        currentQuizPage--;
        renderQuizPage();
    }
}

window.nextQuizPage = function() {
    currentQuizPage++;
    renderQuizPage();
}

async function submitQuizBulk() {
    try {
        const wrapper = document.getElementById('quiz-questions-wrapper');
        const data = await LEARNX_API.submitQuizBulk(lessonId, selectedAnswers);
        quizResults = data;
        
        let resultsHtml = `
            <div class="glass-panel" style="border-left: 4px solid var(--color-success); margin-bottom: 2rem;">
                <h3 style="color: var(--color-success); margin-top: 0;">Knowledge Check Complete!</h3>
                <p style="font-size: 16px;">Score: <strong>${data.correct} / ${data.total}</strong> (${Math.round(data.score * 100)}%)</p>
            </div>
        `;
        
        data.results.forEach((r, idx) => {
            resultsHtml += `
                <div class="glass-panel" style="margin-bottom: 1rem; border-left: 4px solid ${r.correct ? 'var(--color-success)' : 'var(--color-danger)'};">
                    <h4 style="margin: 0; color: #fff;">Q${idx + 1}: ${r.correct ? '✓ Correct' : '✗ Incorrect'}</h4>
                    <p style="margin-top: 0.5rem; font-size: 14px;"><strong>Your Answer:</strong> ${r.selected_answer}</p>
                    ${!r.correct ? `<p style="font-size: 14px; color: var(--color-success);"><strong>Correct Answer:</strong> ${r.correct_answer}</p>` : ''}
                    <div style="margin-top: 0.5rem; padding: 0.75rem; background: rgba(0,0,0,0.3); border-radius: 6px; font-size: 13px; color: var(--text-secondary);">
                        ${r.explanation || 'No explanation provided.'}
                    </div>
                </div>
            `;
        });
        
        wrapper.innerHTML = resultsHtml;
        updateIntelligenceSidebar();
        renderMasterySummary();
    } catch (e) {
        document.getElementById('quiz-questions-wrapper').innerHTML = `
            <div class="glass-panel" style="border-left: 4px solid var(--color-danger);">
                <h3 style="color: var(--color-danger); margin-top: 0;">Submission Error</h3>
                <p>${e.message}</p>
                <button class="btn btn-secondary" onclick="currentQuizPage = 0; renderQuizPage();">Retry</button>
            </div>
        `;
    }
}

function normalizeList(value) {
    if (Array.isArray(value)) return value;
    if (typeof value === 'string') {
        try {
            const parsed = JSON.parse(value);
            if (Array.isArray(parsed)) return parsed;
        } catch (_) {}
        return value.split(/\r?\n/).map(v => v.trim()).filter(Boolean);
    }
    if (value && typeof value === 'object') {
        return Object.values(value);
    }
    return [];
}

function setupMiniProject() {
    if (!lessonData.projects || lessonData.projects.length === 0) return;
    document.getElementById('project-container').style.display = 'block';
    
    const proj = lessonData.projects[0];
    const wrapper = document.getElementById('project-wrapper');
    
    const reqs = normalizeList(proj.requirements).map(r => `<li>${r}</li>`).join('');
    const feats = normalizeList(proj.features).map(f => `<span class="badge" style="background: rgba(255,255,255,0.08); margin-right: 0.5rem; font-size: 12px;">${f}</span>`).join('');
    const guidance = normalizeList(proj.guidance).map(g => `<li>${g}</li>`).join('');
    const hints = normalizeList(proj.hints).map(h => `<li>${h}</li>`).join('');

    wrapper.innerHTML = `
        <div class="glass-panel" style="margin-bottom: 2rem;">
            <div class="flex-between">
                <h3 style="margin-top: 0; color: var(--color-primary);">${proj.title}</h3>
                <span class="badge" style="background: rgba(0, 200, 255, 0.15); color: #00c8ff; font-weight: 600;">MODULE MINI PROJECT</span>
            </div>
            
            <p style="font-size: 15px; color: var(--text-primary); margin-top: 1rem;"><strong>Objective:</strong> ${proj.objective}</p>
            <div style="background: rgba(0,0,0,0.25); padding: 1rem; border-radius: 8px; margin: 1rem 0; border-left: 3px solid var(--color-primary);">
                <p style="margin: 0; font-size: 14px; color: var(--text-secondary);"><strong>Real-World Scenario:</strong> ${proj.scenario}</p>
            </div>

            <div style="margin-top: 1.5rem;">
                <h4 style="margin-bottom: 0.5rem; color: #fff;">Project Requirements:</h4>
                <ul style="color: var(--text-secondary); padding-left: 1.2rem; font-size: 14px;">${reqs}</ul>
            </div>

            <div style="margin-top: 1rem;">
                <h4 style="margin-bottom: 0.5rem; color: #fff;">Key Features:</h4>
                <div>${feats}</div>
            </div>

            <details style="margin-top: 1.5rem; background: rgba(255,255,255,0.02); padding: 0.75rem; border-radius: 6px; cursor: pointer;">
                <summary style="font-weight: 600; color: var(--color-primary);">💡 Architecture & Guidance Hints</summary>
                <div style="margin-top: 0.75rem; font-size: 13px; color: var(--text-secondary);">
                    <p><strong>Architecture:</strong> ${proj.architecture || 'Follow single-responsibility function design.'}</p>
                    <p><strong>Workflow:</strong> ${proj.workflow || 'Input -> Transform -> Output'}</p>
                    <p><strong>Guidance:</strong></p>
                    <ul>${guidance}</ul>
                    <p><strong>Hints:</strong></p>
                    <ul>${hints}</ul>
                </div>
            </details>
        </div>

        <div class="glass-panel" style="margin-bottom: 2rem;">
            <h4 style="margin-top:0;">Project Code Workspace</h4>
            <div style="margin-bottom: 1rem;">
                <textarea id="project-code-input" style="width: 100%; height: 220px; font-family: monospace; background: rgba(0,0,0,0.6); color: #00ff88; border: 1px solid var(--border-card); border-radius: 8px; padding: 1rem;">${proj.starter_code || '# Write your project implementation here\n'}</textarea>
            </div>
            <div class="flex-between">
                <button class="btn btn-secondary" onclick="resetProjectCode()">Reset Starter Code</button>
                <button class="btn btn-primary" onclick="submitProjectCode(${proj.id})">🚀 Submit Project for Automated Evaluation</button>
            </div>
        </div>

        <div id="project-results-panel"></div>
    `;
}

window.resetProjectCode = function() {
    if (lessonData && lessonData.projects && lessonData.projects[0]) {
        document.getElementById('project-code-input').value = lessonData.projects[0].starter_code || '';
    }
}

window.submitProjectCode = async function(projectId) {
    const panel = document.getElementById('project-results-panel');
    const code = document.getElementById('project-code-input').value;
    
    panel.innerHTML = `<div class="glass-panel text-center"><p>Evaluating project against automated feature test cases...</p></div>`;
    
    try {
        const res = await LEARNX_API.submitProject(projectId, code);
        projectSubmission = res;
        
        const isPassed = res.status === 'passed';
        let feedbackHtml = `
            <div class="glass-panel" style="border-left: 4px solid ${isPassed ? 'var(--color-success)' : 'var(--color-danger)'}; margin-bottom: 2rem;">
                <div class="flex-between">
                    <h3 style="margin:0; color: ${isPassed ? 'var(--color-success)' : 'var(--color-danger)'};">
                        ${isPassed ? '🎉 Project Evaluation Passed!' : '❌ Project Evaluation Failed'}
                    </h3>
                    <span style="font-size: 16px; font-weight: 700;">Score: ${Math.round(res.score * 100)}% (${res.passed_tests}/${res.total_tests} Tests)</span>
                </div>
                <p style="margin-top: 0.5rem; font-size: 13px; color: var(--text-secondary);">Execution Time: ${res.execution_time_ms} ms</p>
            </div>
            <h4>Automated Test Case Feedback</h4>
        `;

        res.feedback.forEach((item, idx) => {
            feedbackHtml += `
                <div class="glass-panel" style="margin-bottom: 0.75rem; padding: 1rem; border-left: 3px solid ${item.passed ? 'var(--color-success)' : 'var(--color-danger)'}; font-size: 14px;">
                    <div class="flex-between">
                        <strong>Feature Test ${idx + 1}: ${item.test_case}</strong>
                        <span style="color: ${item.passed ? 'var(--color-success)' : 'var(--color-danger)'}; font-weight: 600;">
                            ${item.passed ? 'PASSED' : 'FAILED (' + item.status + ')'}
                        </span>
                    </div>
                    <p style="margin-top: 0.25rem; font-size: 13px; color: var(--text-secondary);">${item.message}</p>
                </div>
            `;
        });

        panel.innerHTML = feedbackHtml;
        updateIntelligenceSidebar();
        renderMasterySummary();
    } catch (err) {
        panel.innerHTML = `
            <div class="glass-panel" style="border-left: 4px solid var(--color-danger);">
                <h4 style="color: var(--color-danger); margin-top: 0;">Evaluation Failed</h4>
                <p>${err.message}</p>
            </div>
        `;
    }
}

function setupMasterySection() {
    document.getElementById('mastery-container').style.display = 'block';
    renderMasterySummary();
}

function renderMasterySummary() {
    const panel = document.getElementById('mastery-summary-panel');
    const totalEx = lessonData.exercises ? lessonData.exercises.length : 0;
    const passedEx = Object.values(exerciseScores).filter(s => s === 1.0).length;
    const quizDone = quizResults !== null;
    const projectPassed = projectSubmission && projectSubmission.status === 'passed';
    
    const allReady = (totalEx === 0 || passedEx === totalEx) && (!lessonData.quizzes || quizDone) && (!lessonData.projects || projectPassed);

    panel.innerHTML = `
        <h3 style="margin-top: 0; color: #fff;">Lesson Mastery Criteria</h3>
        <div style="margin: 1rem 0;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem; font-size: 14px;">
                <span>1. Practice Exercises (${passedEx}/${totalEx})</span>
                <span style="color: ${passedEx === totalEx ? 'var(--color-success)' : 'var(--color-warning)'};">${passedEx === totalEx ? '✓ Completed' : 'Pending'}</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem; font-size: 14px;">
                <span>2. Knowledge Check (MCQs)</span>
                <span style="color: ${quizDone ? 'var(--color-success)' : 'var(--color-warning)'};">${quizDone ? `✓ Completed (${Math.round(quizResults.score * 100)}%)` : 'Pending'}</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem; font-size: 14px;">
                <span>3. Module Mini Project</span>
                <span style="color: ${projectPassed ? 'var(--color-success)' : 'var(--color-warning)'};">${projectPassed ? '✓ Passed' : 'Pending'}</span>
            </div>
        </div>

        <div style="margin-top: 2rem; text-align: center;">
            <button class="btn btn-primary" style="padding: 0.75rem 2rem; font-size: 16px;" onclick="handleCompleteLesson()" ${allReady ? '' : 'disabled'}>
                ${allReady ? '🎉 Mark Lesson Complete & Continue' : '🔒 Complete All Requirements to Unlock'}
            </button>
        </div>
    `;
}

window.handleCompleteLesson = async function() {
    try {
        await LEARNX_API.completeLesson(lessonId);
        alert('Congratulations! Lesson marked as completed.');
        const nextId = parseInt(lessonId) + 1;
        if (nextId <= 30) {
            window.location.href = `/lesson.html?id=${nextId}`;
        } else {
            window.location.href = '/courses.html';
        }
    } catch (err) {
        alert('Completion failed: ' + err.message);
    }
}

function updateIntelligenceSidebar() {
    const totalEx = lessonData.exercises ? lessonData.exercises.length : 0;
    const passedEx = Object.values(exerciseScores).filter(s => s === 1.0).length;
    const quizDone = quizResults !== null;
    const projectPassed = projectSubmission && projectSubmission.status === 'passed';

    let masteryCalc = 0;
    let parts = 0;

    if (totalEx > 0) {
        masteryCalc += (passedEx / totalEx) * 0.3;
        parts += 0.3;
    }
    if (quizDone) {
        masteryCalc += quizResults.score * 0.3;
        parts += 0.3;
    }
    if (projectPassed) {
        masteryCalc += projectSubmission.score * 0.4;
        parts += 0.4;
    }

    const finalPercent = parts > 0 ? Math.round((masteryCalc / parts) * 100) : 0;

    document.getElementById('intelligence-mastery').textContent = `${finalPercent}%`;

    const statusEl = document.getElementById('intelligence-status');
    if (finalPercent >= 80) {
        statusEl.textContent = 'Mastered';
        statusEl.style.color = 'var(--color-success)';
    } else if (finalPercent > 0) {
        statusEl.textContent = 'In Progress';
        statusEl.style.color = 'var(--color-warning)';
    } else {
        statusEl.textContent = 'Not Started';
        statusEl.style.color = 'var(--text-secondary)';
    }

    const reqsEl = document.getElementById('intelligence-requirements');
    if (reqsEl) {
        reqsEl.innerHTML = `
            <h5 style="margin-bottom: 0.5rem; color: #fff;">Requirements:</h5>
            <ul style="font-size: 12px; color: var(--text-secondary); padding-left: 1rem;">
                <li style="color: ${passedEx === totalEx ? 'var(--color-success)' : 'inherit'};">Exercises: ${passedEx}/${totalEx}</li>
                <li style="color: ${quizDone ? 'var(--color-success)' : 'inherit'};">Quiz: ${quizDone ? 'Submitted' : 'Pending'}</li>
                <li style="color: ${projectPassed ? 'var(--color-success)' : 'inherit'};">Project: ${projectPassed ? 'Passed' : 'Pending'}</li>
            </ul>
        `;
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

// ----------------------------------------------------
// ACTIVE LEARNING TRACKING & DETERRENCE
// ----------------------------------------------------

let activeTimeSeconds = 0;
let lastPingTime = Date.now();

// Ping every 60 seconds of active time
setInterval(async () => {
    if (!document.hidden && lessonData) {
        let now = Date.now();
        let diff = (now - lastPingTime) / 1000;
        lastPingTime = now;
        
        activeTimeSeconds += diff;
        
        if (activeTimeSeconds >= 60) {
            const minutesToLog = Math.floor(activeTimeSeconds / 60);
            activeTimeSeconds = activeTimeSeconds % 60; // keep remainder
            
            try {
                await LEARNX_API.pingActivity(minutesToLog);
            } catch(e) {
                console.error("Failed to ping activity", e);
            }
        }
    } else {
        lastPingTime = Date.now(); // reset on background
    }
}, 5000); // Check every 5 seconds

document.addEventListener('visibilitychange', () => {
    if (!document.hidden) {
        lastPingTime = Date.now();
    }
});

// Copy/Paste Deterrence in learning areas
document.addEventListener('DOMContentLoaded', () => {
    const lockPaste = (e) => {
        if (e.target.tagName === 'TEXTAREA' || e.target.tagName === 'INPUT') {
            e.preventDefault();
            alert("Copy/Paste is disabled to encourage active learning and typing.");
        }
    };
    
    document.addEventListener('paste', lockPaste);
    document.addEventListener('copy', (e) => {
        if (e.target.tagName === 'TEXTAREA' || e.target.tagName === 'INPUT' || document.getSelection().toString().length > 100) {
             console.log("Large copy detected - deterrence could be applied here.");
        }
    });
});



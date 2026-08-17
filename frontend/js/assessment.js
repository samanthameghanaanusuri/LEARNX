let questions = [];
let currentIndex = 0;
let answers = {}; // Maps question_id -> student_answer string
let subjectId = null;

document.addEventListener('DOMContentLoaded', async () => {
    const urlParams = new URLSearchParams(window.location.search);
    subjectId = urlParams.get('subject_id');
    
    if (!subjectId) {
        window.location.href = '/dashboard.html';
        return;
    }

    try {
        const response = await LEARNX_API.getSubjectQuestions(subjectId);
        
        // Flatten questions grouped by concept
        const concepts = response.concepts_questions;
        for (const conceptId in concepts) {
            const conceptInfo = concepts[conceptId];
            conceptInfo.questions.forEach(q => {
                questions.push({
                    id: q.id,
                    concept_id: q.concept_id,
                    concept_name: conceptInfo.concept_name,
                    question_text: q.question_text,
                    options: q.options
                });
            });
        }

        // Shuffle questions to make it a dynamic quiz experience (optional, but let's keep them in order of concepts first to be clean)
        if (questions.length === 0) {
            document.getElementById('loading-container').innerHTML = `
                <div class="alert alert-danger" style="margin-bottom:0;">No assessment questions found for this subject.</div>
            `;
            return;
        }

        document.getElementById('subject-badge').textContent = response.subject.code;
        document.getElementById('loading-container').style.display = 'none';
        document.getElementById('assessment-panel').style.display = 'flex';
        
        displayQuestion();

    } catch (err) {
        console.error('Error loading quiz:', err);
        document.getElementById('loading-container').innerHTML = `
            <div class="alert alert-danger" style="margin-bottom:0;">Failed to load assessment.</div>
        `;
    }
});

function displayQuestion() {
    const q = questions[currentIndex];
    
    document.getElementById('concept-badge').textContent = q.concept_name;
    document.getElementById('current-question-num').textContent = currentIndex + 1;
    document.getElementById('total-questions-num').textContent = questions.length;
    document.getElementById('question-text').textContent = q.question_text;
    
    const optionsList = document.getElementById('options-list');
    optionsList.innerHTML = '';
    
    q.options.forEach(opt => {
        const div = document.createElement('div');
        const isSelected = (answers[q.id] === opt);
        div.className = `option-card ${isSelected ? 'selected' : ''}`;
        div.onclick = () => selectOption(q.id, opt);
        
        div.innerHTML = `
            <input type="radio" name="question_${q.id}" class="option-radio" ${isSelected ? 'checked' : ''}>
            <span>${opt}</span>
        `;
        optionsList.appendChild(div);
    });

    // Update navigation button labels
    document.getElementById('prev-btn').disabled = (currentIndex === 0);
    const nextBtn = document.getElementById('next-btn');
    if (currentIndex === questions.length - 1) {
        nextBtn.textContent = 'Submit Answers';
    } else {
        nextBtn.textContent = 'Next';
    }
}

function selectOption(questionId, optionValue) {
    answers[questionId] = optionValue;
    displayQuestion(); // Refresh selection visual
}

function prevQuestion() {
    if (currentIndex > 0) {
        currentIndex--;
        displayQuestion();
    }
}

async function nextQuestion() {
    const q = questions[currentIndex];
    if (!answers[q.id]) {
        alert('Please choose an answer choice before moving forward.');
        return;
    }

    if (currentIndex < questions.length - 1) {
        currentIndex++;
        displayQuestion();
    } else {
        // Last question -> submit!
        submitQuiz();
    }
}

async function submitQuiz() {
    const panel = document.getElementById('assessment-panel');
    const loading = document.getElementById('loading-container');
    
    panel.style.display = 'none';
    loading.style.display = 'flex';
    loading.innerHTML = '<p>Evaluating answers and updating knowledge state models...</p>';

    try {
        const answersList = [];
        for (const qId in answers) {
            answersList.push({
                question_id: parseInt(qId),
                student_answer: answers[qId]
            });
        }

        const response = await LEARNX_API.submitAssessment(answersList);
        
        loading.style.display = 'none';
        const resultsPanel = document.getElementById('results-panel');
        resultsPanel.style.display = 'flex';
        
        const summary = response.summary;
        document.getElementById('results-summary').innerHTML = `
            You completed the diagnostic assessment!<br>
            <strong>Score:</strong> ${summary.correct_count} / ${summary.total_submitted} correct (${Math.round(summary.score_percent)}% accuracy).
        `;

        document.getElementById('results-diag-btn').href = `/diagnosis.html?subject_id=${subjectId}`;

    } catch (err) {
        console.error('Error submitting quiz answers:', err);
        loading.style.display = 'none';
        panel.style.display = 'flex';
        alert('Failed to submit assessment answers. Try again.');
    }
}

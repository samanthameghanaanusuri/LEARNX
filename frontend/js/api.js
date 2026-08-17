const getApiBase = () => {
    // If running locally (e.g. VS Code Live Server on port 5500, or directly via file://)
    const isLocal = window.location.hostname === 'localhost' || 
                    window.location.hostname === '127.0.0.1' || 
                    window.location.protocol === 'file:';
    
    if (isLocal) {
        return 'http://127.0.0.1:5000/api';
    }
    
    // PRODUCTION / NETLIFY
    // If the frontend is hosted on Netlify, the requests must point to a deployed backend.
    // Replace 'YOUR_DEPLOYED_BACKEND_URL' with the actual production Flask server URL (e.g., https://learnx-backend.onrender.com).
    return 'https://YOUR_DEPLOYED_BACKEND_URL/api'; 
};

const API_BASE = getApiBase();

async function apiRequest(endpoint, method = 'GET', body = null) {
    const headers = {
        'Content-Type': 'application/json'
    };

    // Attach student token/id header if logged in
    const studentId = localStorage.getItem('student_id');
    if (studentId) {
        headers['X-Student-ID'] = studentId;
    }

    const options = {
        method,
        headers
    };

    if (body) {
        options.body = JSON.stringify(body);
    }

    try {
        const response = await fetch(`${API_BASE}${endpoint}`, options);
        const contentType = response.headers.get("content-type");
        
        let data = null;
        if (contentType && contentType.indexOf("application/json") !== -1) {
            data = await response.json();
        } else {
            const raw = await response.text();
            throw new Error(`Server returned unexpected format (${response.status}). Raw: ${raw.substring(0, 100)}...`);
        }
        
        if (!response.ok) {
            throw new Error(data.error || 'API Request failed');
        }
        
        return data;
    } catch (error) {
        console.error(`API Error on ${endpoint}:`, error);
        throw error;
    }
}

const LEARNX_API = {
    // Auth
    async register(username, email, password) {
        const data = await apiRequest('/auth/register', 'POST', { username, email, password });
        if (data.student && data.student.id) {
            localStorage.setItem('student_id', data.student.id);
            localStorage.setItem('student_name', data.student.username);
        }
        return data;
    },

    async login(username, password) {
        const data = await apiRequest('/auth/login', 'POST', { username, password });
        if (data.student && data.student.id) {
            localStorage.setItem('student_id', data.student.id);
            localStorage.setItem('student_name', data.student.username);
        }
        return data;
    },

    async logout() {
        try {
            await apiRequest('/auth/logout', 'POST');
        } finally {
            localStorage.removeItem('student_id');
            localStorage.removeItem('student_name');
        }
    },

    async forgotPassword(email) {
        return await apiRequest('/auth/forgot-password', 'POST', { email });
    },

    async resetPassword(token, newPassword) {
        return await apiRequest('/auth/reset-password', 'POST', { token, new_password: newPassword });
    },

    async getCurrentStudent() {
        return await apiRequest('/auth/me');
    },

    // Subjects & Concept Maps
    async getSubjects() {
        return await apiRequest('/concepts/subjects');
    },

    async getSubjectMap(subjectId) {
        return await apiRequest(`/concepts/subjects/${subjectId}/map`);
    },

    // Assessments
    async getSubjectQuestions(subjectId) {
        return await apiRequest(`/assessments/subjects/${subjectId}/questions`);
    },

    async submitAssessment(answers) {
        return await apiRequest('/assessments/submit', 'POST', { answers });
    },

    // Performance (BKT & History)
    async recordAttempt(studentId, questionId, studentAnswer) {
        return await apiRequest('/performance/attempt', 'POST', {
            student_id: studentId,
            question_id: questionId,
            student_answer: studentAnswer
        });
    },

    async getKnowledgeState(studentId, subjectId) {
        return await apiRequest(`/performance/knowledge-state/${studentId}/${subjectId}`);
    },

    async getKnowledgeHistory(studentId, conceptId) {
        return await apiRequest(`/performance/knowledge-history/${studentId}/${conceptId}`);
    },

    // Diagnosis
    async runDiagnosis(subjectId) {
        return await apiRequest('/diagnosis/run', 'POST', { subject_id: subjectId });
    },

    async getDiagnosisHistory() {
        return await apiRequest('/diagnosis/history');
    },

    // Intervention / Recovery
    async getActiveIntervention() {
        return await apiRequest('/intervention/active');
    },

    async completeIntervention(interventionId, studentAnswer) {
        return await apiRequest('/intervention/complete', 'POST', {
            intervention_id: interventionId,
            student_answer: studentAnswer
        });
    },

    // Progress & Dashboard
    async getProgressSummary() {
        return await apiRequest('/progress/summary');
    },
    async getDashboardSummary() {
        return await apiRequest('/progress/dashboard');
    },
    async pingActivity(minutes) {
        return await apiRequest('/progress/ping', 'POST', { active_minutes: minutes });
    },

    // Courses
    async getCourses() {
        return await apiRequest('/courses/');
    },
    async getCourse(courseId) {
        return await apiRequest(`/courses/${courseId}`);
    },
    async getCourseModules(courseId) {
        return await apiRequest(`/courses/${courseId}/modules`);
    },
    async getLesson(lessonId) {
        return await apiRequest(`/courses/lessons/${lessonId}`);
    },
    async enrollCourse(courseId) {
        return await apiRequest(`/courses/${courseId}/enroll`, 'POST');
    },
    async getCourseProgress(courseId) {
        return await apiRequest(`/courses/${courseId}/progress`);
    },
    async completeLesson(lessonId) {
        return await apiRequest(`/courses/lessons/${lessonId}/complete`, 'POST');
    },
    async submitQuiz(lessonId, quizQuestionId, answer) {
        return await apiRequest(`/courses/lessons/${lessonId}/quiz`, 'POST', { quiz_question_id: quizQuestionId, answer });
    },
    async submitQuizBulk(lessonId, answers) {
        return await apiRequest(`/courses/lessons/${lessonId}/quiz/bulk`, 'POST', { answers });
    },
    async runCode(language, code, stdin = '') {
        return await apiRequest('/code/run', 'POST', { language, code, stdin });
    },
    async submitExercise(exerciseId, code) {
        return await apiRequest(`/courses/exercises/${exerciseId}/submit`, 'POST', { code });
    },
    async getProject(projectId) {
        return await apiRequest(`/courses/projects/${projectId}`);
    },
    async submitProject(projectId, code) {
        return await apiRequest(`/courses/projects/${projectId}/submit`, 'POST', { code });
    },
    async getProjectProgress(projectId) {
        return await apiRequest(`/courses/projects/${projectId}/progress`);
    }
};

// Check authentication state for secure pages
function checkAuth() {
    const studentId = localStorage.getItem('student_id');
    if (!studentId && !window.location.pathname.endsWith('auth.html') && !window.location.pathname.endsWith('index.html') && window.location.pathname !== '/') {
        window.location.href = '/auth.html';
    }
}

// Display logged in student name if present
document.addEventListener('DOMContentLoaded', () => {
    const userNameEl = document.getElementById('navbar-username');
    if (userNameEl) {
        const studentName = localStorage.getItem('student_name');
        userNameEl.textContent = studentName ? studentName : 'Student';
    }
});

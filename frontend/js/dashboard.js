document.addEventListener('DOMContentLoaded', async () => {
    checkAuth();
    
    const logoutBtn = document.getElementById('logout-btn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', async (e) => {
            e.preventDefault();
            await LEARNX_API.logout();
            window.location.href = '/auth.html';
        });
    }

    await loadDashboard();
});

async function loadDashboard() {
    try {
        const data = await LEARNX_API.getDashboardSummary();
        
        // Header / Welcome
        const welcome = document.getElementById('welcome-message');
        if (welcome && data.student) {
            welcome.textContent = `Welcome back, ${data.student.username}!`;
        }
        
        const navbarUser = document.getElementById('navbar-username');
        if (navbarUser && data.student) {
            navbarUser.textContent = `${data.student.username} ▼`;
        }

        // Stats
        document.getElementById('stat-total-courses').textContent = data.total_courses || 0;
        document.getElementById('stat-courses-enrolled').textContent = data.courses_enrolled || 0;
        document.getElementById('stat-overall-progress').textContent = `${data.overall_progress || 0}%`;
        document.getElementById('stat-learning-time').textContent = formatMinutes(data.learning_time_minutes);
        document.getElementById('stat-streak').textContent = `${data.current_streak || 0} days`;
        document.getElementById('stat-longest-streak').textContent = `${data.longest_streak || 0} days`;

        // Courses Enrolled List
        const coursesList = document.getElementById('my-courses-list');
        if (data.courses && data.courses.length > 0) {
            coursesList.innerHTML = data.courses.map(c => `
                <div class="course-card">
                    <div style="flex: 1;">
                        <h4 style="margin: 0 0 0.25rem 0; font-size: 1.15rem;">${c.title}</h4>
                        <div style="font-size: 0.8rem; color: var(--text-secondary); margin-bottom: 0.5rem; text-transform: uppercase; font-weight: bold;">
                            ${c.difficulty || 'Intermediate'}
                        </div>
                        <div class="progress-bar-container">
                            <div class="progress-bar-fill" style="width: ${c.progress}%;"></div>
                        </div>
                        <div style="font-size: 0.8rem; color: var(--text-secondary); margin-top: 0.35rem;">
                            Lessons completed: ${c.completed_lessons} / ${c.total_lessons}
                        </div>
                    </div>
                    <div style="margin-left: 2rem; font-weight: bold; color: var(--color-primary); font-size: 1.2rem;">
                        ${Math.round(c.progress)}%
                    </div>
                    <div style="margin-left: 1.5rem;">
                        <a href="/course.html?id=${c.id}" class="btn btn-secondary">Resume</a>
                    </div>
                </div>
            `).join('');
        } else {
            coursesList.innerHTML = `
                <div class="glass-panel text-center" style="padding: 2rem;">
                    <p style="color: var(--text-secondary); margin-bottom: 1rem;">You haven't enrolled in any courses yet.</p>
                    <a href="/courses.html" class="btn btn-primary">Browse Courses</a>
                </div>
            `;
        }

        // Continue Learning Suggestion
        const continueContent = document.getElementById('continue-learning-content');
        if (data.continue_learning) {
            continueContent.innerHTML = `
                <div style="margin-bottom: 1rem;">
                    <p style="margin: 0 0 0.5rem 0; font-size: 0.875rem; color: var(--color-primary); font-weight: bold;">${data.continue_learning.course_title}</p>
                    <h4 style="margin: 0 0 0.5rem 0; font-size: 1.1rem;">${data.continue_learning.lesson_title}</h4>
                    <p style="margin: 0; font-size: 0.875rem; color: var(--text-secondary);">${data.continue_learning.module_title}</p>
                </div>
                <div class="progress-bar-container" style="margin-bottom: 1.25rem;">
                    <div class="progress-bar-fill" style="width: ${data.continue_learning.progress}%;"></div>
                </div>
                <a href="/lesson.html?id=${data.continue_learning.lesson_id}" class="btn btn-primary" style="display: block; text-align: center;">Continue Lesson</a>
            `;
        } else {
            continueContent.innerHTML = `
                <p class="text-secondary" style="font-size: 0.875rem; margin: 0;">You have no active lessons in progress.</p>
                <a href="/courses.html" class="btn btn-primary" style="display: block; text-align: center; margin-top: 1rem;">Browse Courses</a>
            `;
        }

        // Diagnostic Pills
        const diagStrong = document.getElementById('diag-strong');
        const diagWeak = document.getElementById('diag-weak');

        if (data.diagnostic.strong && data.diagnostic.strong.length > 0) {
            diagStrong.innerHTML = data.diagnostic.strong.map(c => 
                `<span class="diagnostic-pill pill-strong">${c}</span>`
            ).join('');
        } else {
            diagStrong.innerHTML = `<span class="text-secondary" style="font-size: 0.875rem;">Not enough data yet.</span>`;
        }
        
        if (data.diagnostic.weak && data.diagnostic.weak.length > 0) {
            diagWeak.innerHTML = data.diagnostic.weak.map(c => 
                `<span class="diagnostic-pill pill-weak">${c}</span>`
            ).join('');
        } else {
            diagWeak.innerHTML = `<span class="text-secondary" style="font-size: 0.875rem;">Not enough data yet.</span>`;
        }

        // Recent Activity
        const activityList = document.getElementById('recent-activity-list');
        if (data.recent_activity && data.recent_activity.length > 0) {
            activityList.innerHTML = data.recent_activity.map(act => {
                const dateStr = new Date(act.timestamp).toLocaleString();
                return `
                    <div class="activity-item">
                        <div class="activity-desc">${act.description}</div>
                        <div class="activity-time">${dateStr}</div>
                    </div>
                `;
            }).join('');
        } else {
            activityList.innerHTML = `<p class="text-secondary" style="font-size: 0.875rem; margin: 0;">No recent activity recorded.</p>`;
        }

    } catch (err) {
        console.error(err);
        const coursesList = document.getElementById('my-courses-list');
        if (coursesList) {
            coursesList.innerHTML = `
                <div class="glass-panel text-center" style="border-color: var(--color-danger); padding: 2rem;">
                    <p style="color: var(--color-danger); margin-bottom: 0;">Failed to load dashboard data. Please try again.</p>
                </div>
            `;
        }
    }
}

function formatMinutes(minutes) {
    if (!minutes) return '0m';
    if (minutes < 60) return `${minutes}m`;
    const h = Math.floor(minutes / 60);
    const m = minutes % 60;
    return `${h}h ${m}m`;
}

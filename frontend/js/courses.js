document.addEventListener('DOMContentLoaded', () => {
    checkAuth();
    loadCourses();

    // Bind Search Input
    document.getElementById('course-search').addEventListener('input', filterCourses);
    
    // Bind Filter Dropdowns
    document.getElementById('filter-difficulty').addEventListener('change', filterCourses);
    document.getElementById('filter-sort').addEventListener('change', filterCourses);

    // Bind Category Tab Buttons
    const tabs = document.querySelectorAll('.category-tab');
    tabs.forEach(tab => {
        tab.addEventListener('click', (e) => {
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            filterCourses();
        });
    });

    // Event Delegation for Course Grid
    const courseGrid = document.getElementById('course-grid');
    if (courseGrid) {
        courseGrid.addEventListener('click', (e) => {
            const btn = e.target.closest('.view-course-btn');
            if (btn) {
                const courseId = btn.getAttribute('data-id');
                if (courseId) {
                    viewCourse(courseId);
                } else {
                    console.error("Navigation Error: No course ID found on button.");
                }
            }
        });
    }

    // Bind Logout
    const logoutBtn = document.getElementById('logout-btn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', async (e) => {
            e.preventDefault();
            await LEARNX_API.logout();
            window.location.href = '/auth.html';
        });
    }
});

let allCourses = [];
let activeCategory = 'all';

const courseIcons = {
    'python': '🐍',
    'java': '☕',
    'html': '🌐',
    'css': '🎨',
    'javascript': '⚡',
    'c': '🅲',
    'cpp': '🚀',
    'cyber': '🛡️',
    'dbms': '💾',
    'dsa': '📊',
    'default': '📚'
};

const courseGradients = {
    'python': 'linear-gradient(135deg, rgba(255, 223, 0, 0.08) 0%, rgba(0, 112, 187, 0.08) 100%)',
    'java': 'linear-gradient(135deg, rgba(227, 26, 28, 0.08) 0%, rgba(240, 127, 0, 0.08) 100%)',
    'html': 'linear-gradient(135deg, rgba(227, 76, 38, 0.08) 0%, rgba(241, 101, 41, 0.08) 100%)',
    'css': 'linear-gradient(135deg, rgba(38, 77, 228, 0.08) 0%, rgba(41, 169, 223, 0.08) 100%)',
    'javascript': 'linear-gradient(135deg, rgba(247, 223, 30, 0.08) 0%, rgba(255, 255, 255, 0.03) 100%)',
    'c': 'linear-gradient(135deg, rgba(57, 73, 171, 0.08) 0%, rgba(255, 255, 255, 0.03) 100%)',
    'cpp': 'linear-gradient(135deg, rgba(0, 89, 156, 0.08) 0%, rgba(0, 144, 218, 0.08) 100%)',
    'cyber': 'linear-gradient(135deg, rgba(16, 185, 129, 0.08) 0%, rgba(5, 150, 105, 0.08) 100%)',
    'dbms': 'linear-gradient(135deg, rgba(220, 38, 38, 0.08) 0%, rgba(79, 70, 229, 0.08) 100%)',
    'dsa': 'linear-gradient(135deg, rgba(79, 70, 229, 0.08) 0%, rgba(99, 102, 241, 0.08) 100%)',
    'default': 'linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(0, 0, 0, 0.2) 100%)'
};

function getCourseKey(title) {
    const t = title.toLowerCase();
    if (t.includes('python')) return 'python';
    if (t.includes('java ') || t.includes('java-') || t.startsWith('java')) return 'java';
    if (t.includes('javascript') || t.includes('js')) return 'javascript';
    if (t.includes('html')) return 'html';
    if (t.includes('css')) return 'css';
    if (t.includes('c++') || t.includes('cpp')) return 'cpp';
    if (t.includes('c programming')) return 'c';
    if (t.includes('cyber')) return 'cyber';
    if (t.includes('database') || t.includes('dbms')) return 'dbms';
    if (t.includes('data structure') || t.includes('dsa') || t.includes('algorithms')) return 'dsa';
    return 'default';
}

async function loadCourses() {
    try {
        const [courses, dashboardData] = await Promise.all([
            LEARNX_API.getCourses(),
            LEARNX_API.getDashboardSummary()
        ]);
        
        // Map enrolled progress
        const enrolledMap = {};
        if (dashboardData && dashboardData.courses) {
            dashboardData.courses.forEach(c => {
                enrolledMap[c.id] = c;
            });
        }
        
        allCourses = courses.map(course => {
            const enrolled = enrolledMap[course.id];
            return {
                ...course,
                is_enrolled: !!enrolled,
                progress: enrolled ? enrolled.progress : 0,
                completed_lessons: enrolled ? enrolled.completed_lessons : 0,
                total_lessons: enrolled ? enrolled.total_lessons : 0
            };
        });
        
        renderCourses(allCourses);
    } catch (error) {
        console.error("Failed to load dashboard data. Retrying with courses only:", error);
        try {
            allCourses = await LEARNX_API.getCourses();
            renderCourses(allCourses);
        } catch (err) {
            document.getElementById('course-grid').innerHTML = '<p class="error-text">Failed to load courses. Please try again later.</p>';
        }
    }
}

function renderCourses(courses) {
    const grid = document.getElementById('course-grid');
    grid.innerHTML = '';

    if (courses.length === 0) {
        grid.innerHTML = '<p class="empty-state" style="grid-column: 1/-1; text-align: center; color: var(--text-secondary); padding: 3rem;">No courses match your search or filters.</p>';
        return;
    }

    courses.forEach(course => {
        const key = getCourseKey(course.title);
        const icon = courseIcons[key] || courseIcons.default;
        const grad = courseGradients[key] || courseGradients.default;

        const card = document.createElement('div');
        card.className = 'course-card';
        card.style.background = grad;

        // Clean difficulty badge class
        const diffClass = course.difficulty.split(' ')[0].toLowerCase();

        card.innerHTML = `
            <div>
                <div class="course-icon-container">
                    ${icon}
                </div>
                <div class="badge-row">
                    <span class="badge ${diffClass}">${course.difficulty}</span>
                    <span class="badge category">${course.category}</span>
                </div>
                <h3 class="course-title">${course.title}</h3>
                <p class="course-desc">${course.description}</p>
            </div>

            <div>
                ${course.is_enrolled ? `
                    <div class="card-progress-section">
                        <div class="card-progress-label">
                            <span>Progress</span>
                            <span>${Math.round(course.progress)}%</span>
                        </div>
                        <div class="card-progress-bar">
                            <div class="card-progress-fill" style="width: ${course.progress}%;"></div>
                        </div>
                        <div style="font-size: 0.75rem; color: var(--text-secondary); margin-top: 0.4rem; font-weight: 500;">
                            ${course.completed_lessons} / ${course.total_lessons} lessons completed
                        </div>
                    </div>
                ` : ''}

                <div class="card-footer">
                    <span class="students-count">👤 Active Student</span>
                    <button class="view-course-btn" data-id="${course.id}">
                        ${course.is_enrolled ? 'Resume Course →' : 'View Course →'}
                    </button>
                </div>
            </div>
        `;
        grid.appendChild(card);
    });
}

function filterCourses() {
    const search = document.getElementById('course-search').value.toLowerCase();
    const difficulty = document.getElementById('filter-difficulty').value;
    const sort = document.getElementById('filter-sort').value;

    // Get active category tab
    const activeTab = document.querySelector('.category-tab.active');
    const category = activeTab ? activeTab.getAttribute('data-val') : 'all';

    let filtered = allCourses.filter(course => {
        const matchSearch = course.title.toLowerCase().includes(search) || course.description.toLowerCase().includes(search);
        const matchCategory = category === 'all' || course.category === category;
        const matchDifficulty = difficulty === 'all' || course.difficulty.includes(difficulty);
        
        return matchSearch && matchCategory && matchDifficulty;
    });

    // Sorting
    if (sort === 'title-asc') {
        filtered.sort((a, b) => a.title.localeCompare(b.title));
    } else if (sort === 'title-desc') {
        filtered.sort((a, b) => b.title.localeCompare(a.title));
    }

    renderCourses(filtered);
}

function viewCourse(courseId) {
    if (!courseId || isNaN(courseId)) {
        console.error("Navigation Error: Invalid course ID passed to viewCourse", courseId);
        alert("Unable to open course: Invalid course ID.");
        return;
    }
    window.location.href = `/course.html?id=${courseId}`;
}

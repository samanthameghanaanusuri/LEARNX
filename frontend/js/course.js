const urlParams = new URLSearchParams(window.location.search);
const courseId = urlParams.get('id');

let courseData = null;
let progressData = null;
let modulesData = null;

document.addEventListener('DOMContentLoaded', async () => {
    checkAuth();
    if (!courseId) {
        window.location.href = '/courses.html';
        return;
    }
    
    await loadCourse();
    
    document.getElementById('btn-enroll').addEventListener('click', async () => {
        try {
            await LEARNX_API.enrollCourse(courseId);
            window.location.reload();
        } catch (e) {
            alert('Error enrolling: ' + e.message);
        }
    });
});

async function loadCourse() {
    try {
        courseData = await LEARNX_API.getCourse(courseId);
        modulesData = await LEARNX_API.getCourseModules(courseId);
        
        try {
            progressData = await LEARNX_API.getCourseProgress(courseId);
            renderEnrolledCourse();
        } catch (e) {
            // Not enrolled (403 usually)
            renderUnenrolledCourse();
        }
    } catch (error) {
        document.getElementById('course-header').innerHTML = '<p class="error-text">Course not found.</p>';
    }
}

function renderUnenrolledCourse() {
    const header = document.getElementById('course-header');
    header.innerHTML = `
        <h2>${courseData.title}</h2>
        <p>${courseData.description}</p>
        <span class="badge">${courseData.difficulty}</span>
    `;
    document.getElementById('enrollment-section').style.display = 'block';
    renderModules(false);
}

function renderEnrolledCourse() {
    const header = document.getElementById('course-header');
    header.innerHTML = `
        <h2>${courseData.title}</h2>
        <p>Progress: ${Math.round(progressData.progress_percentage)}%</p>
        <div class="progress-bar-container">
            <div class="progress-bar" style="width: ${progressData.progress_percentage}%"></div>
        </div>
        <p>${progressData.completed_lessons} of ${progressData.total_lessons} lessons completed</p>
    `;
    document.getElementById('enrollment-section').style.display = 'none';
    renderModules(true);
}

function renderModules(isEnrolled) {
    const container = document.getElementById('modules-container');
    container.innerHTML = '';

    modulesData.forEach((mod, index) => {
        const modEl = document.createElement('div');
        modEl.className = 'glass-panel module-accordion';
        
        // Header
        const header = document.createElement('div');
        header.className = 'module-header';
        header.innerHTML = `<h3>Module ${index + 1}: ${mod.title}</h3><span>▼</span>`;
        
        // Lessons list
        const list = document.createElement('div');
        list.className = 'lesson-list';
        
        mod.lessons.forEach(lesson => {
            const lItem = document.createElement('div');
            lItem.className = 'lesson-item';
            
            let statusIcon = '○';
            let statusClass = 'status-not_started';
            
            if (isEnrolled && progressData.lesson_statuses[lesson.id] === 'completed') {
                statusIcon = '✓';
                statusClass = 'status-completed';
            }

            lItem.innerHTML = `
                <span>${lesson.title}</span>
                <span class="status-icon ${statusClass}">${statusIcon}</span>
            `;
            
            if (isEnrolled) {
                lItem.addEventListener('click', () => {
                    window.location.href = `/lesson.html?id=${lesson.id}`;
                });
            } else {
                lItem.style.opacity = '0.5';
                lItem.title = 'Enroll to access';
            }
            list.appendChild(lItem);
        });

        header.addEventListener('click', () => {
            list.classList.toggle('active');
        });
        
        // Expand first module by default
        if (index === 0) list.classList.add('active');

        modEl.appendChild(header);
        modEl.appendChild(list);
        container.appendChild(modEl);
    });
}

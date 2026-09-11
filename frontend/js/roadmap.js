/**
 * LEARNX — Standalone Career Roadmap Interactive Module
 */

let allRoadmaps = [];

document.addEventListener('DOMContentLoaded', async () => {
    initRoadmapView();
});

async function initRoadmapView() {
    const urlParams = new URLSearchParams(window.location.search);
    const courseParam = urlParams.get('course') || urlParams.get('slug') || urlParams.get('key');

    try {
        const response = await LEARNX_API.getRoadmaps();
        allRoadmaps = response.roadmaps || [];

        if (courseParam) {
            loadRoadmapDetail(courseParam);
        } else {
            renderCatalogGrid(allRoadmaps);
        }
    } catch (err) {
        console.error('Error fetching roadmaps:', err);
        showError('Failed to load roadmap data.');
    }
}

function renderCatalogGrid(roadmaps) {
    const catalogWrapper = document.getElementById('roadmap-catalog-wrapper');
    const detailWrapper = document.getElementById('roadmap-detail-wrapper');
    const grid = document.getElementById('roadmap-grid');

    if (detailWrapper) detailWrapper.style.display = 'none';
    if (catalogWrapper) catalogWrapper.style.display = 'block';

    if (!grid) return;
    grid.innerHTML = '';

    if (roadmaps.length === 0) {
        grid.innerHTML = `<div class="alert alert-info">No roadmaps available.</div>`;
        return;
    }

    roadmaps.forEach(rm => {
        const card = document.createElement('div');
        card.className = 'roadmap-card';

        card.innerHTML = `
            <div>
                <div class="roadmap-card-header">
                    <div class="roadmap-card-icon">${rm.icon || '🚀'}</div>
                    <div>
                        <div class="roadmap-card-category">${escapeHtml(rm.category)}</div>
                        <h3 class="roadmap-card-title">${escapeHtml(rm.title)}</h3>
                    </div>
                </div>
                <div class="roadmap-card-tagline">${escapeHtml(rm.tagline)}</div>
            </div>
            <div>
                <div class="roadmap-card-meta">
                    <span>⚡ ${rm.difficulty_progression}</span>
                    <span>💼 ${rm.career_roles_count} Roles</span>
                </div>
                <button class="roadmap-card-btn" onclick="openRoadmapDetail('${rm.key}')">
                    Explore Career Roadmap →
                </button>
            </div>
        `;
        grid.appendChild(card);
    });

    setupFilterButtons();
}

function setupFilterButtons() {
    const buttons = document.querySelectorAll('.roadmap-filter-btn');
    buttons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            buttons.forEach(b => b.classList.remove('active'));
            e.target.classList.add('active');

            const filter = e.target.getAttribute('data-filter');
            if (filter === 'all') {
                renderCatalogGrid(allRoadmaps);
            } else {
                const filtered = allRoadmaps.filter(r => 
                    (r.category || '').toLowerCase().includes(filter.toLowerCase()) ||
                    (r.title || '').toLowerCase().includes(filter.toLowerCase())
                );
                renderCatalogGrid(filtered);
            }
        });
    });
}

function openRoadmapDetail(key) {
    const newUrl = window.location.pathname + '?course=' + key;
    window.history.pushState({ key: key }, '', newUrl);
    loadRoadmapDetail(key);
}

function backToCatalog() {
    const newUrl = window.location.pathname;
    window.history.pushState({}, '', newUrl);
    renderCatalogGrid(allRoadmaps);
}

async function loadRoadmapDetail(key) {
    const catalogWrapper = document.getElementById('roadmap-catalog-wrapper');
    const detailWrapper = document.getElementById('roadmap-detail-wrapper');

    if (catalogWrapper) catalogWrapper.style.display = 'none';
    if (detailWrapper) detailWrapper.style.display = 'block';

    const detailContainer = document.getElementById('roadmap-detail-content');
    if (!detailContainer) return;

    detailContainer.innerHTML = `
        <div style="text-align: center; padding: 3rem;">
            <p>Loading Career Roadmap details...</p>
        </div>
    `;

    try {
        const response = await LEARNX_API.getRoadmapDetail(key);
        const data = response.roadmap;
        if (!data) {
            detailContainer.innerHTML = `<div class="alert alert-danger">Roadmap not found for key: ${escapeHtml(key)}</div>`;
            return;
        }

        renderRoadmapDetail(data, detailContainer);
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } catch (err) {
        console.error('Error loading roadmap detail:', err);
        detailContainer.innerHTML = `<div class="alert alert-danger">Failed to load roadmap detail.</div>`;
    }
}

function renderRoadmapDetail(rm, container) {
    // 1. Why Learn list
    const whyItems = (rm.why_learn || []).map(w => `<li>${escapeHtml(w)}</li>`).join('');
    
    // 2. What you will learn list
    const whatItems = (rm.what_you_will_learn || []).map(w => `<li>${escapeHtml(w)}</li>`).join('');

    // 3. Visual Node Flow Steps
    const nodesHtml = (rm.skill_stages || []).map((stage, idx) => {
        const topicsChips = (stage.topics || []).map(t => `<span class="roadmap-topic-chip">${escapeHtml(t)}</span>`).join('');
        const arrow = (idx < rm.skill_stages.length - 1) ? '<div class="roadmap-connector-line"></div>' : '';
        return `
            <div class="roadmap-node-card">
                <div class="roadmap-node-stage">${escapeHtml(stage.stage)}</div>
                <div class="roadmap-node-title">${escapeHtml(stage.title)}</div>
                <div class="roadmap-node-desc">${escapeHtml(stage.description)}</div>
                <div class="roadmap-node-topics">${topicsChips}</div>
            </div>
            ${arrow}
        `;
    }).join('');

    // 4. Specializations
    const specsHtml = (rm.specialization_branches || []).map(s => {
        const toolsChips = (s.tools || []).map(t => `<span class="roadmap-topic-chip" style="background: rgba(168, 85, 247, 0.12); border-color: rgba(168, 85, 247, 0.3); color: #e9d5ff;">${escapeHtml(t)}</span>`).join('');
        return `
            <div class="roadmap-spec-card">
                <div class="roadmap-spec-title">✨ ${escapeHtml(s.name)}</div>
                <div class="roadmap-spec-desc">${escapeHtml(s.desc)}</div>
                <div style="display: flex; flex-wrap: wrap; gap: 0.4rem;">${toolsChips}</div>
            </div>
        `;
    }).join('');

    // 5. Projects
    const projectsHtml = (rm.projects || []).map(p => {
        const badgeClass = (p.level || '').toLowerCase();
        const skillsChips = (p.skills || []).map(s => `<span class="roadmap-topic-chip">${escapeHtml(s)}</span>`).join('');
        return `
            <div class="roadmap-project-card">
                <span class="roadmap-level-badge ${badgeClass}">${escapeHtml(p.level)} Project</span>
                <div class="roadmap-project-title">${escapeHtml(p.title)}</div>
                <div class="roadmap-project-desc">${escapeHtml(p.description)}</div>
                <div style="display: flex; flex-wrap: wrap; gap: 0.4rem;">${skillsChips}</div>
            </div>
        `;
    }).join('');

    // 6. Careers
    const careersHtml = (rm.career_directions || []).map(c => `
        <div class="roadmap-career-card">
            <div class="roadmap-career-role">🎯 ${escapeHtml(c.role)}</div>
            <div class="roadmap-career-skills">Stack: ${escapeHtml(c.skills_required)}</div>
            <div class="roadmap-career-desc">${escapeHtml(c.description)}</div>
        </div>
    `).join('');

    // 7. Opportunities
    const oppsHtml = (rm.opportunities || []).map(o => `<li>${escapeHtml(o)}</li>`).join('');

    // 8. Additional Skills
    const addSkillsHtml = (rm.additional_skills || []).map(s => `
        <div class="roadmap-companion-chip">${escapeHtml(s)}</div>
    `).join('');

    container.innerHTML = `
        <!-- Top Back Button -->
        <button class="roadmap-back-btn" onclick="backToCatalog()">
            ← Back to All Roadmaps
        </button>

        <!-- Hero Card -->
        <div class="roadmap-detail-hero">
            <div class="roadmap-detail-header">
                <div class="roadmap-detail-icon">${rm.icon || '🚀'}</div>
                <div>
                    <h1 class="roadmap-detail-title">${escapeHtml(rm.title)}</h1>
                    <p class="roadmap-detail-tagline">${escapeHtml(rm.tagline)}</p>
                </div>
            </div>
            <div style="display: flex; gap: 1.5rem; flex-wrap: wrap; font-size: 0.9rem; color: #cbd5e1; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.08);">
                <span>📊 <strong>Progression:</strong> ${escapeHtml(rm.difficulty_progression)}</span>
                <span>🏷️ <strong>Category:</strong> ${escapeHtml(rm.category)}</span>
            </div>
        </div>

        <!-- Summary Grid -->
        <div class="roadmap-summary-grid">
            <div class="roadmap-summary-box">
                <h3>💡 Why Learn This Skill Path?</h3>
                <ul>${whyItems}</ul>
            </div>
            <div class="roadmap-summary-box">
                <h3>🎓 What You Will Master</h3>
                <ul>${whatItems}</ul>
            </div>
        </div>

        <!-- Visual Node Pipeline Flow -->
        <div class="roadmap-pipeline-section">
            <h2 class="roadmap-section-title">🗺️ Visual Skill Roadmap Pipeline</h2>
            <p class="roadmap-section-sub">Follow this milestone progression from fundamentals to real-world integration.</p>
            <div class="roadmap-pipeline-flow">
                ${nodesHtml}
            </div>
        </div>

        <!-- Specialization Tracks -->
        ${rm.specialization_branches && rm.specialization_branches.length ? `
            <div class="roadmap-pipeline-section">
                <h2 class="roadmap-section-title">🔀 Specialization Branches</h2>
                <p class="roadmap-section-sub">Choose a career track after mastering core fundamentals.</p>
                <div class="roadmap-specs-grid">
                    ${specsHtml}
                </div>
            </div>
        ` : ''}

        <!-- Portfolio Projects -->
        <div class="roadmap-pipeline-section">
            <h2 class="roadmap-section-title">💻 Portfolio Projects To Build</h2>
            <p class="roadmap-section-sub">Demonstrate your skills to recruiters with specific hands-on projects.</p>
            <div class="roadmap-projects-grid">
                ${projectsHtml}
            </div>
        </div>

        <!-- Career Roles -->
        <div class="roadmap-pipeline-section">
            <h2 class="roadmap-section-title">👔 Targeted Career Roles</h2>
            <p class="roadmap-section-sub">Job positions unlocked by this skill roadmap and companion technologies.</p>
            <div class="roadmap-careers-grid">
                ${careersHtml}
            </div>
        </div>

        <!-- Opportunities & Next Steps -->
        <div class="roadmap-summary-grid">
            <div class="roadmap-summary-box">
                <h3>🚀 Internship & Opportunity Categories</h3>
                <ul>${oppsHtml}</ul>
            </div>
            <div class="roadmap-summary-box">
                <h3>🛠️ Companion Technologies to Learn</h3>
                <div class="roadmap-chips-container" style="margin-bottom: 0; margin-top: 0.5rem;">
                    ${addSkillsHtml}
                </div>
            </div>
        </div>

        <!-- Final Call to Action -->
        <div class="roadmap-learnx-link-box">
            <h3>Ready to start your ${escapeHtml(rm.title)} journey?</h3>
            <p>${escapeHtml(rm.next_steps || 'Start with the interactive lessons in the LEARNX course.')}</p>
            <a href="/courses.html" class="roadmap-start-course-btn">
                Explore LEARNX Interactive Courses →
            </a>
        </div>
    `;
}

function showError(msg) {
    const grid = document.getElementById('roadmap-grid');
    if (grid) {
        grid.innerHTML = `<div class="alert alert-danger">${escapeHtml(msg)}</div>`;
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

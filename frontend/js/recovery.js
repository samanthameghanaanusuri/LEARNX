let activeInterventionId = null;
let selectedOptionVal = null;
let interventionData = null;

document.addEventListener('DOMContentLoaded', async () => {
    try {
        const res = await LEARNX_API.getActiveIntervention();
        
        document.getElementById('loading-recovery').style.display = 'none';

        if (!res || !res.intervention) {
            document.getElementById('no-active-recovery').style.display = 'flex';
            return;
        }

        interventionData = res.intervention;
        activeInterventionId = res.intervention.id;

        document.getElementById('recovery-panel').style.display = 'grid';
        document.getElementById('recovery-concept-title').textContent = `Recovery: ${res.intervention.concept_name}`;
        
        // Render study guide content
        const guideHtml = parseGuideMarkdown(res.intervention.content_parsed.guide);
        document.getElementById('recovery-guide-content').innerHTML = guideHtml;

        // Render question & options
        document.getElementById('recovery-question-text').textContent = res.intervention.content_parsed.post_question;
        renderOptions(res.intervention.content_parsed.options);

    } catch (err) {
        console.error('Error fetching active intervention:', err);
        document.getElementById('loading-recovery').innerHTML = `
            <div class="alert alert-danger" style="margin-bottom:0;">Failed to load recovery material.</div>
        `;
    }
});

function parseGuideMarkdown(markdown) {
    if (!markdown) return '';
    
    // Quick simple parser for study guides
    let html = markdown;
    
    // Replace headers
    html = html.replace(/### (.*)/g, '<h3>$1</h3>');
    
    // Replace strong text
    html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    
    // Replace list items
    // Parse lines starting with '- ' to '<li>' and wrap sequences in '<ul>'
    const lines = html.split('\n');
    let insideList = false;
    
    for (let i = 0; i < lines.length; i++) {
        let line = lines[i].trim();
        if (line.startsWith('- ')) {
            const content = line.substring(2);
            if (!insideList) {
                lines[i] = '<ul><li>' + content + '</li>';
                insideList = true;
            } else {
                lines[i] = '<li>' + content + '</li>';
            }
        } else {
            if (insideList) {
                lines[i] = '</ul>' + lines[i];
                insideList = false;
            }
        }
    }
    
    if (insideList) {
        lines.push('</ul>');
    }
    
    html = lines.join('\n');
    // Replace newlines with breaks for normal paragraphs
    html = html.replace(/\n\n/g, '<br><br>');
    
    return html;
}

function renderOptions(options) {
    const list = document.getElementById('recovery-options-list');
    list.innerHTML = '';
    
    options.forEach(opt => {
        const div = document.createElement('div');
        const isSelected = (selectedOptionVal === opt);
        div.className = `option-card ${isSelected ? 'selected' : ''}`;
        div.onclick = () => selectOption(opt);
        
        div.innerHTML = `
            <input type="radio" name="recovery_option" class="option-radio" ${isSelected ? 'checked' : ''}>
            <span>${opt}</span>
        `;
        list.appendChild(div);
    });
}

function selectOption(value) {
    selectedOptionVal = value;
    renderOptions(interventionData.content_parsed.options); // Refresh highlights
}

async function submitRecovery() {
    if (!selectedOptionVal) {
        alert('Please choose an answer choice before verifying recovery.');
        return;
    }

    const feedback = document.getElementById('recovery-feedback');
    const submitBtn = document.getElementById('recovery-submit-btn');
    const dashBtn = document.getElementById('recovery-dash-btn');

    feedback.style.display = 'none';
    submitBtn.setAttribute('disabled', 'disabled');
    submitBtn.textContent = 'Verifying...';

    try {
        const res = await LEARNX_API.completeIntervention(activeInterventionId, selectedOptionVal);
        
        submitBtn.removeAttribute('disabled');
        submitBtn.textContent = 'Verify Recovery Mastery';

        if (res.success) {
            feedback.className = 'alert alert-success';
            feedback.innerHTML = `<strong>🎉 Recovery Verified!</strong><br>${res.message}`;
            feedback.style.display = 'flex';
            
            submitBtn.style.display = 'none';
            dashBtn.style.display = 'block';
            
            // Highlight option card as success (disable pointer events to prevent changes)
            document.querySelectorAll('.option-card').forEach(card => {
                card.style.pointerEvents = 'none';
            });
        } else {
            feedback.className = 'alert alert-danger';
            feedback.innerHTML = `<strong>❌ Incorrect Answer</strong><br>${res.message}`;
            feedback.style.display = 'flex';
        }

    } catch (err) {
        console.error('Error submitting recovery response:', err);
        submitBtn.removeAttribute('disabled');
        submitBtn.textContent = 'Verify Recovery Mastery';
        feedback.className = 'alert alert-danger';
        feedback.textContent = 'Failed to submit answer. Try again.';
        feedback.style.display = 'flex';
    }
}

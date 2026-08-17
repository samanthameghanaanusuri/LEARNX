document.addEventListener('DOMContentLoaded', async () => {
    const urlParams = new URLSearchParams(window.location.search);
    const subjectId = urlParams.get('subject_id');
    const studentId = localStorage.getItem('student_id');

    if (!subjectId || !studentId) {
        window.location.href = '/dashboard.html';
        return;
    }

    try {
        // Run diagnosis on backend
        const diagRes = await LEARNX_API.runDiagnosis(subjectId);
        
        // Fetch student knowledge state
        const stateRes = await LEARNX_API.getKnowledgeState(studentId, subjectId);
        
        // Fetch subject metadata
        const subjectMap = await LEARNX_API.getSubjectMap(subjectId);
        const subjectCode = subjectMap.subject.code;

        document.getElementById('loading-diag').style.display = 'none';
        document.getElementById('diag-panel').style.display = 'grid';

        let rootCauseId = null;
        let prereqWeakIds = [];

        const resultsBox = document.getElementById('diag-results-box');
        const actionContainer = document.getElementById('diag-action-container');

        if (diagRes && diagRes.diagnosis) {
            rootCauseId = diagRes.diagnosis.root_cause_concept_id;
            prereqWeakIds = diagRes.diagnosis.prerequisite_weakness_ids || [];
            
            resultsBox.innerHTML = `
                <div class="alert alert-danger" style="flex-direction: column; gap: 0.5rem;">
                    <strong style="font-size: 1.05rem;">🔴 Blocker Identified</strong>
                    <span style="font-size: 0.9rem;">Prerequisite failure diagnosed in concept: <strong>${diagRes.root_cause_concept.name}</strong>.</span>
                </div>
                <div style="margin-top: 1rem; display: flex; flex-direction: column; gap: 0.75rem;">
                    <p style="font-size: 0.95rem; line-height: 1.6; margin-bottom: 0;">
                        ${diagRes.diagnosis.diagnostic_summary}
                    </p>
                    ${prereqWeakIds.length > 0 ? `
                        <p style="font-size: 0.9rem; margin-top: 0.5rem; margin-bottom: 0;">
                            <strong>Prerequisite Weaknesses in Chain:</strong><br>
                            ${prereqWeakIds.map(id => {
                                const c = stateRes.concepts.find(item => item.concept_id === id);
                                return c ? `<span class="badge badge-prereq" style="margin-top: 0.25rem; margin-right: 0.25rem;">${c.concept_name}</span>` : '';
                            }).join('')}
                        </p>
                    ` : ''}
                </div>
            `;
            
            actionContainer.innerHTML = `
                <a href="/recovery.html" class="btn btn-primary" style="width: 100%;">Resolve Learning Blocker</a>
            `;
        } else {
            resultsBox.innerHTML = `
                <div class="alert alert-success" style="flex-direction: column; gap: 0.5rem;">
                    <strong style="font-size: 1.05rem;">🟢 Good Standing</strong>
                    <span style="font-size: 0.9rem;">No active cognitive failures diagnosed for this subject. Excellent work!</span>
                </div>
                <p style="font-size: 0.95rem; margin-top: 1rem;">
                    Your knowledge states estimated via Bayesian Knowledge Tracing show that your prerequisite skills are sufficient.
                </p>
            `;
            actionContainer.innerHTML = `
                <a href="/dashboard.html" class="btn btn-secondary" style="width: 100%;">Return to Dashboard</a>
            `;
        }

        renderDAG(subjectCode, stateRes.concepts, rootCauseId, prereqWeakIds);

    } catch (err) {
        console.error('Error running diagnosis:', err);
        document.getElementById('loading-diag').innerHTML = `
            <div class="alert alert-danger" style="margin-bottom:0;">Failed to load diagnosis results.</div>
        `;
    }
});

function renderDAG(subjectCode, conceptsList, rootCauseId, prereqWeakIds) {
    const vizContainer = document.getElementById('dag-visualization-container');
    vizContainer.innerHTML = '';

    // Create a mapping of concept_name -> concept model details
    const conceptsMap = {};
    conceptsList.forEach(c => {
        conceptsMap[c.concept_name] = c;
    });

    const getNodeClass = (concept) => {
        if (!concept) return 'badge-unassessed';
        if (concept.concept_id === rootCauseId) return 'weak';
        if (prereqWeakIds.includes(concept.concept_id)) return 'prereq-weakness';
        if (concept.mastery_status === 'Mastered') return 'mastered';
        return '';
    };

    const getScoreHtml = (concept) => {
        if (!concept || concept.evidence_count === 0) return 'Unassessed';
        return `Mastery: ${Math.round(concept.mastery_score * 100)}%`;
    };

    if (subjectCode === 'DBMS') {
        const cRelations = conceptsMap['Relations'];
        const cKeys = conceptsMap['Keys'];
        const cSql = conceptsMap['SQL Querying'];
        const cNorm = conceptsMap['Normalization'];
        const cTx = conceptsMap['Transactions & ACID'];

        vizContainer.innerHTML = `
            <div class="graph-row">
                <div class="graph-node ${getNodeClass(cRelations)}">
                    <div class="graph-node-title">Relations</div>
                    <div class="graph-node-score">${getScoreHtml(cRelations)}</div>
                </div>
            </div>
            
            <div class="connector-line"></div>
            
            <div class="graph-row" style="gap: 4rem;">
                <div class="graph-node ${getNodeClass(cKeys)}">
                    <div class="graph-node-title">Keys</div>
                    <div class="graph-node-score">${getScoreHtml(cKeys)}</div>
                </div>
                <div class="graph-node ${getNodeClass(cSql)}">
                    <div class="graph-node-title">SQL Querying</div>
                    <div class="graph-node-score">${getScoreHtml(cSql)}</div>
                </div>
            </div>
            
            <div class="graph-row" style="gap: 4rem;">
                <div style="display: flex; flex-direction: column; align-items: center;">
                    <div class="connector-line"></div>
                    <div class="graph-node ${getNodeClass(cNorm)}">
                        <div class="graph-node-title">Normalization</div>
                        <div class="graph-node-score">${getScoreHtml(cNorm)}</div>
                    </div>
                </div>
                <div style="display: flex; flex-direction: column; align-items: center;">
                    <div class="connector-line"></div>
                    <div class="graph-node ${getNodeClass(cTx)}">
                        <div class="graph-node-title">Transactions & ACID</div>
                        <div class="graph-node-score">${getScoreHtml(cTx)}</div>
                    </div>
                </div>
            </div>
        `;
    } else if (subjectCode === 'DSA') {
        const cArrays = conceptsMap['Arrays'];
        const cLists = conceptsMap['Linked Lists'];
        const cSq = conceptsMap['Stacks & Queues'];
        const cTrees = conceptsMap['Binary Trees'];
        const cBst = conceptsMap['Binary Search Trees (BST)'];
        const cGraphs = conceptsMap['Graph Basics'];

        vizContainer.innerHTML = `
            <div class="graph-row">
                <div class="graph-node ${getNodeClass(cArrays)}">
                    <div class="graph-node-title">Arrays</div>
                    <div class="graph-node-score">${getScoreHtml(cArrays)}</div>
                </div>
            </div>
            
            <div class="connector-line"></div>
            
            <div class="graph-row">
                <div class="graph-node ${getNodeClass(cLists)}">
                    <div class="graph-node-title">Linked Lists</div>
                    <div class="graph-node-score">${getScoreHtml(cLists)}</div>
                </div>
            </div>
            
            <div class="connector-line"></div>
            
            <div class="graph-row">
                <div class="graph-node ${getNodeClass(cSq)}">
                    <div class="graph-node-title">Stacks & Queues</div>
                    <div class="graph-node-score">${getScoreHtml(cSq)}</div>
                </div>
            </div>
            
            <div class="connector-line"></div>
            
            <div class="graph-row">
                <div class="graph-node ${getNodeClass(cTrees)}">
                    <div class="graph-node-title">Binary Trees</div>
                    <div class="graph-node-score">${getScoreHtml(cTrees)}</div>
                </div>
            </div>
            
            <div class="connector-line"></div>
            
            <div class="graph-row" style="gap: 4rem;">
                <div class="graph-node ${getNodeClass(cBst)}">
                    <div class="graph-node-title">BST</div>
                    <div class="graph-node-score">${getScoreHtml(cBst)}</div>
                </div>
                <div class="graph-node ${getNodeClass(cGraphs)}">
                    <div class="graph-node-title">Graph Basics</div>
                    <div class="graph-node-score">${getScoreHtml(cGraphs)}</div>
                </div>
            </div>
        `;
    }
}

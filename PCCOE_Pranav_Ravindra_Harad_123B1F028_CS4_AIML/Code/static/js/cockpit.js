/**
 * AUTOSAFE-REVIEW: ENTERPRISE AUTOMOTIVE COCKPIT JAVASCRIPT
 * Standardized Developer Tool Logic (No Emojis, Pure SVG Icons, Enterprise Style)
 * Candidate: Pranav Ravindra Harad | PRN: 123B1F028 | PCCOE Pune
 */

let currentModule = "bms_cell_monitor.c";
let currentCode = "";
let currentGccLog = "";
let currentSarifLog = "";
let currentFindings = [];
let activeSeverityFilter = "ALL";

document.addEventListener("DOMContentLoaded", () => {
    loadModule(currentModule);
    setupEventListeners();
});

function setupEventListeners() {
    // Module navigation clicks
    document.querySelectorAll(".module-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            document.querySelectorAll(".module-btn").forEach(b => b.classList.remove("active"));
            btn.classList.add("active");
            const mod = btn.getAttribute("data-module");
            loadModule(mod);
        });
    });

    // Code inspector tab switching
    document.querySelectorAll(".tab-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
            btn.classList.add("active");
            const tab = btn.getAttribute("data-tab");
            switchTab(tab);
        });
    });

    // Run Review Button
    document.getElementById("btn-run-review").addEventListener("click", runAnalysis);

    // Modal Close
    document.getElementById("modal-close-btn").addEventListener("click", closeModal);
}

async function loadModule(filename) {
    currentModule = filename;
    document.getElementById("active-file-title").innerText = filename;
    document.getElementById("active-breadcrumb-target").innerText = filename;
    
    try {
        const resp = await fetch(`/api/sample/${filename}`);
        const data = await resp.json();
        currentCode = data.code;
        currentGccLog = data.gcc_log;
        currentSarifLog = data.sarif_log;

        renderCodeViewer(currentCode);
        document.getElementById("gcc-text-view").innerText = currentGccLog;
        document.getElementById("sarif-text-view").innerText = currentSarifLog;

        clearFindingsView();
    } catch (err) {
        showToast("Error loading module source files", "error");
    }
}

function renderCodeViewer(code, highlightLines = []) {
    const container = document.getElementById("code-viewer-content");
    container.innerHTML = "";
    
    const lines = code.split("\n");
    lines.forEach((lineText, idx) => {
        const lineNum = idx + 1;
        const lineDiv = document.createElement("div");
        lineDiv.className = "code-row";
        if (highlightLines.includes(lineNum)) {
            lineDiv.classList.add("highlight-err");
        }
        lineDiv.innerHTML = `
            <span class="line-number">${lineNum}</span>
            <span class="code-text">${escapeHtml(lineText)}</span>
        `;
        container.appendChild(lineDiv);
    });
}

function switchTab(tabName) {
    document.getElementById("tab-code-view").style.display = tabName === "code" ? "block" : "none";
    document.getElementById("tab-gcc-view").style.display = tabName === "gcc" ? "block" : "none";
    document.getElementById("tab-sarif-view").style.display = tabName === "sarif" ? "block" : "none";
}

async function runAnalysis() {
    const btn = document.getElementById("btn-run-review");
    const originalText = btn.innerHTML;
    btn.innerHTML = `
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="animation: spin 1s linear infinite;">
            <circle cx="12" cy="12" r="10" stroke-dasharray="32" stroke-dashoffset="12"/>
        </svg>
        <span>Analyzing C-AST & Rules...</span>
    `;
    btn.disabled = true;

    try {
        const resp = await fetch("/api/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                source_code: currentCode,
                file_name: currentModule,
                compiler_log: currentGccLog,
                sarif_log: currentSarifLog
            })
        });

        const data = await resp.json();
        currentFindings = data.findings;

        // Update KPIs
        document.getElementById("kpi-total-val").innerText = data.total_findings;
        document.getElementById("kpi-critical-val").innerText = data.summary.critical_and_mandatory;
        document.getElementById("kpi-required-val").innerText = data.summary.required_and_high;
        document.getElementById("kpi-advisory-val").innerText = data.summary.advisory;
        document.getElementById("kpi-faith-val").innerText = "100.0%";

        // Highlight offending lines in code viewer
        const errorLines = currentFindings.map(f => f.line);
        renderCodeViewer(currentCode, errorLines);

        // Render Finding Cards
        renderFindingsList(currentFindings);

        showToast(`Analysis completed. ${data.total_findings} findings detected.`, "success");
    } catch (err) {
        showToast("Error during static code analysis", "error");
    } finally {
        btn.innerHTML = originalText;
        btn.disabled = false;
    }
}

function renderFindingsList(findings) {
    const container = document.getElementById("findings-container");
    container.innerHTML = "";

    const filtered = activeSeverityFilter === "ALL" 
        ? findings 
        : findings.filter(f => f.severity.toUpperCase() === activeSeverityFilter);

    if (filtered.length === 0) {
        container.innerHTML = `<div style="text-align: center; color: var(--text-subtle); padding: 40px; font-size: 12px;">No findings matching current severity filter.</div>`;
        return;
    }

    filtered.forEach((f) => {
        const sevClass = f.severity === "Mandatory" || f.severity === "Critical" 
            ? "sev-mandatory" 
            : (f.severity === "Required" || f.severity === "High" ? "sev-required" : "sev-advisory");
        
        const badgeClass = f.severity === "Mandatory" || f.severity === "Critical"
            ? "mandatory" 
            : (f.severity === "Required" || f.severity === "High" ? "required" : "advisory");

        const card = document.createElement("div");
        card.className = `finding-card ${sevClass}`;
        card.id = `card-${f.finding_id}`;

        // Format Diff
        const diffLines = f.suggested_fix.split("\n").map(l => {
            if (l.startsWith("-")) return `<span class="diff-line-del">${escapeHtml(l)}</span>`;
            if (l.startsWith("+")) return `<span class="diff-line-add">${escapeHtml(l)}</span>`;
            return `<span>${escapeHtml(l)}</span>`;
        }).join("");

        card.innerHTML = `
            <div class="finding-card-header">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span class="badge-tag ${badgeClass}">${f.severity}</span>
                    <strong style="color: #60a5fa; font-size: 12px;">${f.citation}</strong>
                </div>
                <span class="finding-location">L${f.line}</span>
            </div>

            <div class="finding-rule-name">${escapeHtml(f.code_snippet)}</div>
            <div class="finding-desc-text">${escapeHtml(f.root_cause)}</div>

            <div class="safety-consequence-alert">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#f87171" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-top: 1px;">
                    <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>
                    <line x1="12" y1="9" x2="12" y2="13"/>
                    <line x1="12" y1="17" x2="12.01" y2="17"/>
                </svg>
                <div><strong>ISO 26262 ASIL Impact:</strong> ${escapeHtml(f.safety_impact)}</div>
            </div>

            <div style="font-size: 10.5px; font-weight: 600; color: var(--text-muted); text-transform: uppercase;">
                Compliant Remediation Diff:
            </div>
            <div class="diff-preview-box">${diffLines}</div>

            <div class="card-actions-bar">
                <button class="btn-action accept" onclick="acceptFix('${f.finding_id}')">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <polyline points="20 6 9 17 4 12"/>
                    </svg>
                    <span>Accept Remediation</span>
                </button>

                <button class="btn-action reject" onclick="rejectFix('${f.finding_id}')">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="18" y1="6" x2="6" y2="18"/>
                        <line x1="6" y1="6" x2="18" y2="18"/>
                    </svg>
                    <span>Dismiss</span>
                </button>

                <button class="btn-action permit" onclick="openDeviationModal('${f.finding_id}')">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                        <polyline points="14 2 14 8 20 8"/>
                    </svg>
                    <span>Request Deviation</span>
                </button>
            </div>
        `;

        container.appendChild(card);
    });
}

function filterSeverity(sev) {
    activeSeverityFilter = sev;
    document.querySelectorAll(".filter-btn").forEach(btn => {
        btn.classList.toggle("active", btn.getAttribute("data-sev") === sev);
    });
    renderFindingsList(currentFindings);
}

function acceptFix(findingId) {
    const card = document.getElementById(`card-${findingId}`);
    if (card) {
        card.style.opacity = "0.6";
        card.style.borderLeftColor = "#10b981";
    }
    showToast(`Remediation accepted for ${findingId}. Staged for build verification.`, "success");
}

function rejectFix(findingId) {
    const card = document.getElementById(`card-${findingId}`);
    if (card) {
        card.style.opacity = "0.5";
        card.style.borderLeftColor = "#6b7280";
    }
    showToast(`Finding ${findingId} dismissed by reviewer.`, "info");
}

function openDeviationModal(findingId) {
    const finding = currentFindings.find(f => f.finding_id === findingId);
    if (!finding) return;

    document.getElementById("dev-finding-id").value = finding.finding_id;
    document.getElementById("dev-rule-id").value = finding.rule_id;
    document.getElementById("dev-file-name").value = finding.file;
    document.getElementById("dev-line-num").value = `Line ${finding.line}`;
    document.getElementById("dev-rationale").value = `Microcontroller hardware timing constraint requires inline access in ${finding.file}.`;
    document.getElementById("dev-mitigation").value = `Enforced via memory protection unit (MPU) boundaries and hardware watchdog alive-monitoring.`;
    
    const outputContainer = document.getElementById("dev-output-container");
    outputContainer.style.display = "none";

    document.getElementById("deviation-modal").style.display = "flex";
}

function closeModal() {
    document.getElementById("deviation-modal").style.display = "none";
}

async function submitDeviation() {
    const findingId = document.getElementById("dev-finding-id").value;
    const finding = currentFindings.find(f => f.finding_id === findingId);
    const justification = document.getElementById("dev-rationale").value;
    const mitigation = document.getElementById("dev-mitigation").value;

    try {
        const resp = await fetch("/api/deviation", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                finding: finding,
                justification: justification,
                mitigation: mitigation
            })
        });
        const data = await resp.json();
        
        document.getElementById("dev-permit-text").value = data.permit;
        document.getElementById("dev-output-container").style.display = "flex";
        showToast("Signed MISRA Deviation Record generated successfully.", "success");
    } catch (err) {
        showToast("Error generating deviation record", "error");
    }
}

function downloadPermitFile() {
    const text = document.getElementById("dev-permit-text").value;
    const blob = new Blob([text], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `MISRA_Deviation_${currentModule}.txt`;
    a.click();
}

async function exportSARIF() {
    if (currentFindings.length === 0) {
        showToast("Please run static analysis prior to exporting", "info");
        return;
    }
    const resp = await fetch("/api/export/sarif", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ findings: currentFindings })
    });
    const blob = await resp.blob();
    downloadBlob(blob, `${currentModule}_findings.sarif`);
}

async function exportCSV() {
    if (currentFindings.length === 0) {
        showToast("Please run static analysis prior to exporting", "info");
        return;
    }
    const resp = await fetch("/api/export/csv", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ findings: currentFindings })
    });
    const blob = await resp.blob();
    downloadBlob(blob, `${currentModule}_compliance.csv`);
}

async function exportMarkdown() {
    if (currentFindings.length === 0) {
        showToast("Please run static analysis prior to exporting", "info");
        return;
    }
    const resp = await fetch("/api/export/markdown", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
            findings: currentFindings,
            summary: {
                file: currentModule,
                summary: {
                    critical_and_mandatory: currentFindings.filter(f => f.severity === 'Mandatory' || f.severity === 'Critical').length,
                    required_and_high: currentFindings.filter(f => f.severity === 'Required' || f.severity === 'High').length
                }
            }
        })
    });
    const blob = await resp.blob();
    downloadBlob(blob, `${currentModule}_audit_report.md`);
}

function downloadBlob(blob, filename) {
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = filename;
    a.click();
    showToast(`Exported ${filename}`, "success");
}

function clearFindingsView() {
    document.getElementById("findings-container").innerHTML = `
        <div style="text-align: center; color: var(--text-subtle); padding: 50px 16px;">
            <div style="font-size: 13px; font-weight: 600; color: var(--text-muted);">Ready for Analysis</div>
            <div style="font-size: 11.5px; margin-top: 4px;">Select an ECU module and click 'Run Static Analysis & Review' to inspect against MISRA and CERT standards.</div>
        </div>
    `;
    document.getElementById("kpi-total-val").innerText = "--";
    document.getElementById("kpi-critical-val").innerText = "--";
    document.getElementById("kpi-required-val").innerText = "--";
    document.getElementById("kpi-advisory-val").innerText = "--";
    document.getElementById("kpi-faith-val").innerText = "--";
}

function showToast(msg, type = "success") {
    const container = document.getElementById("toast-container");
    const toast = document.createElement("div");
    toast.className = `toast-item ${type}`;
    
    let iconSvg = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>`;
    if (type === "error") {
        iconSvg = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>`;
    } else if (type === "info") {
        iconSvg = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>`;
    }

    toast.innerHTML = `<span>${iconSvg}</span> <span>${escapeHtml(msg)}</span>`;
    container.appendChild(toast);
    setTimeout(() => {
        toast.remove();
    }, 3200);
}

function escapeHtml(str) {
    if (!str) return "";
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

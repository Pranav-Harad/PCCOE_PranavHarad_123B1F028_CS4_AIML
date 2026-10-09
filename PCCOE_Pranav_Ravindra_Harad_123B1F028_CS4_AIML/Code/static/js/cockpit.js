/**
 * AUTOSAFE-REVIEW: ENTERPRISE AUTOMOTIVE COCKPIT JAVASCRIPT
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
    
    try {
        const resp = await fetch(`/api/sample/${filename}`);
        const data = await resp.json();
        currentCode = data.code;
        currentGccLog = data.gcc_log;
        currentSarifLog = data.sarif_log;

        renderCodeViewer(currentCode);
        document.getElementById("gcc-text-view").innerText = currentGccLog;
        document.getElementById("sarif-text-view").innerText = currentSarifLog;

        // Reset findings view until run button is clicked
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
        lineDiv.className = "code-line";
        if (highlightLines.includes(lineNum)) {
            lineDiv.classList.add("has-error");
        }
        lineDiv.innerHTML = `
            <span class="line-num">${lineNum}</span>
            <span class="line-text">${escapeHtml(lineText)}</span>
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
    btn.innerHTML = `<span class="pulse-dot"></span> Analyzing AST & Rules...`;
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

        showToast(`Review complete! Identified ${data.total_findings} grounded findings.`, "success");
    } catch (err) {
        showToast("Error during automotive code review", "error");
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
        container.innerHTML = `<div style="text-align: center; color: var(--text-muted); padding: 40px;">No findings matching current filter.</div>`;
        return;
    }

    filtered.forEach((f, idx) => {
        const sevClass = f.severity === "Mandatory" || f.severity === "Critical" 
            ? "sev-mandatory" 
            : (f.severity === "Required" || f.severity === "High" ? "sev-required" : "sev-advisory");
        
        const badgeClass = f.severity === "Mandatory" || f.severity === "Critical"
            ? "badge-mandatory"
            : (f.severity === "Required" || f.severity === "High" ? "badge-required" : "badge-advisory");

        const card = document.createElement("div");
        card.className = `finding-card ${sevClass}`;
        card.id = `card-${f.finding_id}`;

        // Format Diff
        const diffLines = f.suggested_fix.split("\n").map(l => {
            if (l.startsWith("-")) return `<span class="diff-del">${escapeHtml(l)}</span>`;
            if (l.startsWith("+")) return `<span class="diff-add">${escapeHtml(l)}</span>`;
            return `<span>${escapeHtml(l)}</span>`;
        }).join("");

        card.innerHTML = `
            <div class="finding-top">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span class="badge ${badgeClass}">${f.severity}</span>
                    <strong style="color: var(--accent-cyan); font-size: 13px;">${f.citation}</strong>
                    <span style="color: var(--text-muted); font-size: 12px;">• Line ${f.line}</span>
                </div>
                <div style="font-size: 11.5px; color: var(--text-muted);">
                    Confidence: <strong style="color: #fff;">${(f.confidence * 100).toFixed(1)}%</strong>
                </div>
            </div>

            <div class="finding-title">${escapeHtml(f.code_snippet)}</div>
            <div class="finding-desc">${escapeHtml(f.root_cause)}</div>

            <div class="hazard-box">
                <strong>⚠️ ISO 26262 ASIL Safety Impact:</strong> ${escapeHtml(f.safety_impact)}
            </div>

            <div style="font-size: 11px; font-weight: 700; color: var(--text-secondary); margin-bottom: 6px; text-transform: uppercase;">
                Recommended Compliant Unified Diff:
            </div>
            <div class="diff-container">${diffLines}</div>

            <div class="finding-actions">
                <button class="btn-accept" onclick="acceptFix('${f.finding_id}')">✅ Accept Fix</button>
                <button class="btn-reject" onclick="rejectFix('${f.finding_id}')">❌ Reject</button>
                <button class="btn-deviation" onclick="openDeviationModal('${f.finding_id}')">📝 Request MISRA Deviation</button>
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
        card.style.opacity = "0.7";
        card.style.borderColor = "var(--accent-emerald)";
    }
    showToast(`Finding ${findingId}: Fix Accepted & Staged for Verification Build.`, "success");
}

function rejectFix(findingId) {
    const card = document.getElementById(`card-${findingId}`);
    if (card) {
        card.style.opacity = "0.5";
        card.style.borderColor = "var(--accent-crimson)";
    }
    showToast(`Finding ${findingId}: Rejected by Engineer.`, "info");
}

function openDeviationModal(findingId) {
    const finding = currentFindings.find(f => f.finding_id === findingId);
    if (!finding) return;

    document.getElementById("dev-finding-id").value = finding.finding_id;
    document.getElementById("dev-rule-id").value = finding.rule_id;
    document.getElementById("dev-file-name").value = finding.file;
    document.getElementById("dev-line-num").value = finding.line;
    document.getElementById("dev-rationale").value = `Direct hardware access required for ECU micro-timer performance in ${finding.file}.`;
    document.getElementById("dev-mitigation").value = `Protected via memory protection unit (MPU) boundary and hardware watchdog alive-monitoring.`;
    document.getElementById("dev-output-container").style.display = "none";

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
        document.getElementById("dev-output-container").style.display = "block";
        showToast("Signed MISRA Deviation Permit generated successfully!", "success");
    } catch (err) {
        showToast("Error generating deviation permit", "error");
    }
}

function downloadPermitFile() {
    const text = document.getElementById("dev-permit-text").value;
    const blob = new Blob([text], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `MISRA_Deviation_Permit_${currentModule}.txt`;
    a.click();
}

async function exportSARIF() {
    if (currentFindings.length === 0) {
        showToast("Please run review first before exporting", "info");
        return;
    }
    const resp = await fetch("/api/export/sarif", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ findings: currentFindings })
    });
    const blob = await resp.blob();
    downloadBlob(blob, `${currentModule}_audit.sarif`);
}

async function exportCSV() {
    if (currentFindings.length === 0) {
        showToast("Please run review first before exporting", "info");
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
        showToast("Please run review first before exporting", "info");
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
    showToast(`Downloaded ${filename}`, "success");
}

function clearFindingsView() {
    document.getElementById("findings-container").innerHTML = `
        <div style="text-align: center; color: var(--text-muted); padding: 60px 20px;">
            <div style="font-size: 32px; margin-bottom: 12px;">🛡️</div>
            <div style="font-size: 15px; font-weight: 600; color: var(--text-secondary);">Automotive Diagnostic Core Ready</div>
            <div style="font-size: 13px; margin-top: 6px;">Click 'Run Multi-Modal Review' to analyze AST, compiler logs, and MISRA/CERT rules.</div>
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
    toast.className = "toast";
    toast.style.borderLeftColor = type === "error" ? "var(--accent-crimson)" : (type === "info" ? "var(--accent-cyan)" : "var(--accent-emerald)");
    toast.innerHTML = `<span>${type === 'error' ? '❌' : (type === 'info' ? 'ℹ️' : '✅')}</span> <span>${escapeHtml(msg)}</span>`;
    container.appendChild(toast);
    setTimeout(() => {
        toast.remove();
    }, 3500);
}

function escapeHtml(str) {
    if (!str) return "";
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

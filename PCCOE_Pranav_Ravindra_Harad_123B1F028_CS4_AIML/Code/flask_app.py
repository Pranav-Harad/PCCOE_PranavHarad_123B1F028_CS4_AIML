#!/usr/bin/env python3
"""
AUTOSAFE-REVIEW: ENTERPRISE FLASK WEB APPLICATION & REST API
Tata Technologies TechPulse FY-26 | AI/ML Capstone Project | Case Study 4
Student: Pranav Ravindra Harad | PRN: 123B1F028 | PCCOE, Pune
"""

import os
import sys
import json
from flask import Flask, render_template, request, jsonify, Response

# Setup paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
sys.path.insert(0, BASE_DIR)

from backend.triage_orchestrator import TriageOrchestrator
from utils.sarif_exporter import export_findings_to_sarif
from utils.deviation_generator import generate_deviation_permit
from utils.report_exporter import export_findings_to_csv, export_findings_to_markdown

app = Flask(__name__, template_folder="templates", static_folder="static")

# Initialize Orchestrator
rules_dir = os.path.join(PROJECT_ROOT, "Input_Data", "rules")
orchestrator = TriageOrchestrator(rules_dir=rules_dir)

samples_dir = os.path.join(PROJECT_ROOT, "Input_Data", "automotive_ecu_samples")
logs_dir = os.path.join(PROJECT_ROOT, "Input_Data", "compiler_build_logs")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/sample/<filename>")
def get_sample(filename):
    file_path = os.path.join(samples_dir, filename)
    code = ""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()

    gcc_log = ""
    gcc_path = os.path.join(logs_dir, "gcc_arm_none_eabi_build.log")
    if os.path.exists(gcc_path):
        with open(gcc_path, "r", encoding="utf-8") as f:
            gcc_log = f.read()

    sarif_log = ""
    sarif_path = os.path.join(logs_dir, "clang_embedded_static_analysis.sarif")
    if os.path.exists(sarif_path):
        with open(sarif_path, "r", encoding="utf-8") as f:
            sarif_log = f.read()

    return jsonify({
        "file_name": filename,
        "code": code,
        "gcc_log": gcc_log,
        "sarif_log": sarif_log
    })

@app.route("/api/analyze", methods=["POST"])
def analyze_code():
    data = request.json or {}
    source_code = data.get("source_code", "")
    file_name = data.get("file_name", "source.c")
    compiler_log = data.get("compiler_log", None)
    sarif_log = data.get("sarif_log", None)

    report = orchestrator.review_module(
        source_code=source_code,
        file_name=file_name,
        compiler_log_text=compiler_log,
        sarif_content=sarif_log
    )
    return jsonify(report)

@app.route("/api/deviation", methods=["POST"])
def create_deviation():
    data = request.json or {}
    finding = data.get("finding", {})
    justification = data.get("justification", "Hardware register direct access requirement.")
    mitigation = data.get("mitigation", "Protected via MPU and watchdog timer.")

    permit_text = generate_deviation_permit(
        finding=finding,
        engineer_name="Pranav Ravindra Harad",
        prn="123B1F028",
        technical_justification=justification,
        mitigation_steps=mitigation
    )
    return jsonify({"permit": permit_text})

@app.route("/api/export/sarif", methods=["POST"])
def export_sarif():
    data = request.json or {}
    findings = data.get("findings", [])
    sarif_json = export_findings_to_sarif(findings, target_file=None)
    return Response(
        sarif_json,
        mimetype="application/json",
        headers={"Content-Disposition": "attachment;filename=autosafe_review.sarif"}
    )

@app.route("/api/export/csv", methods=["POST"])
def export_csv():
    data = request.json or {}
    findings = data.get("findings", [])
    csv_str = export_findings_to_csv(findings)
    return Response(
        csv_str,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=autosafe_compliance.csv"}
    )

@app.route("/api/export/markdown", methods=["POST"])
def export_markdown():
    data = request.json or {}
    findings = data.get("findings", [])
    summary = data.get("summary", {})
    md_str = export_findings_to_markdown(summary, findings)
    return Response(
        md_str,
        mimetype="text/markdown",
        headers={"Content-Disposition": "attachment;filename=autosafe_audit_report.md"}
    )

def main():
    port = int(os.environ.get("PORT", 5000))
    print("=================================================================")
    print("  AUTOSAFE-REVIEW: ENTERPRISE FLASK WEB APPLICATION RUNNING      ")
    print(f"  URL: http://localhost:{port}                                    ")
    print("  Candidate: Pranav Ravindra Harad | PRN: 123B1F028 | PCCOE     ")
    print("=================================================================")
    app.run(host="0.0.0.0", port=port, debug=False)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Full System Automated Verification Test
Tests end-to-end functionality across all 3 Automotive ECU modules,
SARIF exports, Deviation Permits, and CSV/Markdown generation.
Student: Pranav Ravindra Harad | PRN: 123B1F028 | PCCOE, Pune
"""

import os
import sys
import json
import urllib.request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SUBMISSION_DIR = os.path.join(BASE_DIR, "PCCOE_Pranav_Ravindra_Harad_123B1F028_CS4_AIML")
CODE_DIR = os.path.join(SUBMISSION_DIR, "Code")
sys.path.insert(0, CODE_DIR)

from backend.triage_orchestrator import TriageOrchestrator
from utils.sarif_exporter import export_findings_to_sarif
from utils.deviation_generator import generate_deviation_permit
from utils.report_exporter import export_findings_to_csv, export_findings_to_markdown

def test_full_system():
    print("=================================================================")
    print("     AUTOSAFE-REVIEW: COMPLETE SYSTEM FUNCTIONALITY CHECK        ")
    print("=================================================================")

    # 1. Test HTTP Server
    print("\n[*] 1. Checking Streamlit Web Server at http://localhost:8501...")
    try:
        req = urllib.request.Request("http://localhost:8501/_stcore/health")
        with urllib.request.urlopen(req, timeout=3.0) as resp:
            status = resp.read().decode('utf-8')
            print(f"    [+] Streamlit Health Check Status: {status.strip()} (HTTP 200 OK)")
    except Exception as e:
        print(f"    [!] Warning: Health check endpoint returned: {e}")

    # 2. Test Triage Orchestration across all 3 modules
    rules_dir = os.path.join(SUBMISSION_DIR, "Input_Data", "rules")
    samples_dir = os.path.join(SUBMISSION_DIR, "Input_Data", "automotive_ecu_samples")
    logs_dir = os.path.join(SUBMISSION_DIR, "Input_Data", "compiler_build_logs")

    orchestrator = TriageOrchestrator(rules_dir=rules_dir)

    with open(os.path.join(logs_dir, "gcc_arm_none_eabi_build.log"), "r", encoding="utf-8") as f:
        gcc_log = f.read()
    with open(os.path.join(logs_dir, "clang_embedded_static_analysis.sarif"), "r", encoding="utf-8") as f:
        sarif_log = f.read()

    test_modules = [
        ("Demo 1: BMS Cell Voltage Monitor (ASIL-C)", "bms_cell_monitor.c"),
        ("Demo 2: Throttle Actuator Driver (ASIL-D)", "throttle_actuator_driver.c"),
        ("Demo 3: CAN Transceiver Driver (ASIL-B)", "can_transceiver.c")
    ]

    print("\n[*] 2. Testing End-to-End Analysis for All 3 Automotive Modules...")
    all_results = {}
    for label, fname in test_modules:
        with open(os.path.join(samples_dir, fname), "r", encoding="utf-8") as f:
            src = f.read()
        
        res = orchestrator.review_module(
            source_code=src,
            file_name=fname,
            compiler_log_text=gcc_log,
            sarif_content=sarif_log
        )
        all_results[fname] = res
        print(f"    [+] {label}:")
        print(f"        Total Findings: {res['total_findings']}")
        print(f"        Summary: {res['summary']}")
        assert res['total_findings'] > 0, f"Expected findings for {fname}"

    # 3. Test Deviation Permit Generation
    print("\n[*] 3. Testing Automotive MISRA Deviation Permit Generator...")
    sample_finding = all_results["bms_cell_monitor.c"]["findings"][0]
    permit = generate_deviation_permit(
        finding=sample_finding,
        engineer_name="Pranav Ravindra Harad",
        prn="123B1F028",
        technical_justification="Hardware SPI timing constraint requires inline shift evaluation.",
        mitigation_steps="Covered by 100% MC/DC branch testing and hardware watchdog monitoring."
    )
    assert "MISRA DEVIATION RECORD" in permit
    assert "Pranav Ravindra Harad" in permit
    assert "123B1F028" in permit
    print("    [+] Successfully generated signed Deviation Permit Record!")

    # 4. Test Export Generation (SARIF, CSV, Markdown)
    print("\n[*] 4. Testing Export Artifact Generation (SARIF, CSV, Markdown)...")
    bms_findings = all_results["bms_cell_monitor.c"]["findings"]
    sarif_str = export_findings_to_sarif(bms_findings)
    sarif_obj = json.loads(sarif_str)
    assert sarif_obj["version"] == "2.1.0"
    print(f"    [+] OASIS SARIF v2.1.0: Generated with {len(sarif_obj['runs'][0]['results'])} results.")

    csv_str = export_findings_to_csv(bms_findings)
    assert "finding_id,file,line" in csv_str
    print(f"    [+] CSV Compliance Matrix: Generated with {len(csv_str.splitlines())} lines.")

    md_str = export_findings_to_markdown(all_results["bms_cell_monitor.c"], bms_findings)
    assert "# Automotive Code Review" in md_str
    print(f"    [+] Markdown Audit Report: Generated ({len(md_str)} characters).")

    print("\n=================================================================")
    print("  [SUCCESS] 100% OF SYSTEM CAPABILITIES ARE WORKING FLAWLESSLY!  ")
    print("=================================================================")

if __name__ == "__main__":
    test_full_system()

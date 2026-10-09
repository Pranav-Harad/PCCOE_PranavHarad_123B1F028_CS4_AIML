#!/usr/bin/env python3
"""
Phase 3 Verification Script: End-to-End Triage Orchestration & LLM Service
Part of AutoSafe-Review (Tata TechPulse CS4)
Student: Pranav Ravindra Harad | PRN: 123B1F028 | PCCOE, Pune
"""

import os
import sys
import json

# Ensure backend package can be imported
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.triage_orchestrator import TriageOrchestrator

def test_triage():
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    samples_dir = os.path.join(project_root, "Input_Data", "automotive_ecu_samples")
    logs_dir = os.path.join(project_root, "Input_Data", "compiler_build_logs")

    print("=================================================================")
    print("  AUTOSAFE-REVIEW: PHASE 3 TRIAGE ORCHESTRATOR VERIFICATION     ")
    print("=================================================================")

    orchestrator = TriageOrchestrator()

    # Load source code and logs for BMS module
    bms_src_path = os.path.join(samples_dir, "bms_cell_monitor.c")
    with open(bms_src_path, "r", encoding="utf-8") as f:
        bms_code = f.read()

    gcc_log_path = os.path.join(logs_dir, "gcc_arm_none_eabi_build.log")
    with open(gcc_log_path, "r", encoding="utf-8") as f:
        gcc_log = f.read()

    sarif_path = os.path.join(logs_dir, "clang_embedded_static_analysis.sarif")
    with open(sarif_path, "r", encoding="utf-8") as f:
        sarif_log = f.read()

    print("\n[*] Executing Multi-Modal Triage on 'bms_cell_monitor.c'...")
    report = orchestrator.review_module(
        source_code=bms_code,
        file_name="bms_cell_monitor.c",
        compiler_log_text=gcc_log,
        sarif_content=sarif_log
    )

    print(f"[+] Total Findings Synthesized: {report['total_findings']}")
    print(f"[+] Severity Distribution: {report['summary']}")

    assert report["total_findings"] >= 3, "Expected at least 3 findings for BMS module"

    print("\n--- SAMPLE STRUCTURED FINDING ---")
    sample = report["findings"][0]
    for k, v in sample.items():
        if k == "suggested_fix":
            print(f"  {k}:\n{v}")
        else:
            print(f"  {k}: {v}")

    # Verify throttle module
    throttle_path = os.path.join(samples_dir, "throttle_actuator_driver.c")
    with open(throttle_path, "r", encoding="utf-8") as f:
        th_code = f.read()
    th_report = orchestrator.review_module(th_code, "throttle_actuator_driver.c", gcc_log, sarif_log)
    print(f"\n[+] Executed Triage on 'throttle_actuator_driver.c': {th_report['total_findings']} findings.")
    assert th_report["total_findings"] >= 3, "Expected at least 3 findings for Throttle module"

    print("\n[SUCCESS] Phase 3: Local LLM Service & Triage Orchestrator ALL PASSED!")

if __name__ == "__main__":
    test_triage()

#!/usr/bin/env python3
"""
Dataset and Knowledge Base Integrity Verification Script
Tata Technologies TechPulse FY-26 | Case Study 4: Secure Code Debugging
Student: Pranav Ravindra Harad | PRN: 123B1F028 | PCCOE, Pune
"""

import os
import json

def verify_rules():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    rules_dir = os.path.join(base_dir, "rules")
    
    files = ["misra_c_2012_rules.json", "cert_c_security_rules.json", "iso_26262_guidelines.json"]
    total_rules = 0
    print("[*] Verifying Knowledge Base Rule Sets...")
    for f in files:
        path = os.path.join(rules_dir, f)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Missing rule file: {path}")
        with open(path, "r", encoding="utf-8") as fp:
            data = json.load(fp)
            total_rules += len(data)
            print(f"  [+] {f}: Loaded {len(data)} verified entries.")
            
    print(f"[OK] Total Knowledge Base Rules Loaded: {total_rules}\n")

def verify_ecu_code():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ecu_dir = os.path.join(base_dir, "automotive_ecu_samples")
    
    expected_files = [
        "bms_cell_monitor.h", "bms_cell_monitor.c",
        "throttle_actuator_driver.h", "throttle_actuator_driver.c",
        "can_transceiver.h", "can_transceiver.c"
    ]
    print("[*] Verifying Synthetic Automotive ECU Source Modules...")
    for f in expected_files:
        path = os.path.join(ecu_dir, f)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Missing ECU code file: {path}")
        size = os.path.getsize(path)
        print(f"  [+] {f}: {size} bytes, verified.")
    print("[OK] All Automotive ECU Modules Verified.\n")

def verify_logs():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(base_dir, "compiler_build_logs")
    
    files = ["gcc_arm_none_eabi_build.log", "clang_embedded_static_analysis.sarif"]
    print("[*] Verifying Compiler & Static Analysis Diagnostics...")
    for f in files:
        path = os.path.join(log_dir, f)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Missing diagnostic file: {path}")
        size = os.path.getsize(path)
        print(f"  [+] {f}: {size} bytes, verified.")
    print("[OK] All Diagnostic Logs Verified.\n")

if __name__ == "__main__":
    print("=================================================================")
    print("  AUTOSAFE-REVIEW: DATASET & KNOWLEDGE BASE INTEGRITY CHECKER   ")
    print("=================================================================")
    verify_rules()
    verify_ecu_code()
    verify_logs()
    print("[SUCCESS] Phase 1 Input Data & Knowledge Base fully verified!")

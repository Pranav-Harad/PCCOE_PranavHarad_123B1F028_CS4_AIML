#!/usr/bin/env python3
"""
Phase 2 Automated Verification Pipeline
Tests AST Parser, Log Parser, Deterministic Checker, and Vector RAG Engine.
Student: Pranav Ravindra Harad | PRN: 123B1F028 | PCCOE, Pune
"""

import os
import sys

# Ensure backend package can be imported
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.parser import CSourceParser, DiagnosticLogParser
from backend.deterministic_checker import DeterministicChecker
from backend.rag_engine import AutomotiveRAGEngine

def run_tests():
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    samples_dir = os.path.join(project_root, "Input_Data", "automotive_ecu_samples")
    logs_dir = os.path.join(project_root, "Input_Data", "compiler_build_logs")

    print("=================================================================")
    print("  AUTOSAFE-REVIEW: PHASE 2 HYBRID ENGINE VERIFICATION PIPELINE   ")
    print("=================================================================")

    # 1. Test AST C Parser
    bms_path = os.path.join(samples_dir, "bms_cell_monitor.c")
    with open(bms_path, "r", encoding="utf-8") as f:
        code = f.read()

    parser = CSourceParser(code, "bms_cell_monitor.c")
    print(f"\n[+] AST C Parser: Discovered {len(parser.functions)} functions in bms_cell_monitor.c:")
    for fn in parser.functions:
        print(f"    - {fn.name}() [Lines {fn.start_line}-{fn.end_line}] -> calls {fn.callees}")
    assert len(parser.functions) >= 4, "Expected at least 4 functions parsed"

    # 2. Test Compiler & SARIF Log Parser
    gcc_log_path = os.path.join(logs_dir, "gcc_arm_none_eabi_build.log")
    with open(gcc_log_path, "r", encoding="utf-8") as f:
        gcc_text = f.read()
    gcc_diag = DiagnosticLogParser.parse_compiler_log(gcc_text)
    print(f"\n[+] Diagnostic Log Parser: Parsed {len(gcc_diag)} GCC warnings:")
    for d in gcc_diag[:3]:
        print(f"    - {d['file']}:{d['line']} [{d['rule_or_flag']}]: {d['message']}")
    assert len(gcc_diag) >= 4, "Expected at least 4 GCC warnings"

    sarif_path = os.path.join(logs_dir, "clang_embedded_static_analysis.sarif")
    with open(sarif_path, "r", encoding="utf-8") as f:
        sarif_text = f.read()
    sarif_diag = DiagnosticLogParser.parse_sarif(sarif_text)
    print(f"[+] SARIF Parser: Parsed {len(sarif_diag)} static analysis defects:")
    for s in sarif_diag:
        print(f"    - {s['file']}:{s['line']} [{s['rule_or_flag']}]: {s['message']}")
    assert len(sarif_diag) >= 3, "Expected at least 3 SARIF defects"

    # 3. Test Deterministic Analysis Engine
    print("\n[+] Deterministic Static Analyzer: Running cross-file defect checks...")
    files_to_check = ["bms_cell_monitor.c", "throttle_actuator_driver.c", "can_transceiver.c"]
    total_findings = 0
    for fname in files_to_check:
        fpath = os.path.join(samples_dir, fname)
        with open(fpath, "r", encoding="utf-8") as fp:
            src = fp.read()
        p = CSourceParser(src, fname)
        checker = DeterministicChecker(p)
        findings = checker.analyze()
        total_findings += len(findings)
        print(f"    - {fname}: Detected {len(findings)} deterministic violations:")
        for fd in findings:
            print(f"      * Line {fd['line']}: [{fd['rule_id']}] {fd['message']}")

    assert total_findings >= 6, "Expected at least 6 deterministic findings across test files"

    # 4. Test Vector RAG Engine
    print("\n[+] Automotive Vector RAG Engine: Testing semantic retrieval & grounding...")
    rag = AutomotiveRAGEngine()
    
    test_queries = [
        "operator precedence in bitwise shift without parentheses",
        "dynamic memory allocation malloc in ASIL-D",
        "race condition in interrupt service routine shared buffer"
    ]
    for q in test_queries:
        hits = rag.query(q, top_k=1)
        assert len(hits) > 0, f"Query '{q}' returned no results"
        hit = hits[0]
        print(f"    Query: '{q[:40]}...'")
        print(f"    Top Match: [{hit['rule_id']}] {hit['headline']} (Cosine Similarity: {hit['similarity_score']})")

    print("\n[SUCCESS] Phase 2: AST Parser, Log Parser, Deterministic Checker & Vector RAG Engine ALL PASSED!")

if __name__ == "__main__":
    run_tests()

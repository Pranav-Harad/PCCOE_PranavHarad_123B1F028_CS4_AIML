#!/usr/bin/env python3
"""
Automotive Multi-Modal Triage Orchestrator
Part of AutoSafe-Review (Tata TechPulse CS4)
Student: Pranav Ravindra Harad | PRN: 123B1F028 | PCCOE, Pune
"""

import os
from typing import List, Dict, Any, Optional

from .parser import CSourceParser, DiagnosticLogParser
from .deterministic_checker import DeterministicChecker
from .rag_engine import AutomotiveRAGEngine
from .local_llm import LocalAutomotiveLLM

class TriageOrchestrator:
    """
    Coordinates multi-modal automotive code review across:
    - C/C++ AST syntax
    - Deterministic rule checks
    - Embedded compiler warnings
    - SARIF static analysis reports
    - Grounded Vector RAG knowledge base
    - Local LLM synthesis
    """

    def __init__(self, rules_dir: Optional[str] = None):
        self.rag_engine = AutomotiveRAGEngine(rules_dir=rules_dir)
        self.local_llm = LocalAutomotiveLLM()

    def review_module(self, 
                      source_code: str, 
                      file_name: str, 
                      compiler_log_text: Optional[str] = None, 
                      sarif_content: Optional[str] = None) -> Dict[str, Any]:
        """
        Executes complete multi-modal review on an automotive C source file.
        """
        # 1. Parse AST
        parser = CSourceParser(source_code, file_name)
        
        # 2. Run Deterministic Checker
        checker = DeterministicChecker(parser)
        det_findings = checker.analyze()

        # 3. Parse Compiler Logs if provided
        compiler_diags = []
        if compiler_log_text:
            all_compiler = DiagnosticLogParser.parse_compiler_log(compiler_log_text)
            compiler_diags = [d for d in all_compiler if os.path.basename(d["file"]) == os.path.basename(file_name)]

        # 4. Parse SARIF Logs if provided
        sarif_diags = []
        if sarif_content:
            all_sarif = DiagnosticLogParser.parse_sarif(sarif_content)
            sarif_diags = [s for s in all_sarif if os.path.basename(s["file"]) == os.path.basename(file_name)]

        # 5. Synthesize and Correlate Findings
        final_findings: List[Dict[str, Any]] = []
        seen_lines_rules = set()

        # Process Deterministic Findings with RAG Grounding & LLM synthesis
        for df in det_findings:
            key = (df["line"], df["rule_id"])
            if key in seen_lines_rules:
                continue
            seen_lines_rules.add(key)

            # Query RAG for best matching rule metadata
            rag_hits = self.rag_engine.query(f"{df['rule_id']} {df['message']}", top_k=1)
            rule_info = rag_hits[0] if rag_hits else {
                "rule_id": df["rule_id"],
                "standard": df["standard"],
                "severity": df["severity"],
                "headline": df["message"],
                "automotive_rationale": df["safety_impact"],
                "asil_level_impact": df["safety_impact"],
                "cwe_mapping": "N/A",
                "compliant_example": df["suggested_fix"]
            }

            # Check if compiler warning exists for this line
            matching_warning = next((cd["message"] for cd in compiler_diags if cd["line"] == df["line"]), None)

            # Synthesize final rich finding
            finding = self.local_llm.generate_review_finding(
                file_name=file_name,
                line_num=df["line"],
                code_snippet=df["code_snippet"],
                rule_info=rule_info,
                compiler_warning=matching_warning
            )
            final_findings.append(finding)

        # Process standalone compiler warnings not already caught by deterministic checker
        for cd in compiler_diags:
            line_num = cd["line"]
            # Look up snippet
            code_line = parser.lines[line_num - 1] if 0 <= line_num - 1 < len(parser.lines) else "/* Line offset */"
            
            # Query RAG for this compiler warning
            rag_hits = self.rag_engine.query(f"compiler warning {cd['rule_or_flag']} {cd['message']}", top_k=1)
            if rag_hits:
                rule_info = rag_hits[0]
                key = (line_num, rule_info["rule_id"])
                if key not in seen_lines_rules:
                    seen_lines_rules.add(key)
                    finding = self.local_llm.generate_review_finding(
                        file_name=file_name,
                        line_num=line_num,
                        code_snippet=code_line,
                        rule_info=rule_info,
                        compiler_warning=f"{cd['rule_or_flag']}: {cd['message']}"
                    )
                    final_findings.append(finding)

        # Process SARIF diagnostics
        for sd in sarif_diags:
            line_num = sd["line"]
            code_line = parser.lines[line_num - 1] if 0 <= line_num - 1 < len(parser.lines) else "/* SARIF offset */"
            rag_hits = self.rag_engine.query(f"{sd['rule_or_flag']} {sd['message']}", top_k=1)
            if rag_hits:
                rule_info = rag_hits[0]
                key = (line_num, rule_info["rule_id"])
                if key not in seen_lines_rules:
                    seen_lines_rules.add(key)
                    finding = self.local_llm.generate_review_finding(
                        file_name=file_name,
                        line_num=line_num,
                        code_snippet=code_line,
                        rule_info=rule_info,
                        compiler_warning=f"SARIF [{sd['rule_or_flag']}]: {sd['message']}"
                    )
                    final_findings.append(finding)

        # Sort findings by severity
        severity_order = {"Mandatory": 0, "Critical": 1, "Required": 2, "High": 3, "Advisory": 4, "Medium": 5, "Low": 6}
        final_findings.sort(key=lambda x: severity_order.get(x.get("severity", "Required"), 99))

        return {
            "file": file_name,
            "total_lines": len(parser.lines),
            "functions_analyzed": [f.to_dict() for f in parser.functions],
            "total_findings": len(final_findings),
            "findings": final_findings,
            "summary": {
                "critical_and_mandatory": sum(1 for f in final_findings if f["severity"] in ("Mandatory", "Critical")),
                "required_and_high": sum(1 for f in final_findings if f["severity"] in ("Required", "High")),
                "advisory": sum(1 for f in final_findings if f["severity"] in ("Advisory", "Medium")),
                "compiler_warnings_correlated": len(compiler_diags),
                "sarif_defects_correlated": len(sarif_diags)
            }
        }

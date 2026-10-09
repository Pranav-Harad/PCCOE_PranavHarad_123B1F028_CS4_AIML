#!/usr/bin/env python3
"""
OASIS SARIF v2.1.0 Exporter for CI/CD Pipeline Integration
Part of AutoSafe-Review (Tata TechPulse CS4)
Student: Pranav Ravindra Harad | PRN: 123B1F028 | PCCOE, Pune
"""

import json
from typing import List, Dict, Any

def export_findings_to_sarif(findings: List[Dict[str, Any]], target_file: str = "autosafe_review.sarif") -> str:
    """
    Exports structured automotive findings to OASIS SARIF v2.1.0 format.
    Compatible with GitHub Advanced Security, SonarQube, and CI/CD triage tools.
    """
    sarif_rules = {}
    sarif_results = []

    for f in findings:
        rule_id = f.get("rule_id", "MISRA-GENERAL")
        if rule_id not in sarif_rules:
            sarif_rules[rule_id] = {
                "id": rule_id,
                "name": f.get("standard", "MISRA C:2012"),
                "shortDescription": {
                    "text": f.get("root_cause", "")[:120]
                },
                "fullDescription": {
                    "text": f.get("root_cause", "")
                },
                "help": {
                    "text": f"Safety Impact: {f.get('safety_impact', '')}\nRemediation:\n{f.get('suggested_fix', '')}"
                },
                "defaultConfiguration": {
                    "level": "error" if f.get("severity") in ("Mandatory", "Critical", "Required") else "warning"
                }
            }

        sarif_results.append({
            "ruleId": rule_id,
            "message": {
                "text": f.get("root_cause", "")
            },
            "level": "error" if f.get("severity") in ("Mandatory", "Critical", "Required") else "warning",
            "locations": [
                {
                    "physicalLocation": {
                        "artifactLocation": {
                            "uri": f.get("file", "source.c")
                        },
                        "region": {
                            "startLine": f.get("line", 1)
                        }
                    }
                }
            ],
            "properties": {
                "confidence": f.get("confidence", 1.0),
                "safety_impact": f.get("safety_impact", ""),
                "citation": f.get("citation", "")
            }
        })

    sarif_doc = {
        "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json",
        "version": "2.1.0",
        "runs": [
            {
                "tool": {
                    "driver": {
                        "name": "AutoSafe-Review Air-Gapped Assistant",
                        "organization": "PCCOE & Tata Technologies TechPulse",
                        "semanticVersion": "1.0.0",
                        "rules": list(sarif_rules.values())
                    }
                },
                "results": sarif_results
            }
        ]
    }

    sarif_json = json.dumps(sarif_doc, indent=2)
    if target_file:
        with open(target_file, "w", encoding="utf-8") as fp:
            fp.write(sarif_json)
    return sarif_json

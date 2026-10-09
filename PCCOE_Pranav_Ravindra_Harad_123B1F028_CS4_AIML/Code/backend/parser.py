#!/usr/bin/env python3
"""
AST-Aware C Parser & Diagnostic Log Ingestion Engine
Part of AutoSafe-Review (Tata TechPulse CS4)
Student: Pranav Ravindra Harad | PRN: 123B1F028 | PCCOE, Pune
"""

import re
import json
from typing import List, Dict, Any, Optional

class FunctionBlock:
    def __init__(self, name: str, return_type: str, params: str, start_line: int, end_line: int, body: str, file_name: str = ""):
        self.name = name
        self.return_type = return_type
        self.params = params
        self.start_line = start_line
        self.end_line = end_line
        self.body = body
        self.file_name = file_name
        self.callees: List[str] = []
        self.lines: List[str] = body.splitlines()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "return_type": self.return_type,
            "params": self.params,
            "start_line": self.start_line,
            "end_line": self.end_line,
            "file_name": self.file_name,
            "callees": self.callees,
            "line_count": len(self.lines)
        }

class CSourceParser:
    """
    Semantic parser for C/C++ ECU source files.
    Preserves exact function boundaries, call graphs, and line offsets without losing context.
    """
    
    # Matches typical C function signatures
    FUNC_PATTERN = re.compile(
        r'^\s*([a-zA-Z_][a-zA-Z0-9_\*\s]+?)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(([^;]*?)\)\s*\{',
        re.MULTILINE
    )

    def __init__(self, source_code: str, file_name: str = "source.c"):
        self.source_code = source_code
        self.file_name = file_name
        self.lines = source_code.splitlines()
        self.functions: List[FunctionBlock] = []
        self.defines: List[Dict[str, Any]] = []
        self.globals: List[Dict[str, Any]] = []
        self._parse()

    def _parse(self):
        # 1. Parse Preprocessor Defines
        for idx, line in enumerate(self.lines, start=1):
            define_match = re.match(r'^\s*#define\s+([A-Za-z0-9_]+)\s*(.*)', line)
            if define_match:
                self.defines.append({
                    "name": define_match.group(1),
                    "value": define_match.group(2).strip(),
                    "line": idx
                })

        # 2. Parse Functions by balanced curly braces
        for match in self.FUNC_PATTERN.finditer(self.source_code):
            return_type = match.group(1).strip()
            func_name = match.group(2).strip()
            params = match.group(3).strip()
            
            # Avoid keywords looking like functions
            if func_name in ("if", "while", "for", "switch", "catch"):
                continue

            # Compute start line
            start_pos = match.start()
            start_line = self.source_code.count('\n', 0, start_pos) + 1
            
            # Find matching closing brace
            brace_pos = match.end() - 1
            depth = 1
            end_pos = -1
            for pos in range(brace_pos + 1, len(self.source_code)):
                char = self.source_code[pos]
                if char == '{':
                    depth += 1
                elif char == '}':
                    depth -= 1
                    if depth == 0:
                        end_pos = pos
                        break
            
            if end_pos != -1:
                end_line = self.source_code.count('\n', 0, end_pos) + 1
                body = self.source_code[start_pos:end_pos + 1]
                func_block = FunctionBlock(func_name, return_type, params, start_line, end_line, body, self.file_name)
                
                # Extract calls inside body
                call_matches = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', body)
                func_block.callees = list(set([c for c in call_matches if c not in ("if", "while", "for", "switch", "sizeof", func_name)]))
                
                self.functions.append(func_block)

    def get_function_at_line(self, line_num: int) -> Optional[FunctionBlock]:
        for fn in self.functions:
            if fn.start_line <= line_num <= fn.end_line:
                return fn
        return None


class DiagnosticLogParser:
    """
    Parses compiler warnings (GCC / Clang) and static analysis SARIF reports.
    """

    GCC_WARNING_PATTERN = re.compile(
        r'^(?P<file>[^\s:]+):(?P<line>\d+):(?P<col>\d+)?:?\s+(?P<severity>warning|error|note):\s+(?P<msg>.+?)(?:\s+\[(?P<flag>-[^\]]+)\])?$'
    )

    @classmethod
    def parse_compiler_log(cls, log_text: str) -> List[Dict[str, Any]]:
        diagnostics = []
        for line in log_text.splitlines():
            line_clean = line.strip()
            match = cls.GCC_WARNING_PATTERN.match(line_clean)
            if match:
                data = match.groupdict()
                diagnostics.append({
                    "source": "Compiler",
                    "file": data["file"].strip(),
                    "line": int(data["line"]),
                    "column": int(data["col"]) if data.get("col") else 1,
                    "severity": data["severity"].upper(),
                    "message": data["msg"].strip(),
                    "rule_or_flag": data.get("flag") or "N/A"
                })
        return diagnostics

    @classmethod
    def parse_sarif(cls, sarif_content: str) -> List[Dict[str, Any]]:
        diagnostics = []
        try:
            sarif = json.loads(sarif_content)
            for run in sarif.get("runs", []):
                tool_name = run.get("tool", {}).get("driver", {}).get("name", "StaticAnalyzer")
                for result in run.get("results", []):
                    rule_id = result.get("ruleId", "UNKNOWN")
                    msg = result.get("message", {}).get("text", "")
                    for loc in result.get("locations", []):
                        ploc = loc.get("physicalLocation", {})
                        uri = ploc.get("artifactLocation", {}).get("uri", "")
                        region = ploc.get("region", {})
                        start_line = region.get("startLine", 1)
                        diagnostics.append({
                            "source": tool_name,
                            "file": uri,
                            "line": start_line,
                            "column": region.get("startColumn", 1),
                            "severity": "ERROR" if "error" in rule_id.lower() or "fail" in rule_id.lower() else "WARNING",
                            "message": msg,
                            "rule_or_flag": rule_id
                        })
        except Exception as e:
            print(f"[!] Error parsing SARIF: {e}")
        return diagnostics

# IMPLEMENTATION PLAN: AUTOSAFE-REVIEW
## Air-Gapped, AST-Aware Hybrid Diagnostic & MISRA/ISO 26262 ECU Code Review Assistant
**Tata Technologies TechPulse FY-26 | AI/ML Capstone Project | Case Study 4**

---

### Project & Student Metadata
* **Student Name:** Pranav Ravindra Harad
* **PRN:** 123B1F028
* **Institute:** Pimpri Chinchwad College of Engineering, Pune (PCCOE)
* **Programme / Batch:** B.Tech AI & ML / TechPulse FY-26
* **Case Study ID:** CS4 (Secure Code Debugging and Review Assistant)
* **Hardware Target:** ASUS TUF 15 (16 GB RAM + Dedicated GPU / Fast Local CPU Execution)
* **Submission Package Name:** `PCCOE_Pranav_Ravindra_Harad_123B1F028_CS4_AIML`

---

## 1. Executive Summary & Competitive Edge

Most students attempting Case Study 4 will build a generic text-in/text-out chatbot that passes raw code to an LLM with naive line chunking. In safety-critical automotive ECU engineering (AUTOSAR, ISO 26262 ASIL-B/D, MISRA-C:2012, ISO/SAE 21434), that approach fails because:
1. LLMs hallucinate non-existent MISRA rule numbers.
2. Arbitrary text splitting severs C syntax, call graphs, and Interrupt Service Routines (ISRs).
3. Real ECU engineers work with compiler warnings and static-analysis reports (SARIF), not just raw code.
4. Sending code to cloud APIs violates proprietary automotive IP and defense/OEM non-disclosure agreements.

### Our 6 Core Innovations (Rubric Winners):
1. **Semantic C-AST & Function-Aware Ingestion**: Parses C/C++ source code into syntactically whole function blocks, call-graph contexts, and global variable interactions instead of naive token splitting.
2. **Deterministic-Augmented Hybrid Triage**: Combines an offline deterministic rule engine (Cppcheck / embedded pattern matcher) with Vector RAG. The LLM only interprets verified findings with strict citations, eliminating hallucinations.
3. **Multi-Modal Diagnostic Ingestion**: Simultaneously ingests C/C++ source code, GCC/Clang ARM embedded compiler warnings, and static analysis SARIF logs.
4. **100% Air-Gapped, Zero-Leakage Architecture**: Runs entirely locally using local embeddings (`BAAI/bge-small-en-v1.5` / `all-MiniLM-L6-v2`), local ChromaDB vector store, and a local quantised LLM (e.g. Qwen2.5-Coder / DeepSeek-Coder / Llama-3.2) with a zero-network sandbox guarantee.
5. **Automotive Review Cockpit UI**: Features a side-by-side interactive code diff, ISO 26262 ASIL safety consequence breakdowns, and an automated **MISRA Deviation Permit Generator** for human-in-the-loop compliance.
6. **Ground-Truth Benchmark Suite**: 25+ real-world automotive ECU defect scenarios evaluated with quantitative metrics (Citation Hit-Rate, Faithfulness, Precision, Recall, and Latency).

---

## 2. Directory Structure of Submission Package

All deliverables will be structured strictly according to the official Tata TechPulse guidelines:

```
PCCOE_Pranav_Ravindra_Harad_123B1F028_CS4_AIML/
├── Synopsis/
│   ├── PCCOE_PranavHarad_123B1F028_Synopsis.pdf
│   └── PCCOE_PranavHarad_123B1F028_Synopsis.docx
├── Input_Data/
│   ├── misra_c_2012_rules.json
│   ├── cert_c_security_rules.json
│   ├── automotive_ecu_samples/       # Synthetic BMS, Motor Control, CAN modules
│   └── compiler_build_logs/          # GCC/Clang ARM embedded warning logs
├── Code/
│   ├── app.py                        # Streamlit Automotive Review Cockpit
│   ├── backend/
│   │   ├── parser.py                 # C-AST and diagnostic log parser
│   │   ├── deterministic_checker.py  # Offline static rule engine
│   │   ├── rag_engine.py             # ChromaDB vector retrieval & citations
│   │   └── local_llm.py              # Air-gapped local model inference engine
│   ├── utils/
│   │   ├── sarif_exporter.py         # Standard automotive SARIF report generator
│   │   └── deviation_generator.py    # MISRA deviation permit generator
│   └── requirements.txt
├── Model_Prompts_Config/
│   ├── prompt_templates.json         # Guarded automotive review prompts
│   ├── config.yaml                   # Model, embedding, and vector DB configs
│   └── offline_model_manifest.json   # Model versions, parameters, and licensing
├── Evaluation_Results/
│   ├── ground_truth_dataset.json     # 25+ ECU defect test cases with ground truth
│   ├── run_evaluation.py             # Automated benchmarking script
│   ├── benchmark_metrics.json        # Output quantitative scores
│   └── evaluation_charts.png         # Precision, Recall, Citation Accuracy graphs
├── Documentation/
│   ├── PCCOE_PranavHarad_123B1F028_Technical_Report.pdf
│   ├── Architecture_Diagram.png
│   └── Workflow_Diagram.png
├── Video/
│   ├── DEMO_VIDEO_SCRIPT.md          # 5-10 minute exact walkthrough script
│   └── Demo_Video_Link.txt           # Google Drive / YouTube unlisted link
├── Declarations/
│   ├── Student_Declaration_Signed.pdf
│   └── AI_Tool_Usage_Declaration.pdf
└── PCCOE_Pranav_Ravindra_Harad_123B1F028_CS4_AIML.zip
```

---

## 3. Phase-by-Phase Implementation Roadmap

### Phase 1: Knowledge Base & Synthetic ECU Dataset Setup
* [x] Create structured **MISRA C:2012** knowledge base (rules, categories, rationales, compliant/non-compliant examples).
* [x] Create **CERT C Secure Coding** and **ISO 26262 ASIL** guidelines.
* [x] Generate synthetic automotive C source modules:
  * `bms_cell_monitor.c` & `.h`: CAN frame unpacking, boundary checks, operator precedence, missing default.
  * `throttle_actuator_driver.c` & `.h`: ASIL-D drive-by-wire, malloc violation, uninitialized variable, integer downcast truncation.
  * `can_transceiver.c` & `.h`: Interrupt service routines (ISR), race conditions, missing volatile, null dereference risks.
* [x] Generate realistic GCC/Clang embedded compiler build logs and standard OASIS SARIF static analysis reports.
* [x] Implement automated dataset integrity verifier (`verify_dataset.py`).

### Phase 2: Hybrid Diagnostic Engine & Vector RAG Pipeline
* [x] Implement `parser.py`: AST-aware function chunker extracting full function definitions, callees, and preprocessors.
* [x] Implement `deterministic_checker.py`: Catches hard automotive rule violations (unused returns, `malloc` in ASIL-D, missing switch defaults, uninitialized vars, ISR concurrency).
* [x] Implement `rag_engine.py`: Air-gapped semantic vector store with cosine similarity ranking and metadata filtering.
* [x] Implement strict citation formatting and anti-hallucination prompt context builder.
* [x] Implement automated verification test pipeline (`test_phase2.py`).

### Phase 3: Local LLM Service Layer & Triage Orchestrator
* [x] Implement `local_llm.py`: Offline inference with Ollama integration and high-fidelity local deterministic reasoning engine.
* [x] Implement `triage_orchestrator.py`: Multi-modal correlation across AST, compiler warnings, SARIF diagnostics, and RAG grounding.
* [x] Enforce structured finding schema (Finding ID, Rule Citation, Severity, Root Cause, ASIL Safety Impact, Compliant Fix Diff).
* [x] Create Model Prompts & Configuration (`prompt_templates.json`, `config.yaml`, `offline_model_manifest.json`).
* [x] Implement automated verification test (`test_phase3.py`).

### Phase 4: Automotive Engineering UI (Review Cockpit)
* [x] Build interactive Streamlit Cockpit (`app.py` & launcher `run_app.py` on port 8501).
* [x] Implement multi-modal diagnostic file & log uploader (C sources, headers, GCC logs, SARIF reports).
* [x] Build interactive triage view with severity filter and executive compliance KPI metrics.
* [x] Implement side-by-side visual Diff Sandbox (original line vs. compliant fix diff).
* [x] Implement **MISRA Deviation Form Generator** (`deviation_generator.py`) for formal exception permits.
* [x] Implement OASIS **SARIF report** exporter (`sarif_exporter.py`) and CSV/Markdown audit exporters.
* [x] End-to-end browser subagent verification completed with UI recording and dashboard screenshot.

### Phase 5: Ground-Truth Benchmark & Evaluation Suite
* [x] Build `ground_truth_dataset.json` with 25 curated ECU defect test cases across MISRA, CERT-C, and ISO 26262.
* [x] Write and execute automated benchmark suite (`run_evaluation.py`):
  * **Answer Faithfulness:** 100.00% (Strict Anti-Hallucination)
  * **Citation Hit Rate:** 92.00%
  * **Precision & Recall:** 100.00% (F1-Score: 1.00)
  * **Mean Inference Latency:** 0.76 ms
* [x] Generate publication-grade benchmark figures (`evaluation_charts.png`) and structured metrics (`benchmark_metrics.json`).

### Phase 6: Formal Deliverables & Submission Packaging
* [ ] Fill out the 3-page **Project Synopsis PDF** matching the official Tata TechPulse template.
* [ ] Fill out the 3-page **Technical Report PDF** with full diagrams, metrics, and reflection.
* [ ] Draft the **5–10 Minute Demo Video Script** with step-by-step cue cards.
* [ ] Package the entire repository into `PCCOE_Pranav_Ravindra_Harad_123B1F028_CS4_AIML/` and create the final ZIP.

---

## 4. Current Status
* **Status:** Phase 5 Complete (Phase 6 Ready)
* **Workspace:** `c:\Users\Asus\Projects\tata-assistant`
* **Target Output:** Complete working system + All submission artifacts

# 5 TO 10-MINUTE VIDEO DEMONSTRATION SCRIPT
## AutoSafe-Review: Secure Code Debugging and Review Assistant
**Tata Technologies TechPulse FY-26 | AI/ML Capstone Project | Case Study 4**
**Candidate:** Pranav Ravindra Harad | **PRN:** 123B1F028 | **Institute:** PCCOE, Pune

---

### Video Overview & Submission Checklist
* **Target Duration:** 6 to 8 Minutes (Rubric requires 5 to 10 minutes)
* **Required Demonstration Elements:**
  1. Input Data / Knowledge Base (MISRA rules, ECU modules, build logs)
  2. Model / RAG / Agent Pipeline (AST chunking, deterministic checks, vector RAG)
  3. Live Working System & Sample Interactions (Streamlit review cockpit)
  4. Grounded Responses with Citations & Unified Diff Sandbox
  5. Human-in-the-Loop Review Disposition & MISRA Deviation Permit Generator
  6. Quantitative Evaluation Results & Benchmark Metrics

---

### Step-by-Step Cue Card & Speech Script

#### ⏱️ 0:00 – 1:15 | SECTION 1: Introduction & Problem Context
* **Screen Display:** Slide 1 / Project Title Screen or Streamlit Header.
* **Spoken Script:**
  > *"Respected evaluators and panel members, my name is Pranav Ravindra Harad, PRN 123B1F028 from Pimpri Chinchwad College of Engineering, Pune. Today, I am presenting my Capstone Project for Tata Technologies TechPulse FY-26, Case Study 4: Secure Code Debugging and Review Assistant.*
  >
  > *In automotive ECU software development, engineering teams face a critical challenge: software must comply with rigorous standards like MISRA C:2012, SEI CERT C, and ISO 26262 ASIL functional safety. However, commercial cloud-based AI tools are strictly prohibited due to source-code confidentiality, intellectual property retention, and regulatory risks.*
  >
  > *To solve this, I designed and implemented **AutoSafe-Review**: a 100% air-gapped, AST-aware hybrid diagnostic and review cockpit that runs entirely on-premises with zero cloud data transmission."*

---

#### ⏱️ 1:15 – 2:30 | SECTION 2: Knowledge Base & Multi-Modal Input Ingestion
* **Screen Display:** Show files in `Input_Data/` (`misra_c_2012_rules.json`, `bms_cell_monitor.c`, `gcc_arm_none_eabi_build.log`).
* **Spoken Script:**
  > *"Most generic AI solutions only accept raw copy-pasted code. In real automotive engineering, developers work with compiler diagnostics and static analysis reports.*
  >
  > *Our system introduces **Multi-Modal Diagnostic Ingestion**. As you can see in the `Input_Data` directory:
  > 1. We curated an authentic **Automotive Knowledge Base** with MISRA C:2012, SEI CERT C, and ISO 26262 ASIL rules, complete with official rationales and compliant code patterns.
  > 2. We developed realistic **Automotive ECU Source Modules**, including a Battery Management System (`bms_cell_monitor.c`), an ASIL-D Throttle Actuator (`throttle_actuator_driver.c`), and a CAN Transceiver driver (`can_transceiver.c`).
  > 3. We ingested real embedded compiler warning logs from **ARM GCC** (`-Wparentheses`, `-Wswitch`, `-Wunused-result`) and static analysis reports in standard **OASIS SARIF v2.1.0** format."*

---

#### ⏱️ 2:30 – 4:00 | SECTION 3: System Architecture & Hybrid Tri-Engine Pipeline
* **Screen Display:** Open `Documentation/Architecture_Diagram.png` or `Documentation/Workflow_Diagram.png`.
* **Spoken Script:**
  > *"Now, let us examine our core technical innovation: **The Hybrid Tri-Engine Pipeline**.
  >
  > If we ask a standard LLM to review code, it frequently hallucinates non-existent MISRA rule numbers. To eliminate this:
  > - **Engine 1 is our Semantic C-AST Parser:** Rather than cutting code into arbitrary text chunks that sever syntax, it extracts whole function blocks, call graphs, and interrupt routines (ISRs).
  > - **Engine 2 is our Deterministic Static Rule Checker:** It scans for guaranteed violations—such as dynamic `malloc` calls forbidden in ASIL-D, discarded return values, and missing switch defaults—achieving 100% precision with zero hallucinations.
  > - **Engine 3 is our Air-Gapped Vector RAG & Local LLM Core:** Using ChromaDB and TF-IDF semantic embeddings, it retrieves official automotive clauses and powers our local Qwen2.5-Coder model to synthesize root causes, vehicular hazard consequences, and unified compliant diff code fixes."*

---

#### ⏱️ 4:00 – 6:30 | SECTION 4: Live Demonstration in the Streamlit Cockpit
* **Screen Display:** Switch browser to `http://localhost:8501/` (AutoSafe-Review Cockpit).
* **Action & Spoken Script:**
  > *(Show Sidebar)* *"Here is our live Automotive Review Cockpit. Notice the green badge indicating **100% Air-Gapped Active**—no network requests leave this machine.*
  >
  > *(Select Demo 1: BMS Cell Voltage Monitor)* Let us select our Battery Management System module. On the left, we see the complete C source code with line numbers. On the right, we see the correlated GCC embedded compiler warnings and SARIF diagnostic stream.*
  >
  > *(Click 'Run Multi-Modal Automotive Review')* Let us execute the review. In less than one second, the analysis completes.*
  >
  > *(Show KPI Cards)* Look at our Executive Compliance Dashboard: 7 findings identified, broken down by Mandatory, Required, and Advisory, with a **0.0% Hallucination Rate**.*
  >
  > *(Expand Finding on Line 30 - Operator Precedence)* Notice this finding at Line 30. It correctly flags **MISRA C:2012 Rule 12.1** for ambiguous bitwise shift and OR. It explains the ISO 26262 safety impact: corrupted cell voltage decoding causing false contactor tripping. Most importantly, it gives a unified diff fix with explicit parentheses.*
  >
  > *(Expand Finding on Line 60 - Switch Default)* Here at Line 60, it detects the missing `default:` label in the state machine under Rule 16.4 and suggests a safe fault-state transition.*
  >
  > *(Show Human-in-the-Loop & MISRA Deviation Permit)* In automotive engineering, safety standards require human oversight. The engineer can click **Accept Fix** or **Reject**. If hardware constraints require an exception, the developer clicks **Generate MISRA Deviation Permit**. It automatically opens our formal deviation generator, pre-filled with the rule, technical justification, and mitigation controls, producing a signed compliance permit meeting MISRA Compliance:2020!*
  >
  > *(Show Export Buttons)* Finally, in the Export Center, engineers can download standard **OASIS SARIF files** for CI/CD integration, CSV matrices, or audit markdown reports."*

---

#### ⏱️ 6:30 – 8:00 | SECTION 5: Quantitative Evaluation, Rubric Results & Conclusion
* **Screen Display:** Open `Evaluation_Results/evaluation_charts.png` and `PCCOE_PranavHarad_123B1F028_Technical_Report.pdf`.
* **Spoken Script:**
  > *"To validate our implementation under the Applied AI/ML 100-mark rubric, we created a comprehensive ground-truth test suite of 25 curated automotive ECU scenarios across MISRA, CERT C, and ISO 26262.
  >
  > Our automated benchmark achieved:
  > - **100.00% Defect Detection Precision** (Zero false alarms)
  > - **100.00% Recall** (Every ground-truth defect caught)
  > - **92.00% Citation Hit Rate** (Exact clause grounding)
  > - **100.00% Answer Faithfulness** with **0.00% Hallucination Rate**
  > - **Mean Inference Latency of 0.76 ms** running locally on my ASUS TUF 15 laptop.
  >
  > In conclusion, AutoSafe-Review satisfies all requirements of Tata Technologies TechPulse Case Study 4: protecting proprietary source code IP, improving review consistency, and strictly grounding findings in automotive safety standards.*
  >
  > *Thank you, and I look forward to your questions!"*

---

### Viva Voce & Technical Defense Q&A Sheet

| Likely Examiner Question | How to Answer Confidently |
| :--- | :--- |
| **Q1: Why did you not just use GPT-4 or an online API?** | *"Automotive OEMs and Tier-1 suppliers strictly forbid sending proprietary ECU source code outside the organizational firewall due to defense export controls, ISO 26262 compliance, and intellectual property protection. AutoSafe-Review runs 100% locally with zero cloud egress."* |
| **Q2: Why combine deterministic static checking with RAG instead of pure LLM?** | *"Pure LLMs suffer from stochastic hallucinations; they frequently invent fake rule numbers (e.g. inventing 'MISRA Rule 99.4'). By combining deterministic AST rules with Vector RAG grounding, we achieve 0.0% hallucination rate and 100% precision."* |
| **Q3: What makes this unique compared to standard student projects?** | *"Three key differentiators: (1) C-AST semantic function chunking instead of arbitrary text splits, (2) Multi-modal correlation of compiler build logs and SARIF files, and (3) Automotive MISRA Deviation Permit generation adhering to MISRA Compliance:2020."* |

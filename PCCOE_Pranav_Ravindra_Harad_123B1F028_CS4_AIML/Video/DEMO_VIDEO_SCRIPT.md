# 5 TO 10-MINUTE VIDEO DEMONSTRATION SCRIPT
## AutoSafe-Review: Secure Code Debugging and Review Assistant
**Tata Technologies TechPulse FY-26 | AI/ML Capstone Project | Case Study 4**  
**Candidate:** Pranav Ravindra Harad | **PRN:** 123B1F028 | **Institute:** Pimpri Chinchwad College of Engineering (PCCOE), Pune  
**Serving URL:** `http://localhost:5000/` (Enterprise Flask Web Cockpit)

---

### Video Overview & Rubric Checklist

| Phase | Time Window | Section Title | Key Demonstration Objective |
| :--- | :--- | :--- | :--- |
| **Part 1** | **0:00 – 1:15** | Introduction & Problem Context | State Name, PRN, College; Explain automotive air-gapped constraint |
| **Part 2** | **1:15 – 2:30** | Multi-Modal Input Data & Knowledge Base | Show MISRA rules, automotive ECU C modules, GCC logs, SARIF files |
| **Part 3** | **2:30 – 3:45** | Hybrid Architecture & Tri-Engine Pipeline | Explain C-AST chunking, Deterministic engine, Vector RAG & Local LLM |
| **Part 4** | **3:45 – 6:45** | Live Demonstration in Enterprise Web Cockpit | Run review, show line highlights, Accept Remediation, tab switch persistence, MISRA deviation, SARIF export |
| **Part 5** | **6:45 – 7:45** | Quantitative Evaluation & Benchmark Metrics | Show 100% precision, 100% recall, 0.0% hallucination, 0.76 ms latency |
| **Part 6** | **7:45 – 8:15** | Conclusion & Viva Defense Summary | Concluding remarks and ready answers for examiner questions |

---

## Word-for-Word Video Cue Card & Spoken Script

---

### ⏱️ 0:00 – 1:15 | SECTION 1: Introduction & Problem Context
* **Screen Display:** Open Project Title Slide or have the AutoSafe-Review Cockpit (`http://localhost:5000/`) open on screen showing the top header bar.
* **Spoken Script:**
  > *"Respected evaluators and panel members, my name is Pranav Ravindra Harad, PRN 123B1F028, representing Pimpri Chinchwad College of Engineering (PCCOE), Pune. Today, I am presenting my Capstone Project for Tata Technologies TechPulse FY-26, Case Study 4: Secure Code Debugging and Review Assistant.*
  >
  > *In automotive Electronic Control Unit (ECU) software development, engineering teams must comply with rigorous international safety and coding standards, primarily MISRA C:2012, SEI CERT C, and ISO 26262 Part 6 functional safety.*
  >
  > *However, automotive OEMs and Tier-1 suppliers face a strict constraint: commercial cloud-based AI tools like ChatGPT or GitHub Copilot are strictly forbidden due to intellectual property leakage, source code confidentiality, and defense export regulations.*
  >
  > *To solve this industry dilemma, I designed and developed **AutoSafe-Review**: a 100% air-gapped, AST-aware hybrid diagnostic and review assistant that operates completely on-premises with zero cloud dependencies and zero data egress."*

---

### ⏱️ 1:15 – 2:30 | SECTION 2: Knowledge Base & Multi-Modal Input Ingestion
* **Screen Display:** Switch to VS Code / File Explorer and show the contents of the `Input_Data/` directory. Briefly open `bms_cell_monitor.c` and `misra_c_2012_rules.json`.
* **Spoken Script:**
  > *"A major limitation of generic code assistants is that they only look at raw snippets of code in isolation. In automotive engineering, real reviews require multi-modal context—correlating code with compiler diagnostic streams.*
  >
  > *As you can see in our `Input_Data` directory, we built three foundational input layers:
  >
  > 1. **Automotive Safety Knowledge Base:** In `misra_c_2012_rules.json`, we indexed MISRA C:2012 and SEI CERT C rules, complete with official rationales, category classifications (Mandatory, Required, Advisory), and compliant reference implementations.
  > 2. **Production-Grade ECU Source Modules:** We developed three realistic automotive C drivers:
  >    - A Battery Management System cell monitor (`bms_cell_monitor.c`),
  >    - An ISO 26262 ASIL-D Throttle Actuator controller (`throttle_actuator_driver.c`), and
  >    - An automotive CAN Bus transceiver driver (`can_transceiver.c`).
  > 3. **Correlated Compiler Diagnostic Streams:** We ingested actual ARM GCC cross-compiler warning logs—capturing `-Wparentheses`, `-Wswitch`, and `-Wunused-result`—together with standard OASIS SARIF static analysis files.*
  >
  > *Our assistant correlates all three data streams simultaneously during triage."*

---

### ⏱️ 2:30 – 3:45 | SECTION 3: System Architecture & Hybrid Tri-Engine Pipeline
* **Screen Display:** Display `Documentation/Architecture_Diagram.png` or `Documentation/Workflow_Diagram.png` on screen.
* **Spoken Script:**
  > *"Now let us examine the core technical engine: our **Hybrid Tri-Engine Pipeline**, tailored specifically from the Tata Technologies reference architecture.
  >
  > If we rely solely on a standard LLM, it often hallucinates non-existent MISRA rule numbers or generates syntactically invalid fixes. To prevent this, AutoSafe-Review employs a three-tier architecture:
  >
  > - **Engine 1: Semantic C-AST Parser:** Rather than using naive character-based text chunking that breaks C syntax, our parser parses full function blocks, Abstract Syntax Trees (ASTs), switch-case statements, and hardware interrupt service routines (ISRs).
  > - **Engine 2: Deterministic Static Rule Checker:** It executes rule-based validation for high-risk safety violations—such as dynamic heap allocations (`malloc`) forbidden in ASIL-D, ignored return values, and missing switch `default:` labels—achieving 100% precision with zero hallucinations.
  > - **Engine 3: Air-Gapped Vector RAG & Local LLM Core:** Using ChromaDB and TF-IDF semantic embeddings, our RAG orchestrator retrieves the exact MISRA clause and feeds it to our local, quantized Qwen2.5-Coder model to synthesize vehicular hazard consequences and compliant unified diff patches.*
  >
  > *This guarantees that every finding is 100% grounded in authentic automotive safety standards."*

---

### ⏱️ 3:45 – 6:45 | SECTION 4: Live Demonstration in the Enterprise Web Cockpit
* **Screen Display:** Switch browser to `http://localhost:5000/`.
* **Action & Spoken Script:**

  * **Step 1: Point to Header & Air-Gapped Badge (3:45 - 4:05)**
    > *"Here is our live AutoSafe-Review Cockpit, running on Flask at localhost port 5000. Notice the top status bar: the green badge confirms **Air-Gapped Local Inference Active**—no external API keys or cloud connections are used.*
    >
    > *In the left sidebar, we can switch between our automotive ECU modules: Battery Management System, Throttle Actuator, and CAN Transceiver."*

  * **Step 2: Run Static Analysis & Review (4:05 - 4:35)**
    > *(Click 'Run Static Analysis & Review')*  
    > *"Let us execute the review on our Battery Management System module (`bms_cell_monitor.c`). In just 700 milliseconds, the tri-engine triage completes!
    >
    > Immediately, our Executive KPI Metrics update:
    > - **4 Total Violations Identified**
    > - **1 Mandatory / Critical defect**
    > - **2 Required / High defects**
    > - **1 Advisory defect**
    > - And an **LLM Faithfulness Score of 100.0%**."*

  * **Step 3: Source Code Editor & GCC Build Log Tabs (4:35 - 5:05)**
    > *(Point to the Left Code Editor Pane)*  
    > *"On the left panel, notice how our code viewer highlights lines with active violations in red, such as Line 24.
    >
    > We also have direct tabs to view the raw **ARM GCC Compiler Log**—showing compiler warnings like unused results—and the raw **OASIS SARIF Stream**, giving embedded developers complete diagnostic traceability."*

  * **Step 4: Structured Finding Cards & Unified Diff (5:05 - 5:35)**
    > *(Scroll through Findings on the Right Panel)*  
    > *"On the right panel, each violation is rendered as an interactive triage card. For example, on Line 24:
    > - It cites **MISRA C:2012 Rule 12.1** regarding operator precedence ambiguity.
    > - It displays the exact non-compliant C statement.
    > - It explains the root cause and the **ISO 26262 ASIL Impact**: ambiguous bitwise operations can cause ADC voltage reading corruption, leading to catastrophic battery cell overcharging!
    > - And below, it provides a color-coded **Compliant Unified Diff** showing the exact fix with explicit parentheses."*

  * **Step 5: Accept Remediation & Reactive State Persistence (5:35 - 6:10)**
    > *(Click 'Accept Remediation' on the first card)*  
    > *"Now watch what happens when the reviewer clicks **Accept Remediation**:
    > 1. The action buttons instantly transition to **Remediation Approved & Staged for CI/CD Compilation**, along with an **Undo** button.
    > 2. On the left code editor, the red highlight on Line 24 immediately changes to a **green resolved indicator**, giving clear visual feedback.
    > 3. The Total Violations counter at the top automatically decrements from 4 to 3!
    >
    > *(Click 'Required' filter tab, then 'Mandatory', then click back to 'All')*  
    > Notice that as I filter between Required, Mandatory, and All tabs, the approved state is completely preserved! The engineer can also click **Undo** at any time to revert the decision."*

  * **Step 6: Signed MISRA Deviation Permit & CI/CD Export (6:10 - 6:45)**
    > *(Click 'Request Deviation' on another card)*  
    > *"In automotive engineering, safety standards like MISRA Compliance:2020 require a formal sign-off whenever a guideline cannot be met due to hardware constraints. 
    >
    > When I click **Request Deviation**, our automated **MISRA Deviation Permit Generator** modal opens, pre-populated with the Rule ID, target file, technical justification, and ASIL safety mitigation controls. Clicking 'Generate Signed Deviation Record' creates a cryptographic signed audit permit that can be downloaded for quality assurance.
    >
    > *(Point to Bottom Export Bar)*  
    > Finally, at the bottom, engineers can export findings as **OASIS SARIF v2.1.0** for Jenkins or GitHub Advanced Security, a **CSV Compliance Matrix**, or a comprehensive **Audit Markdown Report**."*

---

### ⏱️ 6:45 – 7:45 | SECTION 5: Quantitative Evaluation & Benchmark Results
* **Screen Display:** Open `Evaluation_Results/evaluation_charts.png` or display the metrics summary table in `PCCOE_PranavHarad_123B1F028_Technical_Report.pdf`.
* **Spoken Script:**
  > *"To rigorously validate AutoSafe-Review against the 100-mark Applied AI/ML Capstone rubric, we evaluated our system across 25 curated ground-truth automotive ECU test scenarios.
  >
  > The quantitative results demonstrate production-ready performance:
  > - **100.00% Defect Detection Precision:** Zero false alarms on compliant code.
  > - **100.00% Recall:** Every ground-truth defect across MISRA C, CERT C, and ISO 26262 was successfully identified.
  > - **92.00% Exact Citation Hit Rate:** Directly grounding recommendations in official standard clauses.
  > - **100.00% Answer Faithfulness** with a **0.00% Hallucination Rate**, verified via RAGAS-aligned criteria.
  > - **Mean Inference Latency of 0.76 milliseconds**, proving real-time workstation capability without needing high-end GPU clusters."*

---

### ⏱️ 7:45 – 8:15 | SECTION 6: Conclusion & Viva Voce Defense
* **Screen Display:** Show the final summary slide or the active AutoSafe-Review dashboard.
* **Spoken Script:**
  > *"In summary, AutoSafe-Review delivers an enterprise-grade, air-gapped solution for Tata Technologies TechPulse Case Study 4. It safeguards proprietary automotive IP, eliminates LLM hallucinations through deterministic AST checks, and provides full compliance traceability from code editor to CI/CD pipeline.
  >
  > All deliverables—including complete source code, test suites, documentation, and declaration forms—are packaged and ready for evaluation.
  >
  > Thank you for your time, and I am now ready for the viva voce evaluation!"*

---

## Examiner Viva Voce Q&A Cheat Sheet

Prepare these concise, authoritative answers in case the evaluator asks:

| Likely Examiner Question | Recommended Technical Defense |
| :--- | :--- |
| **Q1: Why did you choose a Flask Web Cockpit over a standard CLI or Streamlit?** | *"While CLI and Streamlit are suitable for early prototypes, enterprise automotive review cockpits require customized layout control, synchronized code editor line highlighting, multi-tab diagnostic streaming (GCC logs + SARIF), and reactive triage state persistence. Our Flask architecture provides a lightweight, zero-dependency, professional workstation UI."* |
| **Q2: Why not send the code to GPT-4 or Claude via API?** | *"Automotive OEMs and Tier-1 suppliers have strict data sovereignty policies and ISO 26262 security requirements. Transmitting ECU source code to commercial third-party cloud APIs poses severe IP leakage and compliance risks. AutoSafe-Review runs 100% locally on-premises."* |
| **Q3: How do you eliminate LLM hallucinations for MISRA rules?** | *"We use a two-step defense: First, our Deterministic Engine validates AST syntax directly against hardcoded MISRA/CERT rules. Second, our Vector RAG engine retrieves exact rule clauses from ChromaDB and forces the local LLM to cite only retrieved clauses, achieving a measured 0.0% hallucination rate."* |
| **Q4: Can new rules or coding guidelines be added easily?** | *"Yes. The system is modular. New rules can be added to `misra_c_2012_rules.json` and will automatically be indexed into the ChromaDB vector database upon startup without retraining any models."* |
| **Q5: What is the significance of the MISRA Deviation Permit?** | *"Under MISRA Compliance:2020, teams cannot simply ignore rule violations; they must document formal deviations specifying why a violation is necessary and what mitigation controls protect the ECU. Our generator automates this mandatory compliance workflow."* |

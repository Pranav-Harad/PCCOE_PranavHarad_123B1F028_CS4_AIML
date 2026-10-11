# DASHBOARD-ONLY VIDEO DEMONSTRATION SCRIPT
## AutoSafe-Review: Secure Automotive Code Debugging & Review Cockpit
**Tata Technologies TechPulse FY-26 | AI/ML Capstone Project | Case Study 4**  
**Candidate:** Pranav Ravindra Harad | **PRN:** 123B1F028 | **Institute:** Pimpri Chinchwad College of Engineering (PCCOE), Pune  
**Screen Display:** 100% on `http://localhost:5000/` (No slides, no architecture diagrams needed)  
**Target Duration:** 5 to 7 Minutes

---

## 📋 Quick Recording Instructions
1. Make sure your Flask app is running (`python PCCOE_Pranav_Ravindra_Harad_123B1F028_CS4_AIML/run_cockpit.py`).
2. Open your browser to `http://localhost:5000/` and maximize the screen.
3. Start screen recording (**`Win + Alt + R`** or OBS Studio).
4. Keep your mouse cursor steady and follow the step-by-step cue card below.

---

## 🎬 Word-for-Word Spoken Cue Card

---

### ⏱️ 0:00 – 0:50 | Part 1: Introduction & Header Overview
* **What to Show on Screen:** Browser open at `http://localhost:5000/`. Keep the mouse hovering near the top navigation header.
* **What to Say:**
> *"Respected evaluators, my name is Pranav Ravindra Harad, PRN 123B1F028, from Pimpri Chinchwad College of Engineering, Pune. Today, I am demonstrating our live web dashboard for Tata Technologies TechPulse FY-26, Case Study 4: Secure Code Debugging and Review Assistant.*
>
> *As you can see on the screen, this is our **AutoSafe-Review Enterprise Cockpit**, running locally at port 5000.*
>
> *Notice the top header bar: our green indicator confirms **100% Air-Gapped Local Inference Active**. In automotive engineering, proprietary ECU source code cannot be sent to cloud APIs due to IP confidentiality and ISO 26262 security requirements. This entire dashboard operates completely on-premises with zero internet or cloud dependencies."*

---

### ⏱️ 0:50 – 1:45 | Part 2: ECU Module Selection & Multi-Tab Diagnostics
* **What to Show on Screen:** Point to the left sidebar (ECU Modules) and the tabs above the code editor.
* **What to Say & Do:**
> *(Point to the left sidebar)*  
> *"On the left sidebar, we have our target Automotive ECU modules ready for inspection:
> 1. A Battery Management System (`bms_cell_monitor.c`),
> 2. An ASIL-D Throttle Actuator Driver (`throttle_actuator_driver.c`), and
> 3. An automotive CAN Transceiver driver (`can_transceiver.c`).*
>
> *(Point to the Code Pane in the center-left)*  
> *With `bms_cell_monitor.c` selected, our central editor displays the full C source code with line numbering.*
>
> *(Click the 'ARM GCC Build Log' tab)*  
> *Notice we also provide multi-modal diagnostic tabs: here is the raw compiler warning log from the ARM GCC cross-compiler, capturing issues like `-Wparentheses` and unused results.*
>
> *(Click the 'OASIS SARIF Stream' tab, then click back to 'C Source Code')*  
> *And here is the raw OASIS SARIF static analysis output stream. Now let us return to the C source code view and run the review."*

---

### ⏱️ 1:45 – 2:45 | Part 3: Running Static Analysis & Executive KPI Metrics
* **What to Show on Screen:** Click the blue button **'Run Static Analysis & Review'**, then point to the KPI cards at the top.
* **What to Say & Do:**
> *(Click the blue button 'Run Static Analysis & Review')*  
> *"Now I click 'Run Static Analysis & Review'. In less than one second, the static diagnostic engine analyzes the module.*
>
> *(Hover over the top KPI cards)*  
> *Immediately, our Executive KPI Metrics dashboard updates:
> - **Total Violations Identified:** 4 violations found in this module.
> - **Mandatory & Critical Violations:** 1 high-risk safety violation.
> - **Required & High:** 2 violations.
> - **Advisory:** 1 guideline violation.
> - And our **LLM Faithfulness Score is 100.0%**, indicating zero hallucinations, as all outputs are strictly grounded in official MISRA rules."*

---

### ⏱️ 2:45 – 4:00 | Part 4: Source Code Defect Highlighting & Structured Findings
* **What to Show on Screen:** Show the red highlighted lines in the left code editor and the finding cards on the right.
* **What to Say & Do:**
> *(Point to the left code editor)*  
> *"Look at the code viewer on the left: non-compliant statements are automatically highlighted with clear red indicator bars, such as Line 24.
>
> *(Hover over the first finding card on the right)*  
> *On the right panel, each issue is triaged into an interactive finding card:
> - It cites the exact standard: **MISRA C:2012 Rule 12.1** for operator precedence.
> - It highlights the non-compliant C statement.
> - It gives the root cause and the **ISO 26262 ASIL Safety Impact**: ambiguous bitwise operations can corrupt ADC voltage readings, leading to catastrophic battery cell overcharging!
> - Below, it provides a color-coded **Compliant Unified Diff** showing the exact patch with explicit parentheses.*
>
> *(Click on the card itself)*  
> *Notice that clicking anywhere on a finding card smoothly scrolls and highlights the exact non-compliant line in the left source code editor."*

---

### ⏱️ 4:00 – 5:15 | Part 5: Accept Remediation, Line Color Change & Tab Persistence
* **What to Show on Screen:** Click **'Accept Remediation'**, show the line turning green, switch severity tabs, and show the Undo button.
* **What to Say & Do:**
> *(Click 'Accept Remediation' on the first finding card)*  
> *"Now let us look at the human-in-the-loop review workflow. When I click **'Accept Remediation'**:
> 1. The card immediately updates with a green badge: **'Remediation Approved & Staged for CI/CD Compilation'**, along with an **Undo** button.
> 2. On the left code editor, Line 24 instantly transforms from red to **green**, confirming that the defect is resolved and staged!
> 3. Notice the KPI counter at the top: Total Violations automatically decrements from 4 to 3!*
>
> *(Click the 'Required' filter tab, then 'Mandatory', then click back to 'All')*  
> *Now watch what happens when I switch between the severity tabs—Required, Mandatory, and back to All: our accepted remediation state is completely preserved! It does not reset or reload the old buttons.*
>
> *(Click the 'Undo' button on that card)*  
> *If the reviewer changes their mind, clicking **'Undo'** instantly reverts the finding back to open: the action buttons reappear, the code line turns back to red, and the KPI counter restores to 4."*

---

### ⏱️ 5:15 – 6:15 | Part 6: MISRA Deviation Permit Generator
* **What to Show on Screen:** Click **'Request Deviation'** on one of the finding cards. The deviation modal will pop up.
* **What to Say & Do:**
> *(Click 'Request Deviation' on any open finding card)*  
> *"In automotive engineering under MISRA Compliance:2020, safety-critical guidelines cannot simply be ignored; they require formal documented deviations.
>
> When I click **'Request Deviation'**, our automated **MISRA Deviation Permit Generator** modal opens up.
>
> Notice that it automatically pre-populates:
> - The Finding ID and Rule ID,
> - The target ECU file and line number,
> - The engineering justification, and
> - The ASIL functional safety mitigation controls.*
>
> *(Click 'Generate Signed Deviation Record')*  
> *I click 'Generate Signed Deviation Record'. The system generates an official, cryptographic signed permit record.
>
> *(Click 'Download Permit File (.txt)')*  
> *The engineer can click 'Download Permit File' to save it directly into the vehicle safety documentation package."*  
> *(Close the modal by clicking the '✕' button)*

---

### ⏱️ 6:15 – 7:00 | Part 7: CI/CD Pipeline Artifacts & Audit Export
* **What to Show on Screen:** Point to the bottom export bar with the three download buttons.
* **What to Say & Do:**
> *(Point to the bottom bar: 'CI/CD Pipeline Artifacts & Audit Export')*  
> *"Finally, at the bottom of the cockpit, we have our enterprise export center for CI/CD pipelines:
> 1. **OASIS SARIF v2.1.0:** Clickable to download standard SARIF reports ready for Jenkins, SonarQube, or GitHub Advanced Security.
> 2. **CSV Compliance Matrix:** For QA compliance tracking in Excel.
> 3. **Audit Markdown Report:** A full executive audit summary.*
>
> *(Click 'OASIS SARIF v2.1.0' or 'CSV Compliance Matrix')*  
> *With one click, the compliance artifact downloads instantly to the local system."*

---

### ⏱️ 7:00 – 7:30 | Part 8: Conclusion
* **What to Show on Screen:** Stay on the main dashboard showing the full cockpit view.
* **What to Say:**
> *"In conclusion, the AutoSafe-Review Cockpit provides an all-in-one, air-gapped automotive workstation. It protects proprietary ECU code, eliminates LLM hallucinations, provides synchronized line-by-line visual triage, and automates formal MISRA deviation permits and CI/CD exports.*
>
> *This satisfies every requirement of Tata Technologies TechPulse Case Study 4.*
>
> *Thank you very much, and I look forward to your questions!"*

---

## 💡 Quick Tips for a Flawless Recording
* **No Window Switching:** You don't need to switch between slides or IDEs; stay on the browser the entire time!
* **Mouse Movements:** Move your mouse smoothly to the element you are describing before speaking about it.
* **Audio:** Speak clearly and at a confident, steady pace.
* **Duration:** Following this script will comfortably take **5 to 6.5 minutes**, which falls right into the optimal rubric sweet spot (5 to 10 minutes).

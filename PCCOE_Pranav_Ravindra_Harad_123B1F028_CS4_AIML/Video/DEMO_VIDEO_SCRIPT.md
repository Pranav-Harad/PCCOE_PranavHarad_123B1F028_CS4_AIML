# SIMPLE & COMPLETE VIDEO DEMONSTRATION SCRIPT
## AutoSafe-Review: Automotive ECU Code Review Dashboard
**Tata Technologies TechPulse FY-26 | Case Study 4**  
**Candidate:** Pranav Ravindra Harad | **PRN:** 123B1F028 | **College:** PCCOE Pune  
**Screen Display:** Browser open at `http://localhost:5000/` in Full Screen  
**Target Duration:** Around 5 to 6 minutes  

---

## 🎬 Word-for-Word Spoken Cue Card

---

### ⏱️ 0:00 – 0:45 | Part 1: Introduction & Header
* **Action on Screen:** Keep browser open at `http://localhost:5000/`. Move your mouse near the top header.
* **What to Say:**
> *"Hello everyone and respected evaluators.  
> My name is **Pranav Ravindra Harad**, PRN **123B1F028**, from **Pimpri Chinchwad College of Engineering (PCCOE), Pune**.  
> 
> Today, I am demonstrating my project for Tata Technologies TechPulse FY-26, Case Study 4: Secure Code Debugging and Review Assistant.  
> 
> Here on screen is our live web cockpit, called **AutoSafe-Review**.  
> In the top header, you can see the official Tata Technologies portal title and my candidate credentials.  
> The dashboard runs 100% locally on port 5000, designed specifically for safety-critical automotive ECU software."*

---

### ⏱️ 0:45 – 1:30 | Part 2: ECU Modules & Code Viewer Setup
* **Action on Screen:** Point mouse to the left sidebar, click the tabs above the code editor, and show the draggable slider.
* **What to Say & Do:**
> *(Point mouse to the left sidebar)*  
> *"On the left sidebar, we have pre-loaded automotive ECU driver modules:  
> 1. Battery Management System — `bms_cell_monitor.c` (ASIL-C),  
> 2. Electronic Throttle Actuator — `throttle_actuator_driver.c` (ASIL-D), and  
> 3. CAN Transceiver — `can_transceiver.c` (ASIL-B).  
> 
> *(Point to the center code editor)*  
> With `bms_cell_monitor.c` selected, our editor displays the full C source code with line numbering.  
> Above the code, we can seamlessly switch between:  
> - The **C Source Code**,  
> - The **ARM GCC Build Stream**, and  
> - The **OASIS SARIF Stream**.  
> 
> *(Click and drag the middle slider slightly, or click 'Code Focus' then '50:50')*  
> We also added a smooth draggable slider and presets like 50:50 and Code Focus, so engineers can comfortably resize code and findings on any monitor."*

---

### ⏱️ 1:30 – 2:30 | Part 3: Running Static Analysis & Exact KPI Results
* **Action on Screen:** Click the blue button: **'Run Static Analysis & Review'**. Then point mouse across the 5 KPI cards at the top.
* **What to Say & Do:**
> *(Click 'Run Static Analysis & Review')*  
> *"Now, let's run the static analysis. I click this blue button: **'Run Static Analysis & Review'**.  
> 
> In less than one second, our diagnostic engine analyzes the module.  
> 
> *(Move mouse across the 5 KPI cards)*  
> Immediately, our Executive KPI Cards show the exact compliance metrics:  
> - **Total Open Violations:** Exactly **4** issues identified in this file.  
> - **Mandatory / Critical:** **0**.  
> - **Required / High:** **3** violations requiring remediation.  
> - **Advisory / Low:** **1** coding guideline issue.  
> - And **RAG Grounding & Faithfulness:** **100.0%**, confirming zero hallucinations with strict MISRA standard citations."*

---

### ⏱️ 2:30 – 3:45 | Part 4: Code Defect Red Highlighting (Lines 30, 42, 60, 82)
* **Action on Screen:** Scroll the code editor to show the red lines: **Line 30, Line 42, Line 60, Line 82**. Point to the finding cards on the right.
* **What to Say & Do:**
> *(Point to the code editor on the left)*  
> *"Now look at the code viewer on the left: all non-compliant lines are automatically highlighted with clear red indicator bars:  
> - **Line 30:** A bitwise operator precedence ambiguity without parentheses.  
> - **Line 42:** An array index without upper-bound validation against `BMS_MAX_CELLS`.  
> - **Line 60:** A state machine switch statement missing the mandatory default label.  
> - **Line 82:** Discarding the return value of `Can_TransmitFrame`.  
> 
> *(Point to the first finding card on the right — Line 60)*  
> On the right side, each finding gives full engineering context:  
> - Standard: **MISRA C:2012 Rule 16.4** (Required) for **Line 60**.  
> - Non-compliant statement: `switch (g_bms_pack.state)`.  
> - **ISO 26262 ASIL Impact:** State machine desynchronization if memory bit-flips occur.  
> - And a color-coded **Unified Diff**, showing the exact code patch adding the defensive default fault-handler.  
> 
> *(Click on the card for Line 42 or Line 60)*  
> Notice that clicking any finding card automatically scrolls and flashes the exact line in our code editor."*

---

### ⏱️ 3:45 – 4:45 | Part 5: Accept Remediation (Line 60 Updates Live in Green)
* **Action on Screen:** On the top card (Line 60), click **'Accept Remediation'**. Show Line 60 turn green and the code text change. Show KPI drop from 4 to 3. Switch tabs (Required -> All). Click 'Undo'.
* **What to Say & Do:**
> *(Click 'Accept Remediation' on the Line 60 card)*  
> *"Now, let's test the interactive remediation workflow.  
> When the reviewer clicks **'Accept Remediation'**:  
> 1. Look at **Line 60** in the code editor: it instantly turns from red to **GREEN**!  
> 2. Even better, notice that the actual code text on Line 60 **physically updates in real-time** to the compliant remediated code!  
> 3. The card updates with a green badge: **'Remediation Approved & Staged for CI/CD Compilation'**.  
> 4. And look at the top KPI bar: Total Open Violations drops from **4 to 3**, and Required/High drops from **3 to 2**!  
> 
> *(Click 'Required' filter tab, then click back to 'All')*  
> Even when we switch between the filter tabs—Required, Advisory, and back to All—the accepted status remains permanently preserved.  
> 
> *(Click 'Undo' button on that card)*  
> And if the engineer wants to revert, clicking **'Undo'** immediately restores the original red line and code text, and resets our KPI counter back to 4."*

---

### ⏱️ 4:45 – 5:30 | Part 6: MISRA Deviation Permit Generator
* **Action on Screen:** Click **'Request Deviation'** on one card (e.g., Line 82 or Line 60). Show the pop-up modal. Click 'Generate Signed Deviation Record'.
* **What to Say & Do:**
> *(Click 'Request Deviation' on a card)*  
> *"Under MISRA Compliance:2020, if a rule cannot be modified due to legacy or hardware constraints, engineers must file a formal deviation permit.  
> 
> Clicking **'Request Deviation'** opens our automated permit generator.  
> Notice that it automatically fills:  
> - The Finding ID and Rule citation,  
> - The target file `bms_cell_monitor.c` and exact line number,  
> - The engineering rationale, and  
> - The ASIL safety mitigations.  
> 
> *(Click 'Generate Signed Deviation Record')*  
> Clicking 'Generate Signed Deviation Record' creates an official signed permit.  
> The engineer can click **'Download Permit File'** to save it directly into the vehicle safety documentation package."*  
> *(Close modal with '✕')*

---

### ⏱️ 5:30 – 6:15 | Part 7: Add Custom Module & CI/CD Pipeline Exports
* **Action on Screen:** Click **'+ Add Custom C Module'** in the hero banner. Show the modal. Close it. Point to the bottom export bar.
* **What to Say & Do:**
> *(Click 'Add Custom C Module' in the hero banner)*  
> *"What if the evaluation team wants to test custom code?  
> We built the **'Add Custom C Module'** feature!  
> Engineers can upload any local `.c` file, paste code directly, or select pre-configured presets like an ABS Braking driver or EV Motor Inverter, and analyze it immediately.  
> *(Close modal)*  
> 
> *(Point to the bottom export tray)*  
> Finally, at the bottom, we provide one-click CI/CD pipeline exports:  
> - **OASIS SARIF v2.1.0** for SonarQube, Jenkins, and GitHub Advanced Security,  
> - **CSV Compliance Matrix** for spreadsheet audits, and  
> - **Audit Report in Markdown**.  
> 
> *(Click 'Compliance Matrix (.csv)')*  
> With one click, the full compliance matrix downloads locally."*

---

### ⏱️ 6:15 – 6:40 | Part 8: Conclusion
* **Action on Screen:** Bring mouse back to the center of the dashboard.
* **What to Say:**
> *"In conclusion, AutoSafe-Review gives automotive engineers an end-to-end cockpit:  
> Real-time defect detection, line-by-line visual highlighting, interactive remediation, automated MISRA deviation records, and enterprise CI/CD integration.  
> 
> This completely fulfills every objective of Case Study 4.  
> 
> Thank you very much for your time and evaluation!"*

---

## 🎯 Quick Reference Cheat Sheet While Recording
| What Evaluator Sees | Exact Screen Value |
|---|---|
| **Active Module** | `bms_cell_monitor.c` |
| **KPI Total Open** | **4** (drops to **3** on Accept Remediation) |
| **KPI Mandatory / Critical** | **0** |
| **KPI Required / High** | **3** (drops to **2** on Accept Remediation) |
| **KPI Advisory / Low** | **1** |
| **KPI Faithfulness** | **100.0%** |
| **Flagged Red Lines** | **Line 30**, **Line 42**, **Line 60**, **Line 82** |
| **Top Visible Card** | **MISRA C:2012 Rule 16.4 (Required) — Line 60** |
| **Action to Demo** | Click **'Accept Remediation'** on Line 60 -> turns **GREEN** & code text updates live! |

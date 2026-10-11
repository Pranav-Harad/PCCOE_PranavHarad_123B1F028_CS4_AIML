# SIMPLE & CLEAR VIDEO DEMONSTRATION SCRIPT
## AutoSafe-Review: Automotive ECU Code Review Dashboard
**Tata Technologies TechPulse FY-26 | Case Study 4**  
**Candidate:** Pranav Ravindra Harad | **PRN:** 123B1F028 | **College:** PCCOE Pune  
**Screen Setup:** Full screen on `http://localhost:5000/`  
**Duration:** Around 5 to 6 minutes  

---

## 🎬 Step-by-Step Speaking Script (Simple English)

---

### ⏱️ 0:00 – 0:45 | Part 1: Introduction & Header
* **Action on Screen:** Keep browser open at `http://localhost:5000/`. Move mouse near the top header.
* **What to Say:**
> *"Hello everyone and respected evaluators.  
> My name is Pranav Ravindra Harad, PRN 123B1F028, from PCCOE Pune.  
> 
> Today, I am presenting my project for Tata Technologies TechPulse FY-26, Case Study 4: Secure Code Debugging and Review Assistant.  
> 
> Here on screen is our live web dashboard, called **AutoSafe-Review**.  
> At the top header, you can see the official Tata Technologies portal title and my candidate credentials.  
> The entire dashboard is running locally on port 5000, designed specifically for automotive ECU code analysis."*

---

### ⏱️ 0:45 – 1:30 | Part 2: ECU Modules & Code Viewer
* **Action on Screen:** Point mouse to the left sidebar, click the different tabs above the code editor, and show the draggable slider.
* **What to Say & Do:**
> *(Point mouse to the left sidebar)*  
> *"On the left sidebar, we have pre-loaded automotive ECU modules:  
> 1. A Battery Management module — `bms_cell_monitor.c`,  
> 2. A Throttle Actuator driver, and  
> 3. A CAN transceiver module.  
> 
> *(Point to the central code editor)*  
> In the center, we have our full C source code with line numbers.  
> Above the code, we can easily switch between:  
> - The **C Source Code**,  
> - The **ARM GCC Compiler Log**, and  
> - The **SARIF Diagnostic Stream**.  
> 
> *(Click and drag the middle slider slightly, or click 'Code Focus' then '50:50')*  
> We also added a smooth draggable slider and presets like 50:50 and Code Focus, so developers can resize panels comfortably on any screen."*

---

### ⏱️ 1:30 – 2:30 | Part 3: Running Static Analysis & KPI Cards
* **Action on Screen:** Click the blue **'Run Static Analysis & Review'** button. Then point mouse to the top 5 KPI cards.
* **What to Say & Do:**
> *(Click 'Run Static Analysis & Review')*  
> *"Now, let's run the static analysis. I click this blue button: **'Run Static Analysis & Review'**.  
> 
> In just one second, our diagnostic engine inspects the entire file.  
> 
> *(Move mouse across the 5 KPI cards)*  
> At the top, our KPI cards show immediate results:  
> - **Total Open Violations:** 4 issues found in this file.  
> - **Mandatory / Critical:** 1 safety violation.  
> - **Required / High:** 2 violations.  
> - **Advisory / Low:** 1 coding guideline issue.  
> - And **RAG Grounding & Faithfulness:** 100%, meaning all rules are strictly verified with zero hallucination."*

---

### ⏱️ 2:30 – 3:30 | Part 4: Code Defect Highlighting & Finding Cards
* **Action on Screen:** Point to the red highlighted lines in the code (Line 24). Click the finding card on the right to show auto-scrolling.
* **What to Say & Do:**
> *(Point to the red line in the code editor)*  
> *"Notice the code editor on the left: non-compliant code lines are automatically highlighted in red, like Line 24.  
> 
> *(Point to the finding cards on the right)*  
> On the right side, each defect is neatly explained:  
> - It mentions the rule: **MISRA C:2012 Rule 12.1** for operator precedence.  
> - It shows the exact non-compliant line.  
> - It explains the root cause and the **ISO 26262 safety hazard**: missing parentheses can corrupt ADC voltage readings in a battery!  
> - And it gives a clear **Unified Diff fix**, showing exactly what to remove in red and what to add in green.  
> 
> *(Click anywhere on the finding card)*  
> When I click any finding card, it automatically scrolls and highlights the exact line in our code editor."*

---

### ⏱️ 3:30 – 4:30 | Part 5: Accept Remediation & Interactive Triage
* **Action on Screen:** Click **'Accept Remediation'** on the card. Show Line 24 turn green. Click 'Required' tab, then back to 'All'. Show 'Undo'.
* **What to Say & Do:**
> *(Click 'Accept Remediation' on the first card)*  
> *"Now, let's test the interactive review process.  
> When the reviewer clicks **'Accept Remediation'**:  
> 1. Look at Line 24 in our code editor: it instantly turns **GREEN**! This visually confirms the fix is approved and staged.  
> 2. The card shows a green badge: **'Remediation Approved & Staged'**.  
> 3. And our KPI counter at the top automatically drops from 4 to 3!  
> 
> *(Click 'Required' filter tab, then click back to 'All')*  
> If we filter by 'Required' or 'Mandatory' and come back to 'All', the accepted state remains intact and never gets lost.  
> 
> *(Click 'Undo' button on that card)*  
> And if the engineer wants to revert, clicking **'Undo'** immediately brings back the red line and resets the KPI counter to 4."*

---

### ⏱️ 4:30 – 5:15 | Part 6: MISRA Deviation Permit Generator
* **Action on Screen:** Click **'Request Deviation'** on one card. Show the pop-up modal. Click 'Generate Signed Deviation Record'.
* **What to Say & Do:**
> *(Click 'Request Deviation' on any open finding card)*  
> *"In automotive engineering, if a rule cannot be fixed due to hardware constraints, we must create a formal deviation permit under MISRA Compliance:2020.  
> 
> Clicking **'Request Deviation'** opens our automated permit generator.  
> It automatically fills in:  
> - The Finding ID and Rule number,  
> - The filename and line number,  
> - The engineering justification, and  
> - Safety mitigations.  
> 
> *(Click 'Generate Signed Deviation Record')*  
> Clicking this button generates a signed, formal deviation record.  
> We can download this permit file with one click to keep in our safety audit files."*  
> *(Close the modal by clicking '✕')*

---

### ⏱️ 5:15 – 5:50 | Part 7: Adding Custom Modules & CI/CD Export
* **Action on Screen:** Click **'+ Add Custom C Module'** (or in the hero banner). Show the presets. Then point to the bottom export bar.
* **What to Say & Do:**
> *(Click 'Add Custom C Module' in the hero banner)*  
> *"What if the user wants to test their own code?  
> We provided an **'Add Custom C Module'** feature!  
> Engineers can upload any local `.c` file or paste code directly, or choose from ready presets like an ABS Braking driver or EV motor inverter, and analyze it immediately.  
> *(Close custom module modal)*  
> 
> *(Point to the bottom export tray)*  
> Finally, at the bottom, we have one-click exports for CI/CD pipelines:  
> - **OASIS SARIF v2.1.0** for SonarQube and GitHub,  
> - **CSV Compliance Matrix** for Excel sheets, and  
> - **Markdown Audit Report**.  
> 
> *(Click 'Compliance Matrix (.csv)')*  
> With one click, the report is saved directly to your computer."*

---

### ⏱️ 5:50 – 6:15 | Part 8: Conclusion
* **Action on Screen:** Bring mouse back to the center of the dashboard.
* **What to Say:**
> *"To conclude, our AutoSafe-Review dashboard provides an end-to-end, reliable solution for automotive software safety.  
> It highlights code defects instantly, allows real-time interactive fixes, automates MISRA compliance documentation, and integrates directly with CI/CD tools.  
> 
> Thank you very much for your time!"*

---

## 💡 Quick Tips for Speaking Comfortably:
1. Speak in your normal, calm speaking pace — you don't need to rush!
2. Do each action with your mouse first, then speak about it.
3. Keep the video between 5 and 6 minutes.

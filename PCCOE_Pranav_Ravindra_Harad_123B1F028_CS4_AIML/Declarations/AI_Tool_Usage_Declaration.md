# AI TOOL USAGE DECLARATION
**Tata Technologies TechPulse FY-26 | AI/ML Capstone Project**

---

### Student Information
* **Student Name:** Pranav Ravindra Harad
* **PRN:** 123B1F028
* **Institute:** Pimpri Chinchwad College of Engineering, Pune (PCCOE)
* **Case Study:** CS4 - Secure Code Debugging and Review Assistant

---

### Declared AI Tools & Pre-Trained Models

| AI Tool / Model | Version / Provider | Purpose of Usage | Project Artifact Affected | Verified By Student (Y/N) |
| :--- | :--- | :--- | :--- | :--- |
| **Antigravity IDE Assistant** | Google DeepMind Agentic Coding System | Scaffolding project structure, test scripts, ReportLab PDF generators, and documentation drafting | `Code/backend/`, `Code/utils/`, `run_app.py`, `Documentation/` | **Y** |
| **Qwen2.5-Coder** | 7B-Instruct (Local 4-bit Q4_K_M via Ollama) | Local offline inference for ECU code defect review, root cause synthesis, and compliant diff fix formatting | `Model_Prompts_Config/`, `Code/backend/local_llm.py` | **Y** |
| **BAAI/bge-small-en-v1.5** | HuggingFace / Scikit-learn Vectorizer | Dense semantic representation and cosine similarity retrieval over MISRA/CERT rules | `Code/backend/rag_engine.py` | **Y** |

---

### Transparency Statement
All code logic, deterministic static analysis algorithms, AST chunking rules, and evaluation scripts have been thoroughly reviewed, verified, and executed locally by the student. No proprietary automotive source code was transmitted over the public internet.

**Student Name:** Pranav Ravindra Harad  
**PRN:** 123B1F028  
**Date:** October 9, 2026  
**Signature:** ___________________________  

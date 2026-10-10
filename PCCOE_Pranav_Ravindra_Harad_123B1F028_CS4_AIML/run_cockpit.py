#!/usr/bin/env python3
"""
AUTOSAFE-REVIEW: 1-CLICK EVALUATOR LAUNCHER
Tata Technologies TechPulse FY-26 | AI/ML Capstone Project | Case Study 4
Student: Pranav Ravindra Harad | PRN: 123B1F028 | PCCOE, Pune
Case Study: CS4 - Secure Code Debugging and Review Assistant
"""

import os
import sys
import time
import webbrowser
import threading

current_dir = os.path.dirname(os.path.abspath(__file__))
code_dir = os.path.join(current_dir, "Code")
sys.path.insert(0, code_dir)

try:
    from flask_app import app
except ImportError as e:
    print("[ERROR] Could not import Flask application:")
    print(f"        {e}")
    print("[HINT] Ensure dependencies are installed via: pip install -r requirements.txt")
    sys.exit(1)

def open_browser():
    time.sleep(1.5)
    url = "http://localhost:5000/"
    print(f"[*] Opening browser to {url} ...")
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"[!] Could not open browser automatically: {e}")

if __name__ == "__main__":
    print("==========================================================================")
    print("   AUTOSAFE-REVIEW: SECURE AUTOMOTIVE CODE DEBUGGING & REVIEW ASSISTANT   ")
    print("   Tata Technologies TechPulse FY-26 | Case Study 4 (CS4)                 ")
    print("   Student: Pranav Ravindra Harad | PRN: 123B1F028 | PCCOE, Pune         ")
    print("   100% AIR-GAPPED ON-PREMISES LOCAL INFERENCE (ZERO EXTERNAL APIS)       ")
    print("==========================================================================")
    print(" * Serving on: http://localhost:5000/")
    print(" * Standards:  MISRA C:2012 | SEI CERT C | ISO 26262 Part 6 ASIL B/D      ")
    print(" * Press CTRL+C to stop the server at any time.")
    print("==========================================================================")

    # Launch browser thread
    threading.Thread(target=open_browser, daemon=True).start()

    # Run application
    app.run(host="0.0.0.0", port=5000, debug=False)

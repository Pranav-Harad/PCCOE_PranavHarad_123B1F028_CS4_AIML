#!/usr/bin/env python3
"""
Launcher for AutoSafe-Review Enterprise Flask Application
Tata Technologies TechPulse FY-26 | Case Study 4
Student: Pranav Ravindra Harad | PRN: 123B1F028 | PCCOE, Pune
"""

import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))
flask_script = os.path.join(base_dir, "PCCOE_Pranav_Ravindra_Harad_123B1F028_CS4_AIML", "Code", "flask_app.py")

if not os.path.exists(flask_script):
    print(f"[!] Cannot find flask_app.py at {flask_script}")
    sys.exit(1)

# Import and run directly
sys.path.insert(0, os.path.dirname(flask_script))
from flask_app import app

if __name__ == "__main__":
    port = 5000
    print("=================================================================")
    print("  LAUNCHING AUTOSAFE-REVIEW FLASK ENTERPRISE COCKPIT...         ")
    print("  Candidate: Pranav Ravindra Harad | PRN: 123B1F028 | PCCOE     ")
    print(f"  Access Cockpit at: http://localhost:{port}                     ")
    print("=================================================================")
    app.run(host="0.0.0.0", port=port, debug=False)

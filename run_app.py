#!/usr/bin/env python3
"""
Launcher for AutoSafe-Review Streamlit Application
Tata Technologies TechPulse FY-26 | Case Study 4
Student: Pranav Ravindra Harad | PRN: 123B1F028 | PCCOE, Pune
"""

import os
import subprocess
import sys

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(base_dir, "PCCOE_Pranav_Ravindra_Harad_123B1F028_CS4_AIML", "Code", "app.py")
    
    if not os.path.exists(app_path):
        print(f"[!] Cannot find app.py at {app_path}")
        sys.exit(1)
        
    print("=================================================================")
    print("  LAUNCHING AUTOSAFE-REVIEW AUTOMOTIVE COCKPIT...                ")
    print("  Student: Pranav Ravindra Harad | PRN: 123B1F028               ")
    print("  Host: Localhost (Air-Gapped Isolated Execution)                ")
    print("=================================================================")
    
    cmd = [sys.executable, "-m", "streamlit", "run", app_path, "--server.port=8501", "--server.headless=true"]
    subprocess.run(cmd)

if __name__ == "__main__":
    main()

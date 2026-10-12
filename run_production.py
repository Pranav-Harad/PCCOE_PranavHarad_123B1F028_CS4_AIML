#!/usr/bin/env python3
"""
AUTOSAFE-REVIEW: ENTERPRISE PRODUCTION WORKSTATION SERVER
Tata Technologies TechPulse FY-26 | Case Study 4
Candidate: Pranav Ravindra Harad | PRN: 123B1F028 | PCCOE, Pune

Deployment Architecture:
- Server: Waitress Production WSGI Server (Multi-Threaded)
- Mode: 100% Air-Gapped On-Premises Workstation
- Port: 5000
- Standards: ISO 26262 Functional Safety / ISO/SAE 21434 Cybersecurity
"""

import os
import sys
import webbrowser

base_dir = os.path.dirname(os.path.abspath(__file__))
pkg_code_dir = os.path.join(base_dir, "PCCOE_Pranav_Ravindra_Harad_123B1F028_CS4_AIML", "Code")

if os.path.exists(pkg_code_dir):
    sys.path.insert(0, pkg_code_dir)
else:
    sys.path.insert(0, os.path.join(base_dir, "Code"))

try:
    from flask_app import app
except ImportError as e:
    print(f"[ERROR] Could not import Flask application: {e}")
    sys.exit(1)

try:
    from waitress import serve
except ImportError:
    print("[WARN] Waitress not installed, falling back to Flask development server.")
    serve = None

if __name__ == "__main__":
    host = "0.0.0.0"
    port = int(os.environ.get("PORT", 5000))
    threads = int(os.environ.get("WSGI_THREADS", 6))

    print("=" * 80)
    print("  AUTOSAFE-REVIEW: ENTERPRISE PRODUCTION WORKSTATION (WAITRESS WSGI)")
    print("  Tata Technologies TechPulse FY-26 | Automotive Review Workstation")
    print("  Candidate: Pranav Ravindra Harad | PRN: 123B1F028 | PCCOE, Pune")
    print("  Deployment Mode: Air-Gapped On-Premises (ISO 26262 Compliant)")
    print(f"  Listening on: http://{host}:{port} (Threads: {threads})")
    print(f"  Local Web Cockpit: http://localhost:{port}/")
    print("=" * 80)

    # Automatically open local browser if running interactively
    if os.environ.get("AUTO_OPEN_BROWSER", "1") == "1":
        try:
            webbrowser.open(f"http://localhost:{port}/")
        except Exception:
            pass

    if serve:
        serve(app, host=host, port=port, threads=threads)
    else:
        app.run(host=host, port=port, debug=False)

@echo off
TITLE AutoSafe-Review Enterprise Production Cockpit (Waitress WSGI)
COLOR 0B
echo ===============================================================================
echo   TATA TECHNOLOGIES TECHPULSE FY-26 ^| CASE STUDY CS4
echo   AutoSafe-Review: Air-Gapped Automotive Review Workstation
echo   Candidate: Pranav Ravindra Harad ^| PRN: 123B1F028 ^| PCCOE, Pune
echo ===============================================================================
echo.
echo [*] Starting Production WSGI Workstation Service on port 5000...
echo [*] Mode: 100%% Air-Gapped On-Premises (Zero Cloud Telemetry)
echo.

python run_production.py
pause

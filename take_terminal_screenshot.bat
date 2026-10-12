@echo off
TITLE AutoSafe-Review: Automotive Evaluation Benchmark Logs
COLOR 0A
MODE CON: COLS=95 LINES=45
echo.
python run_benchmark_for_screenshot.py
echo.
echo ===============================================================================
echo [TIP] Press 'Alt + PrtScn' or 'Windows + Shift + S' to take a screenshot now!
echo ===============================================================================
echo.
pause

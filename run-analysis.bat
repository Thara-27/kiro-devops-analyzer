@echo off

echo =====================================
echo AI DEVOPS FAILURE ANALYZER STARTED
echo =====================================

echo.
python scripts\analyze.py

echo.
python scripts\report.py

echo.
echo =====================================
echo ANALYSIS COMPLETED SUCCESSFULLY
echo =====================================

pause
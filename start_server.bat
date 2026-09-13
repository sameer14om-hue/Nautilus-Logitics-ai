@echo off
title Nautilus Logistics AI - Local Web Server
echo Starting Nautilus Logistics AI...
python server.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [Notice] Trying with 'py' launcher...
    py server.py
)
pause

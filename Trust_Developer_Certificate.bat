@echo off
setlocal
cd /d "%~dp0"
title Nautilus Logistics AI - Trusted Developer Certificate Setup
echo ============================================================
echo   Nautilus Logistics AI - Trusted Developer Certificate Setup
echo ============================================================
echo.
echo Installing Nautilus Maritime AI Technologies developer certificate to Windows Trusted Store...
certutil -addstore -user "TrustedPublisher" "Nautilus_Developer_Certificate.cer"
certutil -addstore -user "Root" "Nautilus_Developer_Certificate.cer"
echo.
echo [SUCCESS] Developer certificate is now trusted by Windows!
echo SmartScreen and Windows Defender will recognize Nautilus Logistics AI as a verified publisher.
echo.
pause

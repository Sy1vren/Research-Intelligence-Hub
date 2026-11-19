@echo off
chcp 65001 >nul
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo 请先运行 install_windows.bat
  pause
  exit /b 1
)
set CONFIG=%~1
if "%CONFIG%"=="" set CONFIG=config\example.json
".venv\Scripts\python.exe" scripts\pdf_handwrite.py --config "%CONFIG%"
if errorlevel 1 echo 运行失败，请检查配置文件和错误信息。
pause

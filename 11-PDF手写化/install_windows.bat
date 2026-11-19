@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo [1/4] 检查 Python 3.12...
py -3.12 --version
if errorlevel 1 (
  echo 未检测到 Python 3.12。请先安装 Python 3.12 x64，并勾选 Add Python to PATH。
  pause
  exit /b 1
)
echo [2/4] 创建虚拟环境...
if not exist ".venv" py -3.12 -m venv .venv
if errorlevel 1 goto failed
echo [3/4] 安装依赖...
".venv\Scripts\python.exe" -m pip install --upgrade pip
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 goto failed
echo [4/4] 创建本地私有目录...
if not exist "private_data\fonts" mkdir "private_data\fonts"
if not exist "private_data\glyphs" mkdir "private_data\glyphs"
if not exist "input" mkdir "input"
if not exist "output" mkdir "output"
echo.
echo 部署完成。请阅读 README.md，将测试 PDF 放入 input，并修改 config\example.json。
pause
exit /b 0
:failed
echo 安装失败，请检查 Python、网络和报错信息。
pause
exit /b 1

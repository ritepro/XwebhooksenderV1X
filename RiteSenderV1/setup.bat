@echo off

:: Specify the full path to your Python interpreter (e.g., replace 'python' with the path to python.exe)
set python_path=C:\path\to\your\python.exe

:: Check if Python is installed
%python_path% --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python 3 and try again.
    pause
    exit /b 1
)

:: Install required Python packages
echo Installing required Python packages...
%python_path% -m pip install requests colorama

:: Additional requirements (add more if needed)
:: %python_path% -m pip install package_name

:: Check if installation was successful
if %errorlevel% neq 0 (
    echo Installation failed. Please check your internet connection and try again.
    pause
    exit /b 1
)

:: Prompt user to press Enter
echo Installation complete. Press Enter to run the Python script.
pause

:: Run the Python script
%python_path% senderv1.py

:: Pause to keep the console window open
pause

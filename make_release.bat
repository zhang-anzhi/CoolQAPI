@echo off
set name=CoolQAPI
mkdir release
echo set a version: 
set /p ver=

mkdir release\%name%-%ver%

REM 扫地
del CoolQAPI\config.yml
rd /s /q CoolQAPI\__pycache__
rd /s /q CoolQAPI\utils\__pycache__
rd /s /q CoolQAPI\CoolQAPI_update
rd /s /q QQBridge\__pycache__
rd /s /q QQBridge\.idea
rd /s /q QQBridge\logs
del QQBridge\config.yml

REM Readme, requirements, LICENSE
copy readme.md release\%name%-%ver%\readme.md
copy requirements.txt release\%name%-%ver%\requirements.txt
copy LICENSE release\%name%-%ver%\LICENSE

REM CoolQ and CoolQAPI-MCDR
copy CoolQAPI-MCDR.py release\%name%-%ver%\CoolQAPI-MCDR.py
copy CoolQ.zip release\%name%-%ver%\CoolQ.zip

REM CoolQAPI folder
mkdir release\%name%-%ver%\CoolQAPI
xcopy /e /y /q CoolQAPI release\%name%-%ver%\CoolQAPI
xcopy /e /y /q /i QQBridge release\%name%-%ver%\QQBridge

REM zip
cd release
zip -r -q %name%-%ver%.zip %name%-%ver%
rd /s /q %name%-%ver%
cd ..

echo =========== Finish ===========
pause

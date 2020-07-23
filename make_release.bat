@echo off
set name=CoolQAPI
mkdir release
echo set a version: 
set /p ver=

mkdir release\%name%-%ver%

REM 扫地大妈
del CoolQAPI\config.yml
rd /s /q CoolQAPI\__pycache__
rd /s /q CoolQAPI\utils\__pycache__
rd /s /q CoolQAPI\CoolQAPI_update

REM Readme and requirements and LICENSE
copy readme.md release\%name%-%ver%\readme.md
copy requirements.txt release\%name%-%ver%\requirements.txt
copy LICENSE release\%name%-%ver%\LICENSE

REM CoolQ and CoolQAPI-MCDR
copy CoolQAPI-MCDR.py release\%name%-%ver%\CoolQAPI-MCDR.py
copy CoolQ.zip release\%name%-%ver%\CoolQ.zip

REM CoolQAPI folder
mkdir release\%name%-%ver%\CoolQAPI
xcopy /e /y /q CoolQAPI release\%name%-%ver%\CoolQAPI

REM zip
cd release
zip -r -q %name%-%ver%.zip  %name%-%ver%
rd /s /q %name%-%ver%
cd ..

echo =========== Finish ===========
pause

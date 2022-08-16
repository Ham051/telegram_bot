@echo off

call %~dp0telegram_bo\venv\Scripts\activate


cd %~dp0telegram_bo
set TOKEN=

python bot.py 


pause

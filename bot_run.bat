@echo off

call %~dp0telegram_bo\venv\Scripts\activate


cd %~dp0telegram_bo
set TOKEN=5491402580:AAEL906KeUMTaSf7XQ6PSHvLAfeMGBfKEsg

python bot.py 


pause

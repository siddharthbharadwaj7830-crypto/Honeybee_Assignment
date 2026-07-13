@echo off
title Honeybee Project Launcher

echo Starting Backend...
start "Backend" cmd /k "cd /d C:\Users\Prem\Desktop\Honeybee_Assignment\backend && call venv\Scripts\activate.bat && uvicorn main:app --reload"

timeout /t 5 >nul

echo Starting Frontend...
start "Frontend" cmd /k "cd /d C:\Users\Prem\Desktop\Honeybee_Assignment\frontend && npm run dev"

timeout /t 8 >nul

start http://127.0.0.1:8000/docs
start http://localhost:5173

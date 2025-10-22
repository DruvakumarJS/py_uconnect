@echo off
set WORKSPACE=%CD%
set PYTHONPATH=%WORKSPACE%

call %WORKSPACE%\venv\Scripts\activate.bat

if not exist %WORKSPACE%\reports mkdir %WORKSPACE%\reports

python -m pytest -v managementcommitee_propose.py --junitxml=%WORKSPACE%\reports\results.xml --html=%WORKSPACE%\reports\report.html --self-contained-html tests

deactivate


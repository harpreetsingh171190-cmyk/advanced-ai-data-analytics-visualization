#!/usr/bin/env bash
set -euo pipefail
# Run from folder containing the notebook and run_export_26_charts.py
python -m pip install -q numpy pandas matplotlib scipy networkx nbformat ipython
python run_export_26_charts.py
printf '\nCreated Harpreet_Singh_26_Charts_Exports.zip\n'

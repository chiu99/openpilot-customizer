#!/bin/bash
set -e
cat /data/params/d/LastUpdateTime
echo
python3 /data/openpilot/openpilot-customizer/tune.py
cat /data/params/d/LastUpdateTime
echo
echo tuned.

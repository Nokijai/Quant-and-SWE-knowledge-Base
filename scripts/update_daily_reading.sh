#!/bin/bash

# Script to automatically update the Quant-and-SWE-knowledge-Base repository
# Creates a new daily reading task and commits changes

REPO_PATH="/tmp/Quant-and-SWE-knowledge-Base"
DATE=$(date +%Y-%m-%d)
YEAR=$(date +%Y)

cd $REPO_PATH

# Create daily reading task for today if it doesn't exist
if [ ! -f "DailyReading/$YEAR/daily_$DATE.md" ]; then
    python scripts/generate_daily_reading.py $DATE
    git add "DailyReading/$YEAR/daily_$DATE.md"
    git commit -m "Add daily reading task for $DATE" && git push origin main
    echo "Added daily reading task for $DATE and pushed to GitHub"
else
    echo "Daily reading task for $DATE already exists"
fi
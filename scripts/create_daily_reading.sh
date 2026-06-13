#!/bin/bash

# Script to create a new daily reading task file
# Usage: ./create_daily_reading.sh [date]

DATE=${1:-$(date +%Y-%m-%d)}
YEAR=$(date -d "$DATE" +%Y)

# Create the daily reading file from template
TEMPLATE_FILE="/tmp/Quant-and-SWE-knowledge-Base/DailyReading/daily_template.md"
TARGET_FILE="/tmp/Quant-and-SWE-knowledge-Base/DailyReading/$YEAR/daily_$DATE.md"

if [ ! -f "$TARGET_FILE" ]; then
    cp "$TEMPLATE_FILE" "$TARGET_FILE"
    sed -i "s/{{DATE}}/$DATE/g" "$TARGET_FILE"
    echo "Created daily reading task for $DATE: $TARGET_FILE"
else
    echo "Daily reading task for $DATE already exists: $TARGET_FILE"
fi
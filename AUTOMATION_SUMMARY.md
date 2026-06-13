# Quant-and-SWE-Knowledge-Base - Automation Setup

## Overview

I've enhanced your Quant-and-SWE-Knowledge-Base repository with automated daily reading task generation to help maintain consistent learning in both quantitative finance and software engineering.

## Changes Made

### 1. New Directory Structure
- Created `/DailyReading` directory with yearly subdirectories
- Added `daily_template.md` for generating new tasks
- Created `DailyReading/README.md` with usage instructions

### 2. Automation Scripts
- `scripts/generate_daily_reading.py` - Python script to generate intelligent daily reading tasks with suggested topics
- `scripts/create_daily_reading.sh` - Bash script to create daily tasks from template
- `~/.hermes/scripts/daily_reading_update.sh` - Automated script that runs daily via cron
- `~/.hermes/scripts/manual_daily_task.sh` - Manual script to create tasks for any date

### 3. Automated Cron Job
- Set up daily cron job to run at 9 AM
- Automatically creates new daily reading task each day
- Commits and pushes changes to your GitHub repository

### 4. Enhanced README
- Updated main README with information about daily reading tasks
- Added links to daily tasks and usage instructions

## How It Works

### Automatic Daily Updates
- Every day at 9 AM, the cron job runs `daily_reading_update.sh`
- The script checks if a daily task exists for the current date
- If not, it generates a new task with suggested topics in quant finance and software engineering
- Commits and pushes the new task to your GitHub repository

### Manual Updates
- To create a task for today: `~/.hermes/scripts/manual_daily_task.sh`
- To create a task for a specific date: `~/.hermes/scripts/manual_daily_task.sh 2026-06-15`

### Daily Task Content
Each daily task includes:
- Morning reading (30-45 mins) with suggested topics
- Afternoon deep dive (60-90 mins) with hands-on activities
- Evening reflection (15-30 mins) for synthesis and planning

## Benefits

1. **Consistency**: Ensures daily engagement with both domains
2. **Structure**: Provides a framework for systematic learning
3. **Variety**: Randomly selects from trending topics in both fields
4. **Tracking**: Maintains a permanent record of your learning journey
5. **Automation**: Reduces friction to starting daily learning

## Files Created

- `/DailyReading/README.md` - Documentation for daily tasks
- `/DailyReading/daily_template.md` - Template for new tasks
- `/DailyReading/YYYY/daily_YYYY-MM-DD.md` - Individual daily tasks
- `/scripts/generate_daily_reading.py` - Python automation script
- `/scripts/create_daily_reading.sh` - Bash automation script
- `~/.hermes/scripts/daily_reading_update.sh` - Daily cron script
- `~/.hermes/scripts/manual_daily_task.sh` - Manual task creation script
- `~/.hermes/scripts/README.md` - Documentation for automation scripts

## Cron Job Details

- **Job ID**: 5516ebbc782e
- **Schedule**: 0 9 * * * (daily at 9 AM)
- **Script**: daily_reading_update.sh
- **Status**: Enabled

Your knowledge base is now fully automated for daily reading tasks, helping you maintain consistent progress in both quantitative finance and software engineering!
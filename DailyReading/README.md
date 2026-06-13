# Daily Reading Tasks

This directory contains daily reading and learning tasks focused on Quantitative Finance and Software Engineering.

## Structure

- `/YYYY/` - Yearly folders containing daily tasks
- `daily_template.md` - Template used for generating new daily tasks

## Daily Task Format

Each daily task includes:

1. **Morning Reading** - Light reading and overview of new concepts
2. **Afternoon Deep Dive** - Hands-on implementation and experimentation
3. **Evening Reflection** - Synthesis and planning for tomorrow

## Automation

A script automatically creates a new daily task file each day. The script can be run manually or scheduled via cron.

To create a task for today:
```bash
./scripts/create_daily_reading.sh
```

To create a task for a specific date:
```bash
./scripts/create_daily_reading.sh 2026-06-15
```
#!/usr/bin/env python3
"""
Script to generate daily reading tasks with suggested content
based on trending topics in quant finance and software engineering.
"""

import os
import sys
from datetime import datetime, timedelta
import argparse


def generate_daily_reading_task(date_str):
    """Generate a daily reading task with suggested content."""
    
    # Sample trending topics - in a real implementation, 
    # these could be pulled from APIs or RSS feeds
    quant_topics = [
        "Machine Learning in Finance",
        "High Frequency Trading Strategies", 
        "Volatility Modeling (GARCH, Stochastic Volatility)",
        "Risk Parity Portfolios",
        "Cryptocurrency Market Analysis",
        "Factor Investing",
        "Statistical Arbitrage",
        "Options Pricing Models",
        "Portfolio Optimization Techniques",
        "Market Microstructure"
    ]
    
    swe_topics = [
        "System Design Patterns",
        "Microservices Architecture",
        "Cloud Infrastructure (AWS/GCP/Azure)",
        "DevOps and CI/CD Pipelines",
        "Database Design and Optimization",
        "API Design Best Practices",
        "Security Best Practices",
        "Performance Optimization",
        "Distributed Systems",
        "Modern Python/Rust/Go Practices"
    ]
    
    # Select random topics for the day
    import random
    selected_quant_topic = random.choice(quant_topics)
    selected_swe_topic = random.choice(swe_topics)
    
    # Create the daily task content
    content = f"""# Daily Reading Task - {date_str}

**Date:** {date_str}

## Morning Reading (30-45 mins)

### Quant Finance
- [ ] Topic of the day: **{selected_quant_topic}**
- [ ] Read 1 research paper from SSRN/ArXiv related to quantitative finance
- [ ] Review recent market movements and their implications
- [ ] Study a new quantitative concept related to today's topic

### Software Engineering
- [ ] Topic of the day: **{selected_swe_topic}**
- [ ] Read 1 article about system design or architecture
- [ ] Study a new algorithm or data structure
- [ ] Review best practices in software development

## Afternoon Deep Dive (60-90 mins)

### Quantitative Focus
- [ ] Implement a small algorithm related to today's reading
- [ ] Backtest a simple strategy based on new concepts
- [ ] Analyze a new dataset or financial instrument
- [ ] Explore {selected_quant_topic.lower()} in practice

### Software Engineering Focus
- [ ] Practice coding problems or implement algorithms
- [ ] Learn a new library or framework relevant to quant development
- [ ] Review and refactor existing code
- [ ] Apply {selected_swe_topic.lower()} principles

## Evening Reflection (15-30 mins)

### Key Insights
- Quant finance takeaway: 
- Software engineering takeaway: 
- Connection between domains: 

### Tomorrow's Focus
- Topics to explore tomorrow: 
- Resources to read: 

---

## Resources Used Today
- Paper/Article 1: 
- Paper/Article 2: 
- Dataset/Tool explored: 

## Notes
[Any additional notes or observations]
"""
    return content


def main():
    parser = argparse.ArgumentParser(description='Generate daily reading task')
    parser.add_argument('date', nargs='?', default=datetime.now().strftime('%Y-%m-%d'),
                        help='Date for the daily task (YYYY-MM-DD)')
    parser.add_argument('--repo-path', default='/tmp/Quant-and-SWE-knowledge-Base',
                        help='Path to the knowledge base repository')
    
    args = parser.parse_args()
    
    # Validate date format
    try:
        date_obj = datetime.strptime(args.date, '%Y-%m-%d')
    except ValueError:
        print(f"Error: Invalid date format. Use YYYY-MM-DD")
        sys.exit(1)
    
    year = date_obj.strftime('%Y')
    
    # Create directory if it doesn't exist
    daily_dir = os.path.join(args.repo_path, 'DailyReading', year)
    os.makedirs(daily_dir, exist_ok=True)
    
    # Generate file path
    file_path = os.path.join(daily_dir, f"daily_{args.date}.md")
    
    # Check if file already exists
    if os.path.exists(file_path):
        print(f"Daily reading task for {args.date} already exists: {file_path}")
        return
    
    # Generate and write content
    content = generate_daily_reading_task(args.date)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created daily reading task for {args.date}: {file_path}")


if __name__ == "__main__":
    main()
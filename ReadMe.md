# Quant-and-SWE-Knowledge-Base

A learning and research log at the intersection of **Quantitative Finance** and **Software Engineering** (CS junior track).

## Learning Path and Goals

- [ ] **Quant Finance:** Statistical arbitrage through portfolio optimization.
- [ ] **SWE:** System design, efficient programming, and automated testing.

## Directory Structure

- `/Quant` — Strategy backtests, data analysis notebooks, and quantitative theory notes.
- `/SWE` — System design notes, algorithms practice, and software engineering patterns.
- `/Resources` — Papers, books, and curated references.

## Current Research

### Project 1: QQQ vs VOO Pairs Analysis

- **Goal:** Test cointegration and mean-reversion assumptions for a ratio-based relative-value strategy.
- **Status:** Completed (research summary written).

| Deliverable | Link |
|-------------|------|
| Notebook | [01_qqq_voo_pairs_analysis.ipynb](./Quant/Projects/01_qqq_voo_pairs_analysis.ipynb) |
| Summary | [01_qqq_voo_pairs_analysis.md](./Quant/Projects/01_qqq_voo_pairs_analysis.md) |

**Key findings (2020-01 to 2026-05 sample):**

- ADF on log-diff of QQQ/VOO ratio: stationary (p ≈ 0).
- Engle-Granger cointegration on Adj Close: **not cointegrated** (p ≈ 0.21).

### Project 2: Sector ETF Cointegration Scanner

- **Goal:** Automatically scan major U.S. sector ETFs to find statistically cointegrated pairs, then perform spread and z-score diagnostics.
- **Status:** Completed (scanner + notes + summary).

| Deliverable | Link |
|-------------|------|
| Notebook | [02_pairs_trading_scanner.ipynb](./Quant/Projects/02_pairs_trading_scanner.ipynb) |
| Summary | [02_pairs_trading_scanner.md](./Quant/Projects/02_pairs_trading_scanner.md) |

**Key findings (2020-01 to 2026-05 sample):**

- Best detected pair from scan: `XLI` / `XLK`.
- Cointegration p-value: `0.013154` (passes 5% threshold).
- Built workflow for hedge ratio estimation, spread construction, and 30-day z-score monitoring.

## Tech Stack

- **Language:** Python (NumPy, Pandas, Statsmodels)
- **Tools:** Git, Jupyter Notebook, Matplotlib
- **Topics:** Time series analysis, stationarity (ADF), cointegration, ACF/PACF

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook Quant/Projects/01_qqq_voo_pairs_analysis.ipynb
# or open the sector scanner notebook
jupyter notebook Quant/Projects/02_pairs_trading_scanner.ipynb
```

## Featured Notes

- [Time series fundamentals](./Quant/Theory/01_time_series_fundamentals.md)
- [Cointegration theory](./Quant/Theory/02_cointegration_theory.md)
- [QQQ vs VOO pairs analysis summary](./Quant/Projects/01_qqq_voo_pairs_analysis.md)
- [Sector ETF pairs scanner summary](./Quant/Projects/02_pairs_trading_scanner.md)

---

*Stay curious. Keep building.*

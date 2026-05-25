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

- **Project:** QQQ vs VOO pairs trading analysis.
- **Goal:** Test cointegration and mean-reversion assumptions for a ratio-based relative-value strategy.
- **Status:** In progress (analysis phase).

| Deliverable | Link |
|-------------|------|
| Notebook | [01_qqq_voo_pairs_analysis.ipynb](./Quant/Projects/01_qqq_voo_pairs_analysis.ipynb) |
| Summary | [01_qqq_voo_pairs_analysis.md](./Quant/Projects/01_qqq_voo_pairs_analysis.md) |

**Latest findings (sample: 2020-01 to 2026-05):**

- ADF on log-diff of QQQ/VOO ratio: stationary (p ≈ 0).
- Engle–Granger cointegration on Adj Close: **not cointegrated** (p ≈ 0.21).

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
```

## Featured Notes

- [Time series fundamentals](./Quant/Theory/01_time_series_fundamentals.md)
- [QQQ vs VOO pairs analysis summary](./Quant/Projects/01_qqq_voo_pairs_analysis.md)

---

*Stay curious. Keep building.*

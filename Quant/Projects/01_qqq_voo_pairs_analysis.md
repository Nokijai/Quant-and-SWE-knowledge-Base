# Quant Research: QQQ vs VOO Pairs Trading Feasibility

## 1. Research Objective

Test whether Nasdaq-100 (QQQ) and S&P 500 (VOO) share a long-run cointegration relationship, and assess the feasibility of a mean-reversion pairs strategy.

## 2. Data Pipeline

- **Source:** Yahoo Finance (2020-01-01 to 2026-05-01)
- **Processing:** Log-difference of the QQQ/VOO ratio for stationarity testing.

## 3. Results

- **Stationarity (ADF test):** p-value = [0.000]
- **Cointegration (Engle–Granger):** p-value = [0.2117]

## 4. Key Insights

| Test | Result | Interpretation |
|------|--------|----------------|
| **Correlation** | QQQ and VOO Adj Close highly positively correlated (typically > 0.95) | Long-run co-movement; suitable for initial visualization |
| **ADF — ratio** | p ≈ 0.10, **non-stationary** | Mean-reversion ARMA on ratio levels is not valid |
| **ADF — log-diff** | p ≈ 0, **stationary** | Differenced ratio usable for short-horizon modeling |
| **Cointegration `coint()`** | p ≈ 0.21, **not cointegrated** | No stable long-run equilibrium; weak classical pairs case |

## 5. Next Steps

- Analyze sector ETFs (e.g. XLK vs XLF).
- Explore factor momentum models.

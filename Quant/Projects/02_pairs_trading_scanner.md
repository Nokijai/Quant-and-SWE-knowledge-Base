# Quant Research: Sector ETF Pairs Trading Scanner

## 1. Research Objective

Scan a basket of U.S. sector ETFs to identify statistically cointegrated pairs and build a basic spread-monitoring workflow (hedge ratio + z-score) for mean-reversion trading.

## 2. Data Pipeline

- **Universe:** `XLK`, `XLF`, `XLE`, `XLV`, `XLY`, `XLP`, `XLI`, `XLU`, `XLB`
- **Source:** Yahoo Finance (`Adj Close`, 2020-01-01 to 2026-05-01)
- **Method:**
  - Run Engle-Granger cointegration test (`coint`) on all pair combinations.
  - Keep pairs with `p-value < 0.05`.
  - For the best pair (lowest p-value), estimate hedge ratio via OLS:
    - `asset_2 = alpha - beta * asset_1`
  - Compute spread and 30-day rolling z-score.

## 3. Results

- **Detected cointegrated pair:** `XLI` vs `XLK`
- **Cointegration p-value:** `0.013154`
- **Estimated hedge ratio (beta):** approximately `1.00` (from OLS in notebook output title)
- **Spread visualization:** completed (`Spread between XLK and XLI`)
- **Z-score setup:** 30-day rolling mean/std with threshold lines at `+2`, `-2`, and `0`

## 4. Key Insights

| Item | Result | Interpretation |
|------|--------|----------------|
| **Pair scan** | 1 pair passed `p < 0.05` (`XLI`, `XLK`) | Statistical long-run relationship exists inside the tested sector ETF set |
| **Hedge ratio** | beta ~ 1.00 | Relative moves are close to one-for-one after scaling |
| **Spread** | Constructed as `XLK - beta * XLI` | Provides the core mean-reversion signal variable |
| **Z-score** | 30-day standardized spread with +/-2 bands | Practical trigger framework for overbought/oversold spread states |

## 5. Conclusion

The notebook successfully builds an end-to-end **pairs scanner prototype**: it downloads sector ETF data, identifies cointegrated pairs, estimates a hedge ratio, and transforms spread into a tradable z-score signal space.  

Based on this run, **`XLI`-`XLK` is the strongest candidate** for a mean-reversion setup among the selected ETFs. This is a good statistical starting point, but not yet a full strategy validation. A production-ready conclusion still requires backtesting with entry/exit rules, transaction costs, and risk controls.


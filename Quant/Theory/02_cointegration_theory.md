# 02 — Cointegration Theory

Theory note for pairs trading and long-run equilibrium between assets. Each section follows: **Concept → Math → Intuition**.

**Prerequisite:** [01 — Time Series Fundamentals](./01_time_series_fundamentals.md) (stationarity, I(0)/I(1), ADF)

**Related project:** [QQQ vs VOO pairs analysis](../Projects/01_qqq_voo_pairs_analysis.md)

---

## 1. Cointegration

### Concept

Most **asset prices** are **non-stationary** in levels (often modeled as **I(1)**): they drift with trends and shocks. Regressing one price on another without care can produce **spurious regression**—high $R^2$ and significant coefficients even when no real economic link exists.

**Cointegration** means: two or more I(1) series share a **linear combination** that is **I(0)** (stationary). That combination is the **spread** (or error-correction residual): it wanders short term but is **tied to a long-run equilibrium**.

### Math

Let $X_t$ and $Y_t$ both be **I(1)**. They are **cointegrated** if there exists $\beta \neq 0$ such that:

$$
\text{Spread}_t = X_t - \beta Y_t = \varepsilon_t \sim I(0)
$$

Equivalently, in regression form (hedge ratio $\beta$):

$$
Y_t = \alpha + \beta X_t + \varepsilon_t, \quad \varepsilon_t \sim I(0)
$$

$\beta$ is the **hedge ratio**: units of $X$ per unit of $Y$ in a dollar-neutral spread. Some setups use **log prices** or a **ratio** $X_t / Y_t$; the test logic is the same—look for a **stationary residual** around a stable long-run relation.

### Intuition

Imagine **two people walking random paths** ($X_t$ and $Y_t$). Each path alone looks like a drunk walk (I(1)). If they are on a **leash** of fixed length $\beta$, their **separation** $\varepsilon_t$ stays bounded—they cannot drift apart forever. The **leash** is cointegration; **$\beta$** is how tight the leash is.

Without a leash, high **correlation** only means they often turn the same direction today—not that their **gap** is stable over years.

---

## 2. Spurious Regression vs Cointegration

### Concept

**Spurious regression:** Two independent random walks can look related in levels because both trend upward. **Cointegration:** The trends are **linked** so a specific linear combo does not trend.

### Math

If $X_t$ and $Y_t$ are independent random walks, $\Delta X_t$ and $\Delta Y_t$ are uncorrelated, but a level regression $Y_t = \alpha + \beta X_t + u_t$ often has:

- High $R^2$
- Low Durbin–Watson (residuals highly autocorrelated)
- $u_t$ still **I(1)** (non-stationary residuals)

Under **cointegration**, $u_t = \varepsilon_t$ is **I(0)**—residuals mean-revert around a stable equilibrium.

### Intuition

Two strangers climbing separate hills may both go up (correlated height over time) but their **altitude difference** keeps widening. Cointegrated assets are climbers on **the same rope**: each moves randomly, but **relative height** oscillates around a mean.

---

## 3. Engle–Granger Two-Step Method

### Concept

The **Engle–Granger** test is the standard **two-step** procedure to test cointegration between two series. `statsmodels` wraps this in `coint()`.

### Math

**Step 1 — Estimate hedge ratio (OLS on levels):**

$$
\hat{Y}_t = \hat{\alpha} + \hat{\beta} X_t, \quad \hat{\varepsilon}_t = Y_t - \hat{Y}_t
$$

**Step 2 — Test residuals for unit root (ADF on $\hat{\varepsilon}_t$):**

- **H0:** No cointegration (residuals have a unit root).
- **H1:** Cointegration (residuals stationary).

**Decision (5%):** If **p-value < 0.05**, reject H0 → evidence of cointegration.

In Python (as in our project):

```python
from statsmodels.tsa.stattools import coint

score, pvalue, crit = coint(qqq_adj, voo_adj)  # Adj Close levels
```

Run `coint` on **price levels** (I(1)), not on returns or log-diff.

### Intuition

Step 1 finds the **best leash length** $\hat{\beta}$. Step 2 asks whether the **slack in the leash** ($\hat{\varepsilon}_t$) keeps growing without bound or snaps back. Growing slack → no cointegration; mean-reverting slack → cointegration.

---

## 4. Correlation vs Cointegration

### Concept

| | **Correlation** | **Cointegration** |
|---|-----------------|-------------------|
| **Measures** | Co-movement of **changes** or short-run direction | Stability of a **level spread** / long-run gap |
| **Typical use** | Risk, diversification, factor exposure | Pairs trading, stat arb on spread |
| **Strong corr ⇒ coint?** | **No** | High corr can exist without a stationary spread |

### Math

Correlation (returns or levels):

$$
\rho_{XY} = \frac{\mathrm{Cov}(X_t, Y_t)}{\sigma_X \sigma_Y}
$$

Cointegration (existence of stationary spread):

$$
X_t - \beta Y_t \sim I(0) \quad \text{while} \quad X_t, Y_t \sim I(1)
$$

Both can be high in sample; only cointegration supports **mean reversion on the spread in levels**.

### Intuition

**Correlation** = two runners often speed up or slow down together. **Cointegration** = they stay within a few meters because of a rope. QQQ and VOO are highly correlated (> 0.95 on Adj Close) but in our sample **failed** Engle–Granger (p ≈ 0.21): they move together, yet the **QQQ/VOO ratio trends** rather than reverting to a fixed mean.

---

## 5. Spread, Ratio, and Hedge Ratio in Practice

### Concept

Pairs traders monitor a **signal series**:

- **Spread:** $S_t = X_t - \beta Y_t$ (dollar-neutral after sizing).
- **Ratio:** $R_t = X_t / Y_t$ (relative value; common for ETFs like QQQ/VOO).

Cointegration is defined on a **linear combo**; ratio is nonlinear but often used when assets are similar scale. Always **ADF-test the series you trade**.

### Math

Spread z-score (once $S_t$ is treated as stationary):

$$
z_t = \frac{S_t - \bar{S}}{\sigma_S}
$$

Trading rules (illustrative): enter when $|z_t| > z_{\text{entry}}$, exit when $z_t \to 0$.

If the **ratio** is I(1) but **log-diff** is I(0), you may model **short-horizon** moves on $\Delta \ln R_t$, not classic spread mean reversion in levels.

### Intuition

**Spread** is absolute gap; **ratio** is relative size. If the ratio **only goes up** (QQQ outperforming VOO since 2020), there is no stable “fair” ratio to revert to—your strategy is closer to **trending relative value** than classical cointegration pairs.

---

## 6. QQQ vs VOO — What Our Tests Showed

| Test | Result | Implication |
|------|--------|-------------|
| Correlation (Adj Close) | Very high (~0.95+) | Strong co-movement |
| ADF on QQQ/VOO **ratio** (levels) | p ≈ 0.10, non-stationary | No stable mean on ratio levels |
| ADF on **log-diff** of ratio | p ≈ 0, stationary | Short-horizon modeling on changes is valid |
| **Engle–Granger `coint()`** on Adj Close | p ≈ 0.21 | **Do not reject** no cointegration at 5% |

### Intuition

QQQ and VOO walk the same neighborhood (corr) but are **not on a fixed leash** in this window (coint). A pairs book that assumes **spread mean reversion in levels** needs another pair (e.g. sector ETFs) or a different signal (detrended ratio, rolling $\beta$, regime filters).

---

## 7. Practical Checklist

1. Confirm both legs are **I(1)** in levels (ADF on prices; fail to reject unit root).
2. Run **`coint(X, Y)`** on aligned Adj Close (or log prices if that is your convention—be consistent).
3. If p < 0.05: estimate $\hat{\beta}$, build spread, ADF-test spread, then z-score / backtest.
4. If p ≥ 0.05: do **not** assume classical cointegration pairs; revisit pair choice or use stationary transforms.
5. Always separate **correlation**, **stationarity of signal**, and **cointegration** in write-ups.

---

## References

- Engle & Granger (1987) — cointegration and error correction.
- Alexander — *Market Models* — pairs trading and spread construction.
- Prior note: [01_time_series_fundamentals.md](./01_time_series_fundamentals.md)
- Implementation: [01_qqq_voo_pairs_analysis.ipynb](../Projects/01_qqq_voo_pairs_analysis.ipynb)

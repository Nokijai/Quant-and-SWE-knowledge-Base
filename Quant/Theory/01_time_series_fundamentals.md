# 01 — Time Series Fundamentals

Theory notes for quantitative work in this repo. Each section follows: **Concept → Math → Intuition**.

**Related project:** [QQQ vs VOO pairs analysis](../Projects/01_qqq_voo_pairs_analysis.md)

---

## 1. Time Series

### Concept

A **time series** is a sequence of observations ordered in time: $x_1, x_2, \ldots, x_T$. In finance we usually work with **prices** (levels) or **returns** (changes). Many models assume the statistical properties of the series do not change over time—that idea is linked to **stationarity**.

### Math

A discrete-time series $\{X_t\}_{t=1}^{T}$ can be written as:

$$
X_t = \mu_t + \varepsilon_t
$$

where $\mu_t$ is a deterministic or slowly changing component (trend, seasonality) and $\varepsilon_t$ is a random shock.

For **log prices** (common in quant):

$$
p_t = \ln(P_t), \quad r_t = p_t - p_{t-1} = \ln\!\left(\frac{P_t}{P_{t-1}}\right)
$$

### Intuition

Think of a time series as a **movie of one variable over time**, not a bag of random numbers. Order matters: today's price depends on yesterday's. Before modeling mean reversion or pairs trading, you must know *which version* of the series you use—level price, ratio, or return—because each has different statistical behavior.

---

## 2. Stationarity

### Concept

A series is **stationary** if its mean, variance, and autocovariance structure are stable over time (strict stationarity is stronger; in practice we use **weak / covariance stationarity**). **Non-stationary** series often look like they **drift or trend**; naive regression on two trending prices can show **spurious correlation**.

### Math

**Weak stationarity** requires, for all lags $k$:

$$
\mathbb{E}[X_t] = \mu \quad \text{(constant mean)}
$$

$$
\mathrm{Var}(X_t) = \sigma^2 \quad \text{(constant variance)}
$$

$$
\mathrm{Cov}(X_t, X_{t-k}) = \gamma_k \quad \text{(depends only on lag } k \text{, not on } t \text{)}
$$

A simple **random walk** (non-stationary in levels):

$$
X_t = X_{t-1} + \varepsilon_t, \quad \varepsilon_t \sim \text{i.i.d.}
$$

Here $\mathrm{Var}(X_t)$ grows with $t$.

### Intuition

A stationary series **fluctuates around a fixed “home”**—like a thermostat keeping temperature near 72°F. A non-stationary price series is like **a drunk walk**: no fixed home, variance keeps growing. You cannot reliably fit mean-reversion on something that has no stable mean.

**QQQ/VOO example:** The QQQ/VOO **ratio in levels** behaved non-stationary in our ADF test (p ≈ 0.10); the **log-diff of the ratio** was stationary (p ≈ 0).

---

## 3. Integration Order — I(0) and I(1)

### Concept

- **I(0):** Integrated of order zero → **stationary** (or stationary after simple transforms).
- **I(1):** Integrated of order one → **non-stationary in levels**, but **first difference** is (approximately) I(0).

Most **asset prices** are treated as **I(1)**; **returns** are often **I(0)**.

### Math

If $X_t \sim I(1)$, then:

$$
\Delta X_t = X_t - X_{t-1} \sim I(0)
$$

For a **log price** $p_t = \ln P_t$:

$$
\Delta p_t = \ln P_t - \ln P_{t-1} \approx \text{log return}
$$

Two series $X_t$ and $Y_t$ that are both I(1) may still share a **long-run link**—that is **cointegration** (see a future note `02_cointegration_theory.md`).

### Intuition

**I(1)** is “sticky memory”: today's level equals yesterday plus a shock. **I(0)** is “short memory”: shocks die out and the series does not wander forever. Pairs trading often assumes a **spread or ratio** is I(0) so you can trade deviations from a mean—but if the spread itself is I(1), the “mean” is not stable.

---

## 4. Augmented Dickey–Fuller (ADF) Test

### Concept

The **ADF test** checks for a **unit root** (non-stationarity). It is the standard first step before ARMA modeling or before claiming mean reversion on a spread.

- **H0:** Series has a unit root (non-stationary).
- **H1:** Series is stationary.

**Decision rule (5% level):** If **p-value < 0.05**, reject H0 → treat as stationary.

### Math

The ADF regression (with optional trend and lagged differences):

$$
\Delta X_t = \alpha + \beta t + \gamma X_{t-1} + \sum_{i=1}^{p} \delta_i \Delta X_{t-i} + u_t
$$

We test:

$$
H_0: \gamma = 0 \quad \text{(unit root)} \quad \text{vs.} \quad H_1: \gamma < 0 \quad \text{(stationary)}
$$

In Python (`statsmodels`):

```python
from statsmodels.tsa.stattools import adfuller
stat, pvalue, lags, nobs, crit, icbest = adfuller(series.dropna())
```

### Intuition

ADF asks: **“If I subtract yesterday from today, does that change look like it pulls the series back toward a level, or like pure noise on a drifting walk?”** A low p-value means the data reject the “random walk in levels” story.

**Workflow in our notebook:**

1. Test **ratio** (levels) → non-stationary.
2. Build **log-diff** → test again → stationary.
3. Only then consider short-horizon models on the differenced series.

---

## 5. Differencing and Log-Diff (Returns)

### Concept

**Differencing** removes slow trends and converts many I(1) series into I(0). For positive prices and ratios, **log** stabilizes scale and turns products into sums.

### Math

**Simple difference:**

$$
\Delta X_t = X_t - X_{t-1}
$$

**Log level and log-diff (log return on a ratio $R_t = Q_t / V_t$):**

$$
g_t = \ln R_t, \quad \Delta g_t = \ln R_t - \ln R_{t-1} = \ln\!\left(\frac{R_t}{R_{t-1}}\right)
$$

Approximation for small moves:

$$
\ln\!\left(\frac{R_t}{R_{t-1}}\right) \approx \frac{R_t - R_{t-1}}{R_{t-1}}
$$

### Intuition

**Levels** tell you *where* the ratio is (e.g. QQQ is 1.01× VOO). **Log-diff** tells you *how fast* that relative price changed today—like speed instead of position. Mean-reversion trading on **levels** without stationarity is like betting on “return to 72°F” when the thermostat itself is drifting.

---

## 6. Autocorrelation (ACF) and Partial Autocorrelation (PACF)

### Concept

- **ACF** measures correlation between $X_t$ and $X_{t-k}$ (includes indirect paths through intermediate lags).
- **PACF** measures **direct** correlation at lag $k$ after removing effects of shorter lags.

Used to guess **AR/MA order** and to see **persistence** (slow decay in ACF often hints at non-stationarity or near–unit root).

### Math

**Autocorrelation at lag $k$:**

$$
\rho_k = \frac{\mathrm{Cov}(X_t, X_{t-k})}{\mathrm{Var}(X_t)}
$$

Sample ACF uses the same formula on demeaned data. **PACF** at lag $k$ is the correlation between $X_t$ and $X_{t-k}$ after regressing both on $X_{t-1}, \ldots, X_{t-k+1}$.

In Python:

```python
import statsmodels.graphics.tsaplots as tsaplots
tsaplots.plot_acf(series.dropna(), lags=30)
tsaplots.plot_pacf(series.dropna(), lags=30)
```

### Intuition

**ACF** is “how much does yesterday still echo today?” If the echo dies slowly across many lags, the series has **long memory**—typical for price **levels**. **PACF** that drops sharply after lag 1 suggests an **AR(1)**-style structure on the stationary part.

**QQQ/VOO ratio:** High ACF at low lags → persistent, non-stationary ratio; PACF spike at lag 1 → a simple AR(1) on the *stationary* transform may be a reasonable starting model.

---

## 7. Correlation vs Stationarity vs Cointegration (Preview)

| Idea | What it checks | Pairs-trading relevance |
|------|----------------|-------------------------|
| **Correlation** | Short-run co-movement | High corr (QQQ & VOO > 0.95) does **not** guarantee tradable mean reversion |
| **Stationarity (ADF)** | Whether a *single* series has a stable mean | Spread/ratio must be I(0) for classic z-score rules |
| **Cointegration** | Long-run equilibrium between two I(1) series | Engle–Granger on Adj Close; our p ≈ 0.21 → **no cointegration** |

### Intuition

**Correlation** = two runners often move together this month. **Stationarity** = one runner's *distance from a fixed mark* oscillates. **Cointegration** = two random walkers tied by a leash so their *gap* is stable even though each path wanders. QQQ and VOO move together (corr) but failed the leash test (coint) in our sample.

---

## 8. Practical Checklist (Before Any Pairs Model)

1. Plot **levels** and **ratio**; compute **correlation**.
2. Run **ADF** on the trading signal series (spread or ratio).
3. If non-stationary, try **log-diff** or estimate $\beta$ and test the **spread** (cointegration note).
4. Inspect **ACF/PACF** on the series you will actually model.
5. Only then: z-score, ARMA, or backtest—document **H0/H1** and **p-values**.

---

## References

- Hamilton, *Time Series Analysis* — stationarity, unit roots, ARIMA.
- Tsay, *Analysis of Financial Time Series* — returns, volatility, applications.
- Project implementation: `Quant/Projects/01_qqq_voo_pairs_analysis.ipynb`

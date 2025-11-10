
import numpy as np

def VaR(ticker, p=0.95):
    try:
        import yfinance as yf
    except ImportError:
        import os
        os.system("pip install yfinance")
        import yfinance as yf

    try:
        from scipy.stats import norm
    except ImportError:
        import os
        os.system("pip install scipy")
        from scipy.stats import norm

    # fetch 1 year of daily adjusted close prices, compute daily returns and VaR
    data = yf.download(ticker, period="1y", progress=False)["Adj Close"].dropna()
    if data.empty:
        raise ValueError(f"No historical data found for ticker: {ticker}")
    if not (0 < p < 1):
        raise ValueError("p must be between 0 and 1")

    returns = data["Close"]/data["Open"] - 1
    E = returns.mean()
    sigma = returns.std()
    Z_p = norm.ppf(1 - p)
    VaR = (Z_p * sigma) - E
    return VaR 
import yfinance as yf
from scipy.stats import norm

def RoI(ticker, p=0.95,days=365):
    
    # fetch all historical data for the ticker
    data = yf.download(ticker,start="1900-01-01" ,progress=False,auto_adjust=False)
    if data.empty:
        raise ValueError(f"No historical data found for ticker: {ticker}")

    returns = (data['Open']-data['Close'].shift(days))/data['Open']
    returns = returns[returns.columns[0]]
    E = returns.mean()
    return E 
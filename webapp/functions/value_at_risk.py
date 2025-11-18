import yfinance as yf
def VaR(ticker, p=0.95):
    
    # fetch all historical data for the ticker
    data = yf.download(ticker, progress=False,auto_adjust=False)
    if data.empty:
        raise ValueError(f"No historical data found for ticker: {ticker}")

    returns = (data['Open']-data['Close'])/data['Open'] * -1
    return returns[returns.columns[0]].quantile(p)
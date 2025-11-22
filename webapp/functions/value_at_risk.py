import yfinance as yf
def VaR(data, p=0.95):
    try:
        # fetch all historical data for the ticker
        # data = yf.download(ticker, progress=False,auto_adjust=False)
        # if data.empty:
        #     raise ValueError(f"No historical data found for ticker: {ticker}")
        
        returns = (data['Open']-data['Close'])/data['Open'] * -1
        return returns[returns.columns[0]].quantile(p)
    except Exception as e:
        print(e)
        raise ValueError(f"Error calculating VaR for ticker {data.columns[0][1]}: {str(e)}")

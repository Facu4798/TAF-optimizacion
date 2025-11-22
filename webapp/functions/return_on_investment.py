import yfinance as yf
from scipy.stats import norm

def RoI(data, p=0.95,days=365):
    try:
        # fetch all historical data for the ticker
        # data = yf.download(ticker,start="1900-01-01" ,progress=False,auto_adjust=False)
        # if data.empty:
        #     raise ValueError(f"No historical data found for ticker: {ticker}")

        returns = (data['Open']-data['Close'].shift(days))/data['Open']
        returns = returns[returns.columns[0]]
        E = returns.mean()
        return E 
    except Exception as e:
        print(e)
        raise ValueError(f"Error calculating RoI for ticker {data.columns[0][1]}: {str(e)}")
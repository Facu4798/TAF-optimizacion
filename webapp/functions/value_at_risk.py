import yfinance as yf
def VaR(data, p=0.95):
    try:
        
        returns = (data['Open']-data['Close'])/data['Open'] * -1
        return returns[returns.columns[0]].quantile(p)
    except Exception as e:
        print(e)
        raise ValueError(f"Error calculating VaR for ticker {data.columns[0][1]}: {str(e)}")
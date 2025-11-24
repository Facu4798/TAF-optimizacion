import yfinance as yf
def get_series(ticker):
    try:
        return yf.download(ticker,start ="1900-01-01",progress=False,auto_adjust=False)
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None
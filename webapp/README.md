# Portfolio Optimization Web App

A Flask-based web application for portfolio optimization using linear programming.

## Features

- Input investment parameters (budget, risk, return, diversification)
- Dynamically add multiple stock tickers
- Optimize portfolio allocation using Value at Risk (VaR) and Return on Investment (RoI)
- Display recommended investment amounts for each stock
- Show expected risk and return statistics
- Provide optimization recommendations

## Installation

1. Navigate to the webapp directory:
```bash
cd webapp
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask server:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Usage

1. Open your browser and navigate to `http://localhost:5000`
2. Fill in the investment parameters:
   - **Budget**: Total amount available for investment
   - **Maximum Risk**: Target risk level (0-100%)
   - **Expected Return**: Target return percentage (0-∞%)
   - **Diversification Level**: Controls how many stocks to include (0-100%)
3. Add stock tickers using the ticker input fields
   - Click "+ Add Ticker" to add more stocks
   - Click "Remove" to remove a ticker
4. Click "Optimize Portfolio" to generate results
5. View the optimized allocation, statistics, and recommendations

## Input Parameters

- **Budget ($)**: The total amount you want to invest
- **Risk (0-100%)**: Maximum acceptable risk level as a percentage
- **Return (0-∞%)**: Expected return target as a percentage
- **Diversification (0-100%)**: Higher values allow more stocks in the portfolio
- **Tickers**: Stock symbols (e.g., AAPL, MSFT, GOOGL)

## Output

The results page shows:
- **Investment Allocation**: How much to invest in each stock
- **Portfolio Statistics**: Expected risk, return, budget utilization, and number of stocks
- **Recommendations**: Suggestions for improving your portfolio based on the optimization

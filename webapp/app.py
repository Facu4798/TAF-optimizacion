from flask import Flask, render_template, request, jsonify
from functions.report import generate_report
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/optimize', methods=['POST'])
def optimize():
    try:
        # Get form data
        budget = float(request.form.get('budget'))
        risk = float(request.form.get('risk'))
        expected_return = float(request.form.get('return'))
        diversification = float(request.form.get('diversification'))
        
        # Get tickers (dynamic fields)
        tickers = []
        i = 0
        while True:
            ticker = request.form.get(f'ticker_{i}')
            if ticker is None or ticker.strip() == '':
                break
            tickers.append(ticker.strip().upper())
            i += 1
        
        if len(tickers) == 0:
            return render_template('index.html', error="Please add at least one ticker symbol")
        
        # Default days parameter (you can make this configurable if needed)
        days = 30
        
        # Convert diversification from 0-100 to 0-1 range
        diver = diversification / 100
        
        # Call the generate_report function
        z, inputs, envs, vars_df, constraints, stats, recommendations = generate_report(
            budget=budget,
            risk=risk,
            expected_return=expected_return,
            tickers=tickers,
            days=days,
            diver=diver
        )
        
        # Extract investment amounts
        investments = {}
        for ticker in tickers:
            var_name = f'stocks_{ticker}'
            if var_name in vars_df.index:
                amount = vars_df.loc[var_name, 'Value']
                if amount > 0:
                    investments[ticker] = round(amount, 2)
        
        # Extract statistics
        actual_risk = round(stats.loc['Risk', 'Value'], 2) if 'Risk' in stats.index else 0
        actual_return = round(stats.loc['Expected Return', 'Value'], 2) if 'Expected Return' in stats.index else 0
        percentage_invested = round(stats.loc['Pergcentage invested', 'Value'], 2) if 'Pergcentage invested' in stats.index else 0
        num_stocks = int(stats.loc['Number of stocks', 'Value']) if 'Number of stocks' in stats.index else 0
        
        return render_template('results.html',
                             budget=budget,
                             risk=risk,
                             expected_return=expected_return,
                             diversification=diversification,
                             tickers=tickers,
                             investments=investments,
                             actual_risk=actual_risk,
                             actual_return=actual_return,
                             percentage_invested=percentage_invested,
                             num_stocks=num_stocks,
                             recommendations=recommendations)
    
    except Exception as e:
        print(e)
        return render_template('index.html', error=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



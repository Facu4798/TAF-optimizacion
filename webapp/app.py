try:
    from flask import Flask, render_template, request
except ImportError:
    import os
    os.system("pip install Flask")
    from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    # Provide an initial list of asset tickers (can be empty)
    initial_assets = []
    return render_template("portfolio.html", assets=initial_assets)

@app.route("/resultado", methods=["POST"])
def resultado():
    # collect all form inputs named "asset" (includes dynamically added rows)
    assets = request.form.getlist("asset")
    # normalize and remove empty entries
    assets = [a.strip() for a in assets if a and a.strip()]

    # read budget and risk level from the form
    budget_str = request.form.get("budget", "").strip()
    try:
        budget = float(budget_str) if budget_str else None
    except ValueError:
        budget = None

    # parse risk level as integer 0-100
    risk_level_str = request.form.get("risk_level", "50")
    try:
        # allow float strings like "50.0" but store as int
        risk_level = int(round(float(risk_level_str)))
    except (ValueError, TypeError):
        risk_level = 50
    # clamp to [0,100]
    risk_level = max(0, min(100, risk_level))

    from app_value_at_risk import VaR
    vars = [VaR(a) for a in assets] 

    from app_model import optimize_portfolio
    opt = optimize_portfolio(assets, vars, budget, risk_level)

    return render_template("resultado.html", assets=assets, budget=budget, risk_level=risk_level, vars=vars)



if __name__ == "__main__":
    # Listen on all interfaces for container friendliness
    app.run(host="0.0.0.0", port=5000, debug=True)


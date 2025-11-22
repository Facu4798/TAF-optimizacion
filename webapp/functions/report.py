import pandas as pd
from functions.value_at_risk import VaR
from functions.return_on_investment import RoI
from functions.optimize import optimize


def generate_report(budget, risk, expected_return, tickers, days, diver):
    
    VaRs = {ticker: VaR(ticker) for ticker in tickers}
    RoIs = {ticker: RoI(ticker, days=days) for ticker in tickers}

    z = optimize(tickers = tickers,
                budget=budget,
                VaRs=VaRs,
                RoIs=RoIs,
                mxr=risk,
                exr=expected_return,
                diver =diver
                )

    varvals = {v.name: v.varValue for v in z.model.variables()}


    inputs =pd.DataFrame({
        'Budget':"$"+str(budget),
        "Stocks":", ".join(tickers),
        "Risk (VaR)":str(risk)+"%",
        "Expected Return": str(expected_return)+"%",
        "Days": days,
    },index=["Value"]).T


    envs =pd.DataFrame({'VaR':VaRs,'RoI':RoIs},index=tickers)


    vars =pd.DataFrame([{v.name:v.varValue for v in z.model.variables()},
                        {v.name:v.dj for v in z.model.variables()}],
                        index=["Value","Reduced cost"]).T.map(lambda x: round(x,4))

    constraints = pd.DataFrame([{c.name:c.pi for c in z.model.constraints.values()},
                        {c.name:c.slack for c in z.model.constraints.values()},
                        {c.name:c.value() for c in z.model.constraints.values()}],
                        index=["Dual Value","Slack","Value"]).T



    stats =(pd.DataFrame({
            "Risk": sum([varvals[f'stocks_{t}'] * VaRs[t] for t in tickers]),
            "Expected Return": sum([varvals[f'stocks_{t}'] * RoIs[t] for t in tickers]),
            "Pergcentage invested": z.ts.varValue**2/budget,
            "Number of stocks": sum([1 for t in tickers if varvals[f'stocks_{t}']> 0.0])*z.ts.varValue/100
        },index=["Value"]).T/z.ts.varValue*100).map(lambda x: round(x,2)).fillna(0)


    reccomendations = []

    # diversification analysis
    if constraints[constraints.index.str.startswith("Diversification_Link")]["Dual Value"].sum() > 0:
        reccomendations.append("Consider increasing diversification to reduce risk.")
    elif constraints[constraints.index.str.startswith("Diversification_Link")]["Dual Value"].sum() == 0:
        reccomendations.append("Diversification level is adequate.")
    else:
        reccomendations.append("Consider decreasing diversification to increase returns.")

    # risk/return slack analysis
    if stats.loc["Number of stocks","Value"] < len(tickers):
        if vars.loc["s1","Value"] < 0:
            reccomendations.append("You can increase the risk to potentially improve returns.")
        if vars.loc["s2","Value"] < 0:
            reccomendations.append("You can decrease the expected return to potentially reduce risk.")

    return z, inputs, envs, vars, constraints, stats, reccomendations
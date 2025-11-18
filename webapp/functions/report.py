import pandas as pd
from value_at_risk import VaR
from return_on_investment import RoI
from optimize import optimize2

def generate_report(budget, risk, expected_return, tickers, days):
    VaRs = {ticker: VaR(ticker) for ticker in tickers}
    RoIs = {ticker: RoI(ticker, days=days) for ticker in tickers}

    z = optimize2(tickers = tickers,
              budget=budget,
              VaRs=VaRs,
              RoIs=RoIs,
              mxr=risk,
              exr=expected_return
            )

    varvals = {v.name: v.varValue for v in z.model.variables()}

    # print inputs
    inputs = pd.DataFrame(
        {
            'Budget':"$"+str(budget),
            "Stocks":", ".join(tickers),
            "Risk (VaR)":str(risk)+"%",
            "Expected Return": str(expected_return)+"%",
            "Days": days,
        },
        index=["Value"]
    ).T

    # evironment
    enviroment = pd.DataFrame({'VaR':VaRs,'RoI':RoIs},index=tickers)

    # variables
    variables = pd.DataFrame(
        [
            {v.name:v.varValue for v in z.model.variables()},
            {v.name:v.dj for v in z.model.variables()}
        ],
        index=["Value","Reduced cost"]).T.map(lambda x: round(x,4))
    

    # constraints
    constraints = pd.DataFrame(
        [
            {c.name:c.pi for c in z.model.constraints.values()},
            {c.name:c.slack for c in z.model.constraints.values()},
            {c.name:c.value() for c in z.model.constraints.values()}
        ],
        index=["Dual Value","Slack","Value"]).T

    # summary statistics of process
    stats = (pd.DataFrame(
        {
            "Risk": sum([varvals[f'stocks_{t}'] * VaRs[t] for t in tickers]),
            "Expected Return": sum([varvals[f'stocks_{t}'] * RoIs[t] for t in tickers]),
            "Pergcentage invested": z.ts.varValue**2/budget
        },
        index=["Value"]).T/z.ts.varValue*100).map(lambda x: round(x,2))
    
    return z, inputs, enviroment, variables, constraints, stats
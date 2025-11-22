from pulp import *
def optimize(tickers,budget,VaRs,RoIs,mxr,exr,ponder=0.5,diver=0.5):
    
    if mxr >= 1:
        mxr = mxr / 100
    if exr >= 1:
        exr = exr / 100

    # Penalty weights
    M1 = budget * ponder  # risk penalty
    M2 = budget * (1 - ponder)  # return penalty

    # Create the model
    model = LpProblem("Portfolio_Optimization", LpMaximize)

    # Decision variables
    stocks = {t: LpVariable(f"stocks_{t}", lowBound=0) for t in tickers}
    s1 = LpVariable("s1")  # risk slack
    s2 = LpVariable("s2")  # return slack
    ts = LpVariable("ts", lowBound=0)  # total spent
    d = {t: LpVariable(f"d_{t}", lowBound=0, upBound=1,cat=LpBinary) for t in tickers}  # diversification binaries

    # Objective function: maximize return minus penalties
    model += (
        lpSum([stocks[t] * RoIs[t] for t in tickers]) - ponder*s1 - (1 - ponder)*s2,
        "Total_Return_Minus_Penalties"
    )


    # Constraints
    # Budget constraint
    model += lpSum([stocks[t] for t in tickers]) <= budget, "Max_Expenditure"

    # Total spent continuity
    model += lpSum([stocks[t] for t in tickers]) == ts, "Total_Spent"

    # Risk constraint (with slack)
    model += lpSum([stocks[t] * VaRs[t] for t in tickers]) == ts * mxr + s1, "Risk_Constraint"

    # Return constraint (with slack)
    model += lpSum([stocks[t] * RoIs[t] for t in tickers]) == ts * exr - s2, "Return_Constraint"

    # Diversification constraint
    model += lpSum([d[t] for t in tickers]) <= diver * len(tickers), "Diversification_Constraint"
    for t in tickers:
        model += stocks[t] <= d[t] * budget, f"Diversification_Link_{t}"

    # Solve
    model.solve()
    # import os
    # os.system("cls" if os.name == "nt" else "clear")

    class result:
        def __init__(self):
            pass
         
    r = result(); r.model = model; r.stocks = stocks; r.s1 = s1; r.s2 = s2; r.ts = ts

    return r


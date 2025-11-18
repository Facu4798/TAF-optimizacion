from pulp import *
def optimize2(tickers,budget,VaRs,RoIs,mxr,exr,ponder=0.5):
    
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
    s1 = LpVariable("s1", lowBound=0)  # risk slack
    s2 = LpVariable("s2", lowBound=0)  # return slack
    ts = LpVariable("ts", lowBound=0)  # total spent

    # Objective function: maximize return minus penalties
    model += (
        lpSum([stocks[t] * RoIs[t] for t in tickers]) - M1 * s1 - M2 * s2,
        "Total_Return_Minus_Penalties"
    )

    # Constraints
    # Budget constraint
    model += lpSum([stocks[t] for t in tickers]) <= budget, "Max_Expenditure"

    # Total spent continuity
    model += lpSum([stocks[t] for t in tickers]) == ts, "Total_Spent"

    # Risk constraint (with slack)
    model += lpSum([stocks[t] * VaRs[t] for t in tickers]) <= ts * mxr + s1, "Risk_Constraint"

    # Return constraint (with slack)
    model += lpSum([stocks[t] * RoIs[t] for t in tickers]) >= ts * exr - s2, "Return_Constraint"

    # Solve
    model.solve()
    
    import os
    os.system("cls" if os.name == "nt" else "clear")

    class result:
        def __init__(self):
            pass
         
    r = result(); r.model = model; r.stocks = stocks; r.s1 = s1; r.s2 = s2; r.ts = ts

    return r
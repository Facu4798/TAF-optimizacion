from pulp import *
def optimize(tickers,budget,VaRs,RoIs,mxr,exr,ponder=0.5,diver=0.5):
    # scale parameters 
    diver = diver / 100
    mxr = mxr /100
    exr = exr / 100
    ponder = ponder / 100
    diver = diver / 100



    print(budget,VaRs,RoIs,mxr,exr,ponder,diver,sep ="\n",end="\n\n")
    # Create the model
    model = LpProblem("Portfolio_Optimization", LpMaximize)

    # Decision variables
    stocks = {t: LpVariable(f"stocks_{t}", lowBound=0) for t in tickers}
    s1 = LpVariable("s1",lowBound=0)  # risk slack
    s2 = LpVariable("s2", lowBound=0)  # return slack
    e1 = LpVariable("e1", lowBound=0)  # excess risk
    e2 = LpVariable("e2", lowBound=0)  # excess return
    ts = LpVariable("ts", lowBound=0)  # total spent
    d = {t: LpVariable(f"d_{t}", lowBound=0, upBound=1,cat=LpBinary) for t in tickers}  # diversification binaries

    # Penalty weights
    M1 = budget * ponder  # risk penalty
    M2 = budget * (1 - ponder)  # return penalty


    model += (
        lpSum([stocks[t] * RoIs[t] for t in tickers])  
        - lpSum([stocks[t] * VaRs[t] for t in tickers])
        - budget * s1 
        - budget * s2
        ,"Total_Return_Minus_Penalties"
    )


    # Constraints
    # Budget constraint
    model += lpSum([stocks[t] for t in tickers]) <= budget, "Max_Expenditure"

    # Total spent continuity
    model += lpSum([stocks[t] for t in tickers]) == ts, "Total_Spent"

    # Risk constraint (with slack)
    model += lpSum([stocks[t] * VaRs[t] for t in tickers]) - s1 + e1 == ts * mxr, "Risk_Constraint"

    # Return constraint (with slack)
    model += lpSum([stocks[t] * RoIs[t] for t in tickers]) + s2 - e2 == ts * exr, "Return_Constraint"

    # Diversification constraint
    model += lpSum([d[t] for t in tickers]) >= diver * len(tickers), "Diversification_Constraint"
    for t in tickers:
        model += stocks[t] <= d[t] * budget, f"Diversification_Link_{t}"

    # Solve
    model.solve()

    class result:
        def __init__(self):
            pass
         
    r = result(); r.model = model; r.stocks = stocks; r.s1 = s1; r.s2 = s2; r.ts = ts

    return r


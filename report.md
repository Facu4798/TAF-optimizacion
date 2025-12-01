|                 | Value                               |
|:----------------|:------------------------------------|
| Budget          | $100000                             |
| Stocks          | AAPL, ^GSPC, MSFT, GOOG, AMZN, TSLA |
| Risk (VaR)      | 5%                                  |
| Expected Return | 5%                                  |
| Days            | 365                                 |

# Environment Parameters

|       |       VaR |       RoI |
|:------|----------:|----------:|
| AAPL  | 0.0364702 | 0.104073  |
| ^GSPC | 0.0118141 | 0.0505988 |
| MSFT  | 0.0293683 | 0.2017    |
| GOOG  | 0.0233082 | 0.190046  |
| AMZN  | 0.0441989 | 0.046745  |
| TSLA  | 0.046387  | 0.258159  |

# Variables

|              |   Value |   Reduced cost |
|:-------------|--------:|---------------:|
| d_AAPL       |       0 |         0      |
| d_AMZN       |       0 |        -0      |
| d_GOOG       |       0 |         0      |
| d_MSFT       |       0 |         0      |
| d_TSLA       |       0 |        -0      |
| d_^GSPC      |       0 |         0      |
| e1           |       0 |        -0      |
| e2           |       0 |         0.5    |
| s1           |       0 |         0.5    |
| s2           |       0 |        -0      |
| stocks_AAPL  |       0 |        -0.0671 |
| stocks_AMZN  |       0 |        -0.1035 |
| stocks_GOOG  |       0 |        -0.011  |
| stocks_MSFT  |       0 |        -0.0112 |
| stocks_TSLA  |       0 |        -0      |
| stocks_^GSPC |       0 |        -0.0692 |
| ts           |       0 |        -0      |

# Constraints

|                            |   Dual Value |   Slack |   Value |
|:---------------------------|-------------:|--------:|--------:|
| Max_Expenditure            |     0.107693 |      -0 | -100000 |
| Total_Spent                |    -0.025    |      -0 |       0 |
| Risk_Constraint            |     1        |      -0 |       0 |
| Return_Constraint          |    -0.5      |      -0 |       0 |
| Diversification_Constraint |    -0        |      -0 |      -6 |
| Diversification_Link_AAPL  |    -0        |  100000 |       0 |
| Diversification_Link_^GSPC |    -0        |  100000 |       0 |
| Diversification_Link_MSFT  |    -0        |  100000 |       0 |
| Diversification_Link_GOOG  |    -0        |  100000 |       0 |
| Diversification_Link_AMZN  |    -0        |  100000 |       0 |
| Diversification_Link_TSLA  |    -0        |      -0 |       0 |

# Solution Statistics

|                      |   Value |
|:---------------------|--------:|
| Risk                 |     nan |
| Expected Return      |     nan |
| Pergcentage invested |       0 |
| Number of stocks     |       0 |
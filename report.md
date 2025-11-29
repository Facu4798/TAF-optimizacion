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

|              |      Value |   Reduced cost |
|:-------------|-----------:|---------------:|
| d_AAPL       |      1     |         0      |
| d_AMZN       |      1     |         0      |
| d_GOOG       |      1     |         0      |
| d_MSFT       |      1     |         0      |
| d_TSLA       |      1     |      3944.02   |
| d_^GSPC      |      1     |         0      |
| e1           |    361.303 |         0      |
| e2           |  20815.9   |         0      |
| s1           |      0     |   -100000      |
| s2           |      0     |   -100000      |
| stocks_AAPL  |      0     |        -0.1047 |
| stocks_AMZN  |      0     |        -0.1698 |
| stocks_GOOG  |      0     |        -0.0056 |
| stocks_MSFT  |     -0     |         0      |
| stocks_TSLA  | 100000     |        -0      |
| stocks_^GSPC |      0     |        -0.1335 |
| ts           | 100000     |         0      |

# Constraints

|                            |   Dual Value |            Slack |             Value |
|:---------------------------|-------------:|-----------------:|------------------:|
| Max_Expenditure            |    0.172332  |     -0           |      -1.45519e-11 |
| Total_Spent                |    0         |     -1.45519e-11 |      -1.45519e-11 |
| Risk_Constraint            |    0         |     -9.09495e-13 |       3.04588e-06 |
| Return_Constraint          |   -0         |     -9.09495e-13 |       7.85195e-05 |
| Diversification_Constraint |   -0         |     -0           |       0           |
| Diversification_Link_AAPL  |   -0         | 100000           | -100000           |
| Diversification_Link_^GSPC |   -0         | 100000           | -100000           |
| Diversification_Link_MSFT  |   -0         | 100000           | -100000           |
| Diversification_Link_GOOG  |   -0         | 100000           | -100000           |
| Diversification_Link_AMZN  |   -0         | 100000           | -100000           |
| Diversification_Link_TSLA  |    0.0394402 |     -0           |       0           |

# Solution Statistics

|                      |    Value |
|:---------------------|---------:|
| Risk                 | 0.046387 |
| Expected Return      | 0.258159 |
| Pergcentage invested | 1        |
| Number of stocks     | 1        |
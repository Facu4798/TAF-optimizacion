# parameters

$mxr >=0$ maximo riesgo esperado (max xpected risk)

$re >=0$ retorno esperado

$diver$

$ponder$

$days$

$budget$

$tickers$

# entorno
$VaR=p_{1-p}(r^d)$

$E(R^d)=\frac{1}{n-d}\sum_{t=1}^{N-d}\frac{Open_t-Close_{t+d}}{Open_t}$

# variables

$\alpha_{ticker}$ si se invierte en una acción 

$X_{ticker}$ cantidad invertida en la acción

$s1$ y $s2$ que son slack de riesgo y slack de retorno

$ts$ total spent

# Objetivo
$\max Z= \left(\sum X_{ticker} * RoI_{ticker}\right) - budget * ponder * s1 + budget * (1-pobnder) * s2$

# Constrains

$\sum X_{ticker} <= budget$ presupuesto

$ts == \sum X_{ticker}$ continuidad total spent

$\sum X_{ticker} * VaR_{ticker} = mxr * ts + s1$ riesgo

$\sum X_{ticker} * RoI_{ticker} = re * ts - s2$ retorno

$\sum \alpha_{ticker} <= diver * |tickers|$

$X_{ticker} <= \alpha_{ticker} * budget  \quad \forall ticker \in tickers$ cont A_t

# ANALISIS DE SENSIBILIDAD

## diversificación
dual value de las constraints de A_t
$\sum dv const A_t >0$ entonces diversificar mas

## Riesgo

# Retorno
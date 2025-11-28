# Parámetros

$mxr \geq0$ maximo riesgo esperado (max xpected risk) (0.xx)

$re \geq 0$ retorno esperado(0.xx)

$diver$ coefiente de diversificación ($0\leq diver  \leq1$)

$0 \leq ponder \leq 1$ ponderación riesgo - retorno. si el valor es 0, fuerza a que se respete el riesgo definido. si el valor es 1, fuerza a que se respete el retorno definido. cualquier valor en el medio hace que ambas restricciones hagan conseciones (una mas que la otra segun la ponderación) en caso de que no se puedan respetar ambas restricciones. si el valor esta en 0 y con ninguna cartera disponible se puede estar por debajo del riesgo definido, el modelo no invertirá en ningun activo. si esta en 1 y no se puede alcanzar el retorno definido, el retorno no invertirá en ningun activo.

$days \geq 0 $ dias que se consideran que se van a retener las acciones antes de valorar alguna ganancia.

$B \geq 0$ presupuesto a invertir

$tickers$ nombres simbolicos de las acciones (^GSPC = s&p 500, GOOG = google, TSLA = tesla,etc.)

# entorno

$R^d = \frac{Close_{t+d} - Open_t}{Open_t}$ retorno a $d$ dias =  la variación porcentual entre el precio de apertura de un dia $t$ y el precio de cierre dentro de $d$ dias . osea $t+d$.


$VaR=p_{(1-p)}(R^d)$ percentil $1-p$ de la serie de retornos $R^d$ que son los retornos del activo a $d$ dias. ej: si $p=0.95$ el percentil $0.05$ va a ser el $VaR$. Value at risk = medida de riesgo estadística sobre el activo.


$E(R^d)=\frac{1}{N-d}\sum_{t=1}^{N-d}r^d_t$ retorno esperado del activo a $d$ dias. el retono esperado se calcula como el promedio de todos los retornos a $d$ dias de la serie. esto solo se puede hacer desde $t=1$ hasta el dia $N-d$ donde $N$ es la cantidad de retornos de la serie.

# variables

$\alpha_{ticker}$ variable binaria (0,1) que indica si se invierte en una acción o no. 

$X_{t}$ cantidad invertida en la acción

$s_1$ y $s_2$ que son slack de riesgo y slack de retorno negativos. osea los valores que flatan de retorno y que se exceden (exceso negativo) de riesgo en las restricciones correspondientes para balancear las ecuaciones de las mismas.

$e_1$ y $e_2$ que son falta de riesgo (positivo) y exceso de retorno. osea los valores que faltan de riesgo y sobran de retorno en las restricciones correspondientes para balancear las mismas.

$ts$ total gastado entre todas las acciones.

# Objetivo
$\max Z= \underbrace{\sum X_{ticker} * RoI_{ticker}}_{\max retorno} - \underbrace{\sum X_{ticker} \cdot VaR_{ticker}}_{\min riesgo} - \underbrace{B \cdot(ponder \cdot s_1 + (1-ponder) \cdot s_2)}_{\min \text{holguras negativas}}$

termino 1: maximización del retorno. todo lo que invertimos en cada acción multiplicado por su retorno esperado. actua como un promedio ponderado del retorno esperado de la cartera.

termino 2: minimización del riesgo. al poner un termino en negativo en un problema de maximización el modelo minimiza este termino. lo mismo que antes pero multiplicando el riesgo esperado (value at risk). actua como un promedio ponderado del riesgo de la cartera.

termino 3: utiliza $B$ como escalar de la penalización ya que este valor va a ser si o si mayor que los otros terminos y por lo tanto penaliza fuertemente las holguras negativas $s_1$ y $s_2$. si $ponder=1$ toda la penalización irá sobre $s_1$ es decir el riesgo, por lo que solo se penalizarán holguras negativas de riesgo (en este caso excesos) y viceversa para $s_2$ con el retorno.

# Constrains

$\sum X_{ticker} \leq B$ la suma de todo lo invertido no puede superar el presupuesto definido. no se consideraron holguras presupuestarias por exceso como un caso de metas, ya que no resultó realista exigir mas dinero del necesario, ademas de que la repartición porcentual del presupuesto resultaría la misma.

$ts = \sum X_{ticker}$ (restricción de continuidad). definimos que la suma de todas las inversiones es igual a $ts$, variable que representa justamente este mismo concepto. 

$\sum X_{ticker} \cdot VaR_{ticker} = mxr \cdot ts + s_1 - e_1$ 

el riesgo total esperado de la cartera (promedio ponderado) debe ser igual al total invertido $ts$, multiplicado por el riesgo máximo definido $mxr$ + el exceso de riesgo $s_1$ porque si nos pasamos de riesgo invirtiendo en los $X_{ticker}$ este valor balancea, y si nos sobra (tenemos menos riesgo que $mxr$) entonces $-e_1$ balancea la ecuacíon.


$\sum X_{ticker} \cdot RoI_{ticker} = re \cdot ts - s2 +e_1$ 

el retorno total esperado de la cartera (promedio ponderado) debe ser igual al total invertido $ts$, multiplicado por el retorno mínimo definido $re$ - el exceso de retorno $e_1$ porque si nos pasamos de retorno invirtiendo (ganamos mas de lo que pedimos) en los $X_{ticker}$ este valor balancea, y si nos falta (tenemos menos retorno que $re$) entonces $-s_1$ balancea la ecuacíon.

$\sum \alpha_{ticker} \leq diver \cdot |tickers|$ 

la cantidad de acciones en la que podemos invertir ($\sum \alpha$) tiene que ser menor o igual que el $diver$% de la cantidad de acciones consideradas $|tickers|$. ej: si estamos considerando 10 acciones y tenemos un $diver=0.4$ vamos a poder invertir en hasta 4 acciones diferentes. 

$X_{ticker} \leq \alpha_{ticker} \cdot B  \quad \forall ticker \in tickers$ 

esta es una restriccion que vincula las variables binarias con sus respectivas acciones y sus cantidades invertidas. si $\alpha = 0$ esto va a hacer que $\alpha\cdot B =0$ y por lo tanto como $X$ tiene que ser menor o igual, ese respectivo $X$ va a ser 0. por otro lado si $\alpha=1$ el lado derecho de la ecuación vale $\alpha\cdot B= 1 \cdot B = B$ por lo cual $X$ puede tomar un valor hasta $B$ $\Rightarrow X\leq B$. es decir, si se toma en consideración la acción, se puede invertir un valor menor al presupuesto en esta. 

# ANALISIS DE SENSIBILIDAD
$DV(R)$: dual value de la restricción $R$.

$R: x + y \leq \underbrace{a}_{rhs}$

## diversificación

$\sum_{t\in tickers} DV(R_{X_t\leq\alpha_t\cdot B})\geq0 \Rightarrow + diver$ 

si la suma de todos los dual values de las restricciones que vinculan a los alphas con las cantidades es positiva se recomienda diversificar mas. el dual value es una medida que nos indica cuanto mas crece la función objetivo si se agranda el $rsh$ de la restrricción. en este caso si las restricciones tienen un $rhs$ de 0 es porque estas no se estan considerando pero aumentaría el valor de la función objetivo si se aumenta el $rhs$ es decir si $\alpha$ se hace 1 para que se pueda considerar esta acción y que el $rhs$ pase a valer $B$. esto sucede cuando el coeficiente de diversificación es bajo y hay acciones que sería positivo invertir en esa acción pero actualmente no se puede porque el coeficiente no lo permite.

$\sum_{t\in tickers} DV(R_{X_t\leq\alpha_t\cdot B})\leq 0 \Rightarrow - diver$

lo mismo pero si da negativo es porque estamos invirtiendo en acciones en las que no conviene y se recomienda reducir el coeficiente de diversificación para prevenir esto.


## - Retorno - riesgo
$\underbrace{e_2 \geq 0}_{\text{sobra riesgo (positivo)}} \,\wedge\, \underbrace{\sum X_t \cdot VaR_t \leq mxr }_{\text{se respeta el riesgo}} \Rightarrow -mxr$

si la holgura positiva del retorno $e_2$ es mayor a 0 (estamos teniendo mayor retorno de lo esperado) y el riesgo se respeta, podemos buscar una solución con menor riesgo y con un retorno que aún respete lo exigido


## + Riesgo + retorno

$\underbrace{e_1 \geq 0}_{\text{sobra riesgo (positivo)}} \,\wedge\, \underbrace{\sum X_t \cdot RoI_t \geq re }_{\text{se respeta el retrono}} \Rightarrow +re$

si tenemos una holgura del riesgo (el portafolio es menos riesgo de lo esperado) podemos subir el retorno esperado y buscar una solución que nos de un retorno mayor con un nivel de riesgo que aún respete lo exigido. 


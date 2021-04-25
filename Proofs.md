# Proofs



### Minimum Variance Portfolio

The objective is to optimize the weights for each stock such that the variance is minimized. The optimal weights can be derived using Lagrange multipliers. 

$$
\begin{aligned}
X & = N(\mu, \Sigma) \\
L & = w' \Sigma w - \lambda(\iota'w-1)\\
\frac{\partial L}{\partial w} & = \Sigma w - \lambda \iota = 0\\

w & = \lambda \Sigma^{-1}\iota\\
\frac{\partial L}{\partial \lambda} & = \iota'w-1 = 0 \\
\lambda & = \frac{1}{\iota' \Sigma^{-1} \iota} \\
w & = \frac{\Sigma^{-1} \iota}{\iota' \Sigma^{-1} \iota}
\end{aligned} 
$$

### Special Case I: Uncorrelated variables

In case the stocks are uncorrelated, the weights can be calculated with the following formula.

$$
\begin{aligned}
w_i & = \frac{\sigma_i^{-2}}{\sum_j^{n}\sigma_j^{-2}}

\end{aligned}
$$
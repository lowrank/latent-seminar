---
date: 2022-09-26
tags:
  - math-PR
  - math-CA
  - math-CO
comments: "true"
---
>[!info] 
>The Gaussian Correlation Inequality was proved in 2014 ([arXiv: 1408.1028](https://arxiv.org/pdf/1408.1028)). The interesting story can be found in [Quanta Magazine](https://www.quantamagazine.org/statistician-proves-gaussian-correlation-inequality-20170328). 

The inequality is to show the Gaussian measure $\mu$ on centrally symmetric convex sets $A$ and $B$ satisfies

$$
\mu(A\cap B)\ge \mu(A)\mu(B).
$$

That is to say, if a dart hits the wall with standard Gaussian distribution, suppose two targets are centrally symmetric convex sets $A$,  $B$, then hitting both targets with one dart is easier than hitting $A$ with the first dart and hitting $B$ with the second, vice versa.

The proof of inequality is simple and elegant. I think there are a few keys in the proof which are insightful (that is why this note exists 😁).  The first observation is the following. 

>[!important] Observation 
>A centrally symmetric convex closed set can be formed by the intersection of countable symmetric strips. [^1]

This observation of “strips” is natural, since a convex symmetric body can be approximated by a sequence of convex, symmetric polytopes. Moreover, convex, symmetric polytopes are just slices of the unit cube in a higher dimension satisfying the constraints $\{|\langle x, v_i \rangle |\le 1\}$ for $i=1,2,\cdots, k$. Therefore, the problem can be reduced to proving 

>[!important] Gaussian Correlation Theorem
>$$
>\mathbb{P}\left(\bigcap_{i=1}^n A_i\right) \ge \mathbb{P}\left(\bigcap_{i=1}^k A_i\right) \mathbb{P}\left(\bigcap_{i=k+1}^n A_i\right),
>$$
>where $A_i = \{|X_i|\le x_i\}$, $i=1,2,\cdots, n$ and $(X_1, \cdots, X_n)\sim \mathcal{N}(\mathbf{0}, \Sigma_n)$.

The special case $k=1$ was proved by the following theorem [^2].

>[!important] Theorem (Khatri)
>Let $\{X_i\}_{1\le i\le n}$ be a jointly Gaussian random variables with mean zero. Then
>$$
>\mathbb{P}(\max_{1\le i\le n} |X_i| \le 1) \ge \mathbb{P}(|X_1|\le 1)\, \mathbb{P}(\max_{2\le i \le n} |X_i| \le 1).
>$$ 

### Multivariate Gamma-type distribution
The set $\{|X_i|\le 1\}$ is better described by chi-squared distribution or Gamma distribution. Surprisingly, the multivariate Gamma distributions on $\mathbb{R}^n$ have several (non-equivalent) definitions🤣. 

The $\Gamma(\alpha, R)$ distribution is defined as follows [^4]. 

>[!info] Definition
>If the random vector $X = (X_1, \cdots, X_n)$ satisfies the Laplace transform
>$$
>\mathbb{E}[\exp\left(-\langle s, X\rangle \right)] = \frac{1}{|I + R \operatorname{diag}(s)|^{\alpha}},
>$$
>then it obeys the $\Gamma(\alpha, R)$ distribution.  

>[!check] Example 
>If $\alpha=\frac{1}{2}$ and $X\sim \chi^2_n$ or $X\sim \Gamma(\alpha=\frac{n}{2}, \theta=2)$, then the covariance matrix $R = 2I_n$ and
>$$
>\mathbb{E}[\exp(-\langle s, X\rangle)] = \prod_{i=1}^n \mathbb{E}[\exp(-s_i X_i)] = \prod_{i=1}^n \int_0^{\infty} \frac{x^{-1/2} e^{-x/2}}{2^{1/2}\Gamma(\frac{1}{2})} e^{-s_i x} dx = \prod_{i=1}^n \frac{1}{\sqrt{2s_i + 1}}.
>$$



### Technique

- In order to distinguish the dependence and independence, it is very common to introduce the correlation matrix for the $n$ dimensional vector $X$, that is, $C(\tau) = [C_{11}, \tau C_{12}; \tau C_{21} ,C_{22}]$ in the spirit of variational method, then the left-hand and right-hand sides of the desired inequality are referring the case $\tau = 1$ and $\tau = 0$. It equivalently means the function

  

$$\tau \mapsto \mu(Z_i(\tau)\le s_i, i=1,2\dots, n)$$

  

is non-decreasing in $\tau$, where $Z_i = \frac{X_i^2}{2}$ and $s_i = \frac{t_i^2}{2}$. Let $f(z,\tau)$ be the joint distribution's density function of $Z(\tau)$, then that is to show the derivative $\partial_{\tau} f(z, \tau)$ is non-negative.

  

- The following claim is from Lebesgue's dominated convergence theorem. The differentiation can be swapped with the Laplace transform.

  

$$\int_{[0, \infty)^{n}} e^{-\bf{\lambda}\cdot z} \partial_{\tau} f(z, \tau) dz = \partial_{\tau} \int_{[0,\infty)^{n}} e^{-\bf{\lambda}\cdot z} f(z, \tau) dz$$

  

which equals to

$$ \int_{[0,\infty)^{n}} e^{-\bf{\lambda}\cdot z} f(z, \tau) dz = \mathbb{E} \exp(-\frac{1}{2}\sum_{i=1}^n \lambda_i X_i^2(\tau)) = |I + \Lambda C(\tau)|^{-1/2}.$$

  

- The rest is a linear algebra problem only. Here $\Lambda$ is not important anymore, we drop it as identity.

  

$$ \det (I + C(\tau)) = \det(C_{11} + I)\det(C_{22} + I - \tau^2(C_{21})(C_{11} + I)^{-1} (C_{21})^T )$$

  

which should be decreasing in $\tau$.

  

In the original proof by Thomas Royen, the inequality is extended to the distributions such that the Laplace transform is infinitely divisible.

## Notes
- 
## Links
- https://arxiv.org/pdf/1408.1028

[^1]: Schechtman, Gideon, Th Schlumprecht, and Joel Zinn. "On the Gaussian measure of the intersection." _Annals of probability_ (1998): 346-357.

[^2]: Khatri, Chinubhai G. "On certain inequalities for normal distributions and their applications to simultaneous confidence bounds." _The Annals of Mathematical Statistics_ (1967): 1853-1867.

[^3]: Krishnamoorthy, A. S., and M. Parthasarathy. "A multivariate gamma-type distribution." _The Annals of Mathematical Statistics_ 22.4 (1951): 549-557.

[^4]: Note, not all values of $\alpha$ suffice to produce an admissible distribution. 

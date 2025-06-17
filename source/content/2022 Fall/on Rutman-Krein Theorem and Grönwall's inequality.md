---
date: 2022-09-26
tags:
  - math-AP
  - math-CA
comments: "true"
---
We start with a simple application of Grönwall's inequality that proves

$$0\le f(x) \le C \int_0^x f(s) ds,\quad x\in [0, 1],$$

then $f(x) = 0$. Instead of using the traditional (but nice) way that let $h(x) = e^{-x} \int_0^x f(s) ds$ and study $g'$, we try to look at this problem from the integral operator $\mathcal{A} f:= C\int_0^x f(s) ds$. Then $\mathcal{A}: L^{\infty}_{+}(D)\to L^{\infty}_{+}(D)$ is actually a positive and compact operator, then according to the Krein-Rutman theorem, if its spectral radius $r(\mathcal{A})$ is positive, we must have an eigenfunction $g(x) > 0$ strictly positive. However, $\mathcal{A}g (0) = 0$ gives a contradiction. Therefore the spectral radius $r(\mathcal{A}) = 0$. Then $f(x) \le \mathcal{A} f(x)$ implies $f(x) \le \mathcal{A}^n f(x)$, which gives $f(x) = 0$ as $n\to \infty$.

  

- As an extension, if there is another operator $\mathcal{B}$ commutes with $\mathcal A$, then the spectral radius $r(\mathcal{A} + \mathcal{B})$ can be estimated. We consider the problem

$$0\le f(x) \le \mathcal{A} f + \mathcal{B} f$$

where $\mathcal{B}$ is an operator with $\|\mathcal{B}\|<1$, then we can estimate $r(\mathcal A + \mathcal{B}) \le r(\mathcal{A}) + r(\mathcal{B}) < 1$. The same argument holds.

  

- As an immediate application, we consider the inequality that

$$0\le f(x) \le C\int_{v\in V} \int_0^{\tau_{-}(x, v)} f(x - sv) ds$$

where $V$ is a compact directional cone subset of $\mathbb{S}^{d-1}$, that is, there is a direction $w$ such that $v\cdot w > 0$ for all $v\in V$, then such operator is just an extension of the aformentioned integral operator which has zero spectral radius. This is an essential step for uniqueness of nonlinear transport.

- Let $E(x,y) = e^{-c|x-y|}$ and $S f :=\displaystyle\int_{\mathbb{R}^d} \frac{E(x,y)}{|x - y|^{d-1}} f(y) dy$, then

$$S \mathcal{A} f = \int_{\mathbb{R}^d} \int_{V}\int_0^{\infty} \frac{E(x,y)}{|x - y|^{d-1}} f(y - sv) ds dv dy$$

and

$$\mathcal{A} S f = \int_{V}\int_0^{\infty} \int_{\mathbb{R}^d} \frac{E(x-sv, y)}{|x-sv-y|^{d-1}} f(y) dy ds dv = \int_{V} \int_0^{\infty} \int_{\mathbb{R}^d} \frac{E(x-sv, y'-sv)}{|x - y'|^{d-1}} f(y'-sv) dy' ds dv.$$ Therefore $\mathcal{A} S = S \mathcal{A}$. That is, if

$$0\le f(x) \le C \mathcal{A} f + \Sigma_s \int_{D} \frac{e^{-\Sigma_s|x-y|}}{|x-y|^{d-1}} f(y) dy.$$

Then $f(x) = 0$.

## Notes
- 
## Links
- 
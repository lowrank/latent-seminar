---
date: 2022-10-03
tags:
  - math-NA
comments: "false"
---
## Background

Sinkhorn's Theorem bridges the positive matrices (positive entries) with the doubly stochastic matrices by diagonal multipliers, i.e., there are diagonal matrices $D_1$ and $D_2$ that
$$
D_1 A D_2 e = e, \quad e^T D_1 A D_2 = e^T
$$

The proof can be found in various methods, but most are based on certain kind of fixed-point property. For instance, the geometric proof uses the Brouwer's fixed-point theorem. The convergence of the Sinkhorn's algorithm seeks for the vectors $x$ and $y$ by iteratively computing

$$
y_{k+1} = r./(A x_k), \quad x_{k+1} = c ./ (A^T y_{k+1}) 
$$
where $r$ is the row sum vector and $c$ is the column sum vector. They can be merged into one iteration by
$$x_{k+1} = T (x_k):= c ./ (A^T (r ./ A x_{k})).$$
The theory uses the nonlinear Perron-Frobenius theorem to find the fixed-point. Clearly, the map $T$ sends the positive cone $\mathbb{R}^{n}_+$ to itself, here we need a little bit more compactness to exploit the fixed-point theorem. Either seeking for the boundedness or define $\widehat{T} x = T(x) / \|T(x)\|_1$, then a fixed-point of $\widehat{T}$ also works due to invariance of scaling. When the matrix $A$ is relaxed to only nonnegative entries, there are proofs showing if $A$ is fully indecomposable, then the same conclusion holds.

## Thoughts  

By a simple generalization, it is natural to ask for non-singular integral kernel $A(x,y) > 0$ such that

$$\int_{D_q} p(x) A(x, y) q(y) d y = 1,\quad \int_{D_p} p(x) A(x, y) q(y) d x = 1$$

  

Then a natural iteration will be $$h_{k+1}(y) = T h_k:= \dfrac{c(y)} { \displaystyle\int_{D_q} \dfrac{ A(x, y) r(x) }{ \displaystyle\int_{D_p} A(x,y) h_k(y) dy }dx} $$

  

and we seek for a fixed-point of $h = \widehat{T} h$, where $\widehat{T}$ is a normalization of $T$, the boundedness of $h_k$ comes at no price, for a certain kind of compactness, we can add the equi-continuity requirement which becomes a smoothness condition on $A(x,y)$ such that $A(x, y)$ is equi-continuous in $y$, then a convergent subsequence of $h_k$ will be what we need. Therefore $A$ can be also a weakly singular kernel as well.

  

If $A(x, y, t)$ is an evolution of integral operator converges as $t\to\infty$ which gradually looses the equi-continuity or boundedness, it is interesting to see whether the corresponding solution $h^{\ast}(y, t)$ also converges.
## Notes
- 
## Links
- 
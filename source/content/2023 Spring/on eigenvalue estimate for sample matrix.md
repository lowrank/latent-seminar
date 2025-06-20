---
date: 2023-03-20
tags:
  - math-CA
  - math-PR
comments: "false"
---
## Introduction

Given a positive definite kernel function $\mathcal{G}(x, y)$, it is natural to sample some points $(x_i, x_j)$ (so it creates a matrix $G$) as an approximation to the kernel function. It is a classical topic to estimate the eigenvalues of $G$ and compare with $\mathcal{G}$'s eigenvalues. 

The simplest idea to quantify the difference is probably **Weyl's inequality** for self-adjoint compact operators.  

>[!note] Estimate by Weyl's inequality 
>Let $\Omega=[0, 1]^n$ be a unit cube and $\mathcal{G}(x, y)$ is a positive definite kernel defined on $\Omega\times \Omega$. The matrix $G\in \mathbb{R}^{m\times m}$ has entries as $\mathcal{G}(x_i, x_j)$ for $\{x_i\}_{i=1}^m$ be the regular "lattice points" with $\sqrt[n]{m}$ points along each axis. Then 
>$$
>|\mu_i(\mathcal{G}) - \frac{1}{m}\mu_i(G)| = O\left(\frac{1}{\sqrt[n]{m}}\right)
>$$
>where $\mu_i$ denotes the $i$th eigenvalue in descending order.
>

>[!summary] Proof: 
> 
## Notes
- 
## Links
- [[on two-layer ReLU networks]]

[^1]: Widom, Harold. "On the eigenvalues of certain Hermitian operators." _Transactions of the American Mathematical Society_ 88.2 (1958): 491-522.

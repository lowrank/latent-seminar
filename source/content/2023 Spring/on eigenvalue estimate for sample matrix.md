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
>Let $\Omega=[0, 1]^n$ be a unit cube and $\mathcal{G}(x, y)\in C^1(\Omega\times \Omega)$ is a positive definite kernel. The matrix $G\in \mathbb{R}^{m\times m}$ has entries as $\mathcal{G}(x_i, x_j)$ for $\{x_i\}_{i=1}^m$ be the regular "lattice points" with $\sqrt[n]{m}$ points along each axis. Then 
>$$
>|\mu_i(\mathcal{G}) - \frac{1}{m}\mu_i(G)| = O\left(\frac{1}{\sqrt[n]{m}}\right)
>$$
>where $\mu_i$ denotes the $i$th eigenvalue in descending order.
>

>[!summary] Proof: 
> The lattice points automatically generate a partition of $\Omega$, we denote $C(x_i)$ as the small cube centered at $x_i$ which is disjoint from other small cubes. 
> 
> The matrix $G$ constructs an approximated kernel function on each small cube around the lattice points. We define $\mathcal{G}^{\ast}(x, y)$ as
>$$
>\mathcal{G}^{\ast}(x, y) = \mathcal{G}(x_i, y_j)\quad (x, y)\in C(x_i)\times C(y_j).
>$$
>It is straightforward to see $\mu_i(\mathcal{G}^{\ast}) = \frac{1}{m}\mu_i(G)$.  Then by Weyl's inequality, 
>$$
>\begin{aligned}
>|\mu_i(\mathcal{G}) - \mu_i(\mathcal{G}^{\ast})| &\le \|\mathcal{G} - \mathcal{G}^{\ast}\|_{op} \le \sqrt{\int_{\Omega\times\Omega} |\mathcal{G}(x, y) - \mathcal{G}^{\ast}(x, y)|^2 dx dy} \\
>&= \sqrt{\sum_{i=1}^m\sum_{j=1}^m \int_{C(x_i)\times C(x_j)} |\mathcal{G}(x, y) - \mathcal{G}^{\ast}(x, y)|^2 dx dy} \\
>&= O \left( \frac{\|\nabla \mathcal{G}\|_{\infty}}{\sqrt[n]{m}} \right). 
>\end{aligned}
>$$

Intuitively, the insufficiency of samples will only affect smaller eigenvalues (more oscillatory eigenfunctions), thus isolating the "safer" eigenfunctions is natural.

Let the kernel $\mathcal{G}$ be expanded into its eigenfunctions:
$$
\mathcal{G}(x, y) = \sum_{k=1}^{\infty} \lambda_k \psi_k(x) \psi_k(y).
$$
And we pick a truncation $\mathcal{G}_m:= \sum_{k=1}^{m} \lambda_k \psi_k(x) \psi_k(y)$. Then the matrix $G$ can be split into two parts: 
$$
G_{i, j} = \mathcal{G}_m(x_i, x_j) + (\mathcal{G}(x_i, x_j) - \mathcal{G}_m(x_i, x_j)).
$$

## Notes
- 
## Links
- [[on two-layer ReLU networks]]

[^1]: Widom, Harold. "On the eigenvalues of certain Hermitian operators." _Transactions of the American Mathematical Society_ 88.2 (1958): 491-522.

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

>[!important] Estimate by Weyl's inequality 
>Let $\Omega=[0, 1]^n$ be a unit cube and $\mathcal{G}(x, y)\in C^1(\Omega\times \Omega)$ is a positive definite kernel. The matrix $G\in \mathbb{R}^{m\times m}$ has entries as $\mathcal{G}(x_i, x_j)$ for $\{x_i\}_{i=1}^m$ be the regular "lattice points" with $\sqrt[n]{m}$ points along each axis. Then 
>$$
>|\mu_i(\mathcal{G}) - \frac{1}{m}\mu_i(G)| = O\left(\frac{1}{\sqrt[n]{m}}\right)
>$$
>where $\mu_i$ denotes the $i$th eigenvalue in descending order.
>

>[!note]- Proof
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

Intuitively, the insufficiency of samples will only affect smaller eigenvalues (more oscillatory eigenfunctions), thus isolating the “safer” eigenfunctions is natural.

Let the kernel $\mathcal{G}$ be expanded into its eigenfunctions:
$$
\mathcal{G}(x, y) = \sum_{k=1}^{\infty} \mu_k(\mathcal{G}) \psi_k(x) \psi_k(y).
$$
And we pick a truncation $\mathcal{G}_l:= \sum_{k=1}^{l} \lambda_k \psi_k(x) \psi_k(y)$. Then the matrix $G$ can be split into two parts: 
$$
G_{i, j} = \mathcal{G}_l(x_i, x_j) + (\mathcal{G}(x_i, x_j) - \mathcal{G}_l(x_i, x_j)).
$$
The first part should be less affected by the sampling, thus we should expect the correlation   
$$
\frac{1}{m}\sum_{i=1}^m \psi_{k}(x_i) \phi_r (x_i)\approx \delta_{k, r}
$$
The common tool we use is Ostrowski's theorem[^2].

>[!important] Ostrowski theorem
>If $A\in \mathbb{C}^{n\times n}$ and $X\in\mathbb{C}^{n\times n}$, then 
>$$
>\mu_i(X^{\ast}A X) = \theta_i \mu_i(A), i\in [n].
>$$
>where $\mu_n(X^{\ast} X) \le \theta_i \le \mu_1(X^{\ast}X)$. 

Let $(\Phi_l)_{i,j} = \psi_{j}(x_i)$ and $\Lambda_l = \operatorname{diag}(\mu_i(\mathcal{G}))_{i=1}^l$, then the theorem implies

$$
\left|\frac{1}{m}\mu_i(\Phi_l\Lambda_l \Phi_l^{\ast}) - \mu_i(\mathcal{G})\right|\le \mu_i(\mathcal{G})\left\|\frac{1}{m}\Phi_l^T\Phi_l - Id_l\right\|_{op}.
$$
 
Then, we obtain the bound (Ostrowski theorem and Weyl's theorem)

$$
\begin{aligned}
|\mu_i(\mathcal{G}) - \frac{1}{m}\mu_i(G)| &\le |\mu_i(\mathcal{G}) -\frac{1}{m} \mu_i(\Phi_l\Lambda_l\Phi_l^T)| + |\frac{1}{m}\mu_i(\Phi_l\Lambda_l\Phi_l^T) - \frac{1}{m}\mu_i(G)| \\
&\le \mu_i(\mathcal{G}) \left\|\frac{1}{m}\Phi_l^T\Phi_l - Id_l\right\|_{op} + \frac{1}{m}\|G - \Phi_l\Lambda_l \Phi_l^{\ast}\|_{op}.
\end{aligned}
$$
- The remainder term $G - \Phi_l\Lambda_l \Phi_l^{\ast} = \sum_{k > l} \mu_k \psi_k(x_i)\psi_k(x_j)$, a naive bound of the 2nd term will be $C \sum_{k > l} \mu_k$ if the eigenfunctions are uniformly bounded, otherwise the growth needs to be considered. 
- The first term can be quantified by viewing $x_i$ as a certain quadrature rule, or ready for Hoeffding's inequality. We should expect the stochastic bound $O(m^{-1/2}\sqrt{\log l^2/p})$ for each entry with probability $1 - \frac{p}{l^2}$, therefore, with probability $1 - p$,
  $$
   \left\|\frac{1}{m}\Phi_l^T\Phi_l - Id_l\right\|_{op} = O\left(\sqrt{m \log l^2/p}\right).
   $$

Another approach for well-structured points $x_i$ is using the min-max principle for eigenvalues, which usually involves an explicit construction of subspace, see also [[on convergence of graph Laplacian]].
## Links
- [[on two-layer ReLU networks]]
- [[on convergence of graph Laplacian]]

[^1]: Widom, Harold. "On the eigenvalues of certain Hermitian operators." _Transactions of the American Mathematical Society_ 88.2 (1958): 491-522.

[^2]: https://en.wikipedia.org/wiki/Ostrowski%27s_theorem

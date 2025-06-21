---
date: 2023-06-05
tags:
  - math-NA
  - math-CA
comments: "false"
---
>[!info] 
>This post is more like an exercise for personal interest. It does not necessarily contain anything new. 

## 🏷️Introduction

Let $\Gamma\subset \mathbb{R}^3$ be a smooth, closed, oriented surface. And $\Delta_{\Gamma}$ is the Laplace-Beltrami operator on $\Gamma$ and $\nabla_{\Gamma}$ be the gradient operator. We denote $\{\phi_k\}_{k\ge 0}$ as the eigenfunctions of $-\Delta_{\Gamma}$ with corresponding eigenvalues $\{\lambda_k\}_{k\ge 0}$. The first trivial eigenvalue $\lambda_0 = 0$. 

### 🌵Eigenvalue estimates in tube 

Let $d_{\Gamma}$ denote the signed distance function to $\Gamma$ that takes the negative sign for points inside the region enclosed by $\Gamma$. With the distance function to $\Gamma$, the projection operator can be evaluated by
$$
    P_{\Gamma}(x) := x - d_{\Gamma}(x) \nabla d_{\Gamma}(x).
$$
The projection operator is well-defined when the $|d_{\Gamma}(x)|^{-1}$ is larger than the maximum principal curvature of $\Gamma$. 

>[!note]  Definition
>Let $\Gamma_t$ be the level set 
>$$
>\Gamma_t:= \{x\in \mathbb{R}^3 \mid d_{\Gamma} x = t\}
>$$
> and the tube $D_t:= \{x\in \mathbb{R}^3 \mid |d_{\Gamma} x| < t\}$

Then we prove the following lemma, which shows the eigenvalues of the Laplacian on $D_r$ can approximate the eigenvalues of $\Delta_{\Gamma}$ as the tube width $r\ll 1$.

>[!important]  Lemma
>Let $r > 0$ be a small parameter. Assume that $\psi_0, \psi_1, \cdots$ are the eigenfunctions of the following eigenvalue problem with Neumann boundary condition
>$$
>\begin{aligned}
>-\Delta \psi_k &= \mu_k \psi_k & \text{ in }& D_r\\
>\frac{\partial \psi_k}{\partial n} &= 0 &\text{ on }&\partial D_r.
>\end{aligned} 
>$$
>Then there exists a constant $C > 0$ independent of $r$ that $|\lambda_k - \mu_k| \le Cr\lambda_k$.

>[!note] Proof
>Using the min-max principle, 
>$$
>\mu_k = \min_{\dim U = k+1}\max_{f\in U - \{0\}} \frac{\int_{D_r} |\nabla f(x)|^2 dx }{\int_{D_r} |f(x)|^2 dx}.
>$$
>We first provide a lower bound for $\mu_k$.  Our estimate consists of three steps.
>- Explicit construction of the subspace $U$. We define the functions $\{h_m\}_{m=0}^k$ by 
>$$
>h_m(x) = \phi_m(P_{\Gamma} x).
>$$
>and denote $U = \operatorname{span}(h_0,\cdots, h_k)$.
> - Estimate of norms. Let $f\in U$, and we apply the co-area formula
> $$
> \begin{aligned}
> \int_{D_r} |f(x)|^2 dx &= \int_{-r}^r \int_{d_{\Gamma}(x) = t}|f(x)|^2 dS d t \\
> &= \int_{-r}^r \int_{d_{\Gamma}(x) = t}|f(P_{\Gamma} x)|^2 dS d t
> \end{aligned}
>  $$



## Notes
- 
## Links
- 
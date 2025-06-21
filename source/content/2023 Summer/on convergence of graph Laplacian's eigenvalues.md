---
date: 2023-06-05
tags:
  - math-NA
  - math-CA
  - math-AP
comments: "false"
---
>[!info] 
>This post is more like an exercise for personal interest. It does not necessarily contain anything new. 

## 🏷️Introduction
Let us imagine that a closed smooth manifold is constructed in minecraft 😅, we can expect some detailed information is likely to lose. It is natural to ask: 

> How much geometric information is still kept?

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

>[!note]- Proof
>The main tool is the min-max principle, 
>$$
>\mu_k = \min_{\dim U = k+1}\max_{f\in U - \{0\}} \frac{\int_{D_r} |\nabla f(x)|^2 dx }{\int_{D_r} |f(x)|^2 dx}.
>$$
>We first provide a lower bound for $\mu_k$.  Our estimate consists of three steps.
>
>**Step 1**: Explicit construction of the subspace $U$.  We define the functions $\{h_m\}_{m=0}^k$ by 
>$$
>h_m(x) = \phi_m(P_{\Gamma} x).
>$$
>and denote $U = \operatorname{span}(h_0,\cdots, h_k)$.
>
> **Step 2**: Estimate of norms.  Let $f\in U$, and we apply the co-area formula
> $$
> \begin{aligned}
> \int_{D_r} |f(x)|^2 dx &= \int_{-r}^r \int_{d_{\Gamma}(x) = t}|f(x)|^2 dS d t \\
> &= \int_{-r}^r \int_{d_{\Gamma}(x) = t}|f(P_{\Gamma} x)|^2 dS d t
> \end{aligned}
>$$
>Let $J(x)$ be the Jacobian between the surfaces $\{d_{\Gamma} = t\}$ and $\Gamma$, then 
>$$
>\int_{d_{\Gamma}(x) = t}|f(P_{\Gamma} x)|^2 J(x) dS = \int_{\Gamma} |f(x)|^2 dS
>$$
>where $J(x) = 1 - d_{\Gamma}(x) \Delta d_{\Gamma}(x) + |d_{\Gamma}(x)|^2 \langle{\nabla d_{\Gamma}, \nabla^2 d_{\Gamma} \nabla d_{\Gamma}}\rangle$.
>
>Therefore,  $J(x) = 1 + O(r)$, we have the following estimate
>$$
>\int_{D_r} |f(x)|^2 dx = 2r \left(1 + O(r)\right)  \int_{\Gamma} |f(x)|^2 dS.
>$$
>We then estimate
>$$
>\begin{aligned}
>\int_{D_r} |\nabla f|^2 dx &= \int_{-r}^r \int_{d_{\Gamma}(x) = t}|\nabla f(x)|^2 dS d t \\
>&= \int_{-r}^r \int_{d_{\Gamma}(x) = t}|\nabla f(P_{\Gamma} x)|^2 dS d t = 2r(1 + O(r)) \int_{\Gamma} |\nabla f(x)|^2 dS \\
>&= 2r(1 + O(r)) \int_{\Gamma} |\nabla_{\Gamma} f(x)|^2 dS.
>\end{aligned}
>$$
>
>**Step 3**: Apply the min-max principle. 
>$$
>\begin{aligned}
>\mu_k &\le (1 + O(r)) \max_{f\in U -\{0\}} \frac{\int_{\Gamma} |\nabla_{\Gamma} f(x)|^2 dS }{\int_{\Gamma} |f(x)|^2 dS} \\
>&= (1 + O(r)) \lambda_k.
>\end{aligned}
>$$
>Next, we provide an upper bound estimate using the max-min counterpart.
>$$
>\mu_k = \max_{\dim U = k} \min_{f \in U^{\perp} - \{0\}}   \frac{\int_{D_r} |\nabla f(x)|^2 dx }{\int_{D_r} |f(x)|^2 dx}.
>$$
>
>**Step 4**: Explicit construction of $U$.  We define the functions $\{w_m\}_{m=0}^{k-1}$ by 
>$$
>w_m(x) = \sqrt{\mathcal{J}(x)} \phi_m(P_{\Gamma}x) ,\quad {\mathcal{J}}(x):=\frac{J(x)+J(2P_{\Gamma} x - x)}{2}.
>$$
>where $2P_{\Gamma} x - x$ is the mirror point of $x$ across $\Gamma$. Then for $\forall i\neq j$, using the symmetry of the domain along normal direction,
>$$
>\begin{aligned}
>\int_{D_r} w_i(x) w_j(x) dx &= \int_{-r}^r \int_{d_{\Gamma}(x) = t} w_i(x) w_j(x) dS d t   \\
>&= \int_{-r}^r \int_{d_{\Gamma}(x) = t} \phi_i(P_{\Gamma} x) \phi_j(P_{\Gamma} x) \mathcal{J}(x) dS d t \\
>&= \int_{-r}^r \int_{d_{\Gamma}(x) = t} \phi_i(P_{\Gamma} x) \phi_j(P_{\Gamma} x) J(x) dS d t\\
>&= 2r \int_{\Gamma} \phi_i(P_{\Gamma} x) \phi_j(P_{\Gamma} x) dS = 0.
>\end{aligned}
>$$
>which implies $\{w_m\}_{m=0}^{k-1}$ forms an orthogonal set and let $U = \text{span}(w_0,\cdots, w_{k-1})$.
>
>**Step 5**: Norm estimates are similar to the previous case. For $f\in U$, we can write $f(x) = \sqrt{\mathcal{J}(x)} \tilde{f}(x)$ that $\tilde{f}\in \text{span}(h_0, \cdots, h_m)$ and
>$$
>\int_{d_{\Gamma}(x) = t} |f(x)|^2 dS = \int_{\Gamma} |\tilde{f}(x)|^2 dS.
>$$
 >which implies 
 >$$
>\int_{D_r} |f(x)|^2 dx = 2r  \int_{\Gamma} |\tilde f(x)|^2 dS.
>$$
>In a similar spirit, we have 
>$$
>\begin{aligned}
>\int_{D_r} |\nabla f|^2 dx &= \int_{-r}^r \int_{d_{\Gamma}(x) = t}|\nabla f(x)|^2 dS d t \\
>&= \int_{-r}^r \int_{d_{\Gamma}(x) = t}\left|\sqrt{\mathcal{J}(x)}\nabla \tilde{f}(P_{\Gamma} x) + \tilde{f}(x) \nabla \sqrt{\mathcal{J}(x)} \right|^2 dS d t.
>\end{aligned}
>$$
>By cancellation, $\mathcal{J}(x) = 1 + O(r^2)$, which implies that $\sqrt{\mathcal{J}(x)} = 1 + O(r^2)$ and $|\nabla \sqrt{\mathcal{J}(x)}| = O(r)$ as well. Therefore,
>$$
> \int_{D_r} |\nabla f|^2 dx =  2r\left( (1+O(r))\int_{\Gamma} |\nabla_{\Gamma} f|^2 dS + O(r) \int_{\Gamma} |f|^2 dS\right).
>$$
>
>**Step 6**: We will now use the max-min principle 
>$$
>\begin{aligned}
>\mu_k &\ge \min_{f\in U^{\perp}-\{0\}} \frac{(1+O(r))\int_{\Gamma} |\nabla_{\Gamma} f(x)|^2 dS + O(r) \int_{\Gamma} |f(x)|^2 dS }{\int_{\Gamma} |f(x)|^2 dS}
>\end{aligned}
>$$
>For $k\ge 1$, since $\phi_0$ is a constant function, we have $\int_{\Gamma} f(x) dS = 0$, then by the Poincaré inequality, there exists a constant $C ' > 0$ that 
>$$
>\int_{\Gamma} |\nabla_{\Gamma} f|^2 dS \ge C' \int_{\Gamma} |f|^2 dS.
>$$
>Thus we have 
>$$
>\begin{aligned}
>\mu_k &\ge \min_{f\in U^{\perp} - \{0\}} \frac{(1+O(r))\int_{\Gamma} |\nabla_{\Gamma} f(x)|^2 dS + O(r) \int_{\Gamma} |\nabla_{\Gamma} f|^2 dS }{\int_{\Gamma} |f(x)|^2 dS} \\&= (1 + O(r)) \lambda_k.
>\end{aligned}
>$$


## Notes
- 
## Links
- 
---
date: 2022-10-31
tags:
  - math-NA
  - math-CA
  - math-AP
description: "false"
---
>[!info] 
>This note is not intended to be a literature review of any kind nor an original research piece, it is just for fun.

## 🏷️Introduction
The ReLU (rectified linear unit) refers to the following operation 
$$
\operatorname{ReLU}(x) = \max(0, x).
$$
Let us denote this function by $\sigma$ for short. Trivially, we find that
-  $\sigma''(x) = \delta(x)$ which makes $\sigma$ a certain Green's function (w.r.t some boundary conditions) for one dimensional Laplacian. 
- $\sigma(c x) = c\sigma(x)$ for any positive real number $c$. 

In higher dimensions, the ReLU function is often used with a *linear layer*:  
$$
y = \sigma(w\cdot x - b),
$$
where the vector/matrix $w$ is the **weights**, and the scalar/vector $b$ is the **bias**. The commutativity with scalar multiplication makes it possible to consider only normalized weights or normalized input $x$.

>[!info] Definition 
>Two layer ReLU network is defined by 
>$$
>f(x) = \int_{V} h(w, b) \sigma(w\cdot x - b) d\mu(w, b),
>$$ 
>where $\mu$ is the usual measure on the joint space $V = \mathbb{S}^{n-1}\times \mathbb{R}$.
### ☘️Radon transform
For some input $x\in\mathbb{R}^n$, if we let $w\in \mathbb{S}^{n-1}$, then 
$$
\nabla \sigma(w\cdot x - b) = w H(w\cdot x - b),
$$
where $H$ is the Heaviside function and $\Delta \sigma(w\cdot x - b) = \nabla \cdot \nabla  \sigma(w\cdot x - b) = w\cdot w \delta(w\cdot x - b) = \delta(w\cdot x - b)$. Therefore, (at least formally or in weak sense)

$$
\Delta f(x) = \int_V h(w, b) \delta(w\cdot x - b) d\mu(w, b) = \int_{\mathbb{S}^{n-1}} h(w, w\cdot x) d\mu(w) = \mathcal{R}^{\ast} h,
$$

where $\mathcal{R}^{\ast}$ is the adjoint Radon transform and $h$ is a distribution in the dual space. The intertwining property and the inversion formula are well-known.

>[!important]  Intertwining Property
>$$
>\mathcal{R}\Delta f = \partial_b^2 \mathcal{R} f,\quad \mathcal{R}^{\ast} \partial_b^2 g = \Delta \mathcal{R}^{\ast} g.
>$$

>[!important] Helgason's Inversion Formula
>In **Fourier sense**, the inversion formula holds for $f\in C^{\infty}(\mathbb{R}^n)$ with decay $|f(x)| = O(|x|^{-N})$ for some $N > n$:
> $$
> (-\Delta)^{\frac{n-1}{2}}\mathcal{R}^{\ast}\mathcal{R} f = c_n f 
> $$

When appropriate, we can write $f(x) = \Delta^{-1}\mathcal{R}^{\ast} h$ in Fourier sense, where $\Delta^{-1}$ is a Fourier multiplier, and the singular values of the operator $\Delta^{-1}\mathcal{R}^{\ast}$ is essential in terms of $L^2$ optimization.

>[!note] Observation 
>In Fourier sense 
>$$
>\Delta^{-1}\mathcal{R}^{\ast}\mathcal{R}\Delta^{-1}= \frac{1}{c_n}(-\Delta)^{-\frac{n+3}{2}}.
>$$

By Weyl's law, it implies that the singular values of the operator $\Delta^{-1}\mathcal{R}^{\ast}$ will be decaying like $\sigma_k = \Theta(k^{-(n+3)/n})$.  It explains the low-pass filtration property of two-layer ReLU network.

## 🔭Spectral perspective
There are two common (easy yet boring) configurations under the scope of spectral perspectives.

### 🧩Neural-Tangent-Kernel (**NTK**)
The NTK configuration assumes sufficiently wide network, which makes the training behavior degenerated to a linear ODE (under gradient flow).  
  
$$
\frac{d\mathcal{R}^{\ast}h}{dt} = -(-\Delta)^{-\frac{n+3}{2}} \mathcal{R}^{\ast} h, 
$$

At a first sight, we find this evolution equation will be sustaining the initial “noises” for a long time. It also infers that a highly sophisticated initialization (that contains high frequencies) could be toxic to the training process if those are not desired.

### 🧩Random Feature (**RF**)
The RF configuration can be viewed as a discrete version of NTK, but the width of network does not have to be wide. The discrepancy between the eigenvalues in continuous and discrete cases can be studied through trivial tools like Weyl's inequality or slightly more complex ways. It is not the focus of this post, we will leave this topic to a later post, see [[on eigenvalue estimate for sample matrix]].
## 💡Training dynamics
A central topic around neural networks is the quantification of generalization (statistical, approximation, training) error. Mathematically, the only challenging term is to bound the training error, which demands a comprehensive exploration of the training dynamics.

### 🌵 Preliminaries
We consider a generic formulation in one dimension:
$$
f(x, t) = \sum_{i=1}^n a_i(t) \sigma(x - b_i(t))
$$
The biases $b_i(0)$ are initialized on $[-1, 1]$ uniformly (or equispaced), the weight's initialization will be discussed later.  Suppose the target function is denoted by $g$, and we naively consider the gradient flow.





we introduce the auxiliary function $w(b, t)$ that 
$$
\partial^2_b w(b, t) = f(b, t) - g(b). 
$$
Then, taking account of the ReLU function, it is quite easy to derive: 

>[!info] Observation
>$$
>\partial_b^4 w(b, t) = \sum_{k=1}^{\infty} \Theta_k(t) \phi_k(b)
>$$
>where $\{ \phi_k \}_{k\ge 1}$  are the eigenfunctions of the following problem:
>$$
>\phi_k^{(4)} = \lambda_k \phi_k,\qquad \phi_k(1) = \phi_k'(1) = \phi_k''(-1) = \phi_k'''(-1) = 0.
>$$
>

### 

## 💬 Further discussion

### 🌊 Initialization

## Notes
- 
## Links
- [[on eigenvalue estimate for sample matrix]]
- https://arxiv.org/pdf/2306.17301
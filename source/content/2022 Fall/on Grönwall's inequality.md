---
date: 2022-09-26
tags:
  - math-AP
  - math-CA
comments: "true"
---

## 🏷️Introduction
We start with a simple application of Grönwall's inequality.

> [!important]  Grönwall's inequality
> If the following relation holds
> $$
> 0\le f(x) \le C \int_0^x f(s) ds,\quad x\in [0, A],
> $$
>then $f(x) = 0$. 

The traditional way (of course a nice one) is letting 

$$
h(x) = e^{-C x} \int_0^x f(s) ds,
$$

and utilize the relation

$$
h'(x) = e^{-C x} \left(f(x) - C \int_0^x f(s) ds\right) \ge 0.
$$

Here, we attempt with an alternative way.  We define the integral operator $\mathcal{A}: L^{\infty}_{+}[0, A]\mapsto L^{\infty}_{+}[0, A]$ by the following:

$$
\mathcal{A} f:= C\int_0^x f(s) ds.
$$

Then $\mathcal{A}$ is a positive and compact operator (why?).  According to the Krein-Rutman theorem[^1], if its spectral radius $r(\mathcal{A})$ is a positive eigenvalue, and we must have the corresponding eigenfunction $\phi(x) > 0$ strictly positive. However, the definition of $\mathcal{A}$ implies that $\mathcal{A}\phi (0) = 0$, which gives a contradiction. Therefore, the spectral radius $r(\mathcal{A}) = 0$. 

Observe that $0\le f(x) \le \mathcal{A} f(x)$ implies $0\le f(x) \le \mathcal{A}^n f(x)$ (why?), the Gelfand's formula implies $\|\mathcal{A}^k\|_{op}\to 0$ as $k\to\infty$, hence $f(x) = 0$ by taking $n\to \infty$.

---

## 📝Extension
 If there is another operator $\mathcal{B}$ that commutes with $\mathcal A$, then the spectral radius $r(\mathcal{A} + \mathcal{B})$ can be estimated. We consider the abstract problem as follows.
 
>[!note] Extension of Grönwall's inequality
>Let  $\mathcal{B}$ be a linear positive operator with $r(B) < 1$ that commutes with $\mathcal{A}$, and  
>$$
>0\le f(x) \le \mathcal{A} f + \mathcal{B} f,
>$$
> then $f(x) = 0$.

The commutativity implies an estimate $r(\mathcal A + \mathcal{B}) \le r(\mathcal{A}) + r(\mathcal{B}) < 1$ (why?). Then the same argument holds since $(\mathcal{A} + \mathcal{B})^k\to 0$ as $k\to \infty$.

This conclusion seems somewhat trivial.  Let us consider an immediate application in transport equation. 

### 📖Background of transport equation
The transport equation describes the dynamics of radiative particles interacting with the environment (absorption, scattering, etc.). For instance, supposing the medium is homogeneous, the governing equation can be written in the following form:

$$
\begin{aligned}
v\cdot \nabla u(x, v) + \sigma_a u &= \sigma_s (\mathcal{K} u - u)\quad\text{ in } D\times \mathbb{S}^{d-1},\\
u|_{\Gamma_{-}} &= h(x, v),
\end{aligned}
$$

where $\mathcal{K}$ is the scattering operator, which represents the probability of scatter events that change direction $v'$ to the direction $v$.  The function $h(x, v)$ is the source defined on the incoming boundary set:

$$
\Gamma_{-} = \left\{(x, v)\in\partial D\times \mathbb{S}^{d-1}\mid v\cdot n(x) < 0 \right\}. 
$$

### 🔦Cone-beam source

The cone-beam source function means $h(x, v)$ is quite focusing. The precise definition is the following.

>[!info]  Cone-beam source
>If $h(x, v)$ satisfies that 
> - $h$ is non-negative;
> - There exists a set $V\subset \mathbb{S}^{d-1}$ that $\operatorname{supp} h\subset \partial D \times V\cap \Gamma_{-}$.
> 
> Then $h$ is called a *cone-beam source*. 

Intuitively, this means the source is one-way dominated (like a laser) and only supported on a certain subset of $\Gamma_{-}$. In a special case that $\sigma_s = 0$, we find the solution can be solved directly. 

$$
u(x, v) = h(x - \tau_{-}(x, v)v, v) E(x, x - \tau_{-}(x, v)v), \quad E(x, x - sv) = \exp\left( - \int_0^s \sigma_a(x - tv) dt\right),
$$

where $\tau_{-}(x, v)$ denotes the distance from $x$ to the boundary following $-v$ direction.

### 〰️Nonlinearity

In a practical scenario, $\sigma_a$ may depend on the solution's flux (e.g., multi-photon absorption), therefore we obtain a nonlinear equation

$$
u(x, v) = h(x - \tau_{-}(x, v) v, v) \exp\left( - \int_0^{\tau_{-}(x, v)} \sigma_a(x - tv, \langle u \rangle ) dt\right), \quad \langle u \rangle = \int_{\mathbb{S}^{d-1}} u(x, v) dv,
$$
where $dv$ represents the usual probability measure on the sphere. Here, we need some continuity assumption. 

>[!info] Assumption on Lipschitz continuity 
>$$
>\newcommand{\aver}[1]{\langle #1 \rangle}
>|\sigma_a(x, \aver{u}) - \sigma_a(x, \aver{w})| \le L |\aver{u}(x) - \aver{w}(x)|
>$$


Let us first assume the existence of the solution and focus on the uniqueness. If there exists a solution $w$ different from $u$, then we have:

$$
u - w = h(x-\tau_{-}(x, v)v, v) \left[ \exp\left(-\int_0^{\tau_{-}(x,v)} \sigma_a(x-tv, \langle u \rangle )dt\right)-  \exp\left(-\int_0^{\tau_{-}(x,v)} \sigma_a(x-tv, \langle w \rangle )dt\right)\right].
$$

>[!important]  Lemma 
> If $a, b \ge c \ge 0$, then $|e^{-a} - e^{-b}| \le e^{-c} |a - b|$.

Let $f:= \langle u - w\rangle$, using this simple lemma, and integrate over $\mathbb{S}^{d-1}$, there exists a constant $C > 0$ that 

$$
|f(x)| \le \overline{h}  \int_{V} \int_0^{\tau_{-}(x,v)} |\sigma_a(x - tv, \langle u \rangle) - \sigma_a(x - tv, \langle w \rangle)| dt dv \le C   \int_{V} \int_0^{\tau_{-}(x,v)} |f(x-tv)| dt dv,
$$

where $\overline{h} = \sup_{\Gamma_{-}} h$ and $C$ is a constant.  This inequality is just an analog of the previous Grönwall's inequality, which has zero spectral radius. Thus, we must have $f(x) = 0$, which proves the uniqueness. 

>[!note] Remark
>The general uniqueness can be proved in a different flavor, but it requires slightly more restrictive dependence of $\sigma_a$ on $\langle {u} \rangle$. For scatter-free medium plus a cone-beam source, it only needs Lipschitz continuity.

### 🌀Isotropic Scattering

Once the scattering is present, the uniqueness is slightly more challenging (*there is an alternative way to prove this*), assume that $\sigma_s$ is a positive constant, then we can represent the solution by (let $\sigma_t := \sigma_a + \sigma_s$)

$$
\begin{aligned}
u(x, v) = &\,h(x - \tau_{-}(x, v) v, v) \exp\left( - \int_0^{\tau_{-}(x, v)} \sigma_t(x - tv, \langle u \rangle ) dt\right) \\&+ \int_0^{\tau_{-}(x, v)} \exp\left( - \int_0^{s} \sigma_t(x - tv, \langle u \rangle ) dt\right) \sigma_s \langle u \rangle(x-sv) ds.
\end{aligned}
$$
Similar to the previous derivation, we let $f: = \langle u - w\rangle$, then integrate the above equation over the whole $\mathbb{S}^{d-1}$, it shows (using the lemma, polar coordinate transformation, maximum principle)

$$
\begin{aligned}
|f(x)| &\le C   \int_{V} \int_0^{\tau_{-}(x,v)} |f(x-tv)| dt dv + \frac{1}{\nu_{d-1}}\int_{D} \frac{e^{-\sigma_s|x-y|}}{|x - y|^{d-1}} \sigma_s  |f (y)| dy \\&\qquad+ \int_{\mathbb{S}^{d-1}} \int_0^{\tau_{-}(x, v)} \int_0^s e^{-s \sigma_s}L|f(x - tv)| \sigma_s \langle u \rangle(x-sv) dt ds dv  \\
&\le C   \int_{V} \int_0^{\tau_{-}(x,v)} |f(x-tv)| dt dv + \frac{1 + L\ell \overline{h}}{\nu_{d-1}}\int_{D} \frac{e^{-\sigma_s|x-y|}}{|x - y|^{d-1}} \sigma_s  |f (y)| dy,
\end{aligned}
$$

where $\ell = \operatorname{diam}(D)$. We make the following observation. 

>[!important]  Commutativity Lemma
> Let $\mathcal{A}$ and $\mathcal{S}$ be $L^2(D)\mapsto L^2(D)$ operators, 
> $$
> \mathcal{A} f:= \int_{V} \int_0^{\tau_{-}(x,v)} |f(x-tv)| dt dv,\quad S f :=\displaystyle\int_{D} \frac{e^{-\sigma_s |x - y|}}{|x - y|^{d-1}} f(y) dy.
> $$
> Then $\mathcal{A}$ commutes with $\mathcal{S}$.

A quick proof for this property. Let $f$ be extended to $\mathbb{R}^d$ with zero outside $D$, then we can write 
$$
S \mathcal{A} f = \int_{\mathbb{R}^d} \int_{V}\int_0^{\infty} \frac{e^{-\sigma_s |x - y|}}{|x - y|^{d-1}} f(y - sv) ds dv dy,
$$
and we can derive $\mathcal{A}\mathcal{S}$ similarly:

$$
\mathcal{A} S f = \int_{V}\int_0^{\infty} \int_{\mathbb{R}^d} \frac{e^{-\sigma_s|x-sv- y|}}{|x-sv-y|^{d-1}} f(y) dy ds dv = \int_{V} \int_0^{\infty} \int_{\mathbb{R}^d} \frac{e^{-\sigma_s|x-sv - (y'-sv)|}}{|x - y'|^{d-1}} f(y'-sv) dy' ds dv.
$$

That implies the following relation.

$$
|f(x)| \le C \mathcal{A} |f| + \frac{(1 + L\ell \overline{h})}{\nu_{d-1}} \sigma_s \mathcal{S} |f|.
$$

Then we have the concluding theorem by noticing that $\|\mathcal{S}\|_{op} \le 1 - e^{-\sigma_s \ell}$ (why?).

>[!important] Uniqueness Theorem
>If $(1 + L\ell \overline{h}) (1 - e^{-\sigma_s \ell}) < 1$, then the cone-beam source permits a unique solution (if exists).

## 📔Notes
- This uniqueness result simply serves as an exercise utilizing the Grönwall's inequality. This result is only feasible for weak scattering medium. 
- The commutativity is necessary to estimate the spectral radius, a slightly more general condition is mentioned in[^2].

 
[^1]: https://en.wikipedia.org/wiki/Krein%E2%80%93Rutman_theorem
[^2]:Zima, M. "A theorem on the spectral radius of the sum of two operators and its application." _Bulletin of the Australian Mathematical Society_ 48.3 (1993): 427-434.
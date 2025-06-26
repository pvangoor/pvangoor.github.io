---
layout: post
title:  "Example of the Computation of EqF Matrices"
date:   2025-06-26
categories: Papers
---

{% include math.html %}

## Introduction

This post is inspired by a PhD student who emailed me for help in deriving the $$ C $$ and $$ C^\star $$ matrices in the Equivariant Filter equations.
The Equivariant Filter (EqF) is an approach to state estimation of systems with Lie group symmetries (see the paper here: <https://arxiv.org/abs/2010.14666>).
Such systems are very common in robotics and aerospace, particularly due to the need to consider 3D rotations.
In this post, I will explain in detail the example presented also in the [paper](https://arxiv.org/abs/2010.14666), which is the problem of estimating a single bearing.
The main purpose is to expand some of the derivations from the original paper, and to provide an example of how to do practical computations with manifolds and Lie groups.

## Problem Description and Set-up

Before we can apply the EqF methodology, we need to understand the problem we are studying.
We consider a robot (e.g. a quadrotor) equipped with a gyroscope and a magnetometer.
The gyroscope measures the angular velocity $$ \Omega \in \mathbb{R}^3 $$ of the robot and the magnetometer measures the direction of the Earth's magnetic field $$ \eta \in S^2 $$.
Both measurements are taken in the body-fixed frame of the robot.
The kinematics of the magnetic field direction can then be expressed as

$$\begin{aligned}
\dot{\eta} = -\Omega \times \eta = -\Omega^\times \eta,
\end{aligned}$$

where $$ \Omega^\times \in \mathbb{R}^{3\times 3} $$ is the skew-symmetric matrix defined by

$$\begin{aligned}
    \Omega^\times :=
    \begin{pmatrix}
        0 & -\Omega_3 & \Omega_2 \\
        \Omega_3 & 0 & -\Omega_1 \\
        -\Omega_2 & \Omega_1 & 0
    \end{pmatrix}.
\end{aligned}$$

The measurement function is simply $$ y = h(\eta) = c_m\eta $$, where $$ c_m > 0 $$ is the magnetic field strength.

With this set-up out of the way, we can start to apply the EqF methodology.
We will follow the same steps as in the [paper](https://arxiv.org/abs/2010.14666), but I will give a bit more detail at each step.

## EqF Design Procedure

### State Space Symmetry

To design an EqF, the first and most fundamental ingredient is a Lie group that acts transitively on the state space of the system we are studying.
In this case, the state space is the sphere $$ S^2 $$, and a natural choice for the Lie group is the set of 3D rotations, $$ \mathbf{SO}(3) $$.
This is a matrix Lie group and is defined by

$$\begin{aligned}
    \mathbf{SO}(3) = \left\{
        R \in \mathbb{R}^{3\times 3}
        \; \middle| \;
        R^\top R = I_3, \; \det(R) = 1
    \right\}.
\end{aligned}$$

This group has a right-handed group action on $$ S^2 $$ defined by

$$\begin{aligned}
    \phi : \mathbf{SO}(3) \times S^2 \to S^2, && \phi(R, \eta) := R^\top \eta.
\end{aligned}$$

To verify that this is a group action, we just need to check that the **identity** and **compatibility** properties are satisfied:

$$\begin{gathered}
    \phi(I, \eta) = I^\top \eta = I \eta = \eta, \\
    \phi(R_2, \phi(R_1, \eta)) = \phi(R_2, R_1^\top \eta) = R_2^\top R_1^\top \eta = (R_1 R_2)^\top \eta = \phi(R_1 R_2, \eta).
\end{gathered}$$

In other words, the group action applied with the identity matrix does nothing, and the group action applied twice with different group elements is the same as the group action applied once with the product of those elements.
A group action is called transitive if, for any $$ \eta_1, \eta_2 \in S^2 $$, there exists a matrix $$ R \in \mathbf{SO}(3) $$ such that $$ \phi(R, \eta_1) = \eta_2 $$.
This is certainly the case here, although the proof is a little bit more detailed then I would like to include in this post.

### Equivariant Lift

The lift of the system is a map from the inputs and state of the system to the Lie group we have chosen.
It enable the trajectories of the system to be replicated on the Lie group.
The lift is a map $$ \Lambda : S^2 \times \mathbb{R}^3 \to \mathfrak{so}(3) $$.
That is, it is a map from the state space and the input space to the Lie algebra of our chosen symmetry group.
To ensure that trajectories generated on the group by the lift will match trajectories on the original state space, we need to verify the **lift condition**:

$$\begin{aligned}
    \mathrm{D}_R|_I \phi(R, \eta) [\Lambda(\eta, \Omega)] = f_\Omega(\eta) = - \Omega^\times \eta.
\end{aligned}$$

To find a solution to this, we evaluate the left-hand side of the lift condition to

$$\begin{aligned}
    \mathrm{D}_R|_I \phi(R, \eta) [\Lambda(\eta, \Omega)]
    &= \left. \frac{\mathrm{d}}{\mathrm{d}s} \right|_{s=0}  \phi(\exp(s \Lambda(\eta, \Omega)), \eta) \\
    &= \left. \frac{\mathrm{d}}{\mathrm{d}s} \right|_{s=0}  \exp(s \Lambda(\eta, \Omega))^\top \eta \\
    &= \Lambda(\eta, \Omega)^\top \eta \\
    &= - \Lambda(\eta, \Omega) \eta.
\end{aligned}$$

The last line is due to the fact that $$ \Lambda(\eta, \Omega) \in \mathfrak{so}(3) $$.
Now the lift condition is simplified to

$$\begin{aligned}
    - \Lambda(\eta, \Omega) \eta = -\Omega^\times \eta.
\end{aligned}$$

The general solution to this is given by

$$\begin{aligned}
    \Lambda(\eta, \Omega) = \Omega^\times + \alpha(\eta, \Omega) \eta,
\end{aligned}$$

where $$ \alpha(\eta, \Omega) \in \mathbb{R} $$.
For simplicity, we will choose $$ \alpha \equiv 0 $$, so that the lift becomes

$$\begin{aligned}
    \Lambda(\eta, \Omega) = \Omega^\times,
\end{aligned}$$

for all $$ \eta \in S^2 $$ and $$ \Omega \in \mathbb{R}^3 $$.
It is worth noting that this is quite a special case.
It is not always possible to find a lift independent of the state $$ \eta $$, but if it is then this is usually desirable since it greatly simplifies some of the later computations.

### Output Equivariance

Sometimes the measurement function $$ h $$ associated with a system exhibits equivariance with respect to the action $$ \phi $$ on the state space.
To find out whether this is the case, we can evaluate $$ h(\phi(R, \eta)) $$ and see if it is possible to express the result in terms of $$ R $$ and $$ h(\eta) $$:

$$\begin{aligned}
    h(\phi(R, \eta)) = h(R^\top \eta) = c_m R^\top \eta = R^\top (c_m \eta) = R^\top h(\eta).
\end{aligned}$$

So, indeed, the measurement function $$ h $$ is compatible with the group action $$ \phi $$.
Formally, this is expressed as another group action on the output space:

$$\begin{aligned}
    \rho : \mathbf{SO}(3) \times \mathbb{R}^3 \to \mathbb{R}^3, &&
    \rho(R, y) := R^\top y.
\end{aligned}$$

It is not required for this group action to be transitive, but it should also be right-handed.
Output equivariance is desirable because of the ability to use it in deriving the $$ C^\star $$ matrix, which improves filter performance.

### Origin and State Error

Implementing the EqF requires us to choose an origin on the state space $$ S^2 $$.
This choice is arbitrary, although it is generally useful to pick something easy to work with.
For this example, we choose the origin to be the unit vector $$ \mathbf{e}_1 = (1,0,0) \in S^2 $$.

Next, we need to choose a subspace of the Lie algebra $$ \mathfrak{so}(3) $$ to define normal coordinates on the manifold.
The reason this is needed is because the Lie group $$ \mathbf{SO}(3) $$ is larger (in dimension) than the state space $$ S^2 $$, and the normal coordinates are a way to choose a two dimensional subset of $$ \mathbf{SO}(3) $$ that represents the state space $$ S^2 $$ (at least near the chosen origin $$ \mathbf{e}_1 $$ ).
The subspace we choose will be labelled $$ \mathfrak{m} \subset \mathfrak{so}(3) $$, and it must satisfy $$ \mathrm{D}_R|_I \phi(R, \mathbf{e}_1)[\mathfrak{m}] = \mathrm{T}_{\mathbf{e}_1}S^2 $$.
In other words, the differential map $$ \mathrm{D}_R|_I \phi(R, \mathbf{e}_1) : \mathfrak{so}(3) \to \mathrm{T}_{\mathbf{e}_1}S^2 $$ must be full rank when constrained to $$ \mathfrak{m} $$.
For any $$ \Omega^\times \in \mathfrak{so}(3) $$, we have

$$\begin{aligned}
\mathrm{D}_R|_I \phi(R, \mathbf{e}_1)[\Omega^\times]
&= \left. \frac{\mathrm{d}}{\mathrm{d}s} \right|_{s=0}  \phi(\exp(s \Omega^\times), \mathbf{e}_1) \\
&= \left. \frac{\mathrm{d}}{\mathrm{d}s} \right|_{s=0} \exp(s \Omega^\times)^\top \mathbf{e}_1 \\
&= -\Omega^\times \mathbf{e}_1.
\end{aligned}$$

This is nonzero as long as $$ \Omega $$ is not a scalar multiple of $$ \mathbf{e}_1 $$.
Thus, to define $$ \mathfrak{m} $$ it suffices to choose a basis of two linearly independent elements $$ \Omega_1^\times, \Omega_2^\times \in \mathfrak{so}(3) $$ such that $$ \Omega_1, \Omega_2 $$ are not scalar multiples of $$ \mathbf{e}_1 $$.
A very simple choice is then to select the unit vectors $$ \Omega_1 = \mathbf{e}_2, \Omega_2 = \mathbf{e}_3 $$, so that $$ \mathfrak{m} $$ is defined by

$$\begin{aligned}
    \mathfrak{m} &= \left\{ v^\wedge \in \mathfrak{so}(3) \; \middle| \; v \in \mathbb{R}^2  \right\}, \\
    (v_1, v_2)^\wedge &:= (0, v_1, v_2)^\times.
\end{aligned}$$

Having made this choice, we define the **normal coordinates** $$ \vartheta : \mathcal{U} \subset S^2 \to \mathcal{V} \subset \mathbb{R}^2 $$ for $$ S^2 $$ about $$ \mathbf{e}_1 $$ by

$$\begin{aligned}
    \vartheta(e) &:= -\mathrm{atan2}(\vert \mathbf{e}_1 \times e \vert, \mathbf{e}_1^\top e) \begin{pmatrix} 0_{2\times 1} & I_2 \end{pmatrix} \frac{\mathbf{e}_1 \times e}{\vert \mathbf{e}_1 \times e \vert}, \\
    \vartheta^{-1}(\varepsilon^\wedge) &:= \phi(\exp(\varepsilon), \mathbf{e}_1).
\end{aligned}$$

While $$ \vartheta $$ looks complicated, $$ \vartheta^{-1} $$ is very simple in terms of the Lie group exponential and the group action $$ \phi $$.
Also, while it can be useful for analysis, the expressions for $$ \vartheta $$ and $$ \vartheta^{-1} $$ are not strictly necessary for implementation.
Only the derivatives at $$ e=\mathbf{e}_1 $$ and $$ \varepsilon = 0_{2\times 1} $$, respectively, are required.
The derivative of $$ \vartheta^{-1} $$ is computed by letting $$ \varepsilon $$ be arbitrary and computing the directional derivative

$$\begin{aligned}
    \mathrm{D} \vartheta^{-1}(0)[\varepsilon]
    &= \left. \frac{\mathrm{d}}{\mathrm{d}s} \right|_{s=0}  \vartheta^{-1}(s \varepsilon) \\
    &= \left. \frac{\mathrm{d}}{\mathrm{d}s} \right|_{s=0}  \phi(\exp(s\varepsilon^\wedge), \mathbf{e}_1) \\
    &= \left. \frac{\mathrm{d}}{\mathrm{d}s} \right|_{s=0} \exp(s\varepsilon^\wedge)^\top \mathbf{e}_1 \\
    &= -(0, \varepsilon_1, \varepsilon_2)^\times \mathbf{e}_1 \\
    &= \mathbf{e}_1^\times (0, \varepsilon_1, \varepsilon_2) \\
    &= \begin{pmatrix}
        0 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0
    \end{pmatrix} \begin{pmatrix}
        0 \\ \varepsilon_1 \\ \varepsilon_2
    \end{pmatrix} \\
    &= \begin{pmatrix}
        0 & 0 \\ 0 & -1 \\ 1 & 0
    \end{pmatrix} \begin{pmatrix}
        \varepsilon_1 \\ \varepsilon_2
    \end{pmatrix}.
\end{aligned}$$

In other words, we can express the differential $$ \mathrm{D} \vartheta^{-1}(0) $$ as the $$ 3\times 2 $$ matrix shown.
The differential $$ \mathrm{D} \vartheta(\mathbf{e}_1) $$ can be obtained as the left-inverse of $$ \mathrm{D} \vartheta^{-1}(0) $$, i.e.

$$\begin{aligned}
    \mathrm{D} \vartheta(\mathbf{e}_1) &= \begin{pmatrix}
        0 & 0 & 1 \\ 0 & -1 & 0
    \end{pmatrix},
\end{aligned}$$

which satisfies $$ \mathrm{D} \vartheta(\mathbf{e}_1) \cdot \mathrm{D} \vartheta^{-1}(0) = I_2 $$.

### EqF Matrix Computation

The EqF matrices $$ \mathring{A}_t, B_t, C_t, C^\star_t $$ can now be computed by specialising their formulas.

#### A Matrix

Beginning with $$ \mathring{A}_t $$, we use the formula (51) in the paper [[EqF]](https://arxiv.org/abs/2010.14666):

$$\begin{aligned}
    \mathring{A}_t
    = \mathrm{D}_e|_{\mathbf{e}_1} \vartheta(e)
    \cdot \mathrm{D}_\eta|_{\hat{\eta}} \phi(\hat{R}^{-1}, \eta)
    \cdot \mathrm{D}_E|_{I} \phi(E, \hat{\eta})
    \cdot \mathrm{D}_\eta|_{\hat{\eta}} \Lambda(\eta, \Omega)
    \cdot \mathrm{D}_e|_{\mathbf{e}_1} \phi(\hat{R}, e)
    \cdot \mathrm{D}_\varepsilon|_0 \vartheta^{-1}(\varepsilon).
\end{aligned}$$

This formula can be intimidating, but in our case it simplifies greatly due to the fact that the lift $$ \Lambda $$ is independent of $$ \eta $$.
This means that the fourth term in the formula, $$ \mathrm{D}_\eta|_{\hat{\eta}} \Lambda(\eta, \Omega) $$, is zero and therefore the whole matrix $$ \mathring{A}_t $$ is zero as well.

#### B Matrix

The $$ B_t $$ matrix is used in tuning the filter gains (i.e. the covariance of the process noise) and is given by formula (42) in [[EqF]](https://arxiv.org/abs/2010.14666):

$$\begin{aligned}
    B_t
    = \mathrm{D}_e|_{\mathbf{e}_1} \vartheta(e)
    \cdot \mathrm{D}_E|_{I} \phi(E, \mathbf{e}_1)
    \cdot \mathrm{Ad}_{\hat{R}}
    \cdot \mathrm{D}_\Omega|_{\Omega_m} \Lambda(\hat{\eta}, \Omega).
\end{aligned}$$

There are many ways to perform this computation.
I will demonstrate here the method using an arbitrary input vector $$ \mu $$.
Let $$ \mu \in \mathbb{R}^3 $$ and compute:

$$\begin{aligned}
    B_t \mu
    = \mathrm{D}_e|_{\mathbf{e}_1} \vartheta(e)
    \cdot \mathrm{D}_E|_{I} \phi(E, \mathbf{e}_1)
    \cdot \mathrm{Ad}_{\hat{R}}
    \cdot \mathrm{D}_\Omega|_{\Omega_m} \Lambda(\hat{\eta}, \Omega)[\mu].
\end{aligned}$$

To avoid this computation from becoming extremely long, we can work in stages starting from the right-most term.
In other words, we start by working out $$ \mathrm{D}_\Omega|_{\Omega_m} \Lambda(\hat{\eta}, \Omega)[\mu] $$ and then carry on to the next term until we reach the end:

$$\begin{aligned}
    \mathrm{D}_\Omega|_{\Omega_m} \Lambda(\hat{\eta}, \Omega)[\mu]
    &= \left. \frac{\mathrm{d}}{\mathrm{d}s} \right|_{s=0} \Lambda(\hat{\eta}, \Omega_m + s \mu) \\
    &= \left. \frac{\mathrm{d}}{\mathrm{d}s} \right|_{s=0} (\Omega_m + s \mu)^\times \\
    &= \left. \frac{\mathrm{d}}{\mathrm{d}s} \right|_{s=0} \Omega_m^\times + s \mu^\times \\
    &= \mu^\times.
\end{aligned}$$

Now we compute the formula up to the second last term:

$$\begin{aligned}
\mathrm{Ad}_{\hat{R}}
    \cdot \mathrm{D}_\Omega|_{\Omega_m} \Lambda(\hat{\eta}, \Omega)[\mu]
    &= \mathrm{Ad}_{\hat{R}}[\mu^\times] \\
    &= \hat{R} \mu^\times \hat{R}^\top \\
    &= (\hat{R} \mu)^\times.
\end{aligned}$$

We carry on like this for the next term:

$$\begin{aligned}
    \mathrm{D}_E|_{I} \phi(E, \mathbf{e}_1)
    \cdot \mathrm{Ad}_{\hat{R}}
    \cdot \mathrm{D}_\Omega|_{\Omega_m} \Lambda(\hat{\eta}, \Omega)[\mu]
    &= \mathrm{D}_E|_{I} \phi(E, \mathbf{e}_1)[(\hat{R} \mu)^\times] \\
    &= \left. \frac{\mathrm{d}}{\mathrm{d}s} \right|_{s=0} \phi(\exp(s(\hat{R} \mu)^\times), \mathbf{e}_1) \\
    &= \left. \frac{\mathrm{d}}{\mathrm{d}s} \right|_{s=0} \exp(s(\hat{R} \mu)^\times)^\top \mathbf{e}_1 \\
    &= -(\hat{R} \mu)^\times \mathbf{e}_1 \\
    &= \mathbf{e}_1^\times \hat{R} \mu.
\end{aligned}$$

Note that I could have stopped at the second last line, but I chose to rewrite the expression with $$ \mu $$ at the front. This extra step is helpful in simplifying everything at the end.
With these computations, we arrive at the final step:

$$\begin{aligned}
    B_t \mu
    &= \mathrm{D}_e|_{\mathbf{e}_1} \vartheta(e)
    \cdot \mathrm{D}_E|_{I} \phi(E, \mathbf{e}_1)
    \cdot \mathrm{Ad}_{\hat{R}}
    \cdot \mathrm{D}_\Omega|_{\Omega_m} \Lambda(\hat{\eta}, \Omega)[\mu] \\
    &= \mathrm{D}_e|_{\mathbf{e}_1} \vartheta(e)[\mathbf{e}_1^\times \hat{R} \mu] \\
    &= \begin{pmatrix} 0 & 0 & 1 \\ 0 & -1 & 0 \end{pmatrix}
    \mathbf{e}_1^\times \hat{R} \mu \\
    &= \begin{pmatrix} 0 & 0 & 1 \\ 0 & -1 & 0 \end{pmatrix}
    \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix}
    \hat{R} \mu \\
    &= \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}
    \hat{R} \mu \\
    &= \begin{pmatrix} 0_{2\times 1} & I_2 \end{pmatrix}
    \hat{R} \mu.
\end{aligned}$$

Since this all applies for an arbitrary direction $$ \mu $$, we obtain the resulting $$ B_t $$ matrix, which is

$$\begin{aligned}
    B_t &= \begin{pmatrix} 0_{2\times 1} & I_2 \end{pmatrix}\hat{R}.
\end{aligned}$$

#### C Matrix

The $$ C_t $$ matrix can be obtained in a similar fashion to the $$ B_t $$ matrix.
We first recall formula (33) from [[EqF]](https://arxiv.org/abs/2010.14666), specialised to the notation we are using for this example:

$$\begin{aligned}
    C_t
    := \mathrm{D}_{\eta} |_{\hat{\eta}} h(\eta)
    \cdot \mathrm{D}_e|_{\mathbf{e}_1} \phi(\hat{R}, e)
    \cdot \mathrm{D}_\varepsilon|_0 \vartheta^{-1}(\varepsilon).
\end{aligned}$$

Then, we can compute $$ C_t \varepsilon $$ for an arbitrary $$ \varepsilon \in \mathbb{R}^2 $$, although this time we will do it without breaking it up into parts.

$$\begin{aligned}
    C_t \varepsilon
    &= \mathrm{D}_{\eta} |_{\hat{\eta}} h(\eta)
    \cdot \mathrm{D}_e|_{\mathbf{e}_1} \phi(\hat{R}, e)
    \cdot \mathrm{D} \vartheta^{-1}(0)[\varepsilon] \\
    &= \mathrm{D}_{\eta} |_{\hat{\eta}} h(\eta)
    \cdot \mathrm{D}_e|_{\mathbf{e}_1} \phi(\hat{R}, e)
    \left[
        \begin{pmatrix} 0 & 0 \\ 0 & -1 \\ 1 & 0 \end{pmatrix} \varepsilon
    \right] \\
    &= \mathrm{D}_{\eta} |_{\hat{\eta}} h(\eta)\left[
    \left. \frac{\mathrm{d}}{\mathrm{d}s} \right|_{s=0} \phi\left( \hat{R}, \mathbf{e}_1 + s \begin{pmatrix} 0 & 0 \\ 0 & -1 \\ 1 & 0 \end{pmatrix} \varepsilon \right)
    \right]\\
    &= \mathrm{D}_{\eta} |_{\hat{\eta}} h(\eta)\left[
    \left. \frac{\mathrm{d}}{\mathrm{d}s} \right|_{s=0} \hat{R}^\top \left( \mathbf{e}_1 + s \begin{pmatrix} 0 & 0 \\ 0 & -1 \\ 1 & 0 \end{pmatrix} \varepsilon \right)
    \right] \\
    &= \mathrm{D}_{\eta} |_{\hat{\eta}} h(\eta)\left[
    \hat{R}^\top \begin{pmatrix} 0 & 0 \\ 0 & -1 \\ 1 & 0 \end{pmatrix} \varepsilon
    \right]\\
    &= \left. \frac{\mathrm{d}}{\mathrm{d}s} \right|_{s=0}  
    h\left(\hat{\eta} + s\hat{R}^\top \begin{pmatrix} 0 & 0 \\ 0 & -1 \\ 1 & 0 \end{pmatrix} \varepsilon \right) \\
    &= \left. \frac{\mathrm{d}}{\mathrm{d}s} \right|_{s=0}  
    c_m\left(\hat{\eta} + s\hat{R}^\top \begin{pmatrix} 0 & 0 \\ 0 & -1 \\ 1 & 0 \end{pmatrix} \varepsilon \right) \\
    &=
    c_m \hat{R}^\top \begin{pmatrix} 0 & 0 \\ 0 & -1 \\ 1 & 0 \end{pmatrix} \varepsilon.
\end{aligned}$$

Alternative expressions can be found by further manipulations. We have that

$$\begin{aligned}
    C_t
    &= c_m \hat{R}^\top \begin{pmatrix} 0 & 0 \\ 0 & -1 \\ 1 & 0 \end{pmatrix} \\
    &= c_m \hat{R}^\top \mathbf{e}_1^\times \begin{pmatrix} 0_{1\times 2} \\ I_2 \end{pmatrix} \\
    &= c_m \hat{R}^\top \mathbf{e}_1^\times \hat{R} \hat{R}^\top \begin{pmatrix} 0_{1\times 2} \\ I_2 \end{pmatrix} \\
    &= c_m (\hat{R}^\top \mathbf{e}_1)^\times \hat{R}^\top \begin{pmatrix} 0_{1\times 2} \\ I_2 \end{pmatrix} \\
    &= c_m \hat{\eta}^\times \hat{R}^\top \begin{pmatrix} 0_{1\times 2} \\ I_2 \end{pmatrix} \\
    &= \hat{y}^\times \hat{R}^\top \begin{pmatrix} 0_{1\times 2} \\ I_2 \end{pmatrix}.
\end{aligned}$$

Each of these expressions is equally valid, although the last one is most closely related to the $$ C_t^\star $$ matrix we will derive next.

#### C* Matrix

When a system exhibits output equivariance, we can replace the $$ C_t $$ matrix with the $$ C_t^\star $$ matrix to obtain improved performance.
The formula is given by (35) in [[EqF]](https://arxiv.org/abs/2010.14666).
For any $$ \varepsilon \in \mathbb{R}^2 $$,

$$\begin{aligned}
    C_t^\star \varepsilon
    := \frac{1}{2} \left(
        \mathrm{D}_{E} |_I \rho(E, y)
        + \mathrm{D}_{E} |_I \rho(E, \hat{y})
    \right)
    \cdot \mathrm{Ad}_{\hat{R}^\top} \varepsilon^\wedge.
\end{aligned}$$

Note that this formula relies on the output action $$ \rho $$, and also involves the measurement $$ y $$ taken from the real system.
This 'additional information' is what leads to the performance advantage from using $$ C_t^\star $$ over $$ C_t $$.

To compute it $$ C_t^\star $$, we follow similar steps as when computing the $$ B_t $$ matrix.
First,

$$\begin{aligned}
    \mathrm{Ad}_{\hat{R}^\top} \varepsilon^\wedge
    &= \mathrm{Ad}_{\hat{R}^\top} \left(
        \begin{pmatrix} 0_{1\times 2} \\ I_2 \end{pmatrix} \varepsilon
    \right)^\times \\
    &= \left(
        \hat{R}^\top \begin{pmatrix} 0_{1\times 2} \\ I_2 \end{pmatrix} \varepsilon
    \right)^\times.
\end{aligned}$$

Now consider an arbitrary $$ \bar{y} \in \mathbb{R}^3 $$ and $$ \Delta^\times \in \mathfrak{so}(3) $$ and compute

$$\begin{aligned}
    \mathrm{D}_{E} |_I \rho(E, \bar{y})[\Delta^\times]
    &= \left. \frac{\mathrm{d}}{\mathrm{d}s} \right|_{s=0} \rho(\exp(s \Delta^\times), \bar{y}) \\
    &= \left. \frac{\mathrm{d}}{\mathrm{d}s} \right|_{s=0} \exp(s \Delta^\times)^\top \bar{y} \\
    &= -\Delta^\times \bar{y} \\
    &= \bar{y}^\times \Delta.
\end{aligned}$$

Then it follows that

$$\begin{aligned}
    C_t^\star \varepsilon
    &= \frac{1}{2} \left(
        \mathrm{D}_{E} |_I \rho(E, y)
        + \mathrm{D}_{E} |_I \rho(E, \hat{y})
    \right)
    \cdot \mathrm{Ad}_{\hat{R}^\top} \varepsilon^\wedge \\
    &= \frac{1}{2} \left(
        \mathrm{D}_{E} |_I \rho(E, y)
        + \mathrm{D}_{E} |_I \rho(E, \hat{y})
    \right) \left[ \left(
        \hat{R}^\top \begin{pmatrix} 0_{1\times 2} \\ I_2 \end{pmatrix} \varepsilon
    \right)^\times \right] \\
    &= \frac{1}{2} \left(
        \mathrm{D}_{E} |_I \rho(E, y) \left[ \left(
        \hat{R}^\top \begin{pmatrix} 0_{1\times 2} \\ I_2 \end{pmatrix} \varepsilon
    \right)^\times \right]
        + \mathrm{D}_{E} |_I \rho(E, \hat{y}) \left[ \left(
        \hat{R}^\top \begin{pmatrix} 0_{1\times 2} \\ I_2 \end{pmatrix} \varepsilon
    \right)^\times \right]
    \right) \\
    &= \frac{1}{2} \left(
        y^\times
        \hat{R}^\top \begin{pmatrix} 0_{1\times 2} \\ I_2 \end{pmatrix} \varepsilon
        + \hat{y}^\times
        \hat{R}^\top \begin{pmatrix} 0_{1\times 2} \\ I_2 \end{pmatrix} \varepsilon
    \right) \\
    &= \frac{1}{2} \left(
        y^\times + \hat{y}^\times \right)
        \hat{R}^\top \begin{pmatrix} 0_{1\times 2} \\ I_2 \end{pmatrix} \varepsilon.
\end{aligned}$$

This gives us the formula for $$ C^\star_t $$ as

$$\begin{aligned}
    C_t^\star
    &= \frac{1}{2} \left(
        y^\times + \hat{y}^\times \right)
        \hat{R}^\top \begin{pmatrix} 0_{1\times 2} \\ I_2 \end{pmatrix}.
\end{aligned}$$

## Summary

This post should be read as a supplement to the original Equivariant Filter (EqF) paper [[EqF]](https://arxiv.org/abs/2010.14666).
I have tried to provide some context so that things are relatively self-contained, but to understand the motivation behind everything I derived here, I strongly suggest reading through the paper.
If there is anything unclear from my computations, however, or if you suspect a mistake, please reach out and let me know!
I know that it can be overwhelming to start using the mathematics needed for dealing with Lie groups and manifolds, so I hope this post provides some help for understanding how to use it for computations.

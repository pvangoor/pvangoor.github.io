---
layout: post
title:  "The 2D Special Euclidean Group SE(2)"
date:   2024-03-12
categories: Mathematics
---

{% include math.html %}

### Introduction

The Special Euclidean SE(n) group describes the orientation-preserving isometries of the Euclidean space $\mathbb{R}^n$, where $n \in \mathbb{N}$ is some integer.
This group can be represented using matrices, as

$$\begin{aligned}
    \mathbf{SE}(n) = \left\{
        X = \begin{pmatrix}
            R & p \\ 0_{1 \times n} & 1
        \end{pmatrix} \in \mathbb{R}^{n+1 \times n+1}
        \; \middle| \;
        R^\top R = I_n, \;
        \det(R) = 1, \;
        p \in \mathbb{R}^n
    \right\}
\end{aligned}$$

In this post, we will focus solely on the 2D case.
This is particularly relevant for ground-based robotics, where the group reflects the invariance of the robot's dynamics.
The 2D Special Euclidean group is given by

$$\begin{aligned}
    \mathbf{SE}(2) &:= \left\{
        X = \begin{pmatrix}
            R(\theta) & p \\ 0_{1 \times 2} & 1
        \end{pmatrix} \in \mathbb{R}^{3\times 3}
        \; \middle| \;
        \theta \in (\pi,\pi], \;
        p \in \mathbb{R}^2
    \right\}, \\
    R(\theta) &:=
        \begin{pmatrix}
            \cos(\theta) & - \sin(\theta) \\
            \sin(\theta) & \cos(\theta)
        \end{pmatrix}
\end{aligned}$$

The group properties are easily verified. The identity is $I_3 \in \mathbf{SE}(2)$ and the product and inverse are

$$\begin{aligned}
    X_1 X_2 &= \begin{pmatrix}
        R(\theta_1) & p_1 \\ 0_{1 \times 2} & 1
    \end{pmatrix}
    \begin{pmatrix}
        R(\theta_2) & p_2 \\ 0_{1 \times 2} & 1
    \end{pmatrix}
    = 
    \begin{pmatrix}
        R(\theta_1 + \theta_2) & p_1 + R(\theta_1) p_2 \\ 0_{1 \times 2} & 1
    \end{pmatrix}, \\
    X^{-1} &= \begin{pmatrix}
        R(\theta) & p \\ 0_{1 \times 2} & 1
    \end{pmatrix}^{-1}
    = \begin{pmatrix}
        R(-\theta) & - R(-\theta) p \\ 0_{1 \times 2} & 1
    \end{pmatrix}
\end{aligned}$$

Putting these together, we obtain the conjugation

$$\begin{aligned}
    \mathrm{Cn}_{X_1}(X_2)
    &=
    X_1 X_2 X_1^{-1} \\
    &=
    \begin{pmatrix}
        R(\theta_1) & p_1 \\ 0_{1 \times 2} & 1
    \end{pmatrix}
    \begin{pmatrix}
        R(\theta_2) & p_2 \\ 0_{1 \times 2} & 1
    \end{pmatrix}
    \begin{pmatrix}
        R(\theta_1) & p_1 \\ 0_{1 \times 2} & 1
    \end{pmatrix}^{-1} \\
    &=
    \begin{pmatrix}
        R(\theta_1 + \theta_2) & p_1 + R(\theta_1) p_2 \\ 0_{1 \times 2} & 1
    \end{pmatrix}
    \begin{pmatrix}
        R(-\theta_1) & - R(-\theta_1) p_1 \\ 0_{1 \times 2} & 1
    \end{pmatrix} \\
    &=
    \begin{pmatrix}
        R(\theta_1 + \theta_2 - \theta_1) & p_1 + R(\theta_1) p_2  - R(\theta_1 + \theta_2) R(-\theta_1) p_1 \\ 0_{1 \times 2} & 1
    \end{pmatrix} \\
    &=
    \begin{pmatrix}
        R(\theta_2) & (I_2 - R(\theta_2))p_1 + R(\theta_1) p_2  \\ 0_{1 \times 2} & 1
    \end{pmatrix}
\end{aligned}$$

### Lie algebra

The Lie algebra can be obtained by differentiating the matrix $X$ at $\theta = 0$ and $p = 0_{2\times 1}$.
We get that

$$\begin{aligned}
    \mathfrak{se}(2)
    &= \left\{
        U = \begin{pmatrix}
            \omega^\times & v \\ 0_{1 \times 2} & 0
        \end{pmatrix} \in \mathbb{R}^{3\times 3}
        \; \middle| \;
        \omega \in \mathbb{R}, \;
        v \in \mathbb{R}^2
    \right\}, \\
    \omega^\times &:=
        \begin{pmatrix}
            0 & - \omega \\
            \omega & 0
        \end{pmatrix}.
\end{aligned}$$

The notation $\omega^\times$ is a very useful one.
The operator $\cdot^\times : \mathbb{R} \to \mathbb{R}^{2\times 2}$ is linear, so $(\omega_1 + \omega_2)^\times = \omega_1^\times + \omega_2^\times$ and, in particular, $\omega^\times = \omega 1^\times$.
This is a particularly nice feature since $1^\times = R(\pi/2)$.

The Lie algebra $\mathfrak{se}(2)$ is a vector space by definition, and we can relate it to $\mathbb{R}^3$ by choosing a basis, or simply by defining a "wedge" map $\cdot^\wedge : \mathbb{R}^3 \to \mathfrak{se}(2)$.
This map is required to be an isomorphism in the vector space sense, so it must be linear and invertible.
We choose the wedge map and its inverse, the vee map, to be

$$\begin{aligned}
    \begin{pmatrix}
        \omega \\ v
    \end{pmatrix}^\wedge
    &:= \begin{pmatrix}
        \omega^\times & v \\
        0_{1\times 2} & 0
    \end{pmatrix}, &
    \begin{pmatrix}
        \omega^\times & v \\
        0_{1\times 2} & 0
    \end{pmatrix}^\vee
    &:= \begin{pmatrix}
        \omega \\ v
    \end{pmatrix},
\end{aligned}$$

where $\omega \in \mathbb{R}$ and $v \in \mathbb{R}^2$.
In other words, we define a basis of $\mathfrak{se}(2)$ by
$$\begin{aligned}
    E_1 &:= \begin{pmatrix}
        1^\times & 0_{2 \times 1} \\
        0_{1\times 2} & 0
    \end{pmatrix}, &
    E_2 &:= \begin{pmatrix}
        0_{2\times 2} & \mathbf{e}_1 \\
        0_{1\times 2} & 0
    \end{pmatrix}, &
    E_3 &:= \begin{pmatrix}
        0_{2\times 2} & \mathbf{e}_2 \\
        0_{1\times 2} & 0
    \end{pmatrix},
\end{aligned}$$
where $\mathbf{e}_1, \mathbf{e}_2 \in \mathbb{R}^2$ are the standard basis vectors.

#### Adjoint and Lie bracket

Using the wedge and vee operators, we can obtain expressions for the Adjoint operator and Lie bracket.
The simplest way is to differentiate the conjugation operation.
We have 

$$\begin{aligned}
\mathrm{Ad}_{X}(U)
&= \mathrm{D}_Z |_{I_3} \mathrm{Cn}_{X}(Z)[U]
&= \begin{pmatrix}
        \omega^\times & -\omega^\times p + R(\theta) v  \\ 0_{1 \times 2} & 0
    \end{pmatrix}.
\end{aligned}$$

We obtain a matrix expression for $\mathrm{Ad}_X$ by using the wedge and vee isomorphisms. Specifically, for any linear operator $L : \mathfrak{se}(2) \to \mathfrak{se}(2)$, we may define $L^\vee \in \mathbb{R}^{3\times 3}$ to be the matrix such that $L^\vee u = L(u^\wedge)^\vee$ for all $u \in \mathbb{R}^3$.
From this definition, we obtain the Adjoint matrix

$$\begin{aligned}
\mathrm{Ad}_{X}^\vee (U^\vee)
&= \begin{pmatrix}
        \omega^\times & -\omega^\times p + R(\theta) v  \\ 0_{1 \times 2} & 0
    \end{pmatrix}^\vee \\
&= \begin{pmatrix}
        \omega \\ -1^\times p \omega + R(\theta) v
    \end{pmatrix} \\
&= \begin{pmatrix}
    1 & 0_{1\times 2} \\ -1^\times p & R(\theta)
\end{pmatrix}
\begin{pmatrix}
    \omega \\ v
\end{pmatrix}, \\
\mathrm{Ad}_X^\vee &= \begin{pmatrix}
    1 & 0_{1\times 2} \\ -1^\times p & R(\theta)
\end{pmatrix}
\end{aligned}$$

Differentiating this matrix in terms of the variable $X$ at the identity provides the "little" adjoint matrix and the Lie bracket

$$\begin{aligned}
\mathrm{ad}_{U}^\vee&= \begin{pmatrix}
    0 & 0_{1\times 2} \\ -1^\times v & \omega^\times
\end{pmatrix}, \\
[U_1, U_2] &= \mathrm{ad}_{U_1}(U_2)
= \begin{pmatrix}
    0 \\ -\omega_2^\times v_1 + \omega_1^\times v_2
\end{pmatrix}^\wedge.
\end{aligned}$$


#### Exponential and Logarithm

The exponential is "simply" given by the matrix exponential.
However, it is nice to have formulas that do not rely on solving infinite power series, or, at least, hide these solutions in well-known elementary functions like $\sin$ and $\cos$.
Let $U \in \mathfrak{se}(2)$. Then, we have that

$$\begin{aligned}
U^2 &= \begin{pmatrix}
            \omega^\times & v \\ 0_{1 \times 2} & 0
        \end{pmatrix}^2
    = \begin{pmatrix}
            (\omega^\times)^2 & \omega^\times v \\ 0_{1 \times 2} & 0
        \end{pmatrix}
    = \begin{pmatrix}
        -\omega^2 I_2 & \omega^\times v \\ 0_{1 \times 2} & 0
    \end{pmatrix}, \\
U^3 &= \begin{pmatrix}
            \omega^\times & v \\ 0_{1 \times 2} & 0
        \end{pmatrix}^3
    = \begin{pmatrix}
        -\omega^2 \omega^\times & \omega^\times \omega^\times v \\ 0_{1 \times 2} & 0
    \end{pmatrix}
    = \begin{pmatrix}
        -\omega^2 \omega^\times & - \omega^2 v \\ 0_{1 \times 2} & 0
    \end{pmatrix}
    = -\omega^2 U.
\end{aligned}$$

This is the property that lets us simplify the exponential formula.
It follows that $U^{2k+1} = -\omega^2 U^{2k-1} = (-1)^k\omega^{2k} U$ for all $k \geq 0$.
We now solve the matrix exponential. We have that

$$\begin{aligned}
\exp(U) &= \sum_{k=0}^\infty \frac{1}{k!} U^k, \\
&=
I_3 + \sum_{k=1}^\infty \frac{1}{(2k)!} U^{2k}
+ \sum_{k=0}^\infty \frac{1}{(2k+1)!} U^{2k+1}, \\
&=
I_3 + \left(\sum_{k=1}^\infty \frac{1}{(2k)!} U^{2k-1}\right) U
+ \sum_{k=0}^\infty \frac{1}{(2k+1)!} U^{2k+1}, \\
&=
I_3 + \left(\sum_{k=1}^\infty \frac{(-1)^{k-1}}{(2k)!} \omega^{2k-2} U\right) U
+ \sum_{k=0}^\infty \frac{(-1)^{k}}{(2k+1)!} \omega^{2k} U, \\
&=
I_3 - \left(\sum_{k=1}^\infty \frac{(-1)^{k}}{(2k)!} \omega^{2k} \right) \omega^{-2}U^2
+ \left(\sum_{k=0}^\infty \frac{(-1)^{k}}{(2k+1)!} \omega^{2k+1}\right) \omega^{-1}U, \\
&=
I_3 - \left(\cos(\omega) - 1 \right) \omega^{-2}U^2
+ \sin(\omega) \omega^{-1}U, \\
&=
I_3 + \frac{\sin(\omega)}{\omega} U + \frac{1 - \cos(\omega)}{\omega^2} U^2.
\end{aligned}$$

Written in terms of the expanded matrix, we get

$$\begin{aligned}
\exp(U) &= 
I_3 + \frac{\sin(\omega)}{\omega} U + \frac{1 - \cos(\omega)}{\omega^2} U^2 \\
&= 
\begin{pmatrix} I_2 & 0_{2\times 1} \\ 0_{1\times 2} & 1 \end{pmatrix}
+ \frac{\sin(\omega)}{\omega} \begin{pmatrix} \omega^\times & v \\ 0_{1\times 2} & 0 \end{pmatrix}
+ \frac{1 - \cos(\omega)}{\omega^2}
\begin{pmatrix} -\omega^2 I_2 & \omega^\times v \\ 0_{1\times 2} & 0 \end{pmatrix} \\
&= 
\begin{pmatrix}
I_2
+ \frac{\sin(\omega)}{\omega} \omega^\times
-\omega^2 \frac{1 - \cos(\omega)}{\omega^2} I_2
&
\frac{\sin(\omega)}{\omega} v 
+ \frac{1 - \cos(\omega)}{\omega^2} \omega^\times v \\
0_{1\times 2} & 1 \end{pmatrix} \\
&= 
\begin{pmatrix}
\sin(\omega) 1^\times
+ \cos(\omega) I_2 &
\frac{1}{\omega} (\sin(\omega)I_2 + (1 - \cos(\omega))1^\times ) v \\
0_{1\times 2} & 1 \end{pmatrix} \\
&= 
\begin{pmatrix}
R(\omega) &
\frac{1}{\omega} (- \sin(\omega)1^\times + I_2 - \cos(\omega)I_2 ) 1^\times v \\
0_{1\times 2} & 1 \end{pmatrix} \\
&= 
\begin{pmatrix}
R(\omega) &
\frac{I_2 - R(\omega)}{\omega} 1^\times v \\
0_{1\times 2} & 1 \end{pmatrix} \\
\end{aligned}$$

When $\omega = 0$, the formula simplifies to

$$\begin{aligned}
\exp(U) = I_3 + U.
\end{aligned}$$

The expanded formula tells us how to take the logarithm as well.
Given a matrix $X \in \mathbf{SE}(2)$, we match the terms in $\exp(U)= X$ to obtain

$$\begin{aligned}
R(\theta) &= R(\omega), &
p &= \frac{I_2 - R(\omega)}{\omega} 1^\times v.
\end{aligned}$$

The first term is solved by $\omega = \theta + 2k \pi$ for any $k \in \mathbb{N}$, so we choose $\omega \in [-\pi, \pi)$ as the standard solution.
The second term is then given by solving

$$\begin{aligned}
p &= \frac{I_2 - R(\omega)}{\omega} 1^\times v, \\
p &= \frac{I_2 - R(\omega)}{\omega} R(\pi/2) v, \\
v &= \omega R(-\pi/2) (I_2 - R(\omega) )^{-1} p.
\end{aligned}$$

Observe that $(I_2 - R(\omega) ) (I_2 - R(-\omega) ) = 2(1-\cos(\omega))I_2$. Thus,

$$\begin{aligned}
v &= \omega R(-\pi/2) (I_2 - R(\omega) )^{-1} p \\
&= \omega R(-\pi/2) \frac{(I_2 - R(-\omega) )}{2 (1-\cos(\omega))} p \\
&= \frac{\omega}{2 (1-\cos(\omega))} (I_2 - R(-\omega)) R(-\pi/2) p \\
\end{aligned}$$

In summary,

$$\begin{aligned}
X &= \begin{pmatrix}
    R & p \\ 0_{1\times 2} & 1
\end{pmatrix}, \qquad
\log(X) = \begin{pmatrix}
    \omega^\times & v \\ 0_{1\times 2} & 0
\end{pmatrix}, \\
\omega &:= \mathrm{atan2}(R_{2,1}, R_{1,1}) = \mathrm{atan2}(\sin(\theta), \cos(\theta)) = \theta, \\
v &:= \frac{\omega}{2 (1-\cos(\omega))} (I_2 - R(-\omega)) R(-\pi/2) p
\end{aligned}$$

### Conclusion

The formulas presented in this summary are intended to be useful and practical for implementation, which is what I have done in the pylie library.
I hope you find it helpful too, and please let me know if you find any issues or mistakes, or have suggestions for improvement!
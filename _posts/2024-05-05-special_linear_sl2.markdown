---
layout: post
title:  "The 2D Special Linear Group SL(2)"
date:   2024-05-05
categories: Mathematics
---

{% include math.html %}

### Introduction

The special linear group $\mathbf{SL}(n)$ is the set of $n\times n$ matrices with determinant $1$:

$$\begin{aligned}
    \mathbf{SL}(n) = \left\{
        H \in \mathbb{R}^{n\times n}
        \; \middle| \;
        \det(H) = 1
    \right\}
\end{aligned}$$

Geometrically, these matrices represent linear transformations of $n$-dimensional space that preserve (oriented) volume.
In this post, we will focus solely on the case $n=2$.
This group, $\mathbf{SL}(2)$ thus represents the linear transformations of 2D space that preserve oriented area.
Using the definition of the determinant, the 2D Special Linear group is

$$\begin{aligned}
    \mathbf{SL}(2) &:= \left\{
        H = \begin{pmatrix}
            a & b \\ c & d
        \end{pmatrix} \in \mathbb{R}^{2\times 2}
        \; \middle| \;
        ad-bc=1
    \right\}.
\end{aligned}$$

The group properties are easily verified. The identity is $I_2 \in \mathbf{SE}(2)$ and the product and inverse are just the matrix product and inverse, which satisfy

$$\begin{aligned}
    \det(H_1 H_2) &= \det(H_1) \det(H_2) = 1, \\
    \det(H^{-1}) &= \det(H)^{-1} = 1,
\end{aligned}$$

for all $H,H_1,H_2 \in \mathbf{SL}(2)$.
One useful consequence is that the inverse can be expressed simply as

$$\begin{aligned}
    H^{-1} &= 
    \begin{pmatrix}
        a & b \\ c & d
    \end{pmatrix}^{-1}
    = \frac{1}{\det(H)}\begin{pmatrix}
        d & -b \\ -c & a
    \end{pmatrix}
    = \begin{pmatrix}
        d & -b \\ -c & a
    \end{pmatrix}
\end{aligned}$$

The conjugation can thus be written as

$$\begin{aligned}
    \mathrm{Cn}_{H_1}(H_2)
    &=
    H_1 H_2 H_1^{-1} \\
    &=
    \begin{pmatrix}
        a_1 & b_1 \\ c_1 & d_1
    \end{pmatrix}
    \begin{pmatrix}
        a_2 & b_2 \\ c_2 & d_2
    \end{pmatrix}
    \begin{pmatrix}
        a_1 & b_1 \\ c_1 & d_1
    \end{pmatrix}^{-1} \\
    &=
    \begin{pmatrix}
        a_1 a_2 + b_1 c_2 &
        a_1 b_2 + b_1 d_2 \\
        c_1 a_2 + d_1 c_2 &
        c_1 b_2 + d_1 d_2
    \end{pmatrix}
    \begin{pmatrix}
        d_1 & -b_1 \\ -c_1 & a_1
    \end{pmatrix} \\
    &=
    \begin{pmatrix}
        (a_1 a_2 + b_1 c_2)d_1 - (a_1 b_2 + b_1 d_2) c_1&
        -(a_1 a_2 + b_1 c_2)b_1 + (a_1 b_2 + b_1 d_2)a_1\\
        (c_1 a_2 + d_1 c_2)d_1 - (c_1 b_2 + d_1 d_2) c_1&
        -(c_1 a_2 + d_1 c_2)b_1 + (c_1 b_2 + d_1 d_2)a_1
    \end{pmatrix}.
\end{aligned}$$

Realistically, it is probably simpler just to use matrix operations if you even need to compute this.

### Lie algebra

The Lie algebra can be obtained by differentiating the condition $\det(H) = 1$ at the identity.
It turns out that the Lie algebra is exactly the matrices $U \in \mathbb{R}^{2\times 2}$ with trace zero.
We write

$$\begin{aligned}
    \mathfrak{sl}(2)
    &= \left\{
        U = \begin{pmatrix}
            u_1 & u_2 \\ u_3 & -u_1
        \end{pmatrix} \in \mathbb{R}^{2\times 2}
        \; \middle| \;
        u_1,u_2,u_3 \in \mathbb{R}
    \right\}.
\end{aligned}$$

This Lie algebra is a vector space just like any other Lie algebra, and we can relate it to $\mathbb{R}^3$ by choosing a basis, or equivalently by defining a "wedge" map $\cdot^\wedge : \mathbb{R}^3 \to \mathfrak{se}(2)$.
This map is required to be an isomorphism in the vector space sense, so it must be linear and invertible.
We have already suggested the wedge map in our definition of the Lie algebra, but formally,

$$\begin{aligned}
    \begin{pmatrix}
        u_1 \\ u_2 \\ u_3
    \end{pmatrix}^\wedge
    &:= \begin{pmatrix}
        u_1 & u_2 \\ u_3 & -u_1
    \end{pmatrix},
\end{aligned}$$

and the 'vee' map $\cdot^\vee : \mathfrak{sl}(2) \to \mathbb{R}^3$ is simply the inverse.
This choice defines a basis of $\mathfrak{se}(2)$ by
$$\begin{aligned}
    E_1 &:= \begin{pmatrix}
        1 & 0 \\ 0 & -1
    \end{pmatrix}, &
    E_2 &:= \begin{pmatrix}
        0 & 1 \\ 0 & 0
    \end{pmatrix}, &
    E_3 &:= \begin{pmatrix}
        0 & 0 \\ 1 & 0
    \end{pmatrix}.
\end{aligned}$$


#### Adjoint and Lie bracket

Using the wedge and vee operators, we can obtain expressions for the Adjoint operator and Lie bracket.
While the expression for the conjugation operation was a bit complicated, the derivative (which gives the Adjoint operator) is a bit simpler.

$$\begin{aligned}
\mathrm{Ad}_{H}(U)
&= \mathrm{D}_Z |_{I_3} \mathrm{Cn}_{H}(Z)[U] \\
&= \begin{pmatrix}
        (a u_1 + b u_3)d - (a u_2 + b (-u_1)) c&
        -(a u_1 + b u_3)b + (a u_2 + b (-u_1))a\\
        (c u_1 + d u_3)d - (c u_2 + d (-u_1)) c&
        -(c u_1 + d u_3)b + (c u_2 + d (-u_1))a
    \end{pmatrix} \\
&= \begin{pmatrix}
    a d u_1 + b d u_3 - a c u_2 + b c u_1&
    - a b u_1 - b^2 u_3 + a^2 u_2 - a b u_1\\
    c d u_1 + d^2 u_3 - c^2 u_2 + c d u_1&
    -b c u_1 - b d u_3 + a c u_2 - a d u_1
\end{pmatrix} \\
&= \begin{pmatrix}
    (a d + b c) u_1 - a c u_2 + b d u_3&
    - 2 a b u_1 + a^2 u_2 - b^2 u_3\\
    2 c d u_1 - c^2 u_2 + d^2 u_3&
    -(ad + b c) u_1 + a c u_2 - b d u_3
\end{pmatrix} \\
&= \begin{pmatrix}
    (2 b c + 1) u_1 - a c u_2 + b d u_3&
    - 2 a b u_1 + a^2 u_2 - b^2 u_3\\
    2 c d u_1 - c^2 u_2 + d^2 u_3&
    -(2 b c + 1) u_1 + a c u_2 - b d u_3
\end{pmatrix},
\end{aligned}$$

where the last line follow using the fact that $ad-bc = 1$, so $ad = bc+1$.
We obtain a matrix expression for $\mathrm{Ad}_X$ by using the wedge and vee isomorphisms.
From the computations above, we obtain the Adjoint matrix by extracting the coefficients of $u_1,u_2,u_3$:

$$\begin{aligned}
\mathrm{Ad}_{X}^\vee
&= \begin{pmatrix}
    2 b c + 1 & - a c & b d \\
    - 2 a b & a^2 & - b^2 \\
     2 c d & - c^2 & d^2
\end{pmatrix}
\end{aligned}$$

Differentiating this matrix in terms of the variable $H$ at the identity provides the "little" adjoint matrix (and the Lie bracket)

$$\begin{aligned}
\mathrm{ad}_{U}^\vee
&= \begin{pmatrix}
    0 & - u_3 & u_2 \\
    - 2 u_2 & 2 u_1 & 0 \\
     2 u_3 & 0 & -2 u_1
\end{pmatrix}, \\
[U, V] &= \mathrm{ad}_{U}(V)
= \begin{pmatrix}
    -u_3 v_2 + u_2 v_3 \\
    -2 u_2 v_1 + 2 u_1 v_2 \\
    2 u_3 v_1 - 2 u_1 v_3
\end{pmatrix}^\wedge.
\end{aligned}$$


#### Exponential and Logarithm

The exponential is given by the matrix exponential.
This, by definition, involves an infinite power series, but we will try to 'hide' this inside some standard functions (in this case, $\sinh$ and $\cosh$).
Let $U \in \mathfrak{se}(2)$. 
Following the steps in my previous post on the why the Lie exponential is not surjective, we obtain

$$
\begin{aligned}
    \exp(U)
    &= \cosh(\sqrt{\theta})  I_2 + \frac{\sinh(\sqrt{\theta})}{\sqrt{\theta}} U,\\
    \theta &= u_1^2 + u_2 u_3.
\end{aligned}
$$

There are two important things to note in this formula.
First, the fraction $\frac{\sinh(\sqrt{\theta})}{\sqrt{\theta}}$ must be understood as a power series! Formally, we should define

$$
\mathrm{sinhc}(x) := \begin{cases}
    \frac{\sinh(x)}{x} & \text{if } x \neq 0 \\
    1 & \text{if } x = 0
\end{cases}
$$

and then write $\exp(U) = \cosh(\sqrt{\theta}) I_2 + \mathrm{sinhc}(\sqrt{\theta}) U$.
The second tricky part of this formula, is that the square root of $\theta$ may not be real!
That is to say, the value of $\theta = u_1^2 + u_2 u_3$ inside the square root may, in fact, be negative, meaning that $\sqrt{\theta}$ is an imaginary number.
One way to deal with this is to simply choose one of the imaginary square roots, and apply $\cosh$ and $\sinh$ to the imaginary number.
This is okay, but may be a little unsatisfying or cumbersome to implement.
Fortunately, there is an alternative using the fact that
$$\begin{aligned}
\sinh(x) &= -i\sin(ix), &
\cosh(x) &= \cos(ix)
\end{aligned}$$
for all $x \in \mathbb{R}$.
Suppose that $\theta < 0$. Then,

$$
\begin{aligned}
    \frac{\sinh(\sqrt{\theta})}{\sqrt{\theta}}
    &= \frac{-i\sin(i\sqrt{\theta})}{\sqrt{\theta}}
    = \frac{-i\sin(i^2\sqrt{-\theta})}{i\sqrt{-\theta}}
    % = \frac{-\sin(-\sqrt{-\theta})}{\sqrt{-\theta}}
    = \frac{\sin(\sqrt{-\theta})}{\sqrt{-\theta}}, \\
    \cosh(\sqrt{\theta})
    &= \cos(i \sqrt{\theta})
    = \cos(\sqrt{-\theta})
\end{aligned}
$$

This leads to the following final expression for the exponential.
The exponential of $U$ is given by

$$\begin{aligned}
\exp(U) &= \begin{cases}
    \cosh(\sqrt{\theta}) I_2 + \frac{\sinh(\sqrt{\theta})}{\sqrt{\theta}} U & \text{if } \theta > 0 \\
    \cos(\sqrt{-\theta}) I_2 + \frac{\sin(\sqrt{-\theta})}{\sqrt{-\theta}}U & \text{if } \theta < 0 \\
    I_2 + U & \text{if } \theta = 0
\end{cases}\\
\text{where } \theta &:= u_1^2 + u_2 u_3.
\end{aligned}$$

Note that we got rid of the $\mathrm{sinhc}$ by specifying the third case.

Reversing this formula tells us how to find the logarithm as well.
Consider a matrix $H = \exp(U) \in \mathbf{SL}(2)$.
From the formula for the exponential, and the fact that $\mathrm{trace}(U)=0$, we find that

$$
\mathrm{trace}(H) = \begin{cases}
    2\cosh(\sqrt{\theta}) & \text{if } \theta > 0 \\
    2\cos(\sqrt{-\theta}) & \text{if } \theta < 0 \\
    2 & \text{if } \theta = 0
\end{cases}
$$

This makes it easy to distinguish which case we are dealing with, since $\cosh(x) > 1$ for all $x \neq 0$ and $\cos(x) < 1$ for $x \neq 2 k \pi$.
Let $\alpha = \frac{1}{2} \mathrm{trace}(H). Then

$$
\theta = \begin{cases}
    \cosh^{-1}(\alpha)^2 & \text{if } \alpha \geq 1 \\
    -\cos^{-1}(\alpha)^2 & \text{if } \alpha < 1
\end{cases}
$$

Now that we have recovered $\theta$, we can recover $U$ easily.
In the case where $\theta = 0$, then $U = H - I_2$.
In the case where $\theta > 0$, then

$$
\begin{aligned}
    H &= \cosh(\sqrt{\theta}) I_2 + \frac{\sinh(\sqrt{\theta})}{\sqrt{\theta}} U, \\
    \frac{\sinh(\sqrt{\theta})}{\sqrt{\theta}} U
    &= H - \cosh(\sqrt{\theta}) I_2, \\
    U
    &= \frac{\sqrt{\theta}}{\sinh(\sqrt{\theta})} (H - \cosh(\sqrt{\theta}) I_2),
\end{aligned}
$$

and likewise, in the case that $\theta < 0$,

$$
\begin{aligned}
    U
    &= \frac{\sqrt{-\theta}}{\sin(\sqrt{-\theta})} (H - \cos(\sqrt{-\theta}) I_2),
\end{aligned}
$$

Substituting $\theta$ in terms of $\alpha$ into these equations yields the final formula for the logarithm:

$$
\begin{aligned}
    \log(H)
    &= \begin{cases}
    \frac{\cosh^{-1}(\alpha)}{\sinh(\cosh^{-1}(\alpha))} (H - \alpha I_2)
    & \text{if } \alpha > 1 \\
    \frac{\cos^{-1}(\alpha)}{\sin(\cos^{-1}(\alpha))} (H - \alpha I_2)
    & \text{if } \alpha < 1 \\
    H - \alpha I_2
    & \text{if } \alpha = 1
\end{cases}\\
\text{where } \alpha &:= u_1^2 + u_2 u_3.
\end{aligned}
$$

### Conclusion

The special linear group comes up far less in robotics than the quaternions or the special euclidean group.
However, it does have some beautiful formulas, and the exercise of working them out is never a wasted effort.
The formulas here have all been implemented in pylie, so I hope people find them helpful.
As always, please let me know if you have any suggestions for improvement!

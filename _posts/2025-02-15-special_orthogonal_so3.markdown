---
layout: post
title:  "The Special Orthogonal Group SO(3)"
date:   2025-02-15
categories: Mathematics
---

{% include math.html %}

### Introduction

The special orthogonal group  $\mathbf{SO}(3)$ is one of the most important Lie groups encountered in robotics.
It is the most natural way to represent rotations and orientations of rigid bodies in 3D.
Because of how important 3D rotations are, there are many ways to understand and approach them.
I already wrote about one way in my previous post on unit quaternions, but in this post I will focus just on space of rotation matrices itself, and its Lie algebra.
My main goal in writing this article is to provide derivations of some of the most important formulas when dealing with rotation matrices.

The special orthogonal group is defined by

$$\begin{aligned}
    \mathbf{SO}(3) = \left\{
        R \in \mathbb{R}^{3\times 3}
        \; \middle| \;
        R^\top R = I_3, \; \det(R) = 1
    \right\}.
\end{aligned}$$

The first condition $R^\top R = I_3$ is equivalent to saying that each column of $R$ must have length $1$ and be orthogonal (perpendicular) to every other column.
The second condition, $\det(R)=1$ concerns the order of the columns of $R$. It enforces a `right-handed' orientation of each rotation matrix, and it is what makes them *special* orthogonal rather than simply orthogonal matrices.

We can verify the group properties as follows.
The identity matrix clearly satisfies $I^\top I=I$ and $\det(I)=1$, so $I \in \mathbf{SO}(3)$. 
As for matrix inversion, note that the first condition $R^\top R = I_3$ means that $R^{-1} = R^\top$.
Therefore, for any $R \in \mathbf{SO}(3)$, we have that $(R^\top)^\top (R^\top) = R R^{-1} = I_3$, and that $\det(R^\top) = \det(R) = 1$.
So the group is indeed closed under inversion. 
Finally, to see that the group is closed under matrix products, if $R_1, R_2 \in \mathbf{SO}(3)$, then

$$\begin{aligned}
    (R_1 R_2)^\top (R_1 R_2)
    &= R_2^\top R_1^\top R_1 R_2
    = R_2^\top  R_2
    = I_3, \\
    \det(R_1 R_2) &= \det(R_1) \det(R_2) = 1.
\end{aligned}$$

Thus $\mathbf{SO}(3)$ is indeed a group.
What this means intuitively is that composing two or more rotations always leads to another rotation, and that any rotation can be undone by its inverse rotation.

### Lie algebra

The simplest way of obtaining the Lie algebra $\mathfrak{so}(3)$ is to differentiate the condition $R^\top R = I_3$ around $R \approx I + \Omega$.
Doing so leads to

$$\begin{aligned}
    0_{3\times 3} = R^\top R - I_3
    \approx (I + \Omega)^\top (I + \Omega) - I_3
    \approx \Omega^\top + \Omega,
\end{aligned}$$

where all second-order terms have been removed.
Differentiating the condition $\det(R) = 1$ leads only to $\mathrm{tr}(\Omega) = 0$, which is already guaranteed by the fact that $\Omega + \Omega^\top = 0$.
Hence, the Lie algebra of $\mathbf{SO}(3)$ is

$$\begin{aligned}
    \mathfrak{so}(3)
    =  \left\{
        \Omega \in \mathbb{R}^{3\times 3}
        \; \middle| \;
        \Omega^\top + \Omega = 0_{3\times 3}
    \right\}.
\end{aligned}$$

Next, we will define a basis for this Lie algebra.
The condition $\Omega^\top + \Omega = 0_{3\times 3}$ is exactly saying that $\Omega$ is a 'skew-symmetric' matrix.
Let us study this condition in terms of the coefficients of $\Omega$.
We have that

$$\begin{aligned}
\Omega + \Omega^\top
&= \begin{pmatrix}
        \Omega_{11} & \Omega_{12} & \Omega_{13} \\
        \Omega_{21} & \Omega_{22} & \Omega_{23} \\
        \Omega_{31} & \Omega_{32} & \Omega_{33}
    \end{pmatrix}
    +  \begin{pmatrix}
        \Omega_{11} & \Omega_{21} & \Omega_{31} \\
        \Omega_{12} & \Omega_{22} & \Omega_{32} \\
        \Omega_{13} & \Omega_{23} & \Omega_{33}
    \end{pmatrix} \\
&= \begin{pmatrix}
        \Omega_{11} + \Omega_{11} & \Omega_{12} + \Omega_{21} & \Omega_{13} + \Omega_{31} \\
        \Omega_{21} + \Omega_{12} & \Omega_{22} + \Omega_{22} & \Omega_{23} + \Omega_{32} \\
        \Omega_{31} + \Omega_{13} & \Omega_{32} + \Omega_{23} & \Omega_{33} + \Omega_{33}
    \end{pmatrix}
    = 0_{3\times 3}.
\end{aligned}$$

There are nine equations here, which can be reduced to

$$\begin{aligned}
    \Omega_{11} &= \Omega_{22} = \Omega_{33} = 0, \\
    \Omega_{12} &= -\Omega_{21}, \\
    \Omega_{13} &= -\Omega_{31}, \\
    \Omega_{23} &= -\Omega_{32}.
\end{aligned}$$

In other words, there are three degrees of freedom, or equivalently, the Lie algebra is a 3-dimensional vector space.
We will choose the following basis for the Lie algebra:

$$\begin{aligned}
    E_1 &= \begin{pmatrix}
    0 & 0 & 0 \\
    0 & 0 & -1 \\
    0 & 1 & 0
    \end{pmatrix}, &
    E_2 &= \begin{pmatrix}
    0 & 0 & 1 \\
    0 & 0 & 0 \\
    -1 & 0 & 0
    \end{pmatrix}, &
    E_3 &= \begin{pmatrix}
    0 & -1 & 0 \\
    1 & 0 & 0 \\
    0 & 0 & 0
    \end{pmatrix}.
\end{aligned}$$

Using these definitions, any element of the Lie algebra may be uniquely written as a vector $\omega \in \mathbb{R}^3$ by defining the 'skew map' $\cdot^\times : \mathbb{R}^3 \to \mathfrak{so}(3)$ as

$$\begin{aligned}
\omega^\times &:= \omega_1 E_1 + \omega_2 E_2 + \omega_3 E_3
= \begin{pmatrix}
    0 & -\omega_3 & \omega_2 \\
    \omega_3 & 0 & -\omega_1 \\
    -\omega_2 & \omega_1 & 0
    \end{pmatrix}.
\end{aligned}$$

We chose this particular basis and notation for a good reason, namely, that it relates the Lie algebra $\mathfrak{so}(3)$ with the classis vector cross product.
That is also why we use the notation $a^\times$ rather than the notation $a^\wedge$ used for other Lie algebras, although different authors have different conventions.
The reason for these particular basis matrices is that if we have a vector $a \in \mathbb{R}^3$, then the matrix $a^\times \in \mathfrak{so}(3)$ is the unique matrix such that $a \times b = a^\times b$ for all $b \in \mathbb{R}^3$.

#### An Important Cross Product Identity

The following identity will be vital to understanding some of the later manipulations.
Let $a,b \in \mathbb{R}^3$ be arbitrary.
Then we can compute that

$$\begin{aligned}
(a^\times b)^\times
&= \left( \begin{pmatrix}
    0 & -a_3 & a_2 \\
    a_3 & 0 & -a_1 \\
    -a_2 & a_1 & 0
    \end{pmatrix}
    \begin{pmatrix}
    b_1 \\ b_2 \\ b_3
    \end{pmatrix}
    \right)^\times \\
&= \begin{pmatrix}
    -a_3 b_2 + a_2 b_3 \\
    a_3 b_1 - a_1 b_3 \\
    -a_2 b_1 + a_1 b_2
    \end{pmatrix}^\times \\
&= \begin{pmatrix}
    0 & -(-a_2 b_1 + a_1 b_2) & (a_3 b_1 - a_1 b_3) \\
    (-a_2 b_1 + a_1 b_2) & 0 & -(-a_3 b_2 + a_2 b_3) \\
    -(a_3 b_1 - a_1 b_3) & (-a_3 b_2 + a_2 b_3) & 0
    \end{pmatrix} \\
&= \begin{pmatrix}
    b_1 a_1 - a_1 b_1 & b_1 a_2 - a_1 b_2 & b_1 a_3 - a_1 b_3 \\
    b_2 a_1 - a_2 b_1 & b_2 a_2 - a_2 b_2 & b_2 a_3 - a_2 b_3 \\
    b_3 a_1 - a_3 b_1 & b_3 a_2 - a_3 b_2 & b_3 a_3 - a_3 b_3
    \end{pmatrix} \\
&= \begin{pmatrix}
    b_1 a_1 & b_1 a_2 & b_1 a_3 \\
    b_2 a_1 & b_2 a_2 & b_2 a_3 \\
    b_3 a_1 & b_3 a_2 & b_3 a_3
    \end{pmatrix}
    - \begin{pmatrix}
    a_1 b_1 & a_1 b_2 & a_1 b_3 \\
    a_2 b_1 & a_2 b_2 & a_2 b_3 \\
    a_3 b_1 & a_3 b_2 & a_3 b_3
    \end{pmatrix} \\
&= \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix}
\begin{pmatrix} a_1 & a_2 & a_3 \end{pmatrix}
- \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix}
\begin{pmatrix} b_1 & b_2 & b_3 \end{pmatrix} \\
&= b a^\top - a b^\top.
\end{aligned}$$

This identification is extremely useful in manipulating expressions involving cross products and skew matrices.
In the next section, we will use it in deriving the adjoint matrix.


#### Adjoint and Lie bracket

To study the adjoint maps, let $R \in \mathbf{SO}(3)$ be arbitrary, and denote by $R_1,R_2,R_3 \in \R^3$ the columns of $R$.
Then for the basis matrix $E_1 = e_1^\times \in \mathfrak{so}(3)$,

$$\begin{aligned}
\mathrm{Ad}_{R}(e_1^\times)
&= R e_1^\times R^\top \\
&= \begin{pmatrix}
        R_1 & R_2 & R_3
    \end{pmatrix}
    \begin{pmatrix}
    0 & 0 & 0 \\
    0 & 0 & -1 \\
    0 & 1 & 0
    \end{pmatrix}
    R^\top \\
&= \begin{pmatrix}
        R_1 & R_2 & R_3
    \end{pmatrix}
    \begin{pmatrix}
    0_{1\times 3} \\
    -e_3^\top \\
    e_2^\top
    \end{pmatrix}
    R^\top \\
&= (- R_2 e_3^\top + R_3 e_2^\top)
    R^\top \\
&= - R_2 (R e_3)^\top  + R_3 (R e_2)^\top \\
&= - R_2 R_3^\top  + R_3 R_2^\top \\
&= (R_2 \times R_3)^\times \\
&= R_1^\times \\
&= (R e_1)^\times.
\end{aligned}$$

The fact that $R_2\times R_3 = R_1$ follows from the fact that $R_1,R_2,R_3$ are orthogonal and that $\det(R) = 1$.
For the other basis vectors, the same process leads to $\mathrm{Ad}_R(e_2^\times) = (Re_2)^\times$ and $\mathrm{Ad}_R(e_3^\times) = (Re_3)^\times$.
Therefore, for an arbitrary $\omega^\times \in \mathfrak{so}(3)$,

$$\begin{aligned}
\mathrm{Ad}_R(\omega^\times)
&= \mathrm{Ad}_R(\omega_1 e_1^\times + \omega_2 e_2^\times + \omega_3 e_3^\times) \\
&= \omega_1 \mathrm{Ad}_R(e_1^\times)
+ \omega_2 \mathrm{Ad}_R(e_2^\times)
+ \omega_3 \mathrm{Ad}_R(e_3^\times) \\
&= \omega_1 (R e_1)^\times
+ \omega_2 (R e_2)^\times
+ \omega_3 (R e_3)^\times \\
&=  (\omega_1 R e_1
+ \omega_2 R e_2
+ \omega_3 R e_3)^\times \\
&= (R \omega)^\times.
\end{aligned}$$

So, while it may be some work to get there, we end up with a very clean result: the Adjoint applied to the skew matrix of a vector is the same as rotating the vector before applying the skew operator.
Thus the matrix form of the Adjoint operator is simply

$$\begin{aligned}
\mathrm{Ad}_{R}^\vee
&= R
\end{aligned}$$

Differentiating this matrix in terms of the Lie group element $R$ at the identity is an easy way to obtain the "little" adjoint matrix and, equivalently, the Lie bracket.

$$\begin{aligned}
\mathrm{ad}_{\omega}^\vee
&= \omega^\times, \\
[\omega_1, \omega_2] &= \omega_1 \times \omega_2.
\end{aligned}$$

Lastly, this Lie bracket provides us with another useful skew operator identity, namely,

$$\begin{aligned}
(\omega_1^\times \omega_2)^\times
&= [\omega_1, \omega_2]^\times
= [\omega_1^\times, \omega_2^\times]
= \omega_1^\times \omega_2^\times - \omega_2^\times \omega_1^\times.
\end{aligned}$$


#### Exponential and Logarithm

Next are the exponential and logarithm, which also have nice forms.
The exponential formula for $\mathbf{SO}(3)$ is often referred to as the Rodrigues formula.
To derive the exponential formula, we let $\omega^\times \in \mathfrak{so}(3)$ be an arbitrary skew-symmetric matrix.
Then we notice the following important identity:

$$\begin{aligned}
(\omega^\times)^2
&= \omega^\times \omega^\times \\
&= \begin{pmatrix}
    0 & -\omega_3 & \omega_2 \\
    \omega_3 & 0 & -\omega_1 \\
    -\omega_2 & \omega_1 & 0
    \end{pmatrix}
    \begin{pmatrix}
    0 & -\omega_3 & \omega_2 \\
    \omega_3 & 0 & -\omega_1 \\
    -\omega_2 & \omega_1 & 0
    \end{pmatrix} \\
    &= \begin{pmatrix}
    -\omega_3^2 - \omega_2^2 &
    \omega_2 \omega_1 &
    \omega_3 \omega_1 \\
    \omega_1 \omega_2 &
    -\omega_3^2 - \omega_1^2 &
    \omega_3 \omega_2 \\
    \omega_1 \omega_3 &
    \omega_2 \omega_3 &
    -\omega_2^2 - \omega_1^2
    \end{pmatrix} \\
    &= \begin{pmatrix}
    \omega_1^2 &
    \omega_2 \omega_1 &
    \omega_3 \omega_1 \\
    \omega_1 \omega_2 &
    \omega_2^2  &
    \omega_3 \omega_2 \\
    \omega_1 \omega_3 &
    \omega_2 \omega_3 &
    \omega_3^2
    \end{pmatrix}
    - (\omega_1^2 + \omega_2^2 + \omega_3^2) \begin{pmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1
    \end{pmatrix} \\
    &= \omega \omega^\top - \omega^\top \omega I_3.
\end{aligned}$$

A particular consequence of this is that

$$\begin{aligned}
(\omega^\times)^3
    &= \omega^\times (\omega \omega^\top - \omega^\top \omega I_3) \\
    &= 0 - \omega^\top \omega \omega^\times \\
    &= - \vert \omega \vert^2 \omega^\times.
\end{aligned}$$

With this identity available to us, the exponential becomes relatively straightforward to compute.
Assume first that $\omega \neq 0$.
Then, from the definition of the matrix exponential, we have

$$\begin{aligned}
\exp(\omega^\times)
    &= \sum_{n=0}^\infty \frac{1}{n!} (\omega^\times)^n \\
    &= I_3
    + \sum_{n=0}^\infty \frac{1}{(2n+1)!} (\omega^\times)^{2n+1}
    + \sum_{n=1}^\infty \frac{1}{(2n)!} (\omega^\times)^{2n} \\
% ------------
    &= I_3
    + \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)!} \vert \omega \vert^{2n} \omega^\times
    + \sum_{n=1}^\infty \frac{(-1)^{n-1}}{(2n)!} \vert \omega \vert^{2n-2} (\omega^\times)^{2} \\
% ------------
    &= I_3
    + \frac{1}{\vert \omega \vert} \left(\sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)!} \vert \omega \vert^{2n+1} \right) \omega^\times
    - \frac{1}{\vert \omega \vert^2} \left( \sum_{n=1}^\infty \frac{(-1)^{n}}{(2n)!} \vert \omega \vert^{2n} \right) (\omega^\times)^{2} \\
% ------------
    &= I_3
    + \frac{1}{\vert \omega \vert} \left(\sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)!} \vert \omega \vert^{2n+1} \right) \omega^\times
    - \frac{1}{\vert \omega \vert^2} \left(-1 + \sum_{n=0}^\infty \frac{(-1)^{n}}{(2n)!} \vert \omega \vert^{2n} \right) (\omega^\times)^{2} \\
% ------------
    &= I_3
    + \frac{1}{\vert \omega \vert} \sin(\vert \omega \vert) \omega^\times
    - \frac{1}{\vert \omega \vert^2} \left(-1 + \cos(\vert \omega \vert) \right) (\omega^\times)^{2} \\
% ------------
    &= I_3
    + \frac{\sin(\vert \omega \vert)}{\vert \omega \vert} \omega^\times
    + \frac{1 - \cos(\vert \omega \vert)}{\vert \omega \vert^2} (\omega^\times)^{2}.
\end{aligned}$$

To see how the infinite sums collapsed, have a look at the [power series expansions of sine and cosine](https://en.wikipedia.org/wiki/Trigonometric_functions#Power_series_expansion).
The fractions above are well-defined since we assumed $\omega \neq 0$.
In the case that $\omega = 0$, then the exponential is simply $\exp(0^\times) = I_3$.

Computing the logarithm is a matter of inverting the exponential formula, although we need to be careful since there is not always a unique logarithm defined!
Suppose that $R = \exp(\omega^\times)$ for some $\omega \in \mathbb{R}^3$.
Then by taking the trace of both sides,

$$\begin{aligned}
\mathrm{tr}(R)
&= \mathrm{tr}(I_3
    + \frac{\sin(\vert \omega \vert)}{\vert \omega \vert} \omega^\times
    + \frac{1 - \cos(\vert \omega \vert)}{\vert \omega \vert^2} (\omega^\times)^{2}) \\
% ------------
&= \mathrm{tr}(I_3) + \frac{\sin(\vert \omega \vert)}{\vert \omega \vert} \mathrm{tr}(\omega^\times)
    + \frac{1 - \cos(\vert \omega \vert)}{\vert \omega \vert^2} \mathrm{tr}((\omega^\times)^{2}) \\
% ------------
&= 3 + 0
    + \frac{1 - \cos(\vert \omega \vert)}{\vert \omega \vert^2} \mathrm{tr}(\omega \omega^\top - \omega^\top \omega I_3) \\
% ------------
&= 3 + \frac{1 - \cos(\vert \omega \vert)}{\vert \omega \vert^2} ( \omega^\top \omega - 3 \omega^\top \omega ) \\
% ------------
&= 3 - 2 (1 - \cos(\vert \omega \vert)) \\
% ------------
&= 1 + 2 \cos(\vert \omega \vert).
\end{aligned}$$

We will assume that $\vert \omega \vert < \pi$.
Therefore, since $\cos$ is invertible over the domain $[0,\pi]$, we obtain

$$
\vert \omega \vert = \cos^{-1}\left( \frac{\mathrm{tr}(R) - 1}{2} \right)
$$

Then, the vector direction of $\omega$ can be extracted from the skew-symmetric part of $R$.
Observe that

$$\begin{aligned}
R - R^\top
    &= (I_3
    + \frac{\sin(\vert \omega \vert)}{\vert \omega \vert} \omega^\times
    + \frac{1 - \cos(\vert \omega \vert)}{\vert \omega \vert^2} (\omega^\times)^{2})
    - (I_3
    + \frac{\sin(\vert \omega \vert)}{\vert \omega \vert} \omega^\times
    + \frac{1 - \cos(\vert \omega \vert)}{\vert \omega \vert^2} (\omega^\times)^{2})^\top \\
% ------------
&= 2 \frac{\sin(\vert \omega \vert)}{\vert \omega \vert} \omega^\times.
% ------------
\end{aligned}$$

Since we already know $\vert \omega \vert$ from the trace formula, we now obtain

$$\begin{aligned}
\omega  = \frac{\vert \omega \vert}{2 \sin(\vert \omega \vert)}(R - R^\top)^\vee.
\end{aligned}$$

This formula applies when $\vert\omega\vert \in (0, \pi)$, but what about the other cases?
If $\vert\omega\vert = 0$ then it simply means that $R = I_3$ and thus $\omega = 0$ as well.
If, on the other hand, $\vert\omega\vert = \pi$, then the logarithm is not uniquely defined.
In this case, the skew-symmetric part of $R$ disappears, and we must look to the symmetric part of $R$ to find a solution.
Under the condition that $\vert \omega \vert = \pi$, we have

$$\begin{aligned}
R + R^\top
&= (I_3
    + \frac{\sin(\vert \omega \vert)}{\vert \omega \vert} \omega^\times
    + \frac{1 - \cos(\vert \omega \vert)}{\vert \omega \vert^2} (\omega^\times)^{2})
    + (I_3
    + \frac{\sin(\vert \omega \vert)}{\vert \omega \vert} \omega^\times
    + \frac{1 - \cos(\vert \omega \vert)}{\vert \omega \vert^2} (\omega^\times)^{2})^\top \\
&= 2 I_3
    + 2 \frac{1 - \cos(\vert \omega \vert)}{\vert \omega \vert^2} (\omega^\times)^{2} \\
&= 2 I_3 + \frac{4}{\vert \omega \vert^2} (\omega^\times)^{2} \\
&= 2 I_3 + \frac{4}{\vert \omega \vert^2} (\omega \omega^\top - \omega^\top \omega I_3 ) \\
&= 2 I_3 + 4 (\frac{\omega \omega^\top}{\vert \omega \vert^2} -  I_3 ) \\
&= 4 \frac{\omega \omega^\top}{\vert \omega \vert^2} - 2  I_3.
\end{aligned}$$

Multiplying both sides by $\omega$ leads to

$$\begin{aligned}
(R + R^\top) \omega
&= 4 \frac{\omega \omega^\top \omega}{\vert \omega \vert^2} -2\omega \\
(R + R^\top) \omega
&= 2 \omega.
\end{aligned}$$

In other words, $\omega$ is an eigenvector of $R + R^\top$ with eigenvalue 2, and it is not difficult to see that it is unique up to change of sign.
Therefore, if $\vert \omega \vert = \pi$, then $\omega$ is given by solving

$$\begin{aligned}
(R + R^\top - 2I_3) \omega
&= 0, & \vert \omega \vert = \pi,
\end{aligned}$$

and is unique up the choice of sign $\pm \omega$.

### Further Useful Formulas: Projections

We often use $\mathbf{SO}(3)$ and its Lie algebra in their matrix form, and it is useful to be able to understand their relationship with the ambient space of matrices in which they are typically represented.

#### Lie Algebra Projection

For the Lie algbera $\mathfrak{so}(3)$, the projection from $\mathbb{R}^{3\times 3}$ to $\mathfrak{so}(3)$ is often denoted as $\mathbb{P}_{\mathfrak{so}}(3)$, and it is defined by

$$
\mathbb{P}_{\mathfrak{so}}(3)(M)
:= \mathrm{argmin}_{\Omega \in \mathfrak{so}(3)} \vert M - \Omega \vert^2.
$$

Here, the norm is taken as the matrix (Frobenius) norm, so $\vert A \vert^2 := \mathrm{tr}(A^\top A)$.
The solution to the minimisation is unique and can be obtained by differentiation.
For any $M \in \mathbb{R}^{3\times 3}$ and $\Omega \in \mathfrak{so}(3)$, we write the cost function

$$
l(\Omega)
:= \frac{1}{2}\vert M - \Omega \vert^2.
$$

Then, differentiating this with respect to $\Omega$ in an arbitrary direction $\Delta \in \mathfrak{so}(3)$ yields

$$\begin{aligned}
\mathrm{D} l(\Omega)[\Delta]
&= \langle \Omega - M, \Delta \rangle \\
&= \langle \Omega, \Delta \rangle - \langle M, \Delta \rangle \\
&= \langle \Omega, \Delta \rangle - \frac{1}{2} \left( \langle M, \Delta \rangle + \langle M^\top, \Delta^\top \rangle \right) \\
&= \langle \Omega, \Delta \rangle - \frac{1}{2} \left( \langle M, \Delta \rangle + \langle - M^\top, \Delta \rangle \right) \\
&= \langle \Omega, \Delta \rangle - \frac{1}{2} \langle M- M^\top , \Delta \rangle \\
&= \langle \Omega - \frac{1}{2} (M - M^\top), \Delta \rangle.
\end{aligned}$$

This is zero for all $\Delta \in \mathfrak{so}(3)$ exactly when $\Omega = \frac{1}{2}(M - M^\top)$, which is also a skew symmetric matrix (as required).
Therefore, to summarise,

$$
\mathbb{P}_{\mathfrak{so}}(3)(M)
= \frac{1}{2} (M - M^\top).
$$

The projection onto the Lie group $\mathbf{SO}(3)$ is similarly defined, but less straightforward to obtain.
For any $M \in \mathbb{R}^3$,

$$
\mathbb{P}_{\mathbf{SO}}(3)(M)
:= \mathrm{argmin}_{R \in \mathbf{SO}(3)} \vert M - R \vert^2.
$$

To compute this, define $l(R) = \frac{1}{2}\vert R - M \vert^2$ and differentiate to obtain

$$\begin{aligned}
\mathrm{D}l(R)[R \Omega] 
&= \langle R - M, R \Omega \rangle \\
&= \langle I - R^\top M, \Omega \rangle \\
&= \frac{1}{2}\langle M^\top R - R^\top M, \Omega \rangle.
\end{aligned}$$

This is zero for all $\Omega \in \mathfrak{so}(3)$ if and only if $M^\top R = R^\top M$.
Next, compute the singular value decomposition, $M = U S V^\top$, where $S$ is a diagonal matrix with the singular values of $M$ in descending order.
Then the previous condition is equivalent to

$$\begin{aligned}
M^\top R &= R^\top M, \\
V S U^\top R &= R^\top U S V^\top, \\
S U^\top R V &= V^\top R^\top U S , \\
S Q &= Q^\top S,
\end{aligned}$$

where $Q = U^\top R V$.
Note that $Q$ is also an orthogonal (not necessarily special orthogonal matrix).
We will now assume that the singular values of $M$ are distinct, so the values along the diagonal of $S$ are strictly descending $s_1 > s_2 > s_3 \geq 0$.
Then, for the unit vector $e_1$,

$$\begin{aligned}
S Q e_1 &= Q^\top S e_1, \\
S (Q e_1) &= s_1 Q^\top e_1, \\
\vert S (Q e_1) \vert^2 &= s_1^2 \vert Q^\top e_1 \vert^2, \\
\sum_{i=1}^3 s_i^2 Q_{i1}^2 &= s_1^2.
\end{aligned}$$

Since $Q$ is orthogonal and the $s_i$ are descending, the sum on the left can be at most equal to $s_1^2$ and this happens exactly when $Q_{11} = \pm 1$ (meaning also that $Q_{i1} = 0$ for $i \neq 1$).
This moreover implies that $Q_{1i} = 0$ for all $i \neq 1$, and then the argument can be repeated for the second eigenvalue to obtain the result that

$$Q = \mathrm{diag}(\pm 1, \pm 1, \pm 1).$$

If $Q$ were only orthogonal, then any of the eight combinations of signs would be possible.
However, since $Q = U^\top R V$, we have $\det(Q) = \det(U^\top)\det(R) \det(V) = \det(U^\top)\det(V)$, since $\det(R) = 1$ necessarily.
Thus $Q_{33}$ is determined by the other two values and the fixed determinant.

Returning to the original problem, expanding $l$ yields

$$\begin{aligned}
l(R) &:= \vert R - M \vert^2 \\
&= \vert R - U S V^\top \vert^2 \\
&= \vert U^\top R V - S \vert^2 \\
&= \vert Q - S \vert^2 \\
&= (Q_{11} - s_1)^2 + (Q_{22} - s_1)^2 + (Q_{33} - s_3)^2
\end{aligned}$$

Since the $s_i$ are descending, it is clear that the minimiser (among the possible $Q$) is given by $Q = \mathrm{diag}(1,1,\det(U^\top) \det(V))$.
Then, finally, $R$ is recovered as $R = U Q V^\top$, or succinctly,

$$\begin{aligned}
R = U \mathrm{diag}(1,1,\det(U^\top V)) V^\top.
\end{aligned}$$

This argument relied on the assumption that the singular values $s_i$ were distinct, but a similar argument is possible when they are not.
In any case, the procedure provided here will return a matrix $R \in \mathbf{SO}(3)$ that minimises the Euclidean (Frobenius) distance to $M$, although this matrix may not actually be a unique solution to the original problem.

### Conclusion

The special orthogonal group in 3D is a beautiful and classical example of a Lie group, and it is of interest for both theoretical and practical reasons.
My view is that, if you have a problem involving 3D rotations, your first choice should be to use the group $\mathbf{SO}(3)$.
It is sometimes worth using Euler angles or unit quaternions, but without some motivation for this, I would stick to the matrix Lie group.
If you want to look at an implementation of some of the functions I have described, I suggest you to look at [pylie](https://github.com/pvangoor/pylie).
Finally, I will leave a summary of the formulas below for quick reference.

### Quick Reference

The 3D special orthogonal group and Lie algebra

$$\begin{aligned}
    \mathbf{SO}(3) &= \left\{
        R \in \mathbb{R}^{3\times 3}
        \; \middle| \;
        R^\top R = I_3, \; \det(R) = 1
    \right\}, \\
        \mathfrak{so}(3)
    &=  \left\{
        \Omega \in \mathbb{R}^{3\times 3}
        \; \middle| \;
        \Omega^\top + \Omega = 0_{3\times 3}
    \right\}.
\end{aligned}$$

The Lie algebra wedge or 'skew' map

$$\begin{aligned}
    \cdot^\times &: \mathbb{R}^3 \to \mathfrak{so}(3), \\
    \omega^\times &= \begin{pmatrix}
        \omega_1 \\ \omega_2 \\ \omega_3
    \end{pmatrix}^\times
    = \begin{pmatrix}
        0 & -\omega_3 & \omega_2 \\
        \omega_3 & 0 & -\omega_1 \\
        -\omega_2 & \omega_1 & 0
    \end{pmatrix}.
\end{aligned}$$

Cross product and skew matrix identities

$$\begin{aligned}
    (a^\times b)^\times &= b a^\top - a b^\top, \\
    \omega^\times \omega^\times &= \omega \omega^\top - \omega^\top \omega I_3
\end{aligned}$$

Adjoint matrices

$$\begin{aligned}
    \mathrm{Ad}_R^\vee &= R, \\
    \mathrm{ad}_\omega^\vee &= \omega^\times.
\end{aligned}$$

Exponential formula (for $\omega \neq 0$)

$$\begin{aligned}
    \exp(\omega) &= I_3
    + \frac{\sin(\vert \omega \vert)}{\vert \omega \vert} \omega^\times
    + \frac{1 - \cos(\vert \omega \vert)}{\vert \omega \vert^2} (\omega^\times)^{2}.
\end{aligned}$$

Logarithm formula (for $R \neq R^\top$)

$$\begin{aligned}
\log(R)  &= \frac{\theta}{2 \sin(\theta)}(R - R^\top)^\vee, &
\theta &:= \cos^{-1}\left( \frac{\mathrm{tr}(R) - 1}{2} \right).
\end{aligned}$$

Projection maps

$$\begin{aligned}
\mathbb{P}_{\mathfrak{so}(3)}(M)  &= \frac{1}{2} (M - M^\top), \\
\mathbb{P}_{\mathbf{SO}(3)}(A) &= U \mathrm{diag}(1,1,\det(U^\top V)) V^\top, &
A &= U S V^\top.
\end{aligned}$$
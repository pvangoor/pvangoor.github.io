---
layout: post
title:  "The Special Euclidean Group SE(3)"
date:   2026-01-27
categories: Mathematics
---

{% include math.html %}

### Introduction

The special Euclidean group  $$ \mathbf{SE}(3) $$ described the symmetry of rigid bodies and frames of reference.
Aside from describing their symmetry, it can also be used to represent the position and orientation of a frame in one handy matrix.
While the elements of this group can be viewed as consisting of a rotation matrix and a position vector, most people prefer to use the $$ 4\times 4$$ matrix form, sometimes called a *homogeneous matrix*.
Like my other articles on Lie groups, my goal here is to provide derivations of some of the most useful and important formulas and identities that come up for $$ \mathbf{SE}(3) $$.
That said, the previous [post on the special orthogonal group]({% post_url 2025-02-15-special_orthogonal_so3 %}) should be read before reading this one, since I will draw on a number of the results therein.

The special Euclidean group is defined by

$$\begin{aligned}
    \mathbf{SE}(3) = \left\{
        P = \begin{pmatrix}
            R & x \\ 0_{1\times 3} & 1
        \end{pmatrix} \in \mathbb{R}^{4\times 4}
        \; \middle| \;
        R \in \mathbf{SO}(3), \; x \in \mathbb{R}^3
    \right\}.
\end{aligned}$$

On first impressions, this looks as simple as just combining $$\mathbf{SO}(3)$$ with $$\mathbb{R}^3$$, but things get interesting when we look at the multiplication of two $$ \mathbf{SE}(3)$$ elements.
We will typically use the notation $$P \in \mathbf{SE}(3)$$ to refer to the whole matrix, and the notations $$R \in \mathbf{SO}(3), x \in \mathbb{R}^3$$ to refer to the rotation and translation components, respectively.
Given $$ P_1, P_2 \in \mathbf{SE}(3)$$, their product is given by

$$\begin{aligned}
    P_1 P_2 &=
        \begin{pmatrix} R_1 & x_1 \\ 0_{1\times 3} & 1 \end{pmatrix}
        \begin{pmatrix} R_2 & x_2 \\ 0_{1\times 3} & 1 \end{pmatrix}
        = \begin{pmatrix} R_1 R_2 & x_1 + R_1 x_2 \\ 0_{1\times 3} & 1 \end{pmatrix}.
\end{aligned}$$

Note that the rotation components $$R_1,R_2$$ are simply multiplied together, and their product is not affected by the translation component.
On the other hand, the translation components $$x_1,x_2$$ are not simply summed together, rather, the second translation vector $$x_2$$ is rotated by $$R_1$$ before being added to $$x_1$$.
This property, that one component of the product is affected by the other component, but not vice versa, is why $$\mathbf{SE}(3)$$ is called a **semi-direct** product of $$\mathbf{SO}(3)$$ and $$\mathbb{R}^3$$, which is sometimes written as $$\mathbf{SE(3)} = \mathbf{SO(3)} \ltimes \mathbb{R}^3$$.

The group properties are easily verified.
The identity matrix $$I_4$$ lies in $$\mathbf{SE}(3)$$, with its rotation given by $$I_3$$ and its translation vector given by $$0_{3\times 1}$$.
For matrix inversion, examining the product leads to the conclusion that

$$\begin{aligned}
    P^{-1}
    = \begin{pmatrix} R & x \\ 0_{1\times 3} & 1 \end{pmatrix}^{-1}
    = \begin{pmatrix} R^\top & - R^\top x \\ 0_{1\times 3} & 1 \end{pmatrix}.
\end{aligned}$$

This formula yields another element of $$\mathbf{SE}(3)$$, and we should note that it is entirely expressed in terms of sums and products of the original matrix components.
This is useful, since it is usually much easier and computationally cheaper to take sums and products of vectors and matrices than it is to invert them.
All of this shows that $$ \mathbf{SE}(3) $$ is indeed a group.

### Lie algebra

The Lie algebra $$ \mathfrak{se}(3) $$ is obtained by differentiating the defining conditions of the Lie group $$R \in \mathbf{SO}(3)$$ and $$ x \in \mathbb{R}^3$$ near the identity,

$$\begin{aligned}
    \mathfrak{se}(3)
    =  \left\{
        \begin{pmatrix} \omega^\times & v \\ 0_{1\times 3} & 0 \end{pmatrix} \in \mathbb{R}^{4\times 4}
        \; \middle| \;
        \omega^\times \in \mathfrak{so}(3), \; v \in \mathbb{R}^3
    \right\}.
\end{aligned}$$

Recall that $$\mathfrak{so}(3)$$ is the Lie algebra of $$\mathbf{SO}(3)$$, defined by the property that $$\omega^\times \in \mathfrak{so}(3)$$ if and only if $$(\omega^\times)^\top = - \omega^\times$$.
Recall also that the skew map $$\cdot^\times : \mathbb{R}^3 \to \mathbb{R}^{3\times 3}$$ such that $$\omega^\times$$ is the unique matrix for which $$\omega^\times a = \omega \times a$$ for all vectors $$ a\in \mathbb{R}^3$$, that is,

$$\begin{aligned}
\omega^\times
:= \begin{pmatrix}
    0 & -\omega_3 & \omega_2 \\
    \omega_3 & 0 & -\omega_1 \\
    -\omega_2 & \omega_1 & 0
    \end{pmatrix}.
\end{aligned}$$

From here, we define the basis of $\mathfrak{se}(3)$ to be

$$\begin{aligned}
    E_1 &= \begin{pmatrix}
    0 & 0 & 0 & 0 \\
    0 & 0 & -1 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0
    \end{pmatrix}, &
    E_2 &= \begin{pmatrix}
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 0 \\
    -1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0
    \end{pmatrix}, &
    E_3 &= \begin{pmatrix}
    0 & -1 & 0 & 0 \\
    1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0
    \end{pmatrix}, \\
    E_4 &= \begin{pmatrix}
    0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0
    \end{pmatrix}, &
    E_5 &= \begin{pmatrix}
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0
    \end{pmatrix}, &
    E_6 &= \begin{pmatrix}
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0
    \end{pmatrix}.
\end{aligned}$$

Having defined this basis, we can also write down the wedge map $$ \cdot^\wedge : \mathbb{R}^6 \to \mathfrak{se}(3)$$.
For convenience of notation, we will typically write our elements of $$ \mathbb{R}^6$$ as consisting of two concatenated $$\mathbb{R}^3$$ vectors.
Specifically, given $$ \omega, v \in \mathbb{R}^3$$, the wedge map is given by

$$\begin{aligned}
\begin{pmatrix} \omega \\ v \end{pmatrix}^\wedge
&:= \omega_1 E_1 + \omega_2 E_2 + \omega_3 E_3
+ v_1 E_4 + v_2 E_5 + v_3 E_6 \\
&= \begin{pmatrix}
    0 & -\omega_3 & \omega_2 & v_1 \\
    \omega_3 & 0 & -\omega_1 & v_2 \\
    -\omega_2 & \omega_1 & 0 & v_3 \\
    0 & 0 & 0 & 0
    \end{pmatrix}
= \begin{pmatrix}
    \omega^\times & v \\ 0_{1\times 3} & 0
    \end{pmatrix}.
\end{aligned}$$

The final compact form is particularly useful, but if it ever looks confusing, just remember that it is only a convenient way to write things down.
The object we are describing here is ultimately a $$ 4 \times 4 $$ matrix, even if it has an elegant $$ 2 \times 2 $$ block matrix structure.

#### Adjoint and Lie bracket

To study the adjoint maps, we will denote arbitrary elements by $$ P \in \mathbf{SE}(3) $$ and $$ U \in \mathfrak{se}(3)$$.
The rotation and translation components of $$ P$$ are written $$R$$ and $$x$$, respectively, while the rotation and translation components of $$U$$ are written $$\omega^\times $$ and $$v$$, respectively.
Then, the adjoint operator is defined by

$$\begin{aligned}
\mathrm{Ad}_{RP}(U)
&= P U P^{-1} \\
&= \begin{pmatrix} R & x \\ 0_{1\times 3} & 1 \end{pmatrix}^{-1}
\begin{pmatrix} \omega^\times & v \\ 0_{1\times 3} & 0 \end{pmatrix}
\begin{pmatrix} R^\top & - R^\top x \\ 0_{1\times 3} & 1 \end{pmatrix} \\
&= \begin{pmatrix} R \omega^\times & R v \\ 0_{1\times 3} & 0 \end{pmatrix}
\begin{pmatrix} R^\top & - R^\top x \\ 0_{1\times 3} & 1 \end{pmatrix} \\
&= \begin{pmatrix} R \omega^\times R^\top & R \omega^\times (- R^\top x) + R v \\ 0_{1\times 3} & 0 \end{pmatrix} \\
&= \begin{pmatrix} (R \omega)^\times & - (R \omega)^\times x + R v \\ 0_{1\times 3} & 0 \end{pmatrix} \\
&= \begin{pmatrix} (R \omega)^\times & x^\times R \omega + R v \\ 0_{1\times 3} & 0 \end{pmatrix}.
\end{aligned}$$

Here, we have used a few cross-product identities, that were derived in the [post on $$\mathbf{SO}(3)$$]({% post_url 2025-02-15-special_orthogonal_so3 %}).
From simply reading the entries of the result, the matrix form of the Adjoint operator is found to be

$$\begin{aligned}
\mathrm{Ad}_{P}^\vee
&= \begin{pmatrix}
    R & 0_{3\times 3} \\ x^\times R & R
\end{pmatrix} \in \mathbb{R}^{6\times 6}
\end{aligned}$$

The little adjoint matrix and the Lie bracket are easily obtained by differentiating $$\mathrm{Ad}_P^\vee$$ with respect to $$P$$ at the identify $$I_4$$,

$$\begin{aligned}
\mathrm{ad}_{U}^\vee
&= \begin{pmatrix}
    \omega^\times & 0_{3\times 3} \\ v^\times & \omega^\times
\end{pmatrix} \in \mathbb{R}^{6\times 6}, \\
[U_1, U_2] &= \begin{pmatrix} (\omega_1 \times \omega_2)^\times & v_1\times \omega_2 + \omega_1 \times v_2 \\ 0_{1\times 3} & 0 \end{pmatrix}
\end{aligned}$$

As always, the Lie bracket can also be obtained by computing the matrix commutator $$[U_1, U_2] = U_1 U_2 - U_2 U_1$$.
It is useful to be aware of these equivalences so that you can pick the technique you find easiest in your situation.

#### Exponential and Logarithm

The exponential and logarithm of $$ \mathbf{SE}(3) $$ admit elegant terms involving trigonometric expressions, similarly to $$ \mathbf{SE}(2) $$.
Recall from the previous post on $$ \mathbf{SO}(3)$$ that, for any $$ \omega \in \mathbb{R}^3 $$,

$$\begin{aligned}
(\omega^\times)^2 &= \omega \omega^\top - \omega^\top \omega I_3, \\
(\omega^\times)^3 &= - \vert \omega \vert^2 \omega^\times.
\end{aligned}$$

Now consider an arbitrary element $$ U \in \mathfrak{se}(3) $$ with rotational and translational components $$ \omega $$ and $$ v $$.
Looking at the powers of $$ U $$, we find

$$\begin{aligned}
U^2 &= \begin{pmatrix} \omega^\times & v \\ 0_{1\times 3} & 0 \end{pmatrix}^2
= \begin{pmatrix} (\omega^\times)^2 & \omega^\times v \\ 0_{1\times 3} & 0 \end{pmatrix}, \\
U^3 &= \begin{pmatrix} \omega^\times & v \\ 0_{1\times 3} & 0 \end{pmatrix}^3
= \begin{pmatrix} \omega^\times & v \\ 0_{1\times 3} & 0 \end{pmatrix} \begin{pmatrix} (\omega^\times)^2 & \omega^\times v \\ 0_{1\times 3} & 0 \end{pmatrix}
= \begin{pmatrix} (\omega^\times)^3 & (\omega^\times)^2 v \\ 0_{1\times 3} & 0 \end{pmatrix}.
\end{aligned}$$

From here we can prove the pattern by induction.
Assume that

$$\begin{aligned}
U^n &= \begin{pmatrix} (\omega^\times)^n & (\omega^\times)^{n-1} v \\ 0_{1\times 3} & 0 \end{pmatrix},
\end{aligned}$$

for a given $$ n \geq 2 $$. Then

$$\begin{aligned}
U^{n+1} &= \begin{pmatrix} \omega^\times & v \\ 0_{1\times 3} & 0 \end{pmatrix} \begin{pmatrix} (\omega^\times)^n & (\omega^\times)^{n-1} v \\ 0_{1\times 3} & 0 \end{pmatrix}
= \begin{pmatrix} (\omega^\times)^{n+1} & (\omega^\times)^{(n+1)-1} v \\ 0_{1\times 3} & 0 \end{pmatrix}.
\end{aligned}$$

Since the formula holds for $$ n = 2 $$, we have therefore shown that it holds for all $$ n \geq 2 $$ by induction.
From here we can compute the matrix exponential explicitly. By definition,

$$\begin{aligned}
\exp(U)
    &= \sum_{n=0}^\infty \frac{1}{n!} U^n \\
    &= I_4 + U + \sum_{n=2}^\infty \frac{1}{n!} U^n \\
    &= I_4 + U + \sum_{n=2}^\infty \frac{1}{n!} \begin{pmatrix} (\omega^\times)^n & (\omega^\times)^{n-1} v \\ 0_{1\times 3} & 0 \end{pmatrix} \\
% ------------
    &= \begin{pmatrix} I_3 & 0_{3\times 1} \\ 0_{1\times 3} & 1 \end{pmatrix} 
    + \begin{pmatrix} \omega^\times & v \\ 0_{1\times 3} & 0 \end{pmatrix} 
    + \begin{pmatrix} \sum_{n=2}^\infty \frac{1}{n!} (\omega^\times)^n & \sum_{n=2}^\infty \frac{1}{n!} (\omega^\times)^{n-1} v \\ 0_{1\times 3} & 0 \end{pmatrix} \\
% ------------
    &= \begin{pmatrix} I_3 + \omega^\times + \sum_{n=2}^\infty \frac{1}{n!} (\omega^\times)^n & 
    v + \sum_{n=2}^\infty \frac{1}{n!} (\omega^\times)^{n-1} v \\ 
    0_{1\times 3} & 1 \end{pmatrix} \\
% ------------
    &= \begin{pmatrix} \sum_{n=0}^\infty \frac{1}{n!} (\omega^\times)^n & 
    \sum_{n=1}^\infty \frac{1}{n!} (\omega^\times)^{n-1} v \\ 
    0_{1\times 3} & 1 \end{pmatrix} \\
% ------------
    &= \begin{pmatrix} \exp(\omega^\times) & 
    \left( \sum_{n=1}^\infty \frac{1}{n!} (\omega^\times)^{n-1} \right) v \\ 
    0_{1\times 3} & 1 \end{pmatrix} \\
\end{aligned}$$

Let $$ P = \exp(U) $$ denote the result, with rotation and translation terms $$ R \in \mathbf{SO}(3) $$ and $$ x \in \mathbb{R}^3$$, respectively.
Then $$ R = \exp(\omega^\times) $$, which is simply the $$ \mathbf{SO}(3) $$ exponential computed previously.
To determine $$ x = \left( \sum_{n=1}^\infty \frac{1}{n!} (\omega^\times)^{n-1} \right) v $$, we first define $$ M(\omega) = \sum_{n=1}^\infty \frac{1}{n!} (\omega^\times)^{n-1} $$ and then attempt to simplify it using [trigonometric power series expansions](https://en.wikipedia.org/wiki/Trigonometric_functions#Power_series_expansion).
Assume for now that $$\omega \neq 0$$. Then

$$\begin{aligned}
M(\omega)
&= \sum_{n=1}^\infty \frac{1}{n!} (\omega^\times)^{n-1} \\
&= I_3 + \sum_{n=2}^\infty \frac{1}{n!} (\omega^\times)^{n-1} \\
&= I_3 + \sum_{k=1}^\infty \frac{1}{(2k)!} (\omega^\times)^{2k-1} + \sum_{k=1}^\infty \frac{1}{(2k+1)!} (\omega^\times)^{2k} \\
&= I_3 + \sum_{k=1}^\infty \frac{(-1)^{k-1}}{(2k)!} \vert \omega \vert^{2k-2} \omega^\times + \sum_{k=1}^\infty \frac{(-1)^{k}}{(2k+1)!} \vert \omega \vert^{2k-2} (\omega^\times)^{2} \\
% ------------
&= I_3
- \vert \omega \vert^{-2} \sum_{k=1}^\infty \frac{(-1)^{k}}{(2k)!} \vert \omega \vert^{2k} \omega^\times
+ \vert \omega \vert^{-3} \sum_{k=1}^\infty \frac{(-1)^{k}}{(2k+1)!} \vert \omega \vert^{2k+1} (\omega^\times)^{2} \\
% ------------
&= I_3
- \vert \omega \vert^{-2} \left(-1 + \sum_{k=0}^\infty \frac{(-1)^{k}}{(2k)!} \vert \omega \vert^{2k} \right) \omega^\times
+ \vert \omega \vert^{-3} \left(-\vert \omega \vert + \sum_{k=0}^\infty \frac{(-1)^{k}}{(2k+1)!} \vert \omega \vert^{2k+1} \right) (\omega^\times)^{2} \\
% ------------
&= I_3
- \vert \omega \vert^{-2} \left(-1 + \cos( \vert \omega \vert ) \right) \omega^\times
+ \vert \omega \vert^{-3} \left(-\vert \omega \vert + \sin( \vert \omega \vert ) \right) (\omega^\times)^{2} \\
% ------------
&= I_3
+ \frac{ 1 - \cos(\vert \omega \vert) }{ \vert \omega \vert^2 } \omega^\times
+ \frac{ \sin( \vert \omega \vert ) - \vert \omega \vert }{ \vert \omega \vert^3 } (\omega^\times)^{2}
\end{aligned}$$

In summary, the full exponential is given by

$$\begin{aligned}
\exp(U)
% ------------
&= \begin{pmatrix} \exp(\omega^\times) &
M(\omega) v \\
0_{1\times 3} & 1 \end{pmatrix}, \\
% ------------
\exp(\omega^\times)
&= I_3
+ \frac{\sin(\vert \omega \vert)}{\vert \omega \vert} \omega^\times
+ \frac{1 - \cos(\vert \omega \vert)}{\vert \omega \vert^2} (\omega^\times)^{2}, \\
% ------------
M(\omega)
&= I_3
+ \frac{ 1 - \cos(\vert \omega \vert) }{ \vert \omega \vert^2 } \omega^\times
+ \frac{ \sin( \vert \omega \vert ) - \vert \omega \vert }{ \vert \omega \vert^3 } (\omega^\times)^{2}.
\end{aligned}$$

In the case where $$ \omega = 0 $$, the result is simply

$$\begin{aligned}
\exp(U)
% ------------
&= \exp \begin{pmatrix} 0_{3\times 3} &
v \\
0_{1\times 3} & 0 \end{pmatrix}
% ------------
= \begin{pmatrix} I_3 &
v \\
0_{1\times 3} & 1 \end{pmatrix}.
\end{aligned}$$

The logarithm is simply the inverse of the exponential, so suppose that $$ \exp(U) = P $$.
Then $$ \exp(\omega) = R $$, which we already know how to solve using

$$\begin{aligned}
\vert \omega \vert &= \cos^{-1}\left( \frac{\mathrm{tr}(R) - 1}{2} \right) \\
\omega  &= \frac{\vert \omega \vert}{2 \sin(\vert \omega \vert)}(R - R^\top)^\vee,
\end{aligned}$$

for $$ \vert \omega \vert \in (0, \pi) $$.
In this case, we have that $$ x = M(\omega) v$$, which is solved by $$ v = M(\omega)^{-1} x$$, as long as $$M(\omega)$$ is invertible.
When is $$ M(\omega) $$ invertible?
Rather, if $$ M(\omega) $$ is not invertible, then there must be a vector $$ v $$ for which $$M(\omega) v = 0$$.
This would mean that

$$\begin{aligned}
0 &= M(\omega) v \\
&= v
+ \frac{ 1 - \cos(\vert \omega \vert) }{ \vert \omega \vert^2 } \omega^\times v
+ \frac{ \sin( \vert \omega \vert ) - \vert \omega \vert }{ \vert \omega \vert^3 } (\omega^\times)^{2} v.
\end{aligned}$$

If $$ v $$ is not parallel to $$ \omega $$, then the second term $$ \frac{ 1 - \cos(\vert \omega \vert) }{ \vert \omega \vert^2 } \omega^\times v $$ is non-zero and is also orthogonal to the other terms, so the full expression cannot be zero.
Concretely, we can premultiply both sides by $$ (\omega^\times v)^\top $$ to obtain

$$\begin{aligned}
0 &= (\omega^\times v)^\top M(\omega) v \\
&= (\omega^\times v)^\top v
+ \frac{ 1 - \cos(\vert \omega \vert) }{ \vert \omega \vert^2 } (\omega^\times v)^\top \omega^\times v
+ \frac{ \sin( \vert \omega \vert ) - \vert \omega \vert }{ \vert \omega \vert^3 } (\omega^\times v)^\top (\omega^\times)^{2} v \\
&= - v^\top \omega^\times v
+ \frac{ 1 - \cos(\vert \omega \vert) }{ \vert \omega \vert^2 } \vert \omega^\times v \vert^2
+ \frac{ \sin( \vert \omega \vert ) - \vert \omega \vert }{ \vert \omega \vert^3 } (\omega^\times v)^\top \omega^\times (\omega^\times v) \\
&= \frac{ 1 - \cos(\vert \omega \vert) }{ \vert \omega \vert^2 } \vert \omega^\times v \vert^2.
\end{aligned}$$

This is zero if and only if $$ \frac{ 1 - \cos(\vert \omega \vert) }{ \vert \omega \vert^2 } \vert \omega^\times v \vert^2 = 0$$, which can only occur if $$ \omega^\times v = 0$$.
Considering the case that $$ v = a \omega $$ for some scalar $$ a $$, then we would require

$$\begin{aligned}
0 &= M(\omega) (a\omega) \\
&= a \omega
+ a \frac{ 1 - \cos(\vert \omega \vert) }{ \vert \omega \vert^2 } \omega^\times \omega
+ a \frac{ \sin( \vert \omega \vert ) - \vert \omega \vert }{ \vert \omega \vert^3 } (\omega^\times)^{2} \omega \\
&= a \omega,
\end{aligned}$$

which is only solved by $$ a \omega = 0$$.
What this all means is that $$M(\omega) $$ is always invertible, no matter the value of $$ \omega $$.
Thus the full logarithm is given by

$$\begin{aligned}
 \log \begin{pmatrix} R & x \\ 0_{1\times 3} & 1 \end{pmatrix} 
 &= \begin{pmatrix} \log(R) & M(\log(R))^{-1} x \\ 0_{1\times 3} & 0 \end{pmatrix}, \\
\log(R)  &= \frac{\theta}{2 \sin(\theta)}(R - R^\top)^\vee, \hspace{2cm}
\theta := \cos^{-1}\left( \frac{\mathrm{tr}(R) - 1}{2} \right), \\
M(\omega) &:= I_3
+ \frac{ 1 - \cos(\vert \omega \vert) }{ \vert \omega \vert^2 } \omega^\times
+ \frac{ \sin( \vert \omega \vert ) - \vert \omega \vert }{ \vert \omega \vert^3 } (\omega^\times)^{2}.
\end{aligned}$$

### Conclusion

The 3D special Euclidean group is an important Lie group to understand for robotics, where it is used to describe transformations between frames of reference of different rigid bodies.
The goal of this post is not to explain this application, but rather, to go into detail of how the important formulas for $$ \mathbf{SE}(3) $$ can be derived.
If you want to look at an implementation of some of the functions I have described, I suggest you to look at [pylie](https://github.com/pvangoor/pylie).
Remember that a lot of the formulas here are derived from the formulas for $$ \mathbf{SO}(3) $$, which you can find in my [previous post]({% post_url 2025-02-15-special_orthogonal_so3 %}).
Finally, I will leave a summary of the formulas below for quick reference.

### Quick Reference

The 3D special Euclidean group and its Lie algebra

$$\begin{aligned}
        \mathbf{SE}(3) &= \left\{
        P = \begin{pmatrix}
            R & x \\ 0_{1\times 3} & 1
        \end{pmatrix} \in \mathbb{R}^{4\times 4}
        \; \middle| \;
        R \in \mathbf{SO}(3), \; x \in \mathbb{R}^3
    \right\}, \\
        \mathfrak{se}(3)
    &=  \left\{
        \begin{pmatrix} \omega^\times & v \\ 0_{1\times 3} & 0 \end{pmatrix} \in \mathbb{R}^{4\times 4}
        \; \middle| \;
        \omega^\times \in \mathfrak{so}(3), \; v \in \mathbb{R}^3
    \right\}.
\end{aligned}$$

The Lie algebra wedge map

$$\begin{aligned}
    \cdot^\wedge &: \mathbb{R}^6 \to \mathfrak{se}(3), \\
    \begin{pmatrix} \omega \\ v \end{pmatrix}^\wedge
    &= \begin{pmatrix}
    \omega^\times & v \\ 0_{1\times 3} & 0
    \end{pmatrix}, \\
    \omega^\times &= \begin{pmatrix}
        \omega_1 \\ \omega_2 \\ \omega_3
    \end{pmatrix}^\times
    = \begin{pmatrix}
        0 & -\omega_3 & \omega_2 \\
        \omega_3 & 0 & -\omega_1 \\
        -\omega_2 & \omega_1 & 0
    \end{pmatrix}.
\end{aligned}$$

Adjoint matrices

$$\begin{aligned}
\mathrm{Ad}_{P}^\vee
&= \begin{pmatrix}
    R & 0_{3\times 3} \\ x^\times R & R
\end{pmatrix} \in \mathbb{R}^{6\times 6}, \\
\mathrm{ad}_{U}^\vee
&= \begin{pmatrix}
    \omega^\times & 0_{3\times 3} \\ v^\times & \omega^\times
\end{pmatrix} \in \mathbb{R}^{6\times 6}.
\end{aligned}$$

Exponential formula (for $$ \omega \neq 0 $$)

$$\begin{aligned}
\exp \begin{pmatrix} \omega^\times &
v \\
0_{1\times 3} & 0 \end{pmatrix}
% ------------
&= \begin{pmatrix} \exp(\omega^\times) &
M(\omega) v \\
0_{1\times 3} & 1 \end{pmatrix}, \\
% ------------
\exp(\omega^\times)
&= I_3
+ \frac{\sin(\vert \omega \vert)}{\vert \omega \vert} \omega^\times
+ \frac{1 - \cos(\vert \omega \vert)}{\vert \omega \vert^2} (\omega^\times)^{2}, \\
% ------------
M(\omega)
&:= I_3
+ \frac{ 1 - \cos(\vert \omega \vert) }{ \vert \omega \vert^2 } \omega^\times
+ \frac{ \sin( \vert \omega \vert ) - \vert \omega \vert }{ \vert \omega \vert^3 } (\omega^\times)^{2}.
\end{aligned}$$

Logarithm formula (for $$ R \neq R^\top $$)

$$\begin{aligned}
 \log \begin{pmatrix} R & x \\ 0_{1\times 3} & 1 \end{pmatrix} 
 &= \begin{pmatrix} \log(R) & M(\log(R))^{-1} x \\ 0_{1\times 3} & 0 \end{pmatrix}, \\
\log(R)  &= \frac{\theta}{2 \sin(\theta)}(R - R^\top)^\vee, \hspace{2cm}
\theta := \cos^{-1}\left( \frac{\mathrm{tr}(R) - 1}{2} \right).
\end{aligned}$$

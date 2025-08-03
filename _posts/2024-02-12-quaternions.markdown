---
layout: post
title:  "The Non-Zero Quaternions as a Lie Group"
date:   2024-02-12
categories: Mathematics
---

{% include math.html %}

### Introduction

Quaternions are well-known to people working in robotics and aerospace.
They (the unit quaternions, specifically) provide a smooth representation of attitude in using only four numbers, in contrast to rotation matrices that require 9 and Euler angles that are not smooth.
In this post, I will explore the quaternions from a slightly different perspective: the quaternions (excluding zero) form a Lie group under multiplication.
We will not restrict ourselves to the unit quaternions, instead exploring the full four-dimensional Lie group.

### Basic group properties

Throughout this article, we will write a quaternion $$q \in \mathbb{H}$$ as
$$ q = (r, u), $$
where $$r \in \mathbb{R}_{\neq 0}$$ and $$u \in \mathbb{R}^3$$ represent the real and imaginary parts of $$q$$, respectively.
The product is defined by

$$\begin{aligned}
q_1 * q_2 &= (r_1, u_1) * (r_2, u_2) \\
&= (r_1 r_2 - u_1^\top u_2, \; r_1 u_2 + r_2 u_1 + u_1 \times u_2).
\end{aligned}$$

The inverse of a quaternion is defined by

$$ q^{-1} =  (r^2 + \vert u \vert^2)^{-1} (r, -u). $$

And the group identity is given by $$ e := (1, 0_3) $$.

The quaternions act on themselves by conjugation. Specifically,

$$\begin{aligned}
\mathrm{Cn}_{q_1}(q_2)
&= q_1 * q_2 * q_1^{-1} \\
% -----
&= (r_1^2 + \vert u_1 \vert^2)^{-1}
(r_1 r_2 - u_1^\top u_2, \; r_1 u_2 + r_2 u_1 + u_1 \times u_2) * (r_1, -u_1)\\
% -----
&= (r_1^2 + \vert u_1 \vert^2)^{-1}
((r_1 r_2 - u_1^\top u_2) r_1 + (r_1 u_2 + r_2 u_1 + u_1 \times u_2)^\top u_1, \\
&\hspace{1cm}
r_1(r_1 u_2 + r_2 u_1 + u_1 \times u_2) - (r_1 r_2 - u_1^\top u_2)u_1 -(r_1 u_2 + r_2 u_1 + u_1 \times u_2) \times u_1 )\\
% -----
&= (r_1^2 + \vert u_1 \vert^2)^{-1}
(r_1^2 r_2 - r_1 u_1^\top u_2 + r_1 u_2^\top u_1 + r_2 u_1^\top u_1 , \\
&\hspace{1cm}
r_1^2 u_2 + r_1 r_2 u_1 + r_1 u_1 \times u_2 - r_1 r_2 u_1 + u_1 u_1^\top u_2 - r_1 u_2 \times u_1 - (u_1 \times u_2) \times u_1 )\\
% -----
&= (r_1^2 + \vert u_1 \vert^2)^{-1}
(r_1^2 r_2 + r_2 u_1^\top u_1 , \\
&\hspace{1cm}
r_1^2 u_2 + 2 r_1 u_1 \times u_2 + u_1 u_1^\top u_2 + u_1 \times (u_1 \times u_2) )\\
% -----
&= (r_2 , \;
(r_1^2 + \vert u_1 \vert^2)^{-1}(r_1^2 u_2 + \vert u_1 \vert^2 u_2 + 2 r_1 u_1 \times u_2 + 2 u_1 \times (u_1 \times u_2)) )\\
% -----
&= (r_2 , \;
u_2 + (2 r_1 u_1 \times u_2 + 2 u_1 \times (u_1 \times u_2))(r_1^2 + \vert u_1 \vert^2)^{-1}).
\end{aligned}$$

Let us denote $$ \vert q_1 \vert = \sqrt{r_1^2 + \vert u_1 \vert^2}$$ and define $$u_1^\times \in \mathbb{R}^{3\times 3}$$ to be the `skew' matrix such that $$u_1^\times u_2 = u_1 \times u_2$$.
Then we end up with a nice and simple formula:

$$
\mathrm{Cn}_{q_1}(q_2)
= (r_2 , \;
(I_3 + (2 r_1 u_1^\times + 2 (u_1^\times)^2 )\vert q_1 \vert^{-2})u_2 ).
$$

### The Quaternion Lie Algebra

There are many ways to think of the Lie algebra of a given Lie group.
Since our main interest is computation, we will choose the way that is easiest to work with for computation.
The Lie algebra $$\mathfrak{h}$$ of $$\mathbb{H}$$ can identified with the tangent space at the identity $$e$$.
This definition is abstract, so we assign some coordinates.
A Lie algebra element is described as $$w^\vee := (s, v) \in \mathbb{R}^4$$, where the $$\vee$$ operator is the map from the abstract Lie algebra to the coordinates in $$\mathbb{R}^4$$.
Near the identity, quaternion group elements can be written as

$$ q = e + t w, \quad (r,u) = (1+t s, t v), $$

for small values of $$t \in \mathbb{R}$$.

#### Exponential and Logarithm

The exponential relates the Lie algebra to the Lie group.
We will use the `1-parameter subgroup' definition here.
Given a Lie algebra element $$w^\vee = (s,v)$$, the exponential $$\exp(w)$$ is defined as the solution to the initial value problem

$$ q(0) = e, \quad \dot{q}(t) = q(t) * w, $$

at $$t = 1$$. Let us evaluate the differential equation to find

$$ \begin{aligned}
\dot{q} &= q * w \\
&:= \left. \frac{\mathrm{d}}{\mathrm{d} t} \right\vert_{t=0} (r,u) * (1+t s, t v) \\
&= \left. \frac{\mathrm{d}}{\mathrm{d} t} \right\vert_{t=0}
(r (1+ts) - t u^\top v, \; r t v + (1+ts) u + t u \times v) \\
(\dot{r}, \dot{u})
&=
(r s - u^\top v, \; r v + s u + u \times v).
\end{aligned} $$

This ODE is not straightforward to solve, unless we realise that this system is, in fact, linear!
Writing $$q$$ as a vector in $$\mathbb{R}^4$$, we have

$$ \begin{aligned}
\left. \frac{\mathrm{d}}{\mathrm{d} t} \right\vert_{t=0}
\begin{pmatrix} r \\ u \end{pmatrix}
&= \begin{pmatrix} s & - v^\top \\ v & s I_3 - v^\times \end{pmatrix}
\begin{pmatrix} r \\ u \end{pmatrix}
= \begin{pmatrix} 0 & - v^\top \\ v & - v^\times \end{pmatrix}
\begin{pmatrix} r \\ u \end{pmatrix} + s \begin{pmatrix} r \\ u \end{pmatrix}.
\end{aligned} $$

Since $$s$$ acts as a scaling factor, we can pull it out of the equation for now, and solve the problem without it.
Specifically,

$$
\left. \frac{\mathrm{d}}{\mathrm{d} t} \right\vert_{t=0} e^{-t s} q = e^{-t s} \dot{q} - s e^{-t s} q = A e^{-t s} q,
$$

so if we solve the problem while ignoring $$s$$, we can add it back in at the end.
To solve the ODE now, we only have to compute the matrix exponential

$$ \begin{aligned}
A &:= \begin{pmatrix} 0 & - v^\top \\ v & - v^\times \end{pmatrix} &
\exp(A) &= \sum_{k=0}^\infty \frac{1}{k!} A^k.
\end{aligned} $$

Examining the first nontrivial power of $$A$$ reveals that

$$ \begin{aligned}
A^2 &= \begin{pmatrix} 0 & - v^\top \\ v & - v^\times \end{pmatrix}^2
= \begin{pmatrix} -\vert v \vert^2 & 0_{1\times 3} \\ 0_{3\times 1} & (v^\times)^2 - v v^\top \end{pmatrix}
= \begin{pmatrix} -\vert v \vert^2 & 0_{1\times 3} \\ 0_{3\times 1} & - \vert v \vert^2 I_3 \end{pmatrix}
= - \vert v \vert^2 I_4.
\end{aligned} $$

Substituting this into the exponential formula yields

$$ \begin{aligned}
\exp(A) &= \sum_{k=0}^\infty \frac{1}{k!} A^k \\
&= \sum_{k=0}^\infty \frac{1}{(2k)!} A^{2k} + \sum_{k=0}^\infty \frac{1}{(2k+1)!} A^{2k+1} \\
&= \sum_{k=0}^\infty \frac{1}{(2k)!} (- \vert v \vert^2 I_4)^k + \sum_{k=0}^\infty \frac{1}{(2k+1)!} (- \vert v \vert^2 I_4)^{k} A \\
&= \sum_{k=0}^\infty \frac{(-1)^k}{(2k)!} \vert v \vert^{2k} I_4+ \vert v \vert^{-1} \sum_{k=0}^\infty \frac{(-1)^k}{(2k+1)!} \vert v \vert^{2k+1} A \\
&= \cos(\vert v \vert) I_4 + \frac{\sin(\vert v \vert)}{\vert v \vert} A.
\end{aligned} $$

Therefore, we have our final solution,

$$ \begin{aligned}
\exp(w) &= e^s \exp(A) \begin{pmatrix} 1 \\ 0_3 \end{pmatrix} \\
&= \left( \cos(\vert v \vert) I_4 + \frac{\sin(\vert v \vert)}{\vert v \vert} A \right) \begin{pmatrix} e^s \\ 0_3 \end{pmatrix} \\
&= \cos(\vert v \vert)\begin{pmatrix} e^s  \\ 0_3 \end{pmatrix} + \frac{\sin(\vert v \vert)}{\vert v \vert} \begin{pmatrix} 0 & - v^\top \\ v & - v^\times \end{pmatrix}  \begin{pmatrix} e^s \\ 0_3 \end{pmatrix} \\
&= \begin{pmatrix} e^s \cos(\vert v \vert) \\ e^s \sin(\vert v \vert) \frac{v}{\vert v \vert} \end{pmatrix}.
\end{aligned} $$

Note that, if $$\vert v \vert = 0$$, then the whole computation simplifies and the solution is simply $$\exp(w) = ( e^s, 0_3)$$.

The logarithm is found by inverting this formula, although there may be multiple solutions for a given $$q \in \mathbb{H}$$.
Suppose that $$q = \exp(w)$$. Then we wish to determine the components of $$w = (s, v)$$ in terms of $$q = (r, u)$$. We have

$$ \begin{aligned}
q &= \exp(w), \\
(r, u) &= (e^s \cos(\vert v \vert), e^s \sin(\vert v \vert) \frac{v}{\vert v \vert}).
\end{aligned} $$

Immediately, we see that $$e^s = r / \cos(\vert v \vert)$$. Substituting this into the $$u$$-component,

$$ \begin{aligned}
u &= r \tan(\vert v \vert) \frac{v}{\vert v \vert}, \\
\frac{u}{\vert u \vert} \vert u \vert &= r \tan(\vert v \vert) \frac{v}{\vert v \vert}, \\
r^{-1} \vert u \vert \frac{u}{\vert u \vert} &= \tan(\vert v \vert) \frac{v}{\vert v \vert}, \\
v &=  \frac{\arctan(r^{-1} \vert u \vert)}{\vert u \vert} u
\end{aligned} $$

Rather than substitute this back into the formula for $$e^s$$, we observe that the norm of both sides of the original equation satisfies

$$ \begin{aligned}
\vert q \vert &= \vert \exp(w) \vert, \\
\sqrt{r^2 + \vert u \vert^2} &= e^{s} , \\
s &= \ln(\sqrt{r^2 + \vert u \vert^2}).
\end{aligned} $$

In summary, we have thus found the logarithm to be

$$ \begin{aligned}
\log(q) &= \left( \frac{1}{2} \ln(r^2 + \vert u \vert^2), \; \frac{\arctan(r^{-1} \vert u \vert)}{\vert u \vert} u \right).
\end{aligned} $$

Similarly to the exponential formula, we should note that, if $$\vert u \vert = 0$$, the formula simplifies to $$\log(q) = (\ln(r), 0_3)$$.

#### Adjoint Operators and Lie Bracket 

The big and little Adjoint operators are another important aspect of the Quaternion Lie algebra.
The `big' Adjoint operator $$\mathrm{Ad} : \mathbb{H} \times \mathfrak{h} \to \mathfrak{h}$$ is defined by

$$ \begin{aligned}
\mathrm{Ad}_q (w)
&= \left. \frac{\mathrm{d}}{\mathrm{d} t} \right\vert_{t=0} \mathrm{Cn}_q(e + t w) \\
&= \left. \frac{\mathrm{d}}{\mathrm{d} t} \right\vert_{t=0}
(1+ t s , \; (I_3 + (2 r_1 u_1^\times + 2 (u_1^\times)^2 )\vert q_1 \vert^{-2})(t v) ) \\
&= \left. \frac{\mathrm{d}}{\mathrm{d} t} \right\vert_{t=0}
(s , \; (I_3 + (2 r_1 u_1^\times + 2 (u_1^\times)^2 )\vert q_1 \vert^{-2})v ).
\end{aligned} $$

In matrix form,

$$ \begin{aligned}
\mathrm{Ad}_q \simeq  \begin{pmatrix}
    1 & 0_{1\times 3} \\
    0_{3\times 1} & I_3 + (2 r_1 u_1^\times + 2 (u_1^\times)^2 )\vert q_1 \vert^{-2}
\end{pmatrix}.
\end{aligned} $$

The `little' adjoint operator $$\mathrm{ad} : \mathfrak{h} \times \mathfrak{h} \to \mathfrak{h}$$ is defined as the derivative of the big Adjoint operator,

$$ \begin{aligned}
\mathrm{ad}_{w_1} (w_2)
&= \left. \frac{\mathrm{d}}{\mathrm{d} t} \right\vert_{t=0} \mathrm{Ad}_{e+ t w_1}w_2 \\
&= \left. \frac{\mathrm{d}}{\mathrm{d} t} \right\vert_{t=0}
(s_2 , \; (I_3 + (2 (1+t s_1) (t v_1)^\times + 2 ((t v_1)^\times)^2 )\vert e + t w_1 \vert^{-2})v_2 ) \\
&= (0 , \; 2 v_1^\times v_2 ).
\end{aligned} $$

Once more, in matrix form,

$$ \begin{aligned}
\mathrm{ad}_w \simeq  \begin{pmatrix}
    0 & 0_{1\times 3} \\
    0_{3\times 1} & 2v^\times
\end{pmatrix}.
\end{aligned} $$

The Lie bracket is equivalent to the adjoint operator, in the sense that

$$ \begin{aligned}
\left[w_1, w_2\right] := \mathrm{ad}_{w_1}(w_2) = (0 , \; 2 v_1^\times v_2 ).
\end{aligned} $$


### Matrix Representation

The final topic of interest for computations is the matrix representation of $$\mathbb{H}$$.
Matrix representations are rarely unique, but sometimes can be nice.
The matrix representation we consider is $$\rho : \mathbb{H} \to \mathbf{GL}(4)$$, given by

$$ \begin{aligned}
\rho(q) := \begin{pmatrix}
    r& u_1& u_2& u_3 \\
    -u_1& r& -u_3& u_2 \\
    -u_2& u_3& r& -u_1 \\
    -u_3&-u_2&u_1&r \\
\end{pmatrix}.
\end{aligned} $$

The matrix representation of the Lie algebra $$\mathfrak{h}$$ is basically the same.
Verifying that these are indeed representations is a messy and time-consuming computation.
However, working out a matrix representation is very rewarding in that it provides a way to check all the other computations we have done.
Specifically, we can check things like the inverse $$\rho(q)^{-1} = \rho(q^{-1})$$, the exponential $$\mathrm{expm}(\mathrm{d}\rho(w)) = \rho(\exp(w))$$, and the adjoint operators $$\mathrm{Ad}_q w = \rho(q) \mathrm{d}\rho(w) \rho(q)^{-1}$$.

### Summary

I decided to write this post when I needed these formulas for the $$n$$th time, and I realised that deriving them every time I needed them was taking too long.
I hope they are helpful to anyone else who reads them, and please let me know if you spot any mistakes!
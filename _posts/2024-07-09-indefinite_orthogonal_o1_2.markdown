---
layout: post
title:  "The Indefinite Orthogonal Group O(1,2)"
date:   2024-07-09
categories: Mathematics
---

{% include math.html %}

### Introduction

The indefinite orthogonal group $\mathbf{O}(1,2)$ is the set of $3\times 3$ matrices preserving the $(1,2)$ indefinite form.
Specifically, define the indefinite $(1,2)$ form to be

$$\begin{aligned}
    g = \begin{pmatrix}
            1 & 0_{1\times 2} \\ 0_{2\times 1} & -I_2
        \end{pmatrix} \in \mathbb{R}^{3\times 3}
\end{aligned}$$

Then the indefinite orthogonal group is defined to be

$$\begin{aligned}
    \mathbf{O}(1,2) = \left\{
        L \in \mathbb{R}^{3\times 3}
        \; \middle| \;
        L^\top g L = g
    \right\}
\end{aligned}$$

In applications, the indefinite form is important in studying the geometry of physics, where spacetime vectors have a structure like $(t,x,y,z)$.
The relevant group in that case is $\mathbf{O}(1,3)$, but the lower-dimensional $\mathbf{O}(1,2)$ serves as a nice toy model.
The elements of this group can also be thought of as `hyperbolic rotations'. This is because a hyperbola in $\mathbb{R}^3$ can be written as a set $H = \{ \xi \in \mathbb{R}^3 \; | \; \xi^\top g \xi = c \}$, where $c$ is a constant. It follows that the indefinite orthogonal group preserves $H$, much like how the standard orthogonal group preserves spheres.

The group properties are easily verified. 
The identity $I_3$ is clearly in $\mathbf{O}(1,2)$, and the matrix product and inverse preserve the group.
Specifically, if $L_1,L_2 \in \mathbf{O}(1,2)$, then

$$\begin{aligned}
    (L_1 L_2)^\top g (L_1 L_2) &= L_2^\top L_1^\top g L_1 L_2 = L_2^\top g L_2 = g, \\
    (L_1^{-1})^\top g L_1^{-1} &= (L_1^{-1})^\top (L_1^\top g L_1) L_1^{-1} = g.
\end{aligned}$$

It is useful to dissect the definition of the Lie group a bit. Let
$$\begin{aligned}
    L =  \begin{pmatrix} d & b^\top \\ c & A \end{pmatrix} 
    \in \mathbf{O}(1,2) \subset \mathbb{R}^{3\times 3},
\end{aligned}$$
where $A \in \R^{2\times 2}$ is the lower right block, $d \in \R$, and $b,c \in \R^2$.
Then, by the definition of the group,
$$\begin{aligned}
    g &= L^\top g L \\
    % -------
    &= \begin{pmatrix} d & c^\top \\ b & A^\top \end{pmatrix}
    \begin{pmatrix} 1 & 0_{1\times 2} \\ 0_{2\times1} & -I_2 \end{pmatrix}
    \begin{pmatrix} d & b^\top \\ c & A \end{pmatrix} \\
    % -------
    &= \begin{pmatrix} d & c^\top \\ b & A^\top \end{pmatrix}
    \begin{pmatrix} d & b^\top \\ -c & -A \end{pmatrix} \\
    % -------
    &= \begin{pmatrix} 
    d^2 - c^\top c &
    d b^\top - c^\top A \\
    db - A^\top c &
    b b^\top - A^\top A
    \end{pmatrix}.
\end{aligned}$$
This leads to three equations,
$$\begin{aligned}
    d^2 - c^\top c &= 1, &
    A^\top c &= d b, &
    b b^\top - A^\top A &= -I_2 \\
    % ------
    d &= \sqrt{1 + c^\top c}, &
    b &= d^{-1} A^\top c, &
    A^\top A &= b b^\top + I_2 \\
    % ------
    &&
    c &= d A^{-\top} b, &
    &
\end{aligned}$$
For compactness of notation, it is not always useful to write out matrix $L$ into these components, but the relationships are important for simplification of later formulas.

We will use these relations to compute the inverse of the matrix.
The formula for the inverse of a $2\times 2$ block matrix gives
$$\begin{aligned}
    L^{-1} = \begin{pmatrix} d & b^\top \\ c & A \end{pmatrix}^{-1}
    &= \begin{pmatrix} d^{-1} + d^{-2} b^\top S^{-1} c &
    -d^{-1} b^\top S^{-1} \\
    -d^{-1} S^{-1} c & S^{-1} \end{pmatrix}, &
    S &:= A - d^{-1} c b^\top
\end{aligned}$$
Since the inverse of $L$ also belongs to $\mathbf{O}(1,2)$, we only need to compute the upper- and lower-left terms. The remaining terms are determined by the relationships outlined above.
For the matrix $S$, we have
$$\begin{aligned}
    S &= A - d^{-1} c b^\top \\
    &= A - A^{-\top} b b^\top \\
    &= A - A^{-\top} (A^\top A - I_2) \\
    &= A^{-\top}
\end{aligned}$$
Thus $S^{-1} = A^\top$.
This is a nice simplification and helps to compute the remaining terms.
For the top-left term,
$$\begin{aligned}
    d^{-1} + d^{-2} b^\top S^{-1} c
    &= d^{-1} + d^{-2} b^\top A^\top c \\
    &= d^{-1} + d^{-1} b^\top b \\
    &= d^{-1} (1 + b^\top b) \\
    &= d
\end{aligned}$$
For the bottom-left term,
$$\begin{aligned}
    - d^{-1} S^{-1} c
    &= - d^{-1} A^\top c = -b.
\end{aligned}$$
Then by the fact that $(L^{-1})^{-1} = L$, the top-right term must be $-c^\top$.
In summary, the inverse of $L$ is can be greatly simplified from a general $3\times 3$ matrix inverse to
$$\begin{aligned}
    L^{-1} &= \begin{pmatrix} d & b^\top \\ c & A \end{pmatrix}^{-1}
    = \begin{pmatrix} d & -c^\top \\ -b & A^\top \end{pmatrix}
\end{aligned}$$


### Lie algebra

The Lie algebra can be obtained by differentiating the condition $L^\top g L = g$ at the identity.
Computing this, we obtain

$$\begin{aligned}
    \mathfrak{o}(1,2)
    &= \left\{
        U \in \mathbb{R}^{3\times 3}
        \; \middle| \;
        U^\top g + g U = 0
    \right\}.
\end{aligned}$$

We will choose a basis for this Lie algebra in order to map between it and to $\mathbb{R}^3$. To do this, let us decompose a Lie algebra element into its parts and check the condition. We have

$$\begin{aligned}
    0_{2\times 2} &= U^\top g + g U \\
    % ------
    &= \begin{pmatrix} U_{11} & U_{12} \\ U_{21} & U_{22} \end{pmatrix}^\top
    \begin{pmatrix} 1 & 0_{1\times 2} \\ 0_{2\times 1} & -I_2 \end{pmatrix}
    + \begin{pmatrix} 1 & 0_{1\times 2} \\ 0_{2\times 1} & -I_2 \end{pmatrix}
    \begin{pmatrix} U_{11} & U_{12} \\ U_{21} & U_{22} \end{pmatrix} \\
    % ------
    &= \begin{pmatrix} U_{11} & -U_{21}^\top \\ U_{12}^\top & -U_{22} \end{pmatrix}
    + \begin{pmatrix} U_{11} & U_{12} \\ -U_{21} & -U_{22} \end{pmatrix} \\
    &= \begin{pmatrix} 2 U_{11} & U_{12} - U_{21}^\top \\ U_{12}^\top - U_{21} & -U_{22}-U_{22}^\top \end{pmatrix},
\end{aligned}$$
where $U_{11} \in \mathbb{R}$, $U_{12} \in \mathbb{R}^{2\times 1}\simeq \mathbb{R}^2$, $U_{21} \in \mathbb{R}^{1\times 2}$, and $U_{22} \in \mathbb{R}^{2\times 2}$.
It follows that
$$\begin{aligned}
    U_{11} &= 0 &
    U_{21} &= U_{12}^\top \in \mathbb{R}^2& 
    U_{22} = - U_{22}^\top \in \mathfrak{so}(2)
\end{aligned}$$
In other words, there are three degrees of freedom, and we define the basis of $\mathfrak{o}(1,2)$ to be
$$\begin{aligned}
    E_1 &:= \begin{pmatrix}
        0 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0
    \end{pmatrix}, &
    E_2 &:= \begin{pmatrix}
        0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0
    \end{pmatrix}, &
    E_3 &:= \begin{pmatrix}
        0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0
    \end{pmatrix}.
\end{aligned}$$

For convenience, we will also adopt the notation 
$$\omega^\times = \begin{pmatrix}
        0 & -\omega \\ \omega & 0
\end{pmatrix}$$
for any $\omega \in \mathbb{R}$.
Then we may write the wedge map $\cdot^\wedge : \R^3 \to \mathfrak{o}(1,2)$ as
$$\begin{aligned}
        \begin{pmatrix}
        \omega \\ u_1 \\ u_2
    \end{pmatrix}^\wedge &:= \omega E_1 + u_1 E_2 + u_2 E_3
    = \begin{pmatrix} 0 & u^\top \\ u & \omega^\times \end{pmatrix} \in \R^{3\times 3},
\end{aligned}$$
where $u = (u_1,u_2) \in \R^2$.

The inverse of the wedge map is the 'vee' map $\cdot^\vee : \mathfrak{o}(1,2) \to \mathbb{R}^3$.


#### Adjoint and Lie bracket

With the wedge and vee operators defined, we can get to work computing matrix representations of the adjoint operators and the Lie bracket.
The adjoint operator is computed by

$$\begin{aligned}
\mathrm{Ad}_{L}(U)
&= L U L^{-1} \\
% ------------
&= \begin{pmatrix} d & b^\top \\ c & A \end{pmatrix}
\begin{pmatrix} 0 & u^\top \\ u & \omega^\times \end{pmatrix}
\begin{pmatrix} d & b^\top \\ c & A \end{pmatrix}^{-1} \\
% ------------
&= \begin{pmatrix} b^\top u & d u^\top + b^\top \omega^\times \\ 
A u & c u^\top + A \omega^\times \end{pmatrix}
\begin{pmatrix} d & -c^\top \\ -b & A^\top \end{pmatrix} \\
% ------------
&= \begin{pmatrix} d b^\top u - (d u^\top + b^\top \omega^\times) b &
- b^\top u c^\top + (d u^\top + b^\top \omega^\times) A^\top \\
d A u - (c u^\top + A \omega^\times) b &
-A u c^\top + (c u^\top + A \omega^\times) A^\top \end{pmatrix} \\
% ------------
&= \begin{pmatrix} d b^\top u - d u^\top b - b^\top \omega^\times b &
- u^\top b c^\top + d u^\top A^\top + b^\top \omega^\times A^\top \\
d A u - c u^\top b - A \omega^\times b &
-A u c^\top + c u^\top A^\top + A \omega^\times A^\top \end{pmatrix} \\
% ------------
&= \begin{pmatrix} 0 &
u^\top (d A^\top - b c^\top) + \omega b^\top 1^\times A^\top \\
(d A - c b^\top) u - A 1^\times b \omega &
c (Au)^\top - (A u) c^\top + A 1^\times A^\top \omega \end{pmatrix} \\
% ------------
&= \begin{pmatrix} 0 &
((d A - c b^\top) u - A 1^\times b \omega)^\top \\
(d A - c b^\top) u - A 1^\times b \omega &
1^\times c^\top 1^\times A u - \frac{1}{2}\mathrm{tr}(1^\times A 1^\times A^\top) 1^\times \omega \end{pmatrix} \\
\end{aligned}$$

We obtain a matrix expression for $\mathrm{Ad}_X$ by using the wedge and vee isomorphisms.
From the computations above, we obtain the Adjoint matrix by extracting the coefficients of $\omega,u$:

$$\begin{aligned}
\mathrm{Ad}_{X}^\vee
&= \begin{pmatrix}
    -\frac{1}{2}\mathrm{tr}(1^\times A 1^\times A^\top) &
    c^\top 1^\times A \\
    -A 1^\times b &
    d A - c b^\top
\end{pmatrix}
\end{aligned}$$

Differentiating this matrix in terms of the Lie group element $L$ at the identity provides the "little" adjoint matrix (and the Lie bracket)

$$\begin{aligned}
\mathrm{ad}_{U}^\vee
&= \begin{pmatrix}
    0 &
    u^\top 1^\times \\
    -1^\times u &
    \omega^\times
\end{pmatrix}, \\
[U_1, U_2] &= \mathrm{ad}_{U_1}(U_2).
\end{aligned}$$


#### Exponential and Logarithm

As in any matrix Lie group, the exponential is given by the matrix exponential.
However, this is an expensive computation, so we will try to find a simplified form that can be computed quickly.
Let $U \in \mathfrak{o}(1,2)$.
Looking at the characteristic polynomial of $U$, we have

$$
\begin{aligned}
    p(s) &:= \det(U - sI_3) \\
    &= \det \begin{pmatrix} -s & u^\top \\ u & \omega^\times - s I_2 \end{pmatrix} \\
    % ----------
    &= \det \begin{pmatrix} -s & u_1 & u_2 \\ 
    u_1 & -s & -\omega \\
    u_2 & \omega & -s\end{pmatrix} \\
    % ----------
    &= -s \det \begin{pmatrix} -s & -\omega \\ \omega & -s \end{pmatrix}
    -u_1 \det \begin{pmatrix} u_1 & -\omega \\ u_2 & -s \end{pmatrix}
    +u_2 \det \begin{pmatrix} u_1 & -s \\ u_2 & \omega \end{pmatrix} \\
    % ----------
    &= -s (s^2 + \omega^2)
    -u_1 (-u_1 s + \omega u_2)
    +u_2 (u_1 \omega + s u_2) \\
    % ----------
    &= -s^3 - s\omega^2
    +u_1^2 s - \omega u_1 u_2
    + \omega u_1 u_2 + s u_2^2 \\
    % ----------
    &= -s^3 - s\omega^2
    +s u_1^2 + s u_2^2 \\
    % ----------
    &= -s^3 + s(u_1^2 + u_2^2 -\omega^2).
\end{aligned}
$$
From here, we can apply the Caley-Hamilton theorem, which says that every matrix satisfies its own characteristic equation. In other words,

$$
\begin{gathered}
p(U) = -U^3 + U (u_1^2 + u_2^2 -\omega^2) = 0_{3\times 3}, \\
U^3 = U (u_1^2 + u_2^2 -\omega^2).
\end{gathered}
$$

This is a very useful relationship in simplifying the exponential map.
Let 
$$ q^2 = u_1^2 + u_2^2 -\omega^2, $$
noting that $q$ may be either real or pure imaginary.
Then
$$ U^3 = q^2 U, $$
and therefore

$$
\begin{aligned}
U^{2k+1} &= q^2 U^{2(k-1) + 1} = \cdots
= q^{2k} U \\
U^{2k} &= q^2 U^{2(k-1)} = \cdots = q^{2(k-1)} U^2,
\end{aligned}
$$

for all $k =1,2,3,\ldots$.
We are now ready to derive the exponential formula.
We have


$$
\begin{aligned}
\exp(U) 
&= \sum_{n=0}^\infty \frac{1}{n!} U^n \\
% ----------------
&= I_3
+ \sum_{k=0}^\infty \frac{1}{(2k+1)!} U^{2k+1}
+ \sum_{k=1}^\infty \frac{1}{(2k)!} U^{2k} \\
% ----------------
&= I_3
+ \sum_{k=0}^\infty \frac{1}{(2k+1)!} q^{2k} U
+ \sum_{k=1}^\infty \frac{1}{(2k)!} q^{2(k-1)} U^2 \\
% ----------------
&= I_3
+ \frac{1}{q}\left( \sum_{k=0}^\infty \frac{ q^{2k+1}}{(2k+1)!} \right) U
+ \frac{1}{q^2}\left(-1 + \sum_{k=0}^\infty \frac{1}{(2k)!} q^{2k} \right) U^2 \\
% ----------------
&= I_3
+ \frac{\sinh(q)}{q} U
+ \frac{\cosh(q) - 1}{q^2} U^2.
\end{aligned}
$$

This is already a very nice formula, but we need to be careful with the possibility that $q=0$ or $q$ is imaginary.
If $q^2 > 0$ then the formula can be applied directly as shown.
If $q^2 = 0$ then the formula simplifies to
$$ \exp(U) = I_3 + U + \frac{1}{2} U^2.$$
If $q^2 <0$ then we may use the identities $\sinh(x) = - i \sin(ix)$ and $\cosh(x) = \cos(ix)$ to obtain

$$
\begin{aligned}
\exp(U) &= I_3
+ \frac{\sinh(q)}{q} U
+ \frac{\cosh(q) - 1}{q^2} U^2 \\
% ----------------
&= I_3
+ \frac{-i\sin(i q)}{q} U
+ \frac{\cos(i q) - 1}{q^2} U^2 \\
% ----------------
&= I_3
+ \frac{\sin(i q)}{i q} U
+ \frac{\cos(i q) - 1}{q^2} U^2 \\
% ----------------
&= I_3
+ \frac{\sin(\sqrt{-q^2})}{\sqrt{-q^2}} U
+ \frac{\cos(\sqrt{-q^2}) - 1}{q^2} U^2.
\end{aligned}
$$

Finding an expression for the logarithm is a matter of inverting the exponential.
We therefore start by supposing that $L = \exp(U)$ and then solve for the components of $U$ (implicitly assuming that there is such a solution!).
Let $t_1 = \frac{\sinh(q)}{q}$ and $t_2 = \frac{\cosh(q)-1}{q^2}$ as shorthands.
Then,

$$
\begin{aligned}
L &= \exp(U), \\
\begin{pmatrix} d & b^\top \\ c & A \end{pmatrix}
&= \begin{pmatrix} 1 & 0_{1\times 2} \\ 0_{2\times 1} & I_2 \end{pmatrix}
+ t_1 \begin{pmatrix} 0 & u^\top \\ u & \omega^\times \end{pmatrix}
+ t_2 \begin{pmatrix} u^\top u & u^\top \omega^\times \\ \omega^\times u & u u^\top + (\omega^\times)^2 \end{pmatrix}.
\end{aligned}
$$
Taking the symmetric projection of both sides, i.e. mapping $M \mapsto \frac{1}{2} (M + M^\top)$ yields
$$
\begin{aligned}
\frac{1}{2}\begin{pmatrix} d & (b+c)^\top \\ b+c & A+A^\top \end{pmatrix}
&= \begin{pmatrix} 1 & 0_{1\times 2} \\ 0_{2\times 1} & I_2 \end{pmatrix}
+ t_1 \begin{pmatrix} 0 & u^\top \\ u & 0_{2\times 2} \end{pmatrix}
+ t_2 \begin{pmatrix} u^\top u & 0_{1\times 2} \\ 0_{2\times 1} & u u^\top + (\omega^\times)^2 \end{pmatrix}.
\end{aligned}
$$
Likewise, taking the antisymmetric projection $M \mapsto \frac{1}{2} (M - M^\top)$ yields
$$
\begin{aligned}
\frac{1}{2}\begin{pmatrix} 0 & (b-c)^\top \\ c-b & A-A^\top \end{pmatrix}
&= t_1 \begin{pmatrix} 0 & 0_{1\times 2} \\  0_{2\times 1} & \omega^\times \end{pmatrix}
+ t_2 \begin{pmatrix} 0 & u^\top \omega^\times \\ \omega^\times u & 0_{2\times 2} \end{pmatrix}.
\end{aligned}
$$
Extracting the bottom-left component of the symmetric projection equation, we can derive
$$
\begin{aligned}
\frac{1}{2}(b+c) &= t_1 u, \\
\left\vert \frac{b+c}{2} \right\vert^2  &= \vert u \vert^2 t_1^2.
\end{aligned}
$$
Extracting the bottom-right component of the antisymmetric projection equation, we also have
$$
\begin{aligned}
\frac{1}{2}(A-A^\top) &= t_1 \omega^\times, \\
\left\vert \frac{1}{2}(A-A^\top) \right\vert^2 &= t_1^2 \vert \omega^\times \vert^2, \\
\frac{1}{2}\left\vert \frac{1}{2}(A-A^\top) \right\vert^2 &= t_1^2 \vert \omega \vert^2, \\
\frac{1}{4}( A_{12} - A_{21} )^2 &= t_1^2 \omega^2, \\
\end{aligned}
$$
Recall now that $q^2 = \vert u \vert^2 - \omega^2$, so combing these equations we have
$$
\begin{aligned}
\left\vert \frac{b+c}{2} \right\vert^2 - \frac{1}{4}( A_{12} - A_{21} )^2 
&= t_1^2 \vert u \vert^2 - t_1^2 \omega^2
= t_1^2 q^2
= \sinh(q)^2.
\end{aligned}
$$
This now leads us to a solution for $q$. If we allow $q$ to be imaginary then
$$
\begin{aligned}
q = \sinh^{-1}\left( \sqrt{ \left\vert \frac{b+c}{2} \right\vert^2 - \frac{1}{4}( A_{12} - A_{21} )^2 } \right)
\end{aligned}
$$
If we do not want to use imaginary numbers, then we need to consider the case that the left-hand side is less than $0$. If this is the case, then we use the identity $\sinh(x) = -i\sin(ix)$ to obtain
$$
\begin{aligned}
\sinh(q)^2 &= \left\vert \frac{b+c}{2} \right\vert^2 - \frac{1}{4}( A_{12} - A_{21} )^2, \\
(-i\sin(iq))^2 &= \left\vert \frac{b+c}{2} \right\vert^2 - \frac{1}{4}( A_{12} - A_{21} )^2, \\
(\sin(iq))^2 &= -\left( \left\vert \frac{b+c}{2} \right\vert^2 - \frac{1}{4}( A_{12} - A_{21} )^2 \right), \\
iq &= \sin^{-1} \left( \sqrt{-\left( \left\vert \frac{b+c}{2} \right\vert^2 - \frac{1}{4}( A_{12} - A_{21} )^2 \right)} \right).
\end{aligned}
$$
The important thing is that we are able to recover $q$ or at least $iq$, from which we can then immediately compute $t_1$.
Once we have $t_1$, then we simply use the formulas obtained previously to compute
$$
\begin{aligned}
u &= \frac{b+c}{2 t_1}, &
\omega^\times &= \frac{A-A^\top}{2 t_1}, &
\omega &= \frac{A_{21}-A_{12}}{2 t_1}, &
\end{aligned}
$$
This completes the computation of the logarithm.

### Conclusion

The indefinite orthogonal group is not often seen in robotics or control theory, but is highly relevant to physics.
It is also a good chance to explore Lie group theory with a less familiar group, and particularly a group that is not overly similar to $\mathbf{SO}(3)$ or $\mathbf{SE}(3)$.
The formulas presented in this post have all been added to my python Lie group library [pylie](https://github.com/pvangoor/pylie) as well, where they have been tested for correctness.
If you spot any mistakes in this post or have any feedback, I would love to hear it!

---
layout: post
title:  "The Lie-Theoretic Exponential is Not Surjective in General"
date:   2022-07-26
categories: Mathematics
---

{% include math.html %}

In order to test that mathjax is indeed working on my site, I thought I would write a short post about an example that shows the exponential map from a Lie algebra to a Lie group is not necessarily surjective.
In the special orthogonal group $\mathbf{SO}(3)$ (one of the most commonly discussed Lie groups in robotics - the exponential is surjective, and it is even almost everywhere invertible).
However, this is not true for every Lie group, and a classic example is $\mathbf{SL}(2)$.

The Lie group $\mathbf{SL}(2)$ is defined to be the set of $2 \times 2$ matrices with determinant 1.
Its Lie algebra $\mathfrak{sl}(2)$ is exactly the set of $2 \times 2$ matrices with trace 0.
Consider the matrix

$$ H = \begin{pmatrix} -1 & 1 \\ 0 & -1 \end{pmatrix} \in \mathbf{SL}(2). $$

It is trivial to see that, indeed, the determinant of this matrix is 1.
Now let $A \in \mathfrak{sl(2)}$.
Since the trace of $A$ is 0, we may write

$$ A = \begin{pmatrix} a & b \\ c & -a \end{pmatrix} \in \mathfrak{sl}(2). $$

The exponential of $A$ is given by the power series

$$
\begin{aligned}
    \exp(A)
    &= \sum_{k=0}^\infty \frac{1}{k!} A^k.
\end{aligned}
$$

In order to calculate this, let's compute some powers of $A$.

$$
\begin{aligned}
    A^2
    &= \begin{pmatrix} a & b \\ c & -a \end{pmatrix}
    \begin{pmatrix} a & b \\ c & -a \end{pmatrix}
    = \begin{pmatrix} a^2 + bc & ab - ba \\ c a -a c & a^2 + bc \end{pmatrix}
    = \begin{pmatrix} a^2 + bc & 0 \\ 0 & a^2 + bc \end{pmatrix}, \\
    A^3
    &= \begin{pmatrix} a & b \\ c & -a \end{pmatrix} \begin{pmatrix} a^2 + bc & 0 \\ 0 & a^2 + bc \end{pmatrix}
    = \begin{pmatrix} a^3 + a b c & a^2 b + b^2 c \\ a^2 c + b c^2 & -a^3 - a bc \end{pmatrix}, \\
    A^4
    &= \begin{pmatrix} a & b \\ c & -a \end{pmatrix} \begin{pmatrix} a^3 + a b c & a^2 b + b^2 c \\ a^2 c + b c^2 & -a^3 - a bc \end{pmatrix}
    = \begin{pmatrix} a^4 + 2 a^2 bc + b^2 c^2  & 0 \\ 0 &  a^4 + 2 a^2 bc + b^2 c^2 \end{pmatrix}.
\end{aligned}
$$

The emerging pattern is a consequence of $A^2 = (a^2 + bc) I_2$.
In fact, it follows that, for any $k \in \mathbb{N}$,

$$ A^{2k} = (a^2 + bc)^k I_2, \quad A^{2k+1} = (a^2 + bc)^k A. $$

Using this insight, let us return to computing the exponential.
We have

$$
\begin{aligned}
    \exp(A)
    &= \sum_{k=0}^\infty \frac{1}{k!} A^k, \\
    &= \left( \sum_{k=0}^\infty \frac{1}{(2k)!} A^{2k} \right) + \left( \sum_{k=0}^\infty \frac{1}{(2k+1)!} A^{2k+1} \right), \\
    &= \left( \sum_{k=0}^\infty \frac{1}{(2k)!} (a^2 + bc)^k I_2 \right) + \left( \sum_{k=0}^\infty \frac{1}{(2k+1)!} (a^2 + bc)^k A \right), \\
    &= \left( \sum_{k=0}^\infty \frac{(\sqrt{a^2 + bc})^{2k}}{(2k)!}  I_2 \right) + \left( \sum_{k=0}^\infty \frac{(\sqrt{a^2 + bc})^{2k}}{(2k+1)!} A \right), \\
    &= \left( \sum_{k=0}^\infty \frac{(\sqrt{a^2 + bc})^{2k}}{(2k)!}  I_2 \right) + \frac{1}{\sqrt{a^2 + bc}}\left( \sum_{k=0}^\infty \frac{(\sqrt{a^2 + bc})^{2k+1}}{(2k+1)!} A \right), \\
    &= \cosh(\sqrt{a^2 + bc})  I_2 + \frac{\sinh(\sqrt{a^2 + bc})}{\sqrt{a^2 + bc}} A.
\end{aligned}
$$

Isn't that interesting!
If you're not sure where the hyperbolic sin and cos functions came from, have a look at their [series expansions](https://en.wikipedia.org/wiki/Hyperbolic_functions#Taylor_series_expressions).
From here, let $\theta = \sqrt{a^2 + bc}$.
Formally, the expression $\frac{\sinh(\theta)}{\theta}$ is only valid for $\theta \neq 0$.
However, to simplify the infinite series we will use the expression as if $\theta \neq 0$, and at the point $\theta = 0$ replace the undefined value of $\frac{\sinh(\theta)}{\theta}$ with its limit as $\theta \to 0$.
This is given by $\lim_{\theta \to 0}\frac{\sinh(\theta)}{\theta} = 1$.
Then,

$$
\begin{aligned}
    \exp(A)
    &= \cosh(\theta)  I_2 +\sinh(\theta) A, \\
    &= \begin{pmatrix} \cosh(\theta) & 0 \\ 0 & \cosh(\theta) \end{pmatrix}
    + \begin{pmatrix} \frac{\sinh(\theta)}{\theta} a & \frac{\sinh(\theta)}{\theta} b \\ \frac{\sinh(\theta)}{\theta} c & -\frac{\sinh(\theta)}{\theta} a \end{pmatrix} , \\
    &= \begin{pmatrix} \cosh(\theta) + \frac{\sinh(\theta)}{\theta} a & \frac{\sinh(\theta)}{\theta} b \\ \frac{\sinh(\theta)}{\theta} c & \cosh(\theta)-\frac{\sinh(\theta)}{\theta} a \end{pmatrix}.
\end{aligned}
$$


In order for this to be the matrix $H$ we considered at the start, we require that the '1,1' and '2,2' entries are equal to -1 (and therefore each other).

$$\cosh(\theta) + \frac{\sinh(\theta)}{\theta} a = -1 = \cosh(\theta) - \frac{\sinh(\theta)}{\theta} a$$

Therefore either $\frac{\sinh(\theta)}{\theta} = 0$ or $a = 0$.

The first case $\frac{\sinh(\theta)}{\theta} = 0$ is impossible.
This is because the only value of $\theta$ for which $\sinh(\theta) = 0$ is $\theta = 0$, but as discussed $\lim_{\theta \to 0}\frac{\sinh(\theta)}{\theta} = 1$.
In other words, the numerator is never zero outside of the limit case, where the whole fraction evaluates to $1$.
Therefore the fraction $\frac{\sinh(\theta)}{\theta}$ can never be zero.

Now consider the second case $a = 0$.
From the bottom-left '2,1' cell, we require that $\frac{\sinh(\theta)}{\theta} c = 0$. Since $\frac{\sinh(\theta)}{\theta}$ cannot be zero (see the first case), it must be that $c = 0$.
Now, since $c = 0$ and $a = 0$, then $\theta = \sqrt{0^2 + 0b} = 0$.
But this means that $\cosh(\theta) = \cosh(0) = 1$, and thus the '1,1' and '2,2' cells are not equal to $-1$.

In summary, neither case is possible, since assuming either case to be true leads to a contradiction. It follows that there is no choice of $a,b,c \in \mathbb{R}$ such that $\exp(A) = H$.

### Conclusion

This example shows that the exponential map is not surjective for any Lie group.
While this seems like a minor detail and a bit of an artificial problem, in my opinion examples like this are important for building intuition around mathematical structures, and often lead to better insight and intuition down the track.

It also looks like my mathjax is working!
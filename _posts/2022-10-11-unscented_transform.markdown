---
layout: post
title:  "The Unscented Transform"
date:   2022-10-11
categories: Mathematics
---

{% include math.html %}

### Introduction

The unscented transform is a way to approximate the probability distribution of a variable that is normally distributed after it is put through a nonlinear function.
Concretely, let's suppose that $x \sim N(\mu, \Sigma)$, and let $f : \mathbb{R}^n \to \mathbb{R}^m$ be some nonlinear function.
Then we might ask: how can we approximate the distribution of $f(x)$ by another normal distribution?

The 'traditional' approach is through linearisation.
We know that if $f$ is a linear or affine mapping, $f(x) = A x + b$, then the distribution of $f(x)$ is given by

$$
Ax+b \sim N(A\mu + b, A\Sigma A^\top)
$$

So one way to approximate the distribution of $f(x)$ for a nonlinear $f$ is to simply say

$$
f(x) 
\approx f(\mu) + D f(\mu)[x-\mu]
\sim N(f(\mu), D f(\mu) \Sigma D f(\mu)^\top),
$$

where $Df(\mu)$ is the differential (Jacobian) of $f$ at $\mu$.
The problem is that this may not be a very good approximation, so what else can we do?

### Sigma Points

What if, instead of trying to approximate $f$ and then applying it to the distribution, we approximate the distribution and then apply $f$?
This is the idea of the unscented transform.
But how can we approximate the distribution?
The answer is 'sigma points'.
A set of sigma points $S$ for the distribution $N(\mu, \Sigma)$ consists of points $x^{(i)}$ and weights $w^{(i)}$ so that
1. $\sum_i w^{(i)} = 1$,
2. $\sum_i w^{(i)} x^{(i)} = \mu$,
3. $\sum_i w^{(i)} (x^{(i)} - \mu)(x^{(i)} - \mu)^\top = \Sigma$.

This approximates the original distribution if you interpret it as a probability function.
Let $\Omega = \{ x^{(i)} \mid i=0,1,...,p \}$, define a probability function $p: \Omega \to \mathbb{R}$ by $p(x^{(i)}) = w^{(i)}$, and let $x$ be a random variable distributed according to $p$. Then,
1. $\sum_{x \in \Omega} p(x) = \sum_i w^{(i)} = 1$,
2. $\mathbb{E}[x] = \sum_i w^{(i)} x^{(i)} = \mu$,
3. $\mathrm{cov}(x,x) = \mathbb{E}\left[ (x - \mathbb{E}[x])(x - \mathbb{E}[x])^\top \right] = \sum_i w^{(i)} (x^{(i)} - \mu)(x^{(i)} - \mu)^\top = \Sigma$.

Now, this is only possible if there are at least $n+1$ points, but there is no unique choice of sigma points.
However, the original choice by Uhlmann gives us a 'canonical' choice; for $i = 1,..., 2n$ define

$$
\begin{aligned}
w^{(i)} &= \frac{1}{2n}, &
x^{(i)} &= \mu + 
\begin{cases} 
(\sqrt{n \Sigma})_i & \text{if }  i \leq n \\
-(\sqrt{n \Sigma})_i & \text{if } i > n
\end{cases}
\end{aligned}
$$

Here $(\sqrt{n\Sigma})_i$ denotes the $i$th column of the matrix square-root of $\Sigma$ multiplied by $n$.
Specifically, if $A = \sqrt{n \Sigma}$, then $A A^\top = n \Sigma$.

### Unscented Transform

Now that we have a set of sigma points that approximate the original distribution, we need to apply the nonlinear function $f$.
This time, instead of approximating $f$, we simply apply it to our sigma points and gather statistics at the end.
Let $x$ be a random variable distributed according to the sigma points.
Then we compute the mean and covariance of $f(x)$ as follows.

$$
\begin{aligned}
\hat{\eta} 
&:= \mathbb{E} \left[ f(x) \right], \\
&= \sum_i w^{(i)} f(x^{(i)}), \\
%-----------------------------
\hat{\Sigma} 
&:= \mathbb{E} \left[ (f(x) - \mathbb{E} \left[ f(x) \right])(f(x) - \mathbb{E} \left[ f(x) \right])^\top \right], \\
&= \mathbb{E} \left[ (f(x) - \hat{\eta})(f(x) - \hat{\eta})^\top \right], \\
&= \sum_i w^{(i)} (f(x^{(i)}) - \hat{\eta})(f(x^{(i)}) - \hat{\eta})^\top.
\end{aligned}
$$

This is how we now approximate $f(x)$: we say that, approximately, $f(x) \sim N(\hat{\eta}, \hat{\Sigma})$.
This is quite different from the linearisation approach, but is it any better?
That depends on the function $f$, the choice of sigma points, and also on what you mean by "better".

### Analysis

How does the unscented transform compare to the true distribution of $f(x)$?
Let $x \sim N(\mu, \Sigma)$, and let $s = x - \mu \sim N(0, \Sigma)$.
Then we can calculate the expected value of $f(x)$ by using a Taylor expansion,

$$
\begin{aligned}
\mathbb{E} \left[ f(x) \right]
&= \mathbb{E} \left[ f(\mu + s) \right], \\
&= \mathbb{E} \left[
    f(\mu) + Df(\mu)[s] + \frac{1}{2} D^2 f(\mu)[s,s] + \cdots
\right], \\
&= \mathbb{E} [f(\mu)]
    + Df(\mu) \mathbb{E} [s]
    + \frac{1}{2} D^2 f(\mu) \mathbb{E}[s,s]
    + \cdots, \\
&= f(\mu)
    + Df(\mu) [0]
    + \frac{1}{2} D^2 f(\mu) \mathrm{cov}(s,s)
    + \cdots, \\
&= f(\mu) + \frac{1}{2} D^2 f(\mu) \Sigma
    + O(\mathbb{E}[\vert s \vert^3]).
\end{aligned}
$$

In other words, the expected value of $f(x)$ is determined by the mean and covariance of $x$ up to third order deviations from the mean.
In particular, this means that the unscented transform gives the correct transformed distribution for all functions $f$ where $D^k f = 0$ for $k \geq 3$; that is, functions $f$ that are degree 2 polynomials.
In fact, using the canonical choice of sigma points, this is true for polynomials of degree 3 as well.

What about the covariance obtained from the unscented transform?
It turns out that this is equal to the covariance obtained from the unscented transform only when $f$ is a first-order (linear-affine) function.
However, practical experience has shown that it can offer better performance in a range of applications.

### Conclusion

The unscented transform provides a different way to propagate uncertainty through nonlinear functions than the "standard" approach of linearisation.
Rather than approximate the function as a linear function, it approximates the probability distribution as a discrete probability function.
This has the advantage that there is no need to compute the derivative of a function to linearise it, and propagates the mean of the function more accurately than the linearisation approach.
In practice, a number of applications show that the unscented transform can outperform the linearisation approach.
Overall, in my view it is a very interesting perspective on approximations to probability that is not widely enough understood.

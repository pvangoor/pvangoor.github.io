---
layout: post
title:  "New Paper: Synchronous observer design for Inertial Navigation Systems with almost-global convergence"
date:   2025-04-25
categories: Papers
---

{% include math.html %}

I am very happy to announce that our new work on observer design for inertial navigation with GNSS and magnetometer measurements has been published in Automatica!
An Inertial Navigation System (INS) is used to estimate the attitude, velocity, and position of a vehicle by combining measurements from an Inertial Measurement Unit (IMU) with other supporting sensors, such as GNSS, magnetometer, etc.
The main idea behind this paper was to use the fact the dynamics of INS are "group-affine" to create a completely novel observer architecture, which could then be leveraged to design correction terms that guarantee almost-global asymptotic stability of the observer error.
In other words, from practically any initial condition, the estimate provided by the observer we designed in this paper is guaranteed to converge to the true state of the system.
This contrasts with existing methods, which either have a limited domain of convergence, or require high gains to increase the domain of convergence leading to high sensitivity to noise.

I would like to thank my coauthors Tarek Hamel and Robert Mahony for their contributions to this work.
It really came about from a collaborative process of sharing ideas and identifying and overcoming difficulties together.
Finally, if you are interested in this work or have questions, please don't hesitate to reach out!

**Paper**:
<https://www.sciencedirect.com/science/article/pii/S0947358024001079>

**Preprint**:
<https://arxiv.org/abs/2311.02234>

**Code**:
<https://github.com/pvangoor/synchronous_INS>

**Abstract**:
Inertial Navigation Systems (INS) estimate a vehicle’s navigation states (attitude, velocity, and position) by combining measurements from an Inertial Measurement Unit (IMU) with other supporting sensors, typically including a Global Navigation Satellite System (GNSS) and a magnetometer. Recent nonlinear observer designs for INS provide powerful stability guarantees but do not account for some of the real-world challenges of INS. One of the key challenges is to account for the time-delay characteristic of GNSS measurements. This paper addresses this question by extending recent work on synchronous observer design for INS. The delayed GNSS measurements are related to the state at the current time using recursively-computable delay matrices, and this is used to design correction terms that leads to almost-globally asymptotic and locally exponential stability of the error. Simulation results verify the proposed observer and show that the compensation of time-delay is key to both transient and steady-state performance.

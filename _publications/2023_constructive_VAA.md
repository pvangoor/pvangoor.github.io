---
layout: publication
title: Constructive Equivariant Observer Design for Inertial Velocity-Aided Attitude
authors: [Pieter van Goor, Tarek Hamel, Robert Mahony]
link: https://www.sciencedirect.com/science/article/pii/S2405896323016336
venue: 12th IFAC Symposium on Nonlinear Control Systems NOLCOS 2022
pub_date: 2023
pub_type: conference
---

Inertial Velocity-Aided Attitude (VAA), the estimation of the velocity and attitude of a vehicle using gyroscope, accelerometer, and inertial-frame velocity (e.g. GPS velocity) measurements, is an important problem in the control of Remotely Piloted Aerial Systems (RPAS). Existing solutions provide limited stability guarantees, relying on local linearisation, high gain design, or assuming specific trajectories such as constant acceleration of the vehicle. This paper proposes a novel non-linear observer for inertial VAA with almost globally asymptotically and locally exponentially stable error dynamics. The approach exploits Lie group symmetries of the system dynamics to construct a globally valid correction term. To the authors’ knowledge, this construction is the first observer to provide almost global convergence for the inertial VAA problem. The observer performance is verified in simulation, where it is shown that the estimation error converges to zero even with an extremely poor initial condition.

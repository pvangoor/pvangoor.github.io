---
layout: publication
title: Constructive Equivariant Observer Design for Inertial Navigation
authors: [Pieter van Goor, Tarek Hamel, Robert Mahony]
link: https://www.sciencedirect.com/science/article/pii/S2405896323016336
venue: 22nd IFAC World Congress
pub_date: 2023
pub_type: conference
---

Inertial Navigation Systems (INS) are algorithms that fuse inertial measurements of angular velocity and specific acceleration with supplementary sensors including GNSS and magnetometers to estimate the position, velocity and attitude, or extended pose, of a vehicle. The industry-standard extended Kalman filter (EKF) does not come with strong stability or robustness guarantees and can be subject to catastrophic failure. This paper exploits a Lie group symmetry of the INS dynamics to propose the first nonlinear observer for INS with error dynamics that are almost-globally asymptotically and locally exponentially stable, independently of the chosen gains. The observer is aided only by a GNSS measurement of position. As expected, the convergence guarantee depends on persistence of excitation of the vehicle's specific acceleration in the inertial frame. Simulation results demonstrate the observer's performance and its ability to converge from extreme errors in the initial state estimates.

---
layout: publication
title: 'Synchronous Observer Design for Inertial Navigation Systems with Almost-Global Convergence'
authors: [Pieter Van Goor, Tarek Hamel, Robert Mahony]
link: https://arxiv.org/abs/2311.02234
venue: arXiv:2311.02234
pub_date: 2023
pub_type: preprint
---

An Inertial Navigation System (INS) is a system that integrates acceleration and angular velocity readings from an Inertial Measurement Unit (IMU), along with other sensors such as GNSS position, GNSS velocity, and magnetometer, to estimate the attitude, velocity, and position of a vehicle. This paper shows that the INS problem can be analysed using the automorphism group of the extended special Euclidean group: a group we term the extended similarity group. By exploiting this novel geometric framework, we propose an observer architecture with synchronous error dynamics; that is, the error is stationary if the observer correction terms are set to zero. In turn, this enables us to derive a modular, or plug-and-play, observer design for INS that allows different sensors to be added or removed depending on what is available in the vehicle sensor suite. We prove both almost-global asymptotic and local exponential stability of the error dynamics for the common scenario of at least IMU and GNSS position. To the authors' knowledge, this is the first non-linear observer design with almost global convergence guarantees or with plug-and-play modular capability. A simulation with extreme initial error demonstrates the almost-global robustness of the system. Real-world capability is demonstrated on data from a fixed-wing UAV, and the solution is compared to the state-of-the-art ArduPilot INS.

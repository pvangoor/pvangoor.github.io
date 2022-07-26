---
layout: publication
title: "EqVIO: An Equivariant Filter for Visual Inertial Odometry"
authors: [Pieter van Goor, Robert Mahony]
link: https://arxiv.org/abs/2205.01980
venue: arXiv preprint arXiv:2205.01980
pub_date: 2022
---

Visual Inertial Odometry (VIO) is the problem of estimating a robot's trajectory by combining information from an inertial measurement unit (IMU) and a camera, and is of great interest to the robotics community. This paper develops a novel Lie group symmetry for the VIO problem and applies the recently proposed equivariant filter. The symmetry is shown to be compatible with the invariance of the VIO reference frame, lead to exact linearisation of bias-free IMU dynamics, and provide equivariance of the visual measurement function. As a result, the equivariant filter (EqF) based on this Lie group is a consistent estimator for VIO with lower linearisation error in the propagation of state dynamics and a higher order equivariant output approximation than standard formulations. Experimental results on the popular EuRoC and UZH-FPV datasets demonstrate that the proposed system outperforms other state-of-the-art VIO algorithms in terms of both speed and accuracy.

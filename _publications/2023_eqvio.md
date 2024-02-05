---
layout: publication
title: "EqVIO: An Equivariant Filter for Visual Inertial Odometry"
authors: [Pieter van Goor, Robert Mahony]
link: https://ieeexplore.ieee.org/abstract/document/10179117/
venue: IEEE Transactions on Robotics
pub_date: 2023
pub_type: journal
---

Visual-inertial odometry (VIO) is the problem of estimating a robot's trajectory by combining information from an inertial measurement unit (IMU) and a camera and is of great interest to the robotics community. This article develops a novel Lie group symmetry for the VIO problem and applies the recently proposed equivariant filter. The proposed symmetry is compatible with the invariance of the VIO reference frame, leading to improved filter consistency. The bias-free IMU dynamics are group-affine, ensuring that filter linearization errors depend only on the bias estimation error and measurement noise. Furthermore, visual measurements are equivariant with respect to the symmetry, enabling the application of the higher order equivariant output approximation to reduce the approximation error in the filter update equation. As a result, the equivariant filter based on this Lie group is a consistent estimator for VIO with lower linearization error in the propagation of state dynamics and a higher order equivariant output approximation than standard formulations. Experimental results on the popular EuRoC and UZH FPV datasets demonstrate that the proposed system outperforms other state-of-the-art VIO algorithms in terms of both speed and accuracy.

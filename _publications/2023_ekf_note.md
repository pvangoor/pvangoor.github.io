---
layout: publication
title: Reprojection Methods for Koopman-Based Modelling and Prediction
authors: [Yixiao Ge, Pieter van Goor, Robert Mahony]
link: https://ieeexplore.ieee.org/abstract/document/10383899
venue: 2023 62nd IEEE Conference on Decision and Control (CDC)
pub_date: 2023
pub_type: conference
---

The kinematics of many control systems, especially in the robotics field, naturally live on smooth manifolds. Most classical state-estimation algorithms, including the extended Kalman filter, are posed on Euclidean space. Although any filter algorithm can be adapted to a manifold setting by implementing it in local coordinates and ignoring the geometric structure, it has always been clear that there would be advantages in taking the geometric structure into consideration in developing the algorithm. In this paper, we argue that the minimum geometric structure required to adapt the extended Kalman filter to a manifold is that of an affine connection. With this structure, we show that a naive coordinate implementation of the EKF fails to account for geometry of the manifold in the update step and in the reset step. We provide geometric modifications to the classical EKF based on parallel transport of the measurement covariance (for the update) and a-posteriori state covariance (for the reset) that address these limitations. Preliminary results for attitude estimation with two directional measurements demonstrate that the proposed modifications significantly improve the transient behavior of the filter.

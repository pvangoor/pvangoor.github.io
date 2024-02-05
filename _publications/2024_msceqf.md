---
layout: publication
title: 'MSCEqF: A Multi State Constraint Equivariant Filter for Vision-Aided Inertial Navigation'
authors: [Alessandro Fornasier, Pieter Van Goor, Eren Allak, Robert Mahony, Stephan Weiss]
link: https://ieeexplore.ieee.org/abstract/document/10325586
venue: IEEE Robotics and Automation Letters
pub_date: 2024
pub_type: journal
---

This letter re-visits the problem of visual-inertial navigation system (VINS) and presents a novel filter design we dub the multi state constraint equivariant filter (MSCEqF, in analogy to the well known MSCKF). We define a symmetry group and corresponding group action that allow specifically the design of an equivariant filter for the problem of visualinertial odometry (VIO) including IMU bias, and camera intrinsic and extrinsic calibration states. In contrast to state-of-the-art invariant extended Kalman filter (IEKF) approaches that simply tack IMU bias and other states onto the \mathbf SE_2(3) group, our filter builds upon a symmetry that properly includes all the states in the group structure. Thus, we achieve improved behavior, particularly when linearization points largely deviate from the truth (i.e., on transients upon state disturbances). Our approach is inherently consistent even during convergence phases from significant errors without the need for error uncertainty adaptation, observability constraint, or other consistency enforcing techniques. This leads to greatly improved estimator behavior for significant error and unexpected state changes during, e.g., long-duration missions. We evaluate our approach with a multitude of different experiments using three different prominent real-world datasets.

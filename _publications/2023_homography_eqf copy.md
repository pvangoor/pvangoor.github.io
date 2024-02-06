---
layout: publication
title: Equivariant Filter for Feature-Based Homography Estimation for General Camera Motion
authors: [Tarek Bouazza, Katrina Ashton, Pieter van Goor, Robert Mahony]
link: https://ieeexplore.ieee.org/abstract/document/10383627
venue: 2023 62nd IEEE Conference on Decision and Control (CDC)
pub_date: 2023
pub_type: conference
---

Recent advances in nonlinear observer design for homography estimation have exploited the Lie group structure of SL(3). Existing work requires the group (homography) velocity input, while the available measurements are typically only the camera velocity. Consequently, prior contributions exploiting the SL(3) geometry either reconstruct the group velocity or restrict the camera motion to allow adaptive estimation of the group velocity online. This paper presents a novel symmetry-based approach to observer design for the more general problem of estimating both the homography and the structure parameters of a planar scene, allowing homography estimation for arbitrary trajectories using only camera velocity measurements and direct point-feature corre-spondences between images. A new Lie group is introduced for the homography and structure parameters, whose symmetry structure is exploited to establish the system and output equivariance properties. We show that the system kinematics admit an equivariant lift, and the proposed observer is then designed based on the recently developed Equivariant Filter framework. Simulation results demonstrate the performance and consistency of the proposed approach.

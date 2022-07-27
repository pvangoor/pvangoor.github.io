---
layout: post
title:  "EqVIO Paper and Code"
date:   2022-05-05
categories: [Papers, Code]
---

Our [latest research on equivariant filtering](https://arxiv.org/abs/2205.01980) for VIO is now publicly available on arxiv.
The [code used in the paper](https://github.com/pvangoor/eqvio) is also available on github under the GNU GPLv3 license.
This paper is an extension and improvement over our previous work published in ICRA, and we have decided to call the resulting VIO system "EqVIO".
Have a look at the following videos to see the system working on `V2_03_difficult` from the EuRoC dataset and `indoor_forward_7` from the UZH FPV dataset.

<!-- EuRoC video -->
<iframe style="display: block; margin: auto;" width="560" height="315" src="https://www.youtube.com/embed/5y9vs0QASVY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<br>

<!-- UZH FPV video -->
<iframe style="display: block; margin: auto;" width="560" height="315" src="https://www.youtube.com/embed/8VfhjTl7kPQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<br>

### Abstract

Visual Inertial Odometry (VIO) is the problem of estimating a robot's trajectory by combining information from an inertial measurement unit (IMU) and a camera, and is of great interest to the robotics community.
This paper develops a novel Lie group symmetry for the VIO problem and applies the recently proposed equivariant filter.
The symmetry is shown to be compatible with the invariance of the VIO reference frame, lead to exact linearisation of bias-free IMU dynamics, and provide equivariance of the visual measurement function.
As a result, the equivariant filter (EqF) based on this Lie group is a consistent estimator for VIO with lower linearisation error in the propagation of state dynamics and a higher order equivariant output approximation than standard formulations.
Experimental results on the popular EuRoC and UZH-FPV datasets demonstrate that the proposed system outperforms other state-of-the-art VIO algorithms in terms of both speed and accuracy. 
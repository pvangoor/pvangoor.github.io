---
layout: publication
title: Autonomous Error and Constructive Observer Design for Group Affine Systems
authors: [Pieter van Goor, Robert Mahony]
link: https://ieeexplore.ieee.org/abstract/document/9683560/
venue: 2021 60th IEEE Conference on Decision and Control (CDC)
pub_date: 2021
pub_type: conference
---

Many nonlinear systems in robotics and avionics can be represented as group affine dynamical systems on Lie groups. For such systems, the classical pre-observer error dynamics are state-independent but not autonomous (depending on the input signal), making global constructive observer design difficult, although linearisation based observers such as the IEKF are applicable. In this paper, we show that any group affine system can be represented as the sum of a left-invariant vector field and a vector field in the automorphism Lie algebra of the group. This structure is exploited to define a novel geometry-based observer architecture with an autonomous (independent of both the observer state and the input signal) global pre-observer error. The autonomy of the pre-observer error dynamics enables the design of simple observers for group affine systems without the need for linearisation. An example of estimating the relative SE(3) transformation between two vehicles shows the effectiveness of the proposed observer architecture in aiding constructive observer design.

---
layout: publication
title: Exploiting spatial group error and synchrony for a unicycle tracking controller
authors: [Matthew Hampsey, Pieter Van Goor, Robert Mahony]
link: https://arxiv.org/abs/2311.03007
venue: arXiv:2311.03007
pub_date: 2023
pub_type: preprint
---

Trajectory tracking for the kinematic unicycle has been heavily studied for several decades. The unicycle admits a natural $\SE(2)$ symmetry, a key structure exploited in many of the most successful nonlinear controllers in the literature. To the author's knowledge however, all prior work has used a body-fixed, or left-invariant, group error formulation for the study of the tracking problem. In this paper, we consider the spatial, or right-invariant, group error in the design of a tracking controller for the kinematic unicycle. We provide a physical interpretation of the right-invariant error and go on to show that the associated error dynamics are drift-free, a property that is not true for the body-fixed error. We exploit this property to propose a simple nonlinear control scheme for the kinematic unicycle and prove almost-global asymptotic stability of this control scheme for a class of persistently exciting trajectories. We also verify performance of this control scheme in simulation for an example trajectory.

---
layout: post
title:  "Ardupilot Conference Presentation: EqF VIO"
date:   2021-03-17 16:38:21 +1100
categories: Talks
---
Prof. Mahony and I gave a talk at the [ardupilot](https://ardupilot.org/) developer conference, discussing the Equivariant Filter for Visual Inertial Odometry.
In the first half of the talk (until around 33min), Rob covers some of the theory and geometric concepts that are used to develop the filter.
In the second half, I describe the technical challenges in taking our research code, and applying it to real-world data from an outdoor flight at ANU's spring valley field robotics facility.

<iframe style="display: block; margin: auto;" width="560" height="315" src="https://www.youtube.com/embed/vLZdBKRjRi4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

I would like to thank Tridge and the other ardupilot developers for the opportunity to give this talk.
I would also like to thank the ardupilot community for their friendly engagement with us during the questions and afterwards via private emails.

The code used to generate the results shown during the presentation is based on research to be published in ICRA 2021 (preprint available on [arxiv](https://arxiv.org/abs/2104.03532).
The research version of the code is available at [eqf_vio](https://github.com/pvangoor/eqf_vio).
We are actively working on making improved code available to the ardupilot community.
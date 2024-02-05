---
layout: publication
title: 'Event Blob Tracking: An Asynchronous Real-Time Algorithm'
authors: [Ziwei Wang, Timothy Molloy, Pieter Van Goor, Robert Mahony]
link: https://arxiv.org/abs/2307.10593
venue: arXiv:2307.10593
pub_date: 2023
pub_type: preprint
---

Event-based cameras have become increasingly popular for tracking fast-moving objects due to their high temporal resolution, low latency, and high dynamic range. In this paper, we propose a novel algorithm for tracking event blobs using raw events asynchronously in real time. We introduce the concept of an event blob as a spatio-temporal likelihood of event occurrence where the conditional spatial likelihood is blob-like. Many real-world objects generate event blob data, for example, flickering LEDs such as car headlights or any small foreground object moving against a static or slowly varying background. The proposed algorithm uses a nearest neighbour classifier with a dynamic threshold criteria for data association coupled with a Kalman filter to track the event blob state. Our algorithm achieves highly accurate tracking and event blob shape estimation even under challenging lighting conditions and high-speed motions. The microsecond time resolution achieved means that the filter output can be used to derive secondary information such as time-to-contact or range estimation, that will enable applications to real-world problems such as collision avoidance in autonomous driving.

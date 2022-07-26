---
layout: publication
title: Event Camera Calibration of Per-pixel Biased Contrast Threshold
authors: [Ziwei Wang, Yonhon Ng, Pieter van Goor, Robert Mahony]
link: https://arxiv.org/abs/2012.09378
venue: arXiv preprint arXiv:2012.09378
pub_date: 2020
---

Event cameras output asynchronous events to represent intensity changes with a high temporal resolution, even under extreme lighting conditions. Currently, most of the existing works use a single contrast threshold to estimate the intensity change of all pixels. However, complex circuit bias and manufacturing imperfections cause biased pixels and mismatch contrast threshold among pixels, which may lead to undesirable outputs. In this paper, we propose a new event camera model and two calibration approaches which cover event-only cameras and hybrid image-event cameras. When intensity images are simultaneously provided along with events, we also propose an efficient online method to calibrate event cameras that adapts to time-varying event rates. We demonstrate the advantages of our proposed methods compared to the state-of-the-art on several different event camera datasets.

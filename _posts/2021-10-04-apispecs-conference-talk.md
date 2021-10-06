---
layout: post
title: API Specs Conference talk
date: 2021-10-04 19:54
tags: api
excerpt_separator: <!--more-->
---

I should have mentioned this earlier, but last week I wrapped a talk at [API Specs Conference 2021](https://events.linuxfoundation.org/openapi-asc/). It was called ["We brought OpenAPI Docs into our service catalog. Now what?"](https://apispecs21.sched.com/event/lMM1). My colleague Zoe Song and I told the story of how we grabbed [OpenAPI docs](https://www.openapis.org/) from microservices at Wayfair, and loaded them into [Backstage](https://backstage.io/) - and we talked about what we learned along the way. I believe the Youtube video should be live next week.

<!--more-->

It went pretty well! Got some nice questions from the crowd and we had a pretty decent-sized audience. I think it's pretty clear that there's still a huge outstanding question in the industry surrounding API governance - in a microservices world, where teams are encouraged to spin up lots of services which they own *in toto*, how do we ensure or at least encourage uniformity of developer experience? I have some thoughts around this question - especially around providing good defaults and leading developers into the [pit of success](https://shaisachs.com/2021/03/27/falling-into-the-pit-of-success.html) - but it's clear that there's no obvious answer just yet. Should be interesting to see how this issue shakes out over time!
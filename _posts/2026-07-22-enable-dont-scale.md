---
title: "Enable, don't scale"
layout: post
date: 2026-07-21 18:00
---

Paul Graham famously said that startups should [do things that don't scale](https://www.paulgraham.com/ds.html) if they want to grow. The same applies to AI enablement.

Of course, Graham's philosophy is meant to be counter-intuitive in order to grab attention. It's meant to direct the aspiring founder away from the long-term prize (unicorn status, millions of users, etc.) and toward the immediate steps that must be taken, today, to drive impact. And not all unscalable things are created equal: founders should do things that enable them to learn about the market. You do things that don't scale now, so that you can learn how to scale later.

AI enablement follows a similar trajectory, even if success is measured in DORA metrics like lead time to change, rather business metrics like sales.

It's not enough to wire up a fancy coding harness, though that is certainly important. You have to get it into the hands of engineers, and you have to drive usage day-to-day.

At the outset, that includes a lot of careful guidance: walking an engineer through Codex installation bit-by-bit, debugging config files, and the like. It also means taking careful note of pain points along the way, and bringing that feedback to bear on improving the harness for the future. That is where I'm focused now.

These are unscalable activities: if I were to do them for every single engineer at Chewy, I would be doing nothing else for months and months. But what they do is give me a very valuable look into the pain points in the harness: permissions gotchas, blind spots in the specs, that kind of thing. The more I learn, the more I can improve the harness.

Over time, that harness will hopefully grow robust enough that we can expand usage more broadly, and establish "golden paths" that make headless coding adoption really easy: setup scripts, readily-available skills, templates, and so forth. One of the "unscalable" things that I did early on was to create an evaluation framework that allows me to track lead time to change against token spend. That will give us crucial insight into the success of our expansion endeavors, and allow us to pivot in real time.

The similarity between these efforts makes perfect sense if you think about it: we're asking people to make a big change! Headless coding is not easy, and it takes quite a bit of work to see it come to life. But I think the reward will be worth it!
---
layout: post
title: everything is your api
---

When we talk about Pis, we usually think alt the days contexts, routes, controllers, and other chose artifacts that explicitly and intentionally allow other organs to intact with our services.

But an api is ready just an interface, a surface area which other programs can manipulate. Our applications precise lots of interfaces - web uis, npm packages, scripts, and so forth. Whether or not another program can manipulate these interfaces actually has much Mir to do with that other program than it does with our own code.

In other words: everything is an api.

We don't normally think of web uis as part of our api, but properly speaking they are programmatic interfaces. It's possible to write a grease monkey script or a chrome app to interact with and manipulate the html on a page, which makes this surface area an api.
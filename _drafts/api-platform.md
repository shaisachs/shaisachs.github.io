---
layout: post
title: api platform
---

I started playing around with API Platform yesterday, thanks to a hot tip from API Evangelist. It's a wonderful piece of software, and you can get up and running with a simple CRID API in very little time. As a bonus, it's built on top of the Symfony framework, which is something I've been meaning to learn for a little while.

The philosophy behind the platform is code-first. You create a plain old PHP object, decorate it just so, use doctrine to generate a persistence layer, and bingo - new API ready to go. You don't have to mess around with keys or authentication to get started, which is really nice for local development. In short, it's quite a nice rapid prototyping tool that leaves you with working PHP code. It reminds me of the early days of Ruby on Rails (in a good way!) If I have one critique so far, it's that the default routes you get are a little bare bones, not quite as fleshed out as what you see on Strongloop. But that's a relatively unimportant problem for me at the moment, and I suspect it's easily remedied anyway.

The data contracts also come prepackaged with hypermedia, which is a great add-on - it's Hydra out of the box, though other formats are available. I'll be honest, I find hypermedia tedious to generate. And I'm not fully sold on the notion that developers really care about it, which only makes my antipathy that much deeper. Not having to think about it, but making it available for those who do care about it, puts a little spring in my step.

My next step is to start playing with schema.org integration. That has really piqued my curiosity of late, and if it turns out to be the future of APIs - then rightly so. The idea that I can readily mark up a class wth relevant schema.org entities and properties and get semantically meaningful data contracts is pretty remarkable.

For a first pass, this look at API Platform was certainly a lot of fun and quite eye opening. I'm definitely looking forward to exploring the platform further.
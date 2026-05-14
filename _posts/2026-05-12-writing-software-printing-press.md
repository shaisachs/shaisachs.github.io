---
title: "Writing a software printing press"
layout: post
date: 2026-05-12 20:00
bannerimg: /img/posts/books.jpg
photographer: Annie Spratt
photographerurl: https://unsplash.com/@anniespratt
linkedinpost: https://www.linkedin.com/posts/shaisachs_im-writing-a-software-printing-press-inspired-share-7459799036351430656-SvFu
---

I'm writing a software printing press. You can find my code at [https://github.com/shaisachs/software-press](https://github.com/shaisachs/software-press).

Inspired in large part by Riché Zamor's awesome [software factory post](https://www.richezamor.com/thinking/building-a-14-agent-software-factory), I decided to steal his idea and containerize it. I have a bunch of oddball software project ideas, and I want to finally see them take shape! So I'm building the thing to build the thing.

My first step is to create a pretty simple single-agent container. The container takes a workspace as input, and launches ollama and opencode as services. There's an API for accepting jobs, Redis for enqueuing them, Postgres for some pretty basic observability, and a runner for actually triggering opencode runs. Pretty simple stuff, but it's enough to read through my blog archive and extract a "style guide" for me, which is pretty exciting.

The next step is to graduate to git repositories, which means mounting my git credentials and allowing the agent to access the real world. Fortunately I have a ready-made playground with a lot of pretty simple issues for the agent to chew through: my laws-of-software repo. Should be fun to see those PRs roll in and close up some old issues I have lying around!

From there I plan to step into multi-agent orchestration: a planner and an executor, perhaps. Eventually I'll expand into agentic PMs and QAs, architects and whoever else wants to be in the room. At some point I'll probably have to think carefully about how to swap in different workspaces... and eventually I'll be ready to build real products! The hope is that I can build incrementally while realizing value at every step along the way. Who knows, maybe I'll learn something too.

There are a few reasons I'm calling the project a "software printing press" rather than the more typical "software factory." Most importantly, I think of software as a creative, expressive thing to be widely shared, not a widget to be mass-produced. Beyond that, I like the historical analogy to Gutenberg, and I think the underlying forces are just as big and potentially just as transformative.

I hope you'll join me for the adventure!
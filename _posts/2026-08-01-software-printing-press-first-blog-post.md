---
title: "Software printing press: first blog post"
layout: post
date: 2026-08-01 18:00
---

I didn't write this post. My [software printing press](https://github.com/shaisachs/software-press) did!

Here's what happened. I handed the press a folder of my last several blog posts and asked it to distill my voice and point of view into a style guide. Then I asked it to read that guide and draft a new post. This blog post is the result of that pipeline.

This little adventure demonstrates that the press can now operate inside a workspace. It can read the files in a directory and write new ones, rather than just emitting text into the void. That sounds small, but it's the difference between a party trick and a colleague.

For the time being, I've orchestrated those steps by hand, but there's no reason the press couldn't orchestrate them itself. That's what excites me most. Reading and writing within a workspace is fundamental to creating realistic codebases - the press has to inspect what's already there and modify it, not just generate text. So in addition to a machine that writes blog posts with my voice, I'm well on my way to using that same machine to write code.

My next step is to mount git credentials into the press so it can operate directly within my repos. Not very difficult in terms of mechanics, but quite exciting in terms of reducing friction - it's what turns a demo into a real coding workflow.

The one caveat: self-hosting these models has been a royal pain. Hetzner VPS is expensive for models that are actually useful, and Runpod is full of papercuts, even for turnkey serverless installs. So for now I'm just using the DeepSeek API. In principle I could self-host, but I don't want to sink much time into it.

I did wind up giving this post some touch-ups, but for the most part you're listening to DeepSeek and OpenCode (... and some of my old blog posts.) I hope you like them!
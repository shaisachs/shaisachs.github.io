---
title: "Software printing press: first blog post"
layout: post
date: 2026-08-02 18:00
---

I didn't write this post. My [software printing press](https://github.com/shaisachs/software-press) did - and that's the entire point.

Here's what happened. I handed the press a folder of my last several blog posts and asked it to distill my voice and point of view into a style guide. Then I asked it to read that guide and draft a new post. This is the result of that pipeline.

The press now operates inside a workspace. It can read the files in a directory and write new ones, rather than just emitting text into the void. That sounds small, but it's the difference between a party trick and a colleague.

The workflow, as it played out:

1. Read several of my past blog posts.
2. Write a style guide summarizing my voice and point of view.
3. Read the style guide.
4. Draft a blog post in my voice.

Here's the kicker: I orchestrated those steps by hand, but there's no reason the press couldn't orchestrate them itself. That's what excites me most. Reading and writing within a workspace is fundamental to creating realistic codebases - the press has to inspect what's already there and modify it, not just generate text. So in addition to a machine that writes blog posts with my voice, I'm well on my way to using that same machine to write code.

My next step is to mount git credentials into the press so it can operate directly within my repos. Not very difficult in terms of mechanics, but quite exciting in terms of reducing friction - it's what turns a demo into a real coding workflow.

The one caveat: self-hosting these models has been a royal pain. Hetzner VPS is expensive for models that are actually useful, and Runpod is full of papercuts, even for turnkey serverless installs. So for now I'm just using the DeepSeek API. In principle I could self-host, but I don't want to sink much time into it.

It's odd to publish something I didn't fully write myself. But that's sort of the point. I'd love to hear whether it reads like me - and what you're doing with headless coding.

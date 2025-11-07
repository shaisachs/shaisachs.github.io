---
title: "AI CodeGen Productivity Primer"
layout: post 
date: 2025-11-05 08:00
linkedinpost: https://www.linkedin.com/posts/shaisachs_google-notebooklm-your-research-and-thinking-activity-7391821649727348736-p4Gf
---

Where are we at with AI code-generation productivity? Here's a primer, heavily biased, that distills my own research.

🔹 The punchline:

Everyone assumes that AI is making software engineers about 20% more productive. Engineers themselves perceive about that level of improvement, and there is some empirical basis for it.

But the distribution has fat tails, and it's possible to lose productivity in some cases.

Everyone and her uncle are highly motivated to demonstrate a 20% producitivity bump. Beware confirmation bias and remember that Goodhart's Law will certainly mess with your data.

🔹 The studies:

The METR study - small-scale, often cited - found a 19% productivity reduction.

The Stanford study - much larger - found roughly a 20% productivity improvement, especially for greenfield projects.

There are a smattering of other studies published by different companies (CloudKitchens had a nice one).

🔹 The problems:
AI shines in greenfield contexts, where it can fill in patterns or generate boilerplate quickly. But most real engineering work today is brownfield: integrating, refactoring, extending, debugging. That’s where AI struggles most.

Then there’s the rework problem - code that’s generated quickly but has to be rewritten later. If your metrics stop at code acceptance or merge velocity, you might see a false signal of improvement while actual delivery stalls.

And even if code generation really is faster, coding is only one slice of the software development lifecycle. Productivity gains at the keyboard can easily be erased by process gates, unclear requirements, or slow review and deployment stages. The bottleneck often isn’t typing speed - it’s alignment and coordination.

🔹 The metrics that matter:

Adoption - daily usage is a simple, decent proxy for perceived usefulness.

Velocity & quality - track PR throughput and change failure rate, as Pragmatic Engineer recently suggested.

Developer surveys - these can provide high-level directional signals but they are extremely easy to bias in insidious ways. Proceed with extreme caution.

Business value delivered - ultimately, that’s what matters; but it's very hard to measure reliably.

🔹 Next steps:

Write good requirements. Distill them into specs. These are difficult skills to learn but they can lead to extremely good AI productivity.

Don't overwhelm context windows. Give LLMs small, well-defined tasks with relevant tools. (Of course, I'm just restating my first point.)

📘 My sources: I've dropped the various studies that I follow into a NotebookLM notebook, here: [NotebookLM](https://notebooklm.google.com/notebook/a9b3eba0-23e6-4aed-8bc2-9cb88bcae438) - feel free to dig through it and suggest improvements!

Written with ChatGPT.
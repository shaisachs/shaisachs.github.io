---
layout: post
title: "Async Agentic Coding"
date: 2025-09-24
---

The promise of async agentic coding is hard to ignore. Tools like Claude Code point toward a workflow where the AI does more than autocomplete. It tries things — looping asynchronously, exploring options, and surfacing solutions that might be difficult for a human to brute force. More than that, the AI coding assistant is async, meaning that it's possible to run multiple agents in parallel. That's a very different way of writing code than we're used to.

As [Vincent Quigley](https://www.sanity.io/blog/first-attempt-will-be-95-garbage) describes well, the process looks messy. The first attempt will be 95% garbage. That is not a flaw; it is the design. With enough iterations, good code eventually emerges. Or more to the point, senior engineers can sift through the bad code and find the good code.

What's more exciting is that async coding is becoming a reality. As [Zach Wills explains](https://zachwills.net/how-to-use-claude-code-subagents-to-parallelize-development), agentic coding can be parallelized. Engineers can set up subagents to take on multiple sub-tasks at the same time, effectively building automated product development assembly lines. The trick is coordinating and managing all of these subagents, spec'ing out the behavior with sufficient clarity up-front, and monitoring agents to make sure they're not running off the rails. Here again, the tools are better suited to senior engineers, who are more adept at proper spec'ing

On the flip side, async agentic coding can quickly become an expensive enterprise. The price-per-token model adds up quickly, and running multiple agents in parallel, obviously, consumes more tokens than one agent at a time.

The challenge for engineering leadership is, how and when should we adopt this stuff? Clearly it's got a lot of potential, but just as clearly it's easy to adopt it in costly and counter-productive ways.

Here's how I'm thinking about it.

1. Create a small pilot. Carefully select a big-enough project that's not terribly experimental - something that lends itself well to spec-driven-development. Just as carefully, select an engineer who is familiar enough with the code base, and who has decent tenure, to oversee the agents.

2. Train and expand. Develop best practices around writing specs and coordinating sub-agents (i.e., through task lists and centralized markdown files). Share agentic guideline files, akin to the appendix of Wills's post. Run some workshops and office hours to guide early adopters in the process.

3. Evaluate and measure. This step is really tricky. You want to measure time-to-deliver and cost, of course, and you want to get some sense of the speedup provided by async agentic coding - that gives you a sense of ROI. The problem is you won't necessarily know the counterfactual (how long would async projects have taken if you had done them by hand?), so you have to rely on levels-of-effort estimates which are necessarily subject to bias, in a space already rife with confirmation bias.

4. Climb the ladder. Ideally you want junior engineers to "graduate" into async agentic coding. To do so they should prove facility with writing specs and managing async processes. Fortunately, it is possible to demonstrate these skills cheaply. Junior engineers can practice writing specs by drafting Jira tickets and design documents. They can practice managing async processes by providing Cursor with prompts, nudging it to run tests and write commits, and allowlisting the relevant commands.

Hopefully none of the above comes across as talking-down to junior engineers. I think junior engineers are quite talented as a group. It's more a question of putting async agentic agents in a kind of organizational sandbox and fiddling with them until we have a better understanding of how they work.

On the whole, I'm quite skeptical of async agentic coding as a practice. It's very new and not very widely practiced yet. But there's no way to ignore the potential of this approach, and we need to find a reasonable way to explore it.

Written with help from chatgpt.
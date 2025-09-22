---
layout: post
title: "Async Coding Agents"
date: 2025-09-20
---

There is something new brewing in the world of coding, thanks to async coding agents like Claude Code. As [Vincent Quigley](https://www.sanity.io/blog/first-attempt-will-be-95-garbage) and [Zach Wills](https://zachwills.net/how-to-use-claude-code-subagents-to-parallelize-development) describe, async agentic coders are parallelizable. You set up some context, break up a project into multiple pieces, assign sub-agents to tasks within the project, give them a coordination point - and watch them go. It's a pretty exciting idea! Clearly there's a lot of potential here. But there's a steep learning curve to managing async coding agents, and that poses a major challenge for engineering leaders.

First and foremost, that is because this approach has a high price tag. The pricing plans are different and, at a very basic level, more coding agents means more usage means higher bills. Using this approach indiscriminately is just lighting money on fire.

Just as importantly, this approach requires a new kind of skill set which is very different than what we've seen before. It's really hard for an individual engineer to actually run one of these async coding agent sessions. The early discourse on this approach is that it's like having a team of junior engineers at your beck and call. A team of junior engineers is great! They can get a lot done! They also require a huge amount of supervision and guidance!

So the question is, how do we properly roll out these tools in a way that's cost-effective and productive?

Here's how I'm thinking about it.

1. *Carefully design a pilot project.* Choose the right feature and the right engineer. You want a feature that's not too small (because there's no sense parallelizing a small project), that has a good number of well-defined tasks (which can be cleanly sub-divided across sub-agents), and that has a clear end point (so that you can readily detect diversion and rabbit holes.) The engineer should be someone who knows the feature pretty well and could execute the project by hand if need be.

2. *Lay the groundwork.* Quigley and Wills have some good pointers on how to setup context and coordinate agents. In general I prefer not to over-think things, but for a pilot project I suspect that a little extra prep, even going so far as to code-review specs and agentic guidelines, might be worthwhile. It goes without saying that MCPs should be configured properly before diving in.

3. *Execute the project.* Get the code working, and try to keep track of how the agents behaved along the way, what sort of course corrections were needed, etc. I don't think the block-and-tackle of agentic oversight is easy to measure, especially with such a small sample size, but does help train the next round of engineers that adopt this approach.

4. *Measure and celebrate.* The goal is to demonstrate productivity improvements, ideally by comparing, on the one hand, a good-faith level of effort estimate made before the project started; against the time spent with the agents as well as the cost of token usage, on the other hand. Once the code is deployed and working, it's time to celebrate the victory!

5. *Curate the backlog.* Look for projects that fit this mold. Establish and nurture a culture in which Jira tickets are detailed and precise, with all requirements clarified before tickets can be accepted onto a sprint. It's actually possible to use Atlassian Rovo to identify tickets which are poorly specified, though it helps if you can provide some reference tickets indicating the degree of specificity you want.

6. *Train and expand.* Find more engineers who can take parallelizable projects, and circulate the learnings around how to guide async coding agents. Place a special emphasis on spec-driven development. Source control specs / prompts and agentic guideline files, akin to the appendix of Wills's post. Run some workshops and office hours to guide adopters in the process.

7. *Evaluate and validate.* This step is really tricky. You want to measure time-to-deliver and cost, of course, and you want to get some sense of the speedup provided by async coding agents - that gives you a sense of ROI. The problem is you won't necessarily know the counterfactual (how long would async projects have taken if you had done them by hand?). One approach is to rely on levels-of-effort estimates, though these are are necessarily subject to bias, and this space is already rife with confirmation bias. The industry best practice for measuring interactive coding agents like Cursor appears to be centered around [PR throughput and change failure rate](https://newsletter.pragmaticengineer.com/p/how-tech-companies-measure-the-impact-of-ai), and that's probably a good place to start for async coding agents. Of course, for such metrics to really shine, you need to gather data over a reasonably long period of time and across a large cohort of engineers.

This paradigm shift is exciting. It feels like the future. But it's so new that we have yet to fully understand it or to see how it will reshape software engineering practice. I do think it's important to start climbing the learning curve, though.

Written with help from ChatGPT, though I wound up substantially rewriting after a couple of rounds.

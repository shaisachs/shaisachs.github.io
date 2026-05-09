---
title: "Context cohesion"
layout: post
date: 2026-05-09 09:00
---

It's not the size of the context window, it's the cohesion of what's inside.

That's my latest theory of agentic coding. In my travels I've noticed that when I give the agent a focused, cohesive context, it can do well. Thrashing sets in when I start to throw in too much "other stuff."

My mental model of LLMs is that they're giant dictionaries; that's grossly over-simplified of course. With dictionaries, the better-focused your search terms, the more likely you are to get results. This approach matches my own approach to engineering: ideally everything from Jira items to microservices to individual classes should be cohesive and well-focused. Why should prompts be any different?

The agents are getting smarter and smarter, of course, and I think the labs are working around the problem of incohesive context in various ways - periodic compaction and things like that. But ultimately I think it's just so many parlor tricks around what is something of a fundamental limitation - if you try to do too much you wind up doing nothing.

As a result I've taken to tweaking the "task list" part of my spec-driven development approach, so that each task is tightly focused on just the problem at hand, with all of the context it needs on a single line. I'll link my approach in the comments, but the TLDR is that I start with an implementation plan and then I ask the agent to turn it into a task list; then I feed the task list through a Wiggums loop. 

The key learning, for me, is that the task list creation has to be somewhat dumb:

> Read ./docs/plans/add-dingbats/plan.md and turn it into a task list. Each task should be specific and include all of the information it needs to complete the task. Feel free to repeat yourself.

The resulting task list is verbose and repetitive, by design. If someone handed me a task list like that I'd be annoyed. But guess what, agents don't get annoyed! Or if they do they don't mention it and I'm not paying attention anyway. The upshot is that each iteration of my Wiggums loop is well-scoped and more likely to be successful.

I'm thinking about adding a project-level "guardrails.md" file that contains "traps the agent might fall into during this project." Then each iteration of my Wiggums loop can be:

> Get the next task from ./docs/plans/add-dingbats/tasks.md. Then read ./docs/plans/add-dingbats/guardrails.md. Do the task from the task list but respect the guardrails as you do so.

I haven't gotten there but it seems like an obvious tweak, and it keeps my agent from reading a bunch of unnecessary docs.

What I'd love to see is tooling that helps me see how cohesive the context window is, on a task-by-task basis, so I can pivot over time. Right now the tooling is pretty coarse - we're looking at the amount of context, but in my view a little bit of poorly cohesive context is worse than a lot of tightly-scoped context. I'd love to hear about tricks to get some transparency there - please share if you have any!
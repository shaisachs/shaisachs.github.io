---
title: "Agentic code review"
layout: post
date: 2026-06-09 18:00
---

A couple of weeks ago I took a stab at creating an agentic code review framework at Chewy. Since then I've been fiddling around with it for a couple of projects. Turns out, review is much more difficult than implementation!

The framework I've built out is inspired in large part by Ankit Jain's piece on [How to Kill the Code Review](https://www.latent.space/p/reviews-dead). It has three components:

* Make the build green
* Adversarial QA
* Review case files

Each of the above steps is its own agentic skill, and none of them are particularly clever. The first skill, for instance, provides the agents with some bare bones access to Jenkins, and then provides steps to check the build status, identify the cause of failure, fix it, and then rinse-repeat until the build is green.

Review case files are somewhat interesting in that they spin up sub-agents to independently examine a pull request from multiple angles: API design, database logic, resiliency characteristics, etc. At the end an orchestrator agent compiles all of the findings into a programmatic "case file." This case file can kick off a new coding loop to fix the review findings, provided they are reasonably simple. But again, this idea can be found elsewhere: indeed I believe it's the "hello world" example Codex provides for orchestrating sub-agents.

Some of the value that this framework provides, I hope, is real experience inside the confines of Chewy's ecosystem. Indeed I've accumulated quite a few learnings as far as that goes, and I'm working to incorporate them into the framework as I go. For example, I've discovered the need for a skill to manage feature toggles in our config service, so that we can test feature-on and feature-off variants of a pull request inside a single agentic session.

The most important learning, though, is that agentic code review is really, really difficult - much more so than agentic code generation!

On reflection the reason is obvious: there are a lot of ways to screw things up, comparatively fewer ways to succeed. A good framework can handle all sorts of contingencies along the way and react to them nimbly. That means reasoning about everything from linting failures to foreign key violations in seed data, and who knows what else.

For the time being I'm exercising this framework manually - triggering the skills and then inspecting outputs before I move to the next step. That's a useful feedback loop into the improvement of the framework itself, but eventually the training wheels will come off. The goal is to be able to spin a coding loop and a review loop, one after the other until the whole thing has stabilized into satisfactory, working code - while I'm entirely hands-off-keyboard. It's somewhat ambitious, but the early progress is promising.

If all goes well, this framework will be something that can dramatically reduce our PR review cycles. Hopefully, this framework will improve the quality of code that enters the PR review cycle - meaning that human reviewers have a lot less to worry about before they sign off.
---
title: "Search and repeat"
layout: post
date: 2026-07-08 18:00
---

You could (greatly) simplify software engineering into two acts: search for a deterministict artifact; and repeatedly execute that artifact, over and over. Agentic coders are great at the first act, terrible at the second, and it's important to remember what you're trying to do when you leverage them. That is a crucial insight for developing efficient skills.

One of the key breakthroughs in separating "search" and "repeat" for agentic coders was the Cloudflare [Code Mode](https://blog.cloudflare.com/code-mode/) blog post from September. In that post, Cloudflare suggested that agents should not consume MCP tools directly, but rather write code to consume the tools, then execute that code. 

The idea was specific to MCP tool calls but the insight generalizes nicely. Agents are good at searching for deterministic artifacts, not repeatedly executing a deterministic step. On reflection, the reasons are obvious: LLMs are non-deterministic by nature, and sensitive to their input. You can use them for guided search with a reward function, in principle quite similar to the classical AI strategies like A* search.

The latest incarnation of this idea is agentic skills. The key to building a good skill is finding the proper line between determinism and non-determinism; what text goes into SKILL.md, and what should go into a bash script alongside it?

It's quite easy to get the balance wrong, and the cost of doing so is token spend and wall-clock time. For example, you could write "commit to git" in SKILL.md, and the agent would figure out the proper command to use... after spending some time and tokens in the process. Or you can create a "git-commit.sh" script which contains exactly the parameters you want, and just tell the agent to execute that script. Such an approach is much faster and token-efficient, as the agent doesn't have to look up the git reference material buried deep in the LLM's neural network.

Even so, it's reasonable to draft such a skill! It's a easy way to get started and it can be a good proof of concept within a larger workflow. The key point is to improve the skill, and the larger workflow over time: shift the repeatable stuff into a deterministic artifact, and enhance the reward function so that search becomes sharper over time.

Ultimately, it's important to evaluate skills as software products unto themselves. They require testing, monitoring, bug fixes, and all the rest. This degree of maturity for skills development is thin on the ground. But as we endeavor to formalize agentic coding workflows, it will only become more important.

I've got a few ideas in the works for maturing my own skills practice, and as they prove (or disprove!) themselves I'll try to update accordingly. In the meantime I'd love to hear what you're doing and finding useful!
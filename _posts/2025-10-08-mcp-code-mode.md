---
title: MCP Code Mode
layout: post 
date: 2025-10-08 08:00
linkedinpost: https://www.linkedin.com/posts/shaisachs_code-mode-the-better-way-to-use-mcp-activity-7381659678008565760-okCd
---

The Cloudflare [Code Mode](https://blog.cloudflare.com/code-mode/) approach to MCP tool calls sounds like a really significant improvement on the MCP experience. It's one of those rare breakthroughs that is both elegant and obvious in hindsight.

At a high level, the idea is to translate "raw MCP" into TypeScript interfaces, and ask the LLM to code against the TypeScript interface. It's a form of language arbitrage you might say: the agent exchanges a low-resource language (raw MCP) for a high-resource language (TypeScript), so the LLM performs much better. Then something cool happens - the LLM can also write code to chain tool calls together, or otherwise process the tool call responses in interesting ways. The agent is left holding a bunch of LLM-generated code, so it needs a sandbox to go run that code, and of course Cloudflare offers a solution for that.

We'll see if this approach takes hold; it seems to have a lot of traction already. If it does, then it's worth asking whether the MCP protocol itself needs a revision - for example, by making the MCP server provide the TypeScript interface natively. That then raises another round of questions, around what is the best way for MCP servers to "speak" to LLMs - can we do better than Typeface?

Certainly it's a cool idea, and I think it's a great step forward for MCP usage.
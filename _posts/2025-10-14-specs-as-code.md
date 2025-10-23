---
title: Specs as code
layout: post 
date: 2025-10-14 08:00
---

One of the ways we are grappling with the phenomenon of AI-assisted coding is to theorize that specifications are going to replace code. That's basically what this [conference talk by Sean Grove](https://www.youtube.com/watch?v=8rABwKRsec4) argues.

The proponents of this idea claim that specifications are the next layer of abstraction above programming languages. That is, specifications can replace Python code in the same way C code replaced assembly code decades ago. Instead of using a compiler to translate C code into assembly code, we use an LLM to translate specifications into Python code. The benefit is that we can think in terms of specifications, which are easily understood by a wide group of people.

This idea is flawed for several reasons.

1. There is no deterministic mapping from specifications to code. Sending the same specs to the same LLM at two different times will yield two different code bases.
2. The mapping is highly sensitive to the input. This problem applies to LLMs generally. A minor change to specs can have a surprising impact on the resulting code.
3. Evaluating correctness of a spec-to-code mapping is subjective, whereas compiler output can be objectively verified. 
4. Specs are sometimes intentionally ambiguous. It's not uncommon to resolve conflicting priorities among stakeholders by writing ambiguous specs and deferring resolution to implementation time.
5. Specs are often unintentionally ambiguous, because human languages are bigger than programming languages. Words in human language have multiple meanings.
6. Specs are sometimes informed by their own implementation in circular fashion. This idea is core to the agile methodology. In this view, code is not really a function of specs but rather a tool to explore the problem space; you could even say that code actually generates specs.

In brief, the specifications-to-code abstraction is extremely leaky, much more so than the C-to-assembly abstraction. They are two fundamentally different abstractions. 

All that said, the idea of specs as code is still useful, especially as a what-if thought experiment. It's a good way to think about what is becoming possible, to a very rough approximation, in the general case.

Moreover, it's extremely exciting in special-case experiments. For example, [Tomas Vesely's work on the GitHub Brain MCP server](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-using-markdown-as-a-programming-language-when-building-with-ai/) is fascinating and instructive. This project is pretty unusual compared to other software projects in many respects. But it's still cool to see the specs-as-code idea in the wild, and the write-up includes some great learnings.

I'm skeptical that specs will ever replace code. Still, the idea of spec-driven development is clearly compelling and important, and something we need to explore more deeply.

Also find this post on [LinkedIn](https://www.linkedin.com/posts/shaisachs_one-of-the-ways-we-are-grappling-with-the-activity-7384196851140333570-Xwk)!
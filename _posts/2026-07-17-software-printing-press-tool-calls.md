---
title: "Software printing press: tool calls"
layout: post
date: 2026-07-15 18:00
linkedinpost: https://www.linkedin.com/posts/shaisachs_my-software-printing-press-project-reached-share-7483274306475450370-wOAn/
---

My [software printing press](https://github.com/shaisachs/software-press) project reached a nice milestone this week: it's now capable of tool calls using local models on my laptop - entirely dockerized, entirely without Internet. It can write code and blog posts for me now!

There's a catch, which is that my laptop is not that powerful. Most of the trouble I had getting everything to work was finding a tool-calling model that my Ollama could actually bring into memory on my laptop. After quite a bit of trial-and-error I settled on Qwen 2.5 / 0.5B.

That's fine for a demonstration, but it won't actually get useful work done. My favorite toy prompt is "write something about penguins to penguins.txt", or something along those lines, and the other night my software press did just that... but barely! It was a line of text, sort-of cohesive, and that was about it. My software press wrote some Python code to add two numbers but really choked on Fibonacci numbers.

The next step is to rent out some more substantial hardware, probably a Hetzner VPS, and load a more interesting model - Gemma 4, Kimi, something like that. Hopefully that yields more interesting results. I have an idea for a fun little Python script I'd like to "print": input a markdown file with a list of song titles and artists, mount a Spotify API key, and generate a Spotify playlist. That would be a nice milestone!

Assuming all goes well, I hope to improve the affordances of the thing - right now it's accepting jobs via curl API calls, which is fine, but I'd love to hook it up to Linear and start to treat the press as my own little engineering team.

In the meantime, you are welcome to play with my software printing press, and even more welcome to improve it! The code is MIT-licensed and PRs are warmly encouraged.
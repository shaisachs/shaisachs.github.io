# Blog Post Style Guide

This guide captures the voice, structure, and conventions used in the posts under `blog/`. Use it as a reference when drafting future posts about agentic coding and AI developer enablement.

## Voice and persona

- **First-person and personal.** Write as "I." Every post is a genuine account of what you tried, built, read, or thought. Anchor posts in lived experience ("Lately I've been wrestling with...", "A couple of weeks ago I took a stab at...").
- **Learned out loud.** Show the process, not just the conclusion. Share what worked, what didn't, and what you're still unsure about. Admitting limits is a feature: "Turns out, review is much more difficult than implementation!", "I'm not really sure!", "I confess to feeling quite daunted by it."
- **Honest about setbacks.** Call out catches and failures openly rather than sanding them down: "There's a catch, which is that my laptop is not that powerful... it won't actually get useful work done."
- **Curious, not preachy.** The tone is exploratory and humble. Favor "I think," "I hope," "I suspect" over confident declarations, except for the thesis (see below).
- **Informal and warm, but not sloppy.** Colloquial energy is welcome ("Holy geez it is so much fun!"), but the writing stays crisp, grammatical, and technical underneath.

## Structure

Posts are short (~500 words, roughly 18-28 lines) and follow a consistent arc:

1. **Hook.** Open with a personal anecdote, a provocative claim, or a question that pulls the reader in immediately.
2. **Thesis.** State one core insight or counterintuitive point plainly. The best posts carry a twist: "the disruptive technology isn't agentic coding. It's the software no one cares about."
3. **Development.** Build the argument with concrete examples, references, and lived detail. Use short paragraphs. When describing a process or framework, use a numbered list (see "Headless devex" for a canonical six-step example).
4. **Reflection.** Zoom out to the broader implication for the industry, for engineers, or for yourself.
5. **Closing.** End with a forward-looking note, a genuine open question, or a direct invitation to the reader: "I'd be curious to hear from you - are you thinking through this challenge?", "In the meantime I'd love to hear what you're doing and finding useful!"

## Content and topics

- **Recurring themes:** agentic coding, AI dev enablement, headless coding, developer experience, coding skills / SKILL.md design, evaluation (DORA metrics like lead time to change vs. token spend), and the "software printing press."
- **Concrete over abstract.** Name the real tools, models, and services you used (Codex, Jenkins, Ollama, Qwen 2.5/0.5B, Hetzner, Linear, Spotify API, Lovable, GitHub). If you built something, link to it.
- **Ground ideas in sources.** Cite the people, books, and posts that shaped your thinking, with hyperlinks: Paul Graham, Clayton Christensen, Ankit Jain, Mo Bitar, Laura Tacho, Simon Willison, the Cloudflare Code Mode post.
- **One big idea per post.** Pick a single claim or insight and earn it. Don't try to cover a topic exhaustively.

## Mechanics

- **Front matter** (Jekyll-style) with the following fields, in this order:
  - `title:` — quoted, title case, short and punchy (e.g., "Search and repeat", "Enable, don't scale")
  - `layout: post`
  - `date:` — `YYYY-MM-DD HH:MM` (24-hour), roughly the day it's published
  - `linkedinpost:` — optional; full LinkedIn post URL when a companion post exists
- **Filenames:** `YYYY-MM-DD-slug.md` in `blog/`, where the slug is a short kebab-case version of the title.
- **Formatting:**
  - Short paragraphs. Most are one to three sentences.
  - Em-dashes and parentheses for asides; exclamation points and rhetorical questions sparingly for energy.
  - Use **bold** and headings rarely — the prose carries the post.
  - Numbered lists for sequential frameworks or plans; bullet lists for sets of items.
  - Hyperlinks inline with descriptive anchor text; never dump bare URLs.

## Titles

- Short, human, and slightly offbeat. Single evocative words or phrases work well ("Alienation", "Lovable"), as do compound titles ("Software printing press: tool calls", "Agentic code review framework").
- Prefer the counterintuitive or arresting angle over the descriptive one.

## Guardrails

- Do not invent details or stories that were not provided to you.
- Kepp blog post bodies to 3,000 characters or less, so they can be posted to LinkedIn easily.

## Checklist before publishing

- [ ] Does it open with a hook that pulls in a busy reader?
- [ ] Is there one clear thesis or insight, ideally with a twist?
- [ ] Is the experience genuinely first-person and honest about setbacks?
- [ ] Are real tools, people, or sources named and linked?
- [ ] Does it end with a forward-looking note or invitation to the reader?
- [ ] Front matter complete and consistent (title, layout, date, optional linkedinpost)?
- [ ] Roughly 500 words; does every paragraph earn its place?

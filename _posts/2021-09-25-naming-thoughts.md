---
layout: post
title: "What AI can't do: naming thoughts"
date: 2021-09-25 09:07
excerpt_separator: <!--more-->
bannerimg: /img/posts/dictionary.jpg
photographer: Tamara Menzi
photographerurl: https://unsplash.com/@itstamaramenzi
tags: ai
---

Shannon Vallor's piece about [the thoughts the civilized keep](https://www.noemamag.com/the-thoughts-the-civilized-keep/) is a very good critique of the modern hype surrounding AI, and it eviscerates GPT-3 very nicely. Her key point is that machines allow us to do what Alfred Whitehead suggested over one hundred years ago - "\[extend\] the number of important operations which we can perform without thinking about them." GPT-3 and its fellow traveler AI algorithms are no different.

<!--more-->

My vocabulary for discussing this idea is slightly different from Vallor's, but with very similar intent and meaning. My working hypothesis about the limits of AI is as follows: that it cannot, and never will be able to, properly name a thought. This hypothesis will get something of a trial run, incidentally, in The Game - which is the short story I'm working on these days.

The problem of good naming is infamously considered one of the hardest problems in computer science. It is also not very well-defined! One might say that it's the problem of picking a word or short phrase which efficiently summarizes a larger body of thought. For example, "hyper text transfer protocol" is a name for a very large body of specifications about how web servers and browsers (among other clients) communicate with each other.

It's also not very easy to discern what makes a name "good". Is HTTP actually a good name for the protocol it refers to? That is debatable, and there is no agreed-upon metric for rendering judgement. In a less grandiose context we might consider a code base managed by a team or two, and pick a function out of that code base. Is the function well-named? We could maybe endeavor to measure the property of well-named-ness - for example, we could look at how often that function name is changed, or how many defects arise from that function. That would be a start, although Goodhart's Law means we could never get a fully satisfactory answer!

Ultimately I think my working hypothesis amounts to something like tautology - and [tautological arguments are about the best we've got](https://shaisachs.com/2020/07/27/argument-from-tautology.html) in this area.

Could you design an AI algorithm which, given a corpus of text, picks a title for that text? You certainly could, and probably you could design such an algorithm and get some pretty impressive results - judged subjectively, and in small, cherry-picked batches. 

Does that mean that we've designed an intelligent algorithm? I think not, and Vallor's piece points to the reason why. It's because AI would do a good job providing names for textual corpuses that are reasonably similar to pre-existing corpuses. Imagine we took a time machine back to the mid-80s or so, and proceeded to invent a title-generation AI algorithm. Let's say we fed that algorithm the first few chapters of a Charles Dickens novel; we might well get back a title like "Great Expectations," and wouldn't that be fine. But then let's pretend we fed this same algorithm a completely new and ground-breaking piece of text, like the full text of Toni Morrison's novel Beloved. Would we indeed get back a title as elegant as Toni Morrison's? Maybe - but probably not! The titular character in that book is rarely if ever referred to by that name. Indeed, the word appears "beloved" only a handful of times in the entire text. Yet there is no question that the book is about her, and that all the drama revolves around the various ways in which a person might be loved. That is, in small part, why the book was so ground-breaking.

Let's also remember that picking a name for a piece of text is probably the easiest generative task you could pick for an AI algorithm. What about naming... a social movement, or a novel scientific concept, or a really interesting set of techniques in the arts? They are still more difficult to name, because in the case of (say) scientific concepts, it's not at all clear how to group them or how to summarize a particular grouping. It's difficult to imagine a hypothetical AI algorithm deciding that a series of scientific ideas related to the interaction of organisms with their natural environments is a cohesive branch of study, let alone to give this field the name "ecology."

Return to the present day - and now imagine what sort of ground-breaking technology, art, or human affairs are likely to transpire in just the next year or two, never mind the next century and beyond. Can we really expect a hypothetical AI algorithm created in 2021 to nimbly respond to such developments? Especially given that such developments might indeed be *built upon* that algorithm and its cousins? It's something like hubris to suppose we could really make that happen!
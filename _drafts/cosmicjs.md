---
layout: post
title: cosmicjs
---


One of the more interesting trends in content management systems is the separation of editing and rendering, with an API in between the two layers. Whereas traditional content management systems like Drupal and Wordpress will integrate both functions inside a single framework, new entrants like CosmicJS have taken a different approach.

The gist of this approach is as follows. Let editors write, revise, and publish their content in one place; let an API make that content available; and let one - or many - rendering engines display that content. In an era where content must be distributed in many channels - desktop, mobile, TV, and so forth - the appeal of this approach is obvious. So obvious, in fact, that there's a movement, referred to as [headless Drupal](https://groups.drupal.org/headless-drupal), which aims to squeeze Drupal's content editing functionality into this framework.

I'm fascinated to see where this idea will go. In some ways it seems incredibly obvious, since the content delivery landscape is only getting more and more fragmented. And in other ways I wonder if it's also incredibly naive. After all, content is not the perfect commodity which CosmicJS seems to assume. A piece of content which works really well on a mobile phone might be pretty unattractive on a TV. Content which works really well on a desktop might not be very appealing on an e-reader. And so on.

Moreover, I'm not sure I totally subscribe to the philosophy that content and code need to be perfectly decoupled. It sounds nice in theory; it sounds a lot like separation of concerns, which is one of the most successful guiding principles in software programming. But in practice, I believe that versioning is an under-appreciated requirement for content editing. I worry that the philosophy which separates content from code will also degrade the versioning experience, which is such a crucial one for editors and writers.
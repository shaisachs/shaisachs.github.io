---
layout: post
title: "Content Management on the Wire"
date:   2017-02-20 13:00
bannerimg: /img/posts/ocean.jpg
photographer: Francess Gunn
photographerurl: https://unsplash.com/@francesgunn
---


One of the more interesting trends in content management systems is the separation of editing and rendering, with an API in between the two layers. Whereas traditional content management systems like Wordpress will integrate both functions inside a single framework, a new entrant, CosmicJS, has taken a very different approach.

The gist of this approach is as follows. Let editors write, revise, and publish their content in one central location, a SaaS app. Let an API make that content available. Let one - or many - rendering engines display that content across any number of channels. In an era where content must be distributed in many channels - desktop, mobile, TV, and so forth - the appeal of this approach is obvious. So obvious, in fact, that there's a movement, referred to as [headless Drupal](https://groups.drupal.org/headless-drupal), which aims to squeeze Drupal's content editing functionality into this framework.

I'm fascinated to see where this idea will go. In some ways it seems incredibly obvious, since the content delivery landscape is only getting more and more fragmented. And in other ways I wonder if it's also a little naive. After all, content is not the perfect commodity which CosmicJS seems to assume. A piece of content which works really well on a mobile phone might be pretty unattractive on a TV. Content which works really well on a desktop might not be very appealing on an e-reader. And so on.

Moreover, I'm not sure I totally subscribe to the philosophy that content and code need to be perfectly decoupled. It sounds nice in theory; it has echoes of the principle of separation of concerns, one of the most important principles in software programming. But in practice, I believe that versioning is an under-appreciated requirement for content editing. I worry that the philosophy which separates content from code will also degrade the versioning experience, which is such a crucial one for editors and writers.

As a practical matter, I'm also a little surprised by the fact that CosmicJS fails to make it possible to manipulate object types, buckets, or apps via the API. Perhaps that is so because the API is still young, and these resources aren't exactly mission-critical for many API consumers. Perhaps it's an intentional decision meant to push content editors into CosmicJS's own editing UI. One way or the other, my guess is that the demand for these sorts of resources will eventually build, as consumers seek to create more and more interactive scenarioes to their end users. The use case which comes to mind most readily is data journalism, in which a journalist may well wish to create object types on-the-fly so that new crowdsourcing projects can get off the ground quickly.

All of that said: I think the choice to release a [GraphQL API](https://cosmicjs.com/docs/graphql) is exactly the right one for this application. In a fragmented content delivery landscape, there are some channels for which a lot of content is appropriate (a classic desktop experience), and other channels for which only the most miniscule amounts of metadata make sense (e.g., a smart watch.) GraphQL allows clients to pull only as much metadata as they need. Moreover, one of the major constraints with GraphQL - that clients wind up tightly coupled to the server's data structure - make perfect sense in the content delivery space, where typically the content producer also maintains the various content clients.

I'm curious to see how the CMS-as-an-API concept will evolve. In the contest between Headless Drupal and CosmicJS, I wouldn't yet place bets in one direction or the other; Drupal still offers sufficient flexibility and power that it can outmaneuver CosmicJS in functionality, while CosmicJS's easy-to-use setup and editing experience has Drupal easily beaten. It'll certainly be an interesting space to watch.
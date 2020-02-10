---
layout: post
title: "MusicFest - a static, structured-data API inspired by Porchfest"
date: 2018-05-26 12:30
---

This month I put together [Music Fest](https://github.com/shaisachs/musicfest) - a static API, integrated with Schema.org, for a music festival. The API is inspired by Somerville Porchfest, an annual community event in Somerville, MA. The idea is that bands perform on front porches and lawns throughout the city, and residents wander from house to house to listen in. The whole thing is free, and a really great time.

I've been meaning to play around with [Schema.org](http://schema.org/), and I thought Porchfest was a terriffic chance to get my feet wet. The idea behind Schema.org is semantic integration via structured data. Using Schema.org, APIs can describe the resources they offer via a standard, machine-readable vocabulary. The hope is that integrating with Schema.org makes it easy for consumers to mix and match their data sources more readily, easily comparing data from disparate locations via a standard interface.

It's possible to describe nearly any data format with Schema.org, but for APIs that make resources available in JSON, the most common approach is to use [JSON-LD](https://json-ld.org/). The idea is two-fold: one, that Schema.org objects should be identified with an additional reserved key within a JSON object (e.g., `"@type": "Event"`), and two, that the keys within JSON object should conform to proeprty names from the Schema.org integration; hence, the point in space where an event occurs should be indicated with the `location` object key, rather than `eventLocation`, `loc`, or any other key.

The Schema.org website is an excellent reference point, and the semantic data definitions there - which tend to focus around the arts and entertainment - are really well-suited to an API for music festivals. Google provides an excellent [structured data testing tool](https://search.google.com/structured-data/testing-tool) which made it easy to verify that the JSON object provided in the API conforms to Schema.org definitions.

To populate the API, I used the Python [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) library to scrape the [Somerville Porchfest](https://www.somervilleartscouncil.org/porchfest/map/2018) website. The website is powered by Drupal, so it's quite straightforward to scrape and convert the markup into JSON. Most of the trickiness I encountered were quirks in the Beautiful Soup class library, like the fact that the library doesn't provide a ready facility for searching the subtree of a node within the DOM. A little poking around resolved these sorts of issues quickly enough.

Finally, I wanted to spend a little time playing around with the [Decorator pattern](https://sourcemaking.com/design_patterns/decorator), so I snuck that in to the final revision. Decorator is a really interesting pattern to me, since it applies so directly to actual interfaces that users care about, especially in the reporting world. Yet I never seem to get the chance to really take it for a spin. For this API, I created a decorator which follows the structured data format I'm trying to produce: an Event decorator decorates each performance within the music festival, then a MusicGroup decorator adds information about the Event's `performer` property, and so forth. Each individual decorator is "safe", meaning that it only marks up the resource if there's relevant information available in the DOM. The resulting code feels a lot cleaner - the DOM manipulation required to grab one item of data is nicely encapsulated from the manipulation required to grab another. Each decorator does need access to the "global" view of the entire performance, and in a larger application that would certainly be an issue; but for now it works well enough.

All told, this API is a pretty simple exercise, but it's certainly been an interesting learning experience. Integrating structured data into an API turns out to be quite easy, and the Decorator pattern lends itself quite naturally to the job.
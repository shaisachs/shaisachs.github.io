---
layout: post
title: "Gift Ideas: a CRUD API with ASP.NET Core 2 on RapidAPI"
date:   2018-01-03 20:00
bannerimg: /img/posts/gifts.png
photographer: secretlondon on OpenClipArt
photographerurl: https://openclipart.org/detail/27534/purple-present
tags: api, sideproject
---

I’ve never been a particularly good gift-giver, so this time of year can be a little dicey - right around early November I start feeling anxious about what to buy, and as a result I procrastinate and wind up buying pretty lousy gifts.

Next year, I’ve resolved, will be different. I’ll put an end to that madness by planning ahead, and brainstorming gift ideas throughout the year, so that when November comes around I just need to go through my list of ideas, pick the items I want to buy, and get out my credit card.

Because I needed a place to track those ideas - and because I’ve been meaning to play around with ASP.NET Core 2 for quite a while - I developed the [Gift Ideas API](https://market.mashape.com/shaisachs/gift-ideas). The code is MIT-licensed, and you can [check it out on Github](https://github.com/shaisachs/giftideas).

The functionality for this API is very simple: it provides basic CRUD features around Holidays, Recipients, and a join of these two resources: Gift Ideas. So for example, I can record ideas like this:

* For her birthday (a Holiday) I should get my friend Jane (a Recipient) a pair of headphones (a Gift Idea)
* For his birthday (a different Holiday) I should get my friend John (another Recipient) a book (one Gift Idea) or perhaps a CD (a different Gift Idea)
* For Christmas (a third Holiday) I should get my friend Jane (same Recipient as above) tickets to a concert (a new Gift Idea)

... and so forth. There’s nothing particularly special about this API. Indeed, I basically copied verbatim the code in the [Microsoft tutorial](https://docs.microsoft.com/en-us/aspnet/core/tutorials/web-api-vsc) and adjusted the models a little bit.

I have something of an unhealthy obsession with abstract classes, so I decided to try and abstract the basic logic in the tutorial a little. The result is a slightly more generic version of that tutorial, which allows me to easily deploy stock CRUD functionality for new models on the fly; indeed, once I had the abstraction layer in place for Holidays, adding it for Recipients and Gift Ideas was a simple chore that mainly involved wiring up a couple decorated controllers. I’m not the first person to do that - for anyone who’s interested in taking this line of thought to its natural conclusion, I’d highly recommend the [ASP.NET Boilerplate](https://aspnetboilerplate.com/) project, which wires together Web.API, Entity Framework and MVC - plus a bunch of other goodies - into a wonderfully succinct, DRY little package. But I’m certainly enjoying the perks of abstraction - it makes it quite easy to add cross-cutting concerns, like tenancy and date stamps, to every route in the API.

I’ve become quite the fan of the [RapidAPI Marketplace](https://rapidapi.com/) of late, because I like the idea of readily discoverable and billable APIs. So I decided to try and introduce a little bit of RapidAPI integration code. The basic idea behind RapidAPI is fairly simple: API consumers send API calls to the RapidAPI proxy servers; those servers verify credentials and provide a set of headers that authenticate and authorize the request with the backing API, in this case the GiftIdeas API. So what I needed was a custom authentication handler, which could check the RapidAPI proxy headers and compare them to the GiftIdeas RapidAPI secret, stored in Azure Application Settings. As it turns out, writing a custom authentication handler in ASP.NET Core 2 has become quite cumbersome, but [Bruno Garcia’s excellent Basic Authentication package](https://github.com/bruno-garcia/Bazinga.AspNetCore.Authentication.Basic) proved to be a very helpful start.

To cap off the project, I added [Swashbuckle](https://www.nuget.org/packages/Swashbuckle/) integration, in order to automatically generate OpenAPI (ie Swagger) documentation. My abstraction layer proved to be a little bit of an obstacle here - I needed to adjust the visibility of a few methods in the base class to avoid ambiguity that Swashbuckle couldn’t resolve - but even taking that into consideration, this process was easily the smoothest OpenAPI experience I’ve had to date.

The main trouble I had was actually the "final inch" - documenting the API on RapidAPI via the [Mashape Marketplace](http://market.mashape.com/). When you add an API, you can provide a Swagger API doc - but Mashape only accepts Swagger API version 1.2, and Swashbuckle generates version 2.0 by default. That was a relatively small obstacle - I converted the doc in [Apimatic](https://apimatic.io) - but RapidAPI proved unable to read that document, with no explanation for the error. Rather than try my luck over email, I figured I could just use the Mashape API documentation editor. That turned out to be a very time-consuming process - the editor is buggy and slow, and the interface is not particularly good at letting you know when your changes actually took effect. Given how nice and easy Swashbuckle integration was, I had high hopes for a painless RapidAPI listing process - so that was a shame.

At the end of the day, I’ve got a nice, bare-bones ASP.NET Core CRUD API that can be readily deployed to the RapidAPI Marketplace (give or take some errors on RapidAPI’s side). This API is not exactly groundbreaking - but it is a nice starting point for future, CRUD-based work. There are certainly a lot of places where I could improve the code. For example, the controller and data-access concerns should be separated, and likewise the internal business entities should be translated into data contracts. But for a simple quick-and-dirty API, I’m happy to say this project came together quite easily.


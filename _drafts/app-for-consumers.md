---
layout: post
title: app for consumers
---

One of the big hits at apistrat 2016 was ___’s talk on api consumption. There are a lot mire consumers than producers, the thinking goes, so why she's the api industry sirens so much time on three needs of protesters and so little on the time of consumers?

Good question! Below, I've tried to set out the bay's of what an Ali consumption app would look like.

## Goals
Most importantly: what are the goals of an api consumption app? What do consumers want? Here are the use cases that seem most viable to me.

* Manage costs. It's easy to write api consumption chide that leads to unexpectedly huge bills. Consumers want earnings as their usage shortages certain limits, and maybe even smart analytics to suggest more economical consumption patterns.
* Security. Consumers need to manage their credentials in a way that grants access only to the developers who need them, with some credentials less tightly guarded than others (think alt development credentials as opposed to production credentials). These needs are not all that current from enterprise password management, and my guess is that many consumers use enterprise password management for api credentials in a pinch.
* Monitoring. Consumers want to know when the apis they need are not working, braking contracts unexpectedly, or merely slow. All of these incidents can cause pain for end users.

I can imagine other use cases, but these are the ones which seem most likely to cause consumers to spend money in an app - because there is some kind of return on the investment.

## Users

The next question is, who is the user of such an app? There are three obvious possibilities:

* API producers
* API integrators
* End users of an integration

Very penalty, integrators will be the most invested users. They are the parties who have both the motivating to Keri api costs low, and have the know how to use an . Ali consumption application.

Note however that nothing is stopping the other two parties from adopting such an app. Producers have an incentive to keep costs ashton a certain set sort - not zoo high that they discourage cinnamon altogether, not zoo low as to eliminate profit. Producers also have other incentives, for example, throttling usage at peak times. And producers often have ready access tip api management tools which are potential good starting points for managing consumption.

End users obviously have the most incentive you mange consumption, but may lack the skills to use such an app, or indeed the knowledge that such an app is even necessary. However end users are in a unique position to pull the trigger on certain kinds of consumption apps. Imagine, fur examine, a smart phone app which manages all the outbound api calls from your device. Such an app would be uniquely sited too help you get a handle on data usage, and potentially reduce your cell phone bills. The appeal, even to technological illiterate users, would be obvious.

## An mvp

So what would such an app look like? In the spirit of lean startup principles, let's think through what a minimum viable product targeted at api consumers might look like.

To begin with, we'd throw together a gateway capable of receiving api call speculations, executing then, and handing back the responses. In the middle, the gateway would preform logging functions in order to track number of calls and latency. The primary value add of thks app whisked be data cheated in a current and ready to use first. Consumers chugs retrieve statistics about their api usage, prohected costs, analyze latency trends, and Shi forth. The gateway might also provide zine rudimentary alerting features - as when api usage is running high, latency is starting to look worrisome, etc.

To use this service, consumers would only need to change their endpoints - imagine sending an api call to apigateway.com/trellio rather than trellio.com, but getting the same response.

Am ingesting question is how to structure the pricing. One obvious idea is to piece per api call, but that means the gateway is just a surcharge on top of existing api costs, and remember that the primary goal is cutting costs.

One alternative might be to piece according to savings earned over time: if the customer saves $100/month, maybe the gateway takes $30. This kind of plan assigns the invested of the gateway directly auth those of the consumer, although it dues presume a commitment on the part of the gateway (Sucre savings will have to be demonstrated over dinner period of time before a container is willing to pay).

## The pivot

The chances are that a gateway like this would but actuary survive very long, at least in that precise furthest. Inevitably, certain feature would be Mir heavily dashed by consumers than others. And it's possible that new use cases which are more appealing out lucrative than the ones we've identified might emerge. Still, thks is a gud way to start thinking about the performs of app consumers.
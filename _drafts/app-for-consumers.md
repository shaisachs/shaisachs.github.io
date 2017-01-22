---
layout: post
title: Serving Consumers in the API Economy
date: 2017-01-22 14:00
bannerimg: /img/posts/meter.jpg
photographer: Gab Pili
photographerurl: https://unsplash.com/@gabpili
---

One of the big hits at APIStrat 2016 was Mark O'Neill's talk on the [API Economy](https://boston2016.apistrat.com/speakers/mark-oneill), and specifically, on the needs of API consumers. There are a lot more consumers than producers, the thinking goes, so why does the API industry spend so much time on the needs of producers and so little on the time of consumers?

Good question! The implicit answer: we should spend more time providing support to API consumers as a class of users. But how exactly do we do that? O'Neill hinted at a few ideas, but really left the question as an exercise for the listener.

Below, I've attempted to fill in the blanks a bit. What would an API conumption service look like?

## Goals
Most importantly: what are the goals of an API consumption service? What do consumers want? Here are the use cases that seem most viable to me.

* **Manage costs**. It's easy to write API consumption consumption that leads to unexpectedly huge bills. Consumers want warnings as their usage approaches certain limits, and maybe even smart analytics to suggest more economical consumption patterns. Wouldn't it be great (as a consumer) to know that if you just reschedule your API calls a bit, you could cut your bills in half?
* **Security**. Consumers need to manage their credentials in a way that grants access only to the developers who need them, with some credentials less tightly guarded than others (think about credentials for a sandbox or development environment, as opposed to credentials for a production environment). These needs are not all that different from enterprise password management, and my guess is that many consumers use enterprise password management for API credentials in a pinch. But the two services are different, and there are sure to be pain points in this approach: for example, systematically separating production and development credentials, segmenting credentials by tenancy, etc. 
* **Monitoring**. Consumers want to know when the APIs they need are not working, breaking contracts unexpectedly, or merely slow. All of these incidents can cause pain - often very expensive pain - for end users.

There are probably many other use cases that a consumption service could address, but these are the ones which seem most likely to cause consumers to actually plunk down money. Each of these use cases gives consumers a fairly obvious return on investment.

## Users

The next question is, who is actually paying for a consumption service? Who is the user? There are three obvious possibilities:

* API producers
* API integrators
* End users of an integration

Very probably, integrators will be the most invested users. They are the parties who have both the motivation to keep costs low, and the know-how to use an API consumption service.

Note however that there's no reason that such a service couldn't target either of the other two audiences. Producers have an incentive to keep costs within a certain range - not so high that they discourage consumption altogether, and not so low as to eliminate profit. Producers also have other incentives, for example, throttling usage at peak times. And producers often have ready access to API management tools which are potentially good starting points for managing consumption as well as production. So it's entirely possible that an API consumption service might have its origins in an API management service.

End users obviously have the most incentive to mange consumption, but may lack the skills to use such a service, or indeed any knowledge of what an API is, in the first place. However, end users are in a unique position to pull the trigger on certain kinds of consumption services. Imagine, for example, a smart phone app which manages all the outbound API calls from your device. Such an app would be uniquely suited to help you get a handle on data usage, and potentially reduce your cell phone bills. It could have an alluring appeal, even to the most tehcnologically illiterate users.

## An MVP

So what would such a service look like? In the spirit of lean startup principles, - and with the acknowledgement that the ideas below are probably pretty close to what a lot of people were thinking when they first heard Mark's talk - let's think through what a minimum viable product targeted at API consumers might look like.

To begin with, we'd throw together a gateway capable of receiving API call specifications. The gateway would execute those calls, and hand back responses. Along the way, the gateway would preform logging functions in order to track number of calls and latency. The gateway's primary value-add would be clear, easy-to-use data about consumption patterns. Consumers could retrieve statistics about their usage, project out their monthly bills, analyze latency trends, and so forth. The gateway might also provide some rudimentary alerting features - as when API usage is running high, latency is starting to look worrisome, etc.

To use this service, consumers would only need to change their endpoints - imagine sending an api call to `https://apigateway.com/someservice` rather than `https://someservice.com/api`, without having to change a single line of consumption code.

An interesting question is how to structure the pricing. One obvious idea is to price per api call, but that makes the gateway appear to be just a surcharge on top of existing API costs, and remember that the primary goal is cutting costs.

One alternative might be to price according to savings earned over time: if the customer saves $100/month, maybe the gateway takes $30. This kind of plan aligns the incentives of the gateway directly with those of the consumer, although it does presume a commitment on the part of the gateway - since it won't be possible to bill a consumer for a month or two (or even more) after the first API call execution.

A key problem, right out of the gate, will be the increased latency inherent in such a gateway. An additional network hop will require some degree of added latency, no matter how speedy the gateway's application code is. It might be possible to work around that problem by focusing on niche APIs where latency is not a huge problem; or alternatively the problem could be mediated by replicating the code and database in a wide variety of geographic locations. But  this issue would certainly pose a barrier to entry for many customers.

## The pivot

The chances are that a gateway like this would not actually survive very long, at least in the precise format I've described. Inevitably, certain features would be more heavily used by consumers than others. And it's possible that new use cases which are more appealing or lucrative than the ones we've identified might emerge. Still, fleshing out the idea of a consumer-focused gateway is a good way to start thinking about this relatively under-served niche of users.

---
layout: post
title: Down with the standards committee
---


One of the bigger questions in API development is how to keep your API consistent as it undergoes expansion and maintenance from a far-flung and diverse group of programmers. Consistency is crucial because it reduces the barrier to entry for third parties and reduces the burden of documentation.

Many organizations appoint a standards committee. This committee is a small group of developers who act as gatekeepers to the API, deciding which changes are acceptable, and which are not. It's an understandable and even appealing approach, but of course it can be a major bottleneck to ongoing development efforts. Let's look at some alternative approaches that are nimbler and more efficient.

## Use tests to prevent breaking changes

One of the most important functions of the standards committee is to prevent breaking changes from reaching production. Developers who might not know any better could easily delete a property from a data contract and thereby unwittingly break all sort of integrations.

The best approach here, which is fairly well-used, is to write automated tests which detect breaking changes, and to gate releases on these tests. This approach is more expensive at the margins, but much more effective than human review. As a bonus it can help catch regressions in your front end or other key services, to the degree that those services share common code paths with your API.

## Publish api standards

An important, but by no means sufficient, measure is to publish your API standards internally, and to update them as new questions arise.

Such a document should specify how routes are constructed, how responses should be formatted, which kinds of parameters are acceptable, and so forth. It should provide as much clarity as possible, keeping in mind that overly restrictive rules can cause friction in the development process or shut down novel ideas before they after hatched.

It's a good idea to write up standards and make then widely available, but it's not sufficient. Developers don't always read standards documentation, especially when pressed for time.

What developers actually do - whether we like it or not - is copy and paste working code. And for this reason it's important to complement a standards doc with a working example that addresses the various problems that come up in API development. Such example code allows developers to copy, paste and tweak in a way that should result in standards-compliant APIs; it keeps developers safely in the pit of success.

## Facilitate non-compliance, within reason

Despite your best efforts, developers will inevitably want to skirt the standards for one reason or another. Sooner or later, you'll realize that you should not stand in the way. Doing so runs the real risk of delaying valuable feature releases just to satisfy a standards document, which can be a costly error.

The trick is learning when to stand your ground, and when to let a non-standard API through the cracks. Often a good line to draw is an external release - will third parties ever see this API? If not, it's probably safe to bend the rules a little, given that the decision to do so is well understood by everyone involved.

Over time, it may even make sense to lean-in to these sorts of exceptions. Provide programmatic facilities to indicate where standards are not followed - and to ensure that non-compliance is used only in limited circumstances. It may well be that a few carefully chosen exceptions help preserve the integrity of standards for the remaining APIs.

## Provide guidance, early and often

There are some cases where you really can't bend the rules, of course - the API is just too important to third parties, and inconsistency will cause too many headaches.

The best way to face these cases is head on. As much as possible, give developers guidance on their APIs - whether through an email list, Slack channel, or even in-person office hours. And the ideal time to intervene is before a single line of code is written. Encourage developers to send you API documents - preferably as well-formatted OpenAPI files - as a way to prototype their APIs. Docs are to APIs what mockups are to UIs; they are a cheap mechanism for testing out requirements.

## Long live the guidance group

You may have noticed that all of these measures require the efforts of a group of developers whose primary focus is maintaining the API. That sounds a lot like a standards committee. Aren't we trying to get rid of that?

Yes and no. A standards committee that blocks releases is going to be counter-productive more often than not, almost by definition. Instead I prefer to think of a “guidance group" which can help lead fellow developers in the principles of API development. (Even if it doesn't sound as cool as "standards committee.") APIs written for third parties are fundamentally different from code written for internal consumption, and you need developers who understand that difference. But it's better for those API-focused developers to think of their job as helping to guide others, rather than acting as traffic cops.
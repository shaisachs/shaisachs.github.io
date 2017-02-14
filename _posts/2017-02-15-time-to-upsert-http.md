---
layout: post
title: "Time to UPSERT HTTP"
date:   2017-02-07 20:00
bannerimg: /img/posts/pencils.jpg
photographer: Angelina Litvin
photographerurl: https://unsplash.com/@linalitvina
---

The standard dogma in RESTful API design is that HTTP verbs should be used almost like thin translations on top of the SQL statements which they request: GET for SELECT, POST for INSERT, etc. It's an elegant idea which works very well - for databases that were designed 15 years ago.

Modern databases now support UPSERT semantics in one form or another: in a single statement, either create a resource, or update an existing resource if one is found. It's an eficient way to accomplish something end users ultimately want: the ability to store data without worrying about looking it up. Shouldn't modern APIs follow suit?

In classic RESTful design, UPSERTs require two API calls, a GET followed by a POST or PUT as appropriate. Such design is wasteful, requiring two database transactions even if a single UPSERT is possible. Generally speaking it's possible to take advantage of UPSERTs in the UI without much fuss, but of course the problem is that APIs are designed for many more transactions than UIs. To make APIs less efficient than UIs seems terribly pear-shaped.

And of course, there's already a movement towards UPSERT semantics in APIs - for example, see the `/findOrCreate` endpoints that Strongloop generates as a matter of course. While these endpoints are useful, maybe even mission-critical, they are not RESTful, since they embed the operation to be conducted in the resource itself (e.g., `/books/findOrCreate`). It sure would be nice to have a mechanism which allows us to take advantage of RESTful principles and database best practices.

More than performance tuning, there's also a question of consistent semantics. The problem with a "findOrCreate" endpoint isn't really that it doesn't neatly fit a definition in a paper; rather, it's that the meaning of such an idiom can readily change from one service provider to the next. In particular - which part of the POST body is the candidate key used for the find operation, and which part is the part of the resource to be updated? There's no programmatic way to communicate the resource identifier, as there is with a PUT operation. For that matter, there's no programmatic way to determine that `POST /resources/findOrCreate` indicates an UPSERT as opposed to, say, `POST /resources/upsert`, or some other magic string in the route. These endpoints are fine as stop-gap measures, but eventually we will need to improve.

A new HTTP UPSERT verb could readily give us exactly those semantics: just put the candidate key in the parameters on the resource collection. In particular, what I propose is an UPSERT verb which would be called as follows:

```
UPSERT /resources?candKeyPart1={value1}&candKeyPart2={value2}...
{
  "property1": "property1Value",
  "property2": "property2Value"
}
```

For successful inserts, the response would look like this:

```
201 Created
Location: /resources/{id}
```

And successful updates:

```
303 See Other
Location: /resources/{id}
```

A benefit of this approach should be immediately obvious: it allows the client to think about resources in terms of candidate key, without necessarily needing to concern itself with the preferred identifier provided by the server. In some scenarios, this benefit can be quite handy - as when the candidate key is something the end user is very familiar with, and the primary key is somewhat obscure. A case that comes to mind is airline flight information: end users know   approximately when their flight leaves, where it departs and where it arrives, but they usually don't know the flight number. An UPSERT can use the information that an end user has without additional fuss, while a PUT or PATCH must rely on a preceding GET to discover the preferred identifier.

I suspect that there are some purists who wont't like this idea: it requires mucking with standards, it's merely a performance tweak, some of these semantics can be achieved by jerry-rigging PUT, etc.

Needless to say: it's a bad idea to muck with HTTP standards every time someone comes up with a clever database performance improvement.

On the other hand, it's a bad idea to allow standards to fall too far behind current usage, too. Doing so runs the risk of a proliferation of different *de facto* standards, a fragmented landscape for consumers to navigate, and gradual drifting from the original goals of RESTful architecture. Now is the time to UPSERT the standard.

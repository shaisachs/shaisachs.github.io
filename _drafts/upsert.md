---
layout: post
title: upsert
---


Do we need an UPSERT verb?

The standard dogma in RESTful API design is that HTTP verbs should be used almost like thin translations on top of the SQL statements which they request: GET for SELECT, POST for INSERT, etc. It's an elegant idea which works very well - for databases that were designed 15 years ago.

Modern databases now support UPSERT semantics in one form or another: in a single statement, either create a resource, or update an existing resource if one is found. It's an eficient way to accomplish something end users ultimately want: the ability to store data without worying about looking it up. Shouldn't modern APIs follow suit?

In classic RESTful design, UPSERTs require two API calls, a GET followed by a POST or PUT as appropriate. Such design is wasteful, requiring two database transactions even if a single UPSERT is possible. Generally speaking it's possible to take advantage of UPSERTs in the UI without much fuss, but of course the problem is that APIs are designed for many more transactions than UIs. To make APIs less efficient than UIs seems terribly pear-shaped.

To be sure, there's already a movement towards UPSERT semantics in APIs - witness the "findOrCreate" endpoints that come bog-standard in Strongloop. But while these endpoints are useful, maybe even mission-critical, they are not RESTful. It sure would be nice to have a mechanism which allows us to take advantage of RESTful principles and database best practices.

More than performance tuning, there's also a question of consistent semantics. The problem with a "findOrCreate" endpoint isn't really that it doesn't neatly fit a definition in a paper; rather, it's that the meaning of such an idiom can readily change from one service provider to the next. In particular - which part of the POST body is the candidate key used fo the find operation? There's no programmatic way to communicate they key as there is, let's say, with a PUT /{id} operation. For that matter, there's no programmatic way to determine that POST /findOrCreate indicates an UPSERT as opposed to, say, POST /upsert, or some other verb in the route.

An UPSERT verb could readily give us exactly those semantics: just put the candidate key in the parameters on the resource collection. For example, for a book store which uses author and title of book as candidate key, the route would be UPSERT/books?author={authorName}&title={title}. As is currently the case with findOrCreate endpoints, a 200 status code would indicate a successful update, a 201 would indicate a successful insert, and a 400 would indicate an error in the request.

I suspect that there are some purists who wont't like this idea: it requires mucking with standards, it's merely a performance tweak, some of these semantics can be achieved with PATCH, etc. And of course, it's a bad idea to muck with HTTP standards every time someone comes up with a clever database performance improvement.

On the other hand, it's a bad idea to allow standards to fall too far behind current usage, too. Doing so runs the risk of a proliferation of different de facto standards, a fragmented landscape for consumers to navgate, and all the rest of it. It's time to make the UPSERT verb happen!
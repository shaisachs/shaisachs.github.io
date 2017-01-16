---
layout: post
title:  "REST and GraphQL are different languages"
bannerimg:
photographer:
photographerurl:
---

There's a problem in the way we talk about GraphQL and REST.

I've been following the development of GraphQL with a bit of apprehension over the past year or so. There has been something that seemed a little bit off about it, and I couldn't quite put my finger on it. Until, that is, I read Bruno Pedro's interesting [list of reasons not to use GraphQL](https://blog.hitchhq.com/graphql-3-reasons-not-to-use-it-7715f60cb934) this weekend. It's a pretty good analysis of GraphQL's shortcomings, and it puts into words thoughts I couldn't quite put together myself, so I appreciate that.

My first reaction to GraphQL was something like: "great, someone took SOAP, made it look a bit like it was using JSON as a wire format, but retained all the complexity and difficulty of implementation." Having spent plenty of time fiddling with XML parsers and chasing down WSDL validation problems, it wasn't exactly an appetizing prospect.

GraphQL's supporters tend to talk about it as though it's the next iteration in API development: REST succeeded SOAP, and GraphQL will succeed REST in time. Consider, for example, Otto von Wachter's [comparison of REST and GraphQL](https://medium.com/@ottovw/rest-api-downfalls-and-dawn-of-graphql-dd00991a0eb8) from earlier this summer.

He's not wrong... but he's also not entirely right. The same could be same of Bruno Pedro's post. REST is chattier. GraphQL is too lackadaisical about real versioning problems. REST tends to create complicated and annoying payloads; GraphQL binds consumers to producer data models far too deeply. There are real pro's and con's on both sides, and neither is exactly superior to another.

Here's the real problem: REST is not superior to GraphQL in all respects, nor is the reverse true. It is better to think of them as two different languages. REST is a good way to talk to third-party developers. GraphQL is better-suited for internal applications - which is exactly where it originated, as a way for Facebook's mobile app developers to grab data from the server with minimum overhead.

Problems around versioning are not as sharp when developing an API meant only for internal consumers. Nor is it a very serious problem when internal consumers  wind up closely bound to the data model of producers under the same organizational umbrella. On the flip side, chattiness is a very serious problem for internal applications - as two separate services within an organization grow more chatty in their interactions, that organization becomes more and more tempted to abandon APIs altogether in favor of database sharing or other backend tricks. GraphQL is a good way to talk about these sorts of problems.

There's a legitimate need for GraphQL, and it really does appear to solve some important problems. But it's not superior to REST; it's just a different set of rules which happen to be better-suited to certain kinds of API problems.
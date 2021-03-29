---
layout: post
title: "Healthy Habits API: Filling out the API stack"
date: 2018-02-03 13:30
tags: api, sideproject
---

I'm a big fan of the idea that the journey of a thousand miles begins with a single step. That makes me something of a sucker for new year's resolutions, particularly those of the "do something small every day" variety. So this month, I put together an API to help me keep track of healthy habits - things like go to the gym every day, get to bed early, take a walk, and so on.

The goal of this API is to build on the abstraction work in the [Gift Ideas API](https://shaisachs.com/2018/01/03/gift-ideas-crud-aspnet-core2-rapidapi.html). In particular, I wanted to extend the framework I had started there to encompass what I think of as a full API stack. The full API stack includes the following concerns:

* **Documentation**: Providing documentation about available verbs and routes, preferably via OpenAPI spec.
* **Authentication and Authorization**: Identifying the client and verifying that the client may access the desired resource and verb.
* **Validation**: Validating incoming requests, and reporting out errors if necessary.
* **Translation**: Translating incoming requests into business objects.
* **Storing**: Persisting business objects.
* **Testing**: Verifying that the API operates as expected, preferably via functional tests.

In order to separate these concerns, the framework has evolved to include seven different types of base classes:

1. Data transfer objects (dtos), which represent incoming requests and outgoing responses.
2. Validators, which verify that incoming requests are valid given the resource and verb accessed.
3. Translators, which translate incoming requests into business objects, and also translate business objects into outgoing responses.
4. Repositories, which persist those business objects at the request of services.
5. Controllers, which orchestrate the interaction amongst each of these classes.

The documentation and authentication/authorization concerns were taken care of suitably in the [Gift Ideas API](https://shaisachs.com/2018/01/03/gift-ideas-crud-aspnet-core2-rapidapi.html). The former is achieved nicely via a Swashbuckle integration, and the latter requires a tiny bit of code to read and verify custom headers from the RapidAPI marketplace.

Once again I've kept the data model extremely simple, because I wanted to focus on the framework more than the particulars of the domain logic. And in any case that domain logic is pretty simple by nature. Clients can create Habits (such as "take a walk") and can then create Habit Completions for a Habit, indicating a date when a habit was completed (for example, "I took a walk on March 4th.") Full CRUD operations are available on both resources, but there is some simple validation logic included: habit names are limited in length, habit completion dates may not be in the future, and habit completions may not change the habit to which they are associated on an update.

As much as possible I've endeavored to follow the "proudly found elsewhere" philosophy, reusing best-in-class libraries where possible. As a result the translation layer relies heavily on [Automapper](http://automapper.org/), and the validation layer uses the standard .NET Data Annotation system. I'm thinking about incorporating the [Autofac](https://autofac.org/) dependency injection framework, rather than relying on the default ASP.NET Core framework; possibly I'll revisit that in a future update.

The framework is really shaping up nicely, but there's still some progress to be made. I haven't really scratched the surface of functional testing. The dependency injection code is not very DRY, as each separate class must be independently registered. And the authentication layer still relies on magic strings - it could probably benefit from a little touchup.

Still, it's a nice, easy-to-use API, the sort of thing that could become a backend for a product like [42 Goals](https://42goals.com/) or [Loop Habit Tracker](https://play.google.com/store/apps/details?id=org.isoron.uhabits). It's a lot of fun to see the code progressing from iteration to iteration. And on top of that, it's great to see a simple data model become a viable API in no time!
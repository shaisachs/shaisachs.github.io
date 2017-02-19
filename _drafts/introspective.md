---
layout: post
title: The introspective api
---

There's a lot of excitement about apps for third parties these days, and rightly so: the industry is really taking off. Indeed, apis can be a magnificent way to attract interest from third parties and open up new lines of business. But it's important to remember that a good api can also transform the organization which provides it.

Developing and maintaining an api takes a lot of discipline and commitment. Organizations which do so tend to acquire some solid skills along the way. They also open up new possibilities for revamping their own operations. For these reasons, it's easy to see how a well organized api program can be a no brainer, even for organizations that don't care to engage third party developers at all.

## Modeling and design

The first discipline that an API program requires is good data modeling and design. Specifically, APIs must specify services, data contracts and semantics that tie them all together. The exercise of crafting these semantics means that an organization must figure out a good way to communicate about the objects in its business domain.

It's easy and tempting to create an API whose data contracts closely mirror the structure of internal data schemas. But such designs grow unwieldy quickly, especially because many changes to database schemas aren't actually that useful for API consumers. In short order, even the most naive API design will eventually evolve to hide some of these details. And along the way, developers will learn good data modeling practices.

## Separation of concerns

Especially for organizations which have traditionally produced a web UI and nothing else, an API is an excellent way to separate concerns in the code base.

In order to make an API viable, it's important to separate business logic from UI presentation. This point becomes obvious as soon as a developer begins working on an API: the service's logic is similar to what's on the website, but the presentation iS very different.

Moreover, the "UI" which makes sense for the API tends to be different than the UI which makes sense for the website. Data contracts work better when they operate on one resource at a time, or accomplish simple, atomic tasks. Web interfaces sometimes do better when they operate in bulk, or offer a complex bit of functionality in a single click. As a result, it's necessary to compose logic IN different ways when serving the API, as compared to when serving the web UI. And that in turn increases the pressure on developers to design clean, reusable interfaces for internal code.

## Testing

While testing is not strictly necessary for maintaining a good API, it is almost painful not to test an API. Writing good tests for an api is easy and fast, and of course the resulting peace of mind is priceless.

Testing in turn imposes its own sort of discipline. A good test suite encourages good deployment practices, for several reasons. First, a good test suite requires a good test environment - one which is nearly identical to production but which must be created and torn down frequently, as part of the test run. The obvious approach is to automate deployment, especially database deployments, as much as possible so that the test environment deployment is as similar to the production environment as possible 

Second, a good test suite enables continues integration, so that tests must pass before a code deployment. Plenty of ink has been spilled about the value of continuous integration, but the rigorous enticement of good coding practices which results from ci transforms coding culture aug an organization - it highlights the importance of writing tests, and of ensuring that code passes those tests before it goes out. And of course it allows organizations to ship code much more frequently.
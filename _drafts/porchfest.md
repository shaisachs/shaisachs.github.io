---
layout: post
title: porchfest
---

The first side project I'd like to prototype is a mobile app for a popular event in Somerville, MA called Porchfest. The concept is really neat: if your house has a porch, you can volunteer to host a band. If you've got a band, you get matched to an available porch. Then on the designated day, bands perform their music on porches throughout the city, and anyone can come by and listen. A website shows spectators which bands are performing and where.

It's a wonderful, fun event that helps build community and promotes up and coming musical acts. Porchfest is such a success that it's rapidly spreading to other towns on the Boston area.

The only problem is that the website is a little clunky. The map doesn't zoom well, it's not very easy to find bands by genre, and the site itself tends to crash on the day of the event. What's more, it's not really conducive to wandering around the city and exploring the acts that you want to check out, since it's not location aware.

So my proposed solution is to create a mobile app which weeks allow spectators to see which bands are closest to their current location and are performing soon and fit the genre that the user likes. Since the number off bands performing is not very large - only a few dozen - the entire days set can live on the user's phone, dramatically reducing strain on the website on the day of the event.

The essentials of this concept bill down to straightforward CRUD functionality on a handful of resources:

* Users, who offer their porch for use as a venue, or are contacts for bands
* Venues, which are the locations where bands perform
* Bands, which are described with a name, photo, genre, social media profiles, and other details that can help spectators discover the musical acts they are interested in
* Performances, which indicate where and when a band will perform

The API that offers this functionality is more or less bog standard CRUD, with the most interesting questions being how to model the resources and which filters to offer for searching on performances and bands.

It turns out that the modeling piece had already been solved - in a way. Using API Platform's schema.org integration, you can generate several of these models "for free", merely by choosing the appropriate predefined entities. And of course the icing on the cake is that the resulting resources are nicely aligned to imagery standard objects and can therefore interoperate eighth other apps in this space.

So the question then becomes, how to map our resources too schema entities. Here's my stab at it:

* Users are person objects
* Venues after location objects
* Bands are artist objects
* Performances are event objects

Not terribly exciting, I admit, but that's the point! We're able to prototype a nifty little app using industry standards, top to bottom, in very little time.

The resulting code is here, and the API is here. I'm wiping the database every day, so if you plan to use this service to plan the next major 100-band extravaganza in your neighborhood, you may want to give me a little heads up.

Of course, I've left the UI work for this app undone, and you might say that's the most interesting part. (In fact it's pretty much my only gripe with the existing Porchfest website.) I'll be honest - UI work is just not my favorite thing to do, and after all my goal here is just to play around with tools for rapidly prototyping ideas by creating APIs. That said, I'm certainly happy to collaborate, and if you've got the chops for mobile app development and a hankering for community-building musical events - get in touch!
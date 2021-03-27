---
layout: post
title: "Falling into the pit of success"
date: 2021-03-27 06:30
excerpt_separator: <!--more-->
---

One of the favorite ideas I've encountered as an architect is the [Pit of Success](https://ricomariani.medium.com/the-pit-of-success-cfefc6cb64c8), a term which Rico Mariani coined in describing language design.

<!--more-->

> We want our customers to simply fall into winning practices by using our platform and frameworks. To the extent that we make it easy to get into trouble we fail.

This concept applies at all levels of software design, from the tiniest function to large ecommerce websites. If the person using the software gets into trouble without really trying, then the author is doing something wrong.

Here's an example of a perfectly useful function that is also terrible:

```
public decimal PriceToEarningsRatio(decimal price, decimal earningsPerShare = 0) {
    if (earningsPerShare == 0) {
        throw new ArgumentNullException(nameof(earningsPerShare));
    }

    return price / earningsPerShare;
}
```

It's something of a toy example but I hope it dramatizes the problem: if you call this function without thinking about it, you wind up with an exception that you now have to handle. I've heard these kinds of default-failure mechanisms referred to as "foot guns," I think because they make it easy to shoot yourself in the foot. It's far better if the second parameter is not optional, forcing you to think a bit about what's going in there. You might still wind up with an exception, but at least the function author didn't make that the default scenario!

When we talk about non-coding "customers" the problem becomes even more important: imagine an ecommerce website which caused you to buy a product every time you checked out a product's details page, somehow without prompting for credit card details. That's not success! Chances are good that this hypothetical website would quickly lose the ability to process payments and would go out of business rapidly.

## Make good defaults

The positive spin on this concept is that it is possible to guide customers into success, by creating sensible defaults that tend to be the successful path in most cases. In the case of an ecommerce website, a checkout page is an example of such a default - it gives customers the chance to review their purchases before plunking down credit card details. There's an entire field of study for this kind of thing as it applies to software customers - usually going by names like usability design, user experience studies, and the like.

There is not, to my knowledge, a well-defined field of study for making good defaults in software itself, and that's a real shame. The toy example above is a little preposterous, but it's not that far off from some of the code I've seen, and indeed have written myself.

As a software architect I think that one of my primary missions is creating a pit of success for the developers I work with, and the teams that depend on my code. That can take many forms - usually something like shipping a good library, or designing a code template that other developers can repurpose for their own needs.

One of the places where this concept first became real to me was a project I worked on about 10 years ago, to introduce dependency injection into a pretty large legacy code base. We used [Autofac](https://autofac.org/), which is a pretty interesting project from this point of view. The big downside with Autofac, and many dependency injections, is that it's possible to create some really disastrous scenarios - for example you can wind up swapping two users' sessions, thereby winding up with leaked security details. (I'm not sure if this problem is still as prevalent in Autofac these days, but it was a very acute issue in my mind during this project.) We had to be very careful with our program's startup code to ensure that such a thing could not happen, and I'm sure I wrote some code that later developers have cursed through their teeth in pursuit of that particular goal.

The big upside of dependency injection, though, is that it allows developers to "forget" about the problem of the dependency graph, which is a pretty terrible problem if you get too far into the weeds. If you have a service `A` which depends on `B` and `C`, each of which depend on some subset of services `D`, `E`, and `F`... you quickly wind up with a real pain in the neck when you try to use `A`. Without a dependency injection library, developers tend to "flatten" their object dependency graphs, mashing the code for `D`, `E`, and `F` into a single un-cohesive messy class `G` which makes their lives easier... for a little while; eventually they pay a steep price for such shortcuts. Dependency injection reverses this tradeoff, almost eliminating the cost of splitting up classes or creating new layers in the code base. Now developers can have a much more successful mindset, in which refactors can proceed to answer questions like "what is the right abstraction?" rather than "how much of a pain will it be to instantiate this ugly object graph?" On balance that tends to make refactors much more pleasant, and testing a great deal more comfortable.

Since that long-ago project, a lot has changed. Dependency injection is now a first-class citizen in .NET Core, so there's no need for development teams to wrangle the intricacies of Autofac; they get those features for free just by following a typical hello-world tutorial. (Though for what it's worth, I still like Autofac quite a bit.) From the point of view of framework design, that's a perfect example of causing customers to "fall into winning practices."

## Good defaults make good standards

Many is the standards doc that arrived to great fanfare, a tremendous amount of negotiation, and ample hostilities on the subject of formatting conventions. Few and far between is the standards doc which engineers follow with great fidelity. I've seen, and indeed written, a few such documents in my day. Early in my career, I would be disappointed whenever I learned that standards had fallen into disuse; these days, I think it's essentially destined to happen. The reason is fairly obvious: standards docs are boring to read and difficult to remember. If you write a standards doc that is meant to apply to a 100-engineer team, chances are that about 20 engineers will read it, 5 will remember what it says, and maybe 1 will understand it well enough to actually apply its rules in day-to-day coding. Yes I did make those numbers up.

We can use the Pit of Success to invert this problem. If we design good coding mechanisms, and they drive engineers towards success, then those coding mechanisms become a kind of *de facto* standard. Engineers follow the standard because to do otherwise would take time and energy: they would need to invent their own coding standard, which would take more time than just following along with what their colleagues are doing.

To return to the earlier example: dependency injection pairs well with coding standards around separating persistence and business logic. If we have a dependency injection framework which makes it really easy to create a persistence logic class, and a business logic class, and to nicely invoke the one from the other, then the framework makes the standard. Engineers see a lot of code that looks like this sample:

```
class BalanceService {
    
    public BalanceService(IOrdersRepository ordersRepo,
        IPaymentsRepository payemtnsRepo)
    {
        // hold onto injected repos here...        
    }

    public decimal GetOutstandingBalance(int customerId)
    {
        var credits = _paymentsRepo.GetTotalPayments(customerId);
        var debits = _ordersRepo.GetTotalOrderCosts(customerId);

        return credits - debits;
    }  
}

class OrdersRepository : IOrdersRepository
{
    public OrdersRepository(IDatabase db) { }

    public decimal GetTotalOrdersCosts(int customerId)
    {
        return db.Query("
            SELECT SUM(cost)
            FROM Orders 
            WHERE CustomerId = @customerId
        ", customerId);
    }
}
```

The easiest thing for engineers to do is to emulate working code - or, let's face it, to copy-paste. With the above code sample, it's actually kind of difficult to imagine using the `IDatabase` object directly inside the `BalanceService` - more so if all of the other repositories in your code base follow roughly this pattern. Even more so if dependency injection rules only allow for `IDatabase` objects to be injected into `Repository` objects somehow. It's pretty easy to see that repositories use databases and services use repositories. You could write this pattern up in a standards doc, but that would just be gravy - the working code would be the driving factor in enforcing the standard. Hello, lasagna code; goodbye spaghetti!

To be sure, it's not always easy to create a pit of success for every standard. It's difficult to create pits of success around naming practices, for instance, because choosing good names is such a subjective art. But where it's possible to do so, it's often worthwhile.

## ... but build good power tools, too

The problem with good defaults is that they can become, in a sense, *too* good. Not all tools are good for all purposes, and if you have a really good tool but it's packaged in the wrong way, you can wind up encouraging poor usage.

I've seen interesting examples of this problem in email usage. Back when online image sharing was a relatively new phenomenon - before Flickr, before even the advent of good "attach multiple files" workflows in email clients - you'd occasionally run into the problem of needing to share multiple images with someone. Assuming you can't readily spin up a website with a dedicated image gallery library, what do you do? A common practice was to create a document in Word, insert a bunch of pictures into it, and email the Word document to your friends. Problem solved! One way to think of this scenario is, Word had created a kind of pit of success around grouping multiple images into a file; email had created a pit of success around sharing files. Email users connected the dots and created a kind of working solution for sharing multiple images. Of course it was far from ideal - the emails would get marked as spam, the attachments were hard to read if you didn't have Word on your computer, the attachments were vectors for all sorts of nasty viruses, and on and on. Very likely, that is why Flickr and its successors emerged: to create pits of success around photo sharing.

The same problem applies to engineers, though they may not always recognize it. A misused abstraction can be just as damaging as a Word file with a virus, but much more difficult to diagnose. All the more so when that abstraction is packaged inside an attractive developer experience! Among my favorite examples of this problem is the one-at-a-time / bulk usage scenario. Given a really nice API for interacting with the data model one-row-at-a-time, consumers will tend to avoid bulk usage APIs (which are typically much more difficult to consume.) I'm seen this exact problem a number of times, and what often happens is that a for loop which makes sense in code review goes awry in the middle of the night. Combating this kind of problem can be enormously difficult and resource-intensive: the API provider must build good "power tools," and adorn those power tools with a really good developer experience. That way there is no comparative advantage to the "simple tools," - the pit of success for the simple case doesn't wind up being a plain-old pit of failure in the complex case. But of course, digging all these pits takes time and resources!

# Behavioral software

In a way, the concept of the pit of success is not really new, nor is it unique to software. Indeed it borders on trivially common-sensical!

Economists have a name for this kind of thinking: "behavioral economics." The landmark study in this field found that 401k participation rates sky-rocket when employers automatically enlist their employees, instead of setting up arcane opt-in procedures. The study findings famously challenged the foundations of classical economics, because they showed employees acting in a manner which was clearly not in their own economic self-interest. (In a sense, employees who failed to follow opt-in procedures were paying thousands of dollars a year for the luxury of not hunting down and filling out a few forms.) Witness the rise of behavioral economists, who argue for things like sensible defaults in public policy.

The pit-of-success architect is not very different from a behavioral economist. The pit-of-success architect sets up sensible defaults so that engineers don't have to work very hard to write good code. The behavioral economist sets up sensible defaults so that employees don't have to work very hard to reap their 401k benefits. There's plenty more to it than that, but there is certainly a common line of thinking.

In a sense, behavioral economics is really just injecting a little common sense into its parent field. Though it's a very valuable finding, it doesn't exactly require a great deal of insight to see that arcane opt-in procedures limit participation, even at a fairly high cost to potential participants. There's something similarly common sense about pit-of-success architecture: it's fairly obvious to see that a default parameter which immediately triggers a divide-by-zero exception is asking for trouble.

At the same time, designing a pit of success is a good deal more tricky than not designing a pit of failure. The 401k example is telling: provided that an employer wants to automatically enlist employees in a 401k plan, how should the employer allocate those investments on behalf of the employee - how should the employer choose a portfolio with suitable risk exposure for a potentially wide range of employees? What sort of legal liabilities does this policy create for the employer? Software architects face similar kinds of challenges when they set out to design a pit of success.

Alas, there's no really great method I know of to create a pit of success. I do think that it's valuable to enforce automatically the best practices we want to encourage - whether it's linting in a continuous integration pipeline or creating a really great SDK. But it's easy to do the job poorly or incompletely, and we should take caution as we proceed!
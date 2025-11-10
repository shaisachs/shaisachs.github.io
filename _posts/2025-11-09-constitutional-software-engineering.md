---
title: "Constitutional software engineering"
layout: post 
date: 2025-11-09 08:00
---

What is your product's red line? What are the things it must never, never do?

Ken Segall's post on [Apple's red line](https://kensegall.com/2025/11/07/apple-is-crossing-a-steve-jobs-red-line/) the other day got me thinking about red lines for products generally. I've encountered these in many different contexts. A familiar example for anyone who's ever worked in SaaS products is: "tenants must never see one another's data." Each industry tends to have its own red lines, especially around compliance with regulations like PCI, HIPAA, etc.

Software industry red lines are interesting because they are, on the one hand, super-important; and on the other hand, often transmitted by word-of-mouth. I have always thought that part of my job as a software architect is to maintain these red lines in various ways: by learning them, educating others about them, ensuring they are not accidentally violated, etc.

Red lines are not always as clear as regulatory compliance. Often they must be discovered, debated, and socialized over and over again. They require frequent re-negotiaton as customer expectations change. Take the SaaS example above: what if two tenants actually want to share data with one another? Such changes to red lines often cause a lot of turbulence at the architectural level, as red lines are often enshrined in system design precisely to make those red lines hard to cross. 

Red lines can also degrade over time, as Segall's post demonstrates. Because red lines tend to be transmitted by word-of-mouth, and software project members tend to churn over time, the tribal knowledge of the red line churns as well.

I'm very intrigued by [Github Spec Kit's](https://github.com/github/spec-kit) concept of a software "constitution," and I have some hope that this concept, if it sees good adoption, will encourage engineers to make red lines explicit, durable, and even enforceable. I have yet to play with it but it's on my todo list.

I suspect that these are early days in what you might call "constitutional software engineering," because maintaining a constitution is going to be really difficult. To begin with, agreeing to something and remembering to write it down is not trivial. Enforcing it is even more difficult - partly because constitutional rules tend to be subjective and nuanced, partly because they must be enforced across many repositories. Keeping a constitution up-to-date is thorny, especially because constitutional "amendments" sometimes come from stakeholders far removed from the code.

Even with all those difficulties, I am encouraged by the trend towards documenting and enforcing constitutions. It makes my job that much easier!
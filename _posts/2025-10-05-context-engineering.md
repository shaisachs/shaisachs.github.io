---
title: Context engineering
layout: post 
date: 2025-10-05 08:00
---

One of the interesting findings from the Stanford AI developer productivity study (https://lnkd.in/ep8Kjs6u) is that AI is most productive in greenfield projects. That is great, except that most engineering projects are brownfield projects. It's also not that surprising - greenfield projects have always been the easiest and most fun anyway. So then - how do we leverage AI in the places we need it most? 

I am pretty encouraged by some of them emerging techniques in context engineering, especially the idea of the plan-test-implement loop. In brief, the idea is to start a project by asking the agent to analyze the code base and write a plan, which is then saved to source control. Then ask the agent to: write tests for the first subtask; implement the first subtask; ensure the tests pass; and most importantly, update the plan with any new learnings or pivots. Rinse and repeat for the other subtasks. By decomposing the project and updating the plan along the way, we ensure the agent doesn't get overwhelmed with "too much" context. 

Taken to its logical conclusion, this process becomes what Dexter Horthy calls frequent intentional compaction (https://lnkd.in/eqay6tky). The process can also be made to run asynchronously, as I pointed out in my last post, though I think an async approach requires a lot of careful planning.

I have been trying out this approach in some of my projects and I like it for many reasons. First is that it maps very nicely to the way software engineering has been done for a long time - decompose a project, implement a piece at a time, and pivot when roadblocks inevitably emerge. Second, it drives a lot of learning about the underlying code base, and leaves the engineer with a good mental model of the resulting code. Because plans can be source controlled, that mental model is more easily shared. That is critical for long term maintenance. Third, it is amenable to incremental interruptions - each step can be separately reviewed and even deployed if suitable. Perhaps most importantly, it seems to work reasonably well.

Context engineering is not a silver bullet. It requires a lot of focus; it is very sensitive to the initial plan; it is probably best rolled out to one small team at a time; and even then it can fail to materialize real gains. But I think it's a very promising direction for the future!


Also find this post on [LinkedIn](https://www.linkedin.com/posts/shaisachs_advanced-context-engineering-for-coding-agents-activity-7379123073888985089-6ZiN)!
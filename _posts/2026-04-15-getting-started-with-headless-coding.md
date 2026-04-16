---
title: "Getting started with headless coding"
layout: post
date: 2026-04-15 20:00
---

I've finally had a chance to try out some headless coding over the last few weeks, and by and large it's working out pretty well! I don't think I've discovered anything particularly revolutionary - I'm mostly stealing ideas from others and adapting them to my workflow - but I've definitely stumbled into some useful practices. Here's what I've figured out so far.

## What is headless coding?

Let's start with the basics: headless coding is the practice of writing code by prompting a coding agent, and avoiding the use of an IDE. (The IDE is the "head.") The point is not that IDEs are bad, as such, but rather that they're unnecessary, because your interface with the code is the prompt (as input) and the execution results (as output.) The code is a black box.

Claude Code is the poster child for headless coding, but I use codex. Here's an example of a really simple headless coding session:

```
codex exec "Write a python script called hello.py which prints 'hello world'."
python hello.py
```

The same thing can be done in Claude Code, Gemini, or Cursor Agent, and most of what I have to say here should transfer to those other agents as well. (But I haven't checked, feel free to correct me in the particulars.)

## One-liners and skills

The example above is a pretty simple one-line prompt, but a one-line prompt can get you reasonably far. A more realistic example might be:

```
codex exec "Refactor the code in WidgetService so that persistence logic lives in a new WidgetRepository. Make sure all tests pass before you finish. Then commit everything to git."
```

It's easy to extend to multi-line prompts too - just throw together some text into `prompt.md`, then do: `cat prompt.md | codex exec`.

If you're using Jira you can in principle use that as your source of prompts; configure the Atlassian MCP server, and then try a prompt like:

```
codex exec "Read the specifications in Jira item SOMEPROJ-1234, then implement them. Make sure all tests pass before you finish. Then commit everything to git."
```

When you are done, if your permissions are right, you should have your code waiting for you in the git commit log; you can run some smoke tests and then push.

At a certain point, typing "Make sure all tests pass..." and such becomes tiresome, so I recommend using an agentic skill. I've created a skill for myself, which does the following:

* Accept a prompt as input
* Spin up a child instance of `codex exec` to actually implement the prompt
* Make sure all tests pass
* Commit to git when you are done
* Include the prompt, as well as the name of the agent and the model used, in the extended git commit message

The skill uses a helper bash script which prepares the git commit. That means that my extended commit messages are all consistent, which may become useful if I need to parse them in the future; it also spends less tokens because my agent doesn't need to figure out what "commit to git" means when it reads the skill.

Now my one-liner is a little cleaner:

```
codex exec '$prompt-com Refactor the code in WidgetService so that ...'
```

The result is a really nice git log that preserves my prompt history for posterity, and of course nicely refactored code in the bargain.

Not every prompt is simple, and eventually you reach a more complex use case. The agent tries its best against your prompt, but there is too much code to inspect, too many changes to make, and it exhausts its context window. Or worse yet, the contents of the window become uncohesive and the code quality starts thrashing because the agent is no longer focused on a single "thought."

## Spec driven development and the coding loop

To manage this sort of complexity, we have to shift our attention away from the code and toward specs. We need to focus pretty carefully on the final vision of what we want to happen, including clear acceptance criteria, desired structure of the code, and anticipated changes or future directions we want to accommodate.

I recommend spending a good amount of time drafting specifications that lay out as much detail as possible along these lines. Sometimes the Jira item description is good enough that you can pull it directly. In any case I strongly recommend versioning specifications alongside my code, and incorporating the Jira item into the file path. For example the specs for Jira item SOMEPROJ-1234 should live in a location like:

```
./docs/plans/SOMEPROJ-1234-brief-desc/specs.md
```

Commit that thing, then get an implementation plan started:

```
codex exec '$prompt-com Read ./docs/plans/SOMEPROJ-1234-brief-desc/specs.md, then write an implementation plan. If there are any clarifying questions, include them in the plan in a 'Questions' section. Store the plan at ./docs/plans/SOMEPROJ-1234-brief-desc/plan.md'
```

It's worth giving the implementation plan a decent review, and if there are questions, provide the agent with answers and revise, e.g. `codex exec '$prompt-com The WidgetService does not need to know about joins to the fidget table - modify the implementation plan at ./docs/plans/SOMEPROJ-1234-brief-desc/plan.md accordingly.'`.

Once the plan is in order, create a task list:

```
codex exec '$prompt-com Turn the implementation plan at ./docs/plans/SOMEPROJ-1234-brief-desc/plan.md into a Markdown-formatted task list at ./docs/plans/SOMEPROJ-1234-brief-desc/task.md.'
```

The purpose of the task list is to create an artifact which the agent will burn down (as we'll see in a minute.) As the agent moves to implementation, the plan should remain mostly stable, but the task list will drive the coding loop.
x
The task list should be a fairly straightforward translation of the implementation plan, although it's worth a glance just to make sure nothing went haywire.

Now it's time for the fun part!

```
tasklist="./docs/plans/SOMEPROJ-1234-brief-desc/task.md"
while true ; do
  incomplete_count=$(grep -E '^\s- \[ \]' "$tasklist" | wc -l)
  if [[ "$incomplete_count" -lt 1 ]]; then
    break;
  fi

  codex exec "Find the first incomplete task in $tasklist. Execute it with the \$prompt-com skill. Then update the task list to mark the task complete."
done

echo "Task done"
```

This loop is known as the "Ralph loop" or the "Wiggums loop" owing to [Geoffrey Huntley](https://ghuntley.com/loop/). The idea is simple but quite clever: we break a large task down into small tasks, and feed those tasks to the agent one-at-a-time until we're done. Each iteration of the loop is a fresh context window for the agent, so there is no need to do anything clever with context compaction and the like. You could say it's context engineering taken to its logical conclusion.

I've created a little skill called `$task-do` to manage the task list mechanics for me, so in practice I just tell the agent: `codex exec "\$task-do $tasklist"`. That's a nice convenience, but it does reduce the token spend a little because the skill includes a deterministic script to do things like "Find the first incomplete task" - the agent doesn't need to think about that.

The results are pretty astounding: lots and lots of code gets written, and it's all hands-off-keyboard time. I spend an hour or two on the specs/implementation plan phase, depending on the complexity of the task, but then I kick off the coding loop and go do something else. Days' worth of code can be written this way, and the resulting code is pretty decent and generally works well. The specs and implementation plan are interesting artifacts that could be brought to bear on future maintenance, if needed, and become useful documentation of my original intent.

## What's next

There are definitely some places to explore improvements to this process. Most obviously, how can I improve the specs-writing process, and can I gave the agent an "implementation-plan-writing" skill that will ensure specs get translated to plans with good fidelity? How do I ensure that the implementation plan follows red/green TDD practices routinely?

Relatedly, I need to incorporate Architecture Decision Records (ADRs) into the process more snappily. The agent should read ADRs and judge the implementation plan against them. It should also propose new ADRs that may be needed - and maybe I can draft those while it's coding.

From a token mechanics perspective, there are obviously places to improve efficiency. The planning step clearly needs a rigorous thinking model like Opus, but simple tasks can be readily offloaded to a speedy model like Composer. Consequently it may be a good idea to mix-and-match agents so I'm not tied to GPT models for everything I do.

Moving forward, how do we review all this code that's being generated? I haven't yet, but I hope to start implementing some of the ideas Ankit Jain presented in [How to Kill the Code Review](https://www.latent.space/p/reviews-dead), and incorporate these into my loop; for example, once the coding is done, spin up a QA agent, identify bugs, and feed those back to the coding agent.

## Thoughts

For someone who's used to coding by hand, this process is extremely weird.

You can watch the commits roll in, refreshing git log every now and again, and they will steadily accumulate. At least in my setup they have my name attached, so it looks like I'm writing code at spectacular velocity.. but I definitely did not write them! It's the dictionary definition of alienation: code appears with my name on it, but it does not feel like mine and I don't have a meaningful relationship to it.

There is also an interesting question around when to cross over from one-liners to coding loops. Essentially, what kind of task is too complicated for the agent's context window? I think answering this question becomes a kind of art that software engineers will learn over time, in the same way that "decompose big functions" is an art form that we've been refining for some time now.

This practice changes the economics of what I consider feasible. If a task can be well defined and nicely decomposed, then the thought process is, "am I willing to spend about an hour to spec it out?" rather than "I need to estimate that, work out a resource allocation plan, negotiate with stakeholders, ..." Refactors are something the agent does while I'm in meetings, rather than tasks I put off to another day. Data-munging is trivial. Trolling through third-party API docs and creating a client to grab some data is a 5 minute activity (and most of those 5 minutes are spent ensuring my credentials work.)

The higher-order result is that I'm beginning to think in terms of an "outer loop," which looks something like this: prototype and experiment -> refine approach and experiment some more -> polish final product. Each of those steps is its own coding loop, but now I can accomplish weeks' worth of trial and error inside of a day or two, and the result can be much closer to the ideal state I want before I ship off to production.

It's pretty exciting to see this new practice take shape, even though I think there are still a lot of open questions and improvements to be made. I'd love to hear your learnings and suggestions!
---
layout: post
title: "Return the answer"
date: 2021-04-07 06:30
excerpt_separator: <!--more-->
tags: architecture
---

When you write a function, what does it do? What will you get back when all is said and done? The answer. Let's make that explicit, shall we?

<!--more-->

Some years back I found that very frequently I needed a variable to contain the result of a function. Sometimes I called this variable `result` or some variant, but inevitably that caused trouble - particularly in contexts where the function, or one of its neighbors, was sending an API call. In such cases the `result` variable could easily get confused with the HTTP result code, and inevitably that caused confusion about what the function was doing: was it merely a wrapper for an API call? Did it do some interesting processing with the HTTP response? What if there were a chain of API calls, which result code "won"? And so forth. Occasionally I'd slip into a rather uninspired variable name like `returnVar` or `ret` or some such, but that always felt a little weak - it somehow did not really capture the importance of the variable.

The trick I discovered, and it's served me well over many years since, is to use a magic variable called `answer` to contain "the value which this function will return". Here's a really simple example:

```
public decimal ProfitToEarningsRatio(decimal stockPrice, decimal earningsPerShare)
{
    decimal answer = 0;

    if (earningsPerShare == 0) {
        throw ArgumentNullException(nameof(earningsPerShare));
    }

    answer = stockPrice / earningsPerShare;

    return answer;
}
```

Trivial, right? In this case it really seems like there's nothing all that exciting going on; we could readily replace the ceremony of declaring and setting `answer` with a one-line `return stockPrice / earningsPerShare;` at the end of the function.

When the practice of declaring and setting `answer` becomes more interesting is when the function contains some interesting branches and loops, and the logic becomes potentially difficult to follow. In this case, beginning the function with the `answer` declaration means that the reader immediately understands that she can follow this variable through the function to determine what's going to happen at the end. No need to skip to the return statement - or the multiple return statements! - and follow the trail backwards, the code reads linearly down the screen.

The other thing that is nice about this practice, tactically, is that it allows us to introduce new intermediate logic with minimal fuss. Suppose we want to log instances of a negative profit-to-earnings ratio for some reason. When we declare `answer` at the top of the function as a matter of course, adding logic along these lines is a simple line insertion between setting `answer` and returning it. If instead we had used the terser approach - `return stockPrice / earningsPerShare;` or the like - we'd now have to introduce a variable to hold this value, then test it and log it. And chances are we'd not think very carefully about what to call that variable, and declare it only a line or two before the `return` statement, and so on - the function would get messier as a result.

What's most valuable about this practice, however, is the mental framework it gives me, and hopefully my code's readers. It's something like: "every function signature is a question, and my job is to provide the answer."

I really like that framework, because it focuses the function's attention, as it were. There is just one goal at hand, and that is properly setting and returning `answer`. It also tends to discourage side effects and encourage functional paradigms, even in languages that allow side effects. Certainly not every task is ideally suited to functional programming - but minimizing unintended side effects and focusing on the task at hand is always important.

Likewise, this framework tends to uncover scenarios where a function is trying to do too much. Why? Because it quickly becomes unclear which way to set `answer`, or because we wind up needing a new variable that is similar to `answer` but different, or something along those lines. The effort to figure that out - however minimal - hopefully provides enough mental friction to warn us that our function needs a little decomposition.

I don't think this rule is absolute, but rather a helpful framework. For example, sometimes a function lends itself to a natural domain-specific replacement for answer:

```
public int Add(int a, int b)
{
    var sum = a + b;

    return sum;
}
```

In this case we use `sum` rather than `answer` and it seems to me that the function is none the worse. However I think that such cases tend to be the minority - cases where we are merely codifying an age-old mathematical formula, or the like. More often functions have to do messy string manipulation or screwy processing of API responses, and there's no clear-cut name for "the thing that is the result of this process" - in such cases `answer` is perfect.

The other gap in this rule is cases where the final return value of a function is a fairly uninteresting derivation of a much more involved piece of logic with a different return type. In these cases, declaring and returning `answer` in a way that strictly matches the return type may actually be a disservice - the reader would be better served by following a different variable that is doing all the work. A case in point might be something like an API controller returning address standardization, where various business services participate in the actual address standardization:

```
[HttpGet("standardizedAddresses")]
public async Task<string> StandardizeStreetAddress(string streetAddress)
{
    string answer = string.Empty;

    answer = await USPSService.Standardize(streetAddress);

    if (answer == null) {
        answer = await FedExService.Standardize(streetAddress);  
    }

    if (answer = null) {
        answer = await CommercialDBLookup.Standardize(streetAddress);
    }

    return answer;
}
```

In this case you don't really want to declare a `Task<string> answer` because that winds up making the code pretty goofy. The reader winds up working a lot harder to understand the function - which of course defeats the point. 

Other interesting cases might be a complicated algorithm in which each piece of the formula is itself nontrivial, and the `answer` variable winds up doing fairly trivial work on those pieces. The [AKS Primarily Test](https://en.wikipedia.org/wiki/AKS_primality_test) comes to mind as such a scenario: determining whether a number is a perfect power, computing the multiplicative order, computing the totient function, etc., are each fairly nontrivial pieces of work, and `answer` winds up being a fairly uninteresting combination of these pieces. There's nothing wrong with the practice in this case... but more is needed to capture and properly document all of those interesting intermediate results! Unfortunately I don't think there is a really good system for describing intermediate results in cases like these, and we wind up falling back on domain-specific variable names - names like `isPerfectPower` in this case.

Setting aside its value in programming, I really like this practice because it dovetails so nicely with literary devices - particularly the ones in which authors "skip to the end" and reveal the outcome of a book on page 1. Perhaps the most perfect example of this device is from the opening lines of *One Hundred Years of Solitude*:

> Many years later, as he faced the firing squad, Colonel Aureliano Buendía was to remember that distant afternoon when his father took him to discover ice.

If my functions wind up even one-hundredth as well-written as a Gabriel García Márquez novel, I know I'm doing something right!
---
layout: post
title: "Reading up on the Goodreads API"
date:   2017-01-30 19:30
bannerimg: /img/posts/books.jpg
photographer: Annie Spratt
photographerurl: https://unsplash.com/@anniespratt
---

I started playing around with the [Goodreads API](https://www.goodreads.com/api) recently. It's quite a lot of fun, and a [snappy Python library](https://github.com/sefakilic/goodreads) keeps time-to-first-hello-world nice and low.

The app I have in mind is pitifully simple - I want to grab [my reviews](https://www.goodreads.com/review/list/16084341), archive them somewhere, and maybe even republish them here. It's a nice, straightforward exercise.

But now that I've gotten my feet wet, I'm curious what other sorts of applications might be possible. Goodreads helpfully offers a [developer forum to discuss integration ideas](https://www.goodreads.com/topic/group_folder/58737?group_id=8095), and some of these ideas I've shamelessly stolen from over there.

* **Book recommendations**. This idea is the most obvious one, and there are plenty of attempts out there to develop AI-powered book recommendations. What I have in mind is fairly low-hanging-fruit heuristic algorithms. For example, find readers who enjoyed the first book in a series, and recommend the next book in that series; find readers who seem to enjoy a particular author, and recommend other books that author publishes; and so forth. Such algorithms should be trivial to write, but very effective in driving sales.

* **Organic group shelves**. Goodreads has a group feature, and each group can have a shelf. However, the shelf must be manually curated, and doesn't necessarily have anything to do with the contents of each member's personal shelf. The Goodreads API could be used to display "organic group shelves" which list, in one place, all of the books read by members of a group, the average ratings of those books, and so forth. An app like that could be a lot of fun for book clubs, very useful in a corporate setting, and very motivating for students in an academic setting.

* **Market research**. Every book requires a marketing plan, and publishers and authors struggle to determine just which audiences might be best suited to a particular work. One way to attack this problem is to ask authors who are writing a new book to identify a few published works that are most similar to their own. The Goodreads API can then be used to find out how many users liked all of those books, as a metric by which to determine the possible size of the proposed book's audience.

* **Data visualisations**. The Goodreads website offers some interesting visualisations already - my favorite is a graph showing my books read by date of publication. But there are many other possibilities; I like the idea of showing the [change in an author's ratings over time](https://www.goodreads.com/topic/show/794564-my-new-app).

* **Movie mashups**. This idea is more for laughs than anything else, but it's a fun game I like to play at my book club. Pick a book, and let readers of that book "cast" the characters in the story using real actors. Especially in cases where a book has been adapted, it'd be fun to see how readers' casting choices differ from the studios'.

I imagine there are tons of other ideas of this sort. Some of them are more viable than others - a market research app could probably do very well economically. And some of them are potentially transformative - organic group shelves could certainly be an interesting experiment in social reading. 

I think this sort of exercise is useful for any API provider to attempt. Having a ready answer to the question, "what can a consumer do with our API?" allows providers to know if their services are meeting their intended goals.
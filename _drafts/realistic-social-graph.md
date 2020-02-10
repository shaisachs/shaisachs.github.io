---
layout: draft
title: A more realistic probabilistic graph
date: 
bannerimg: /img/posts/friends.jpeg
photographer: Annie Spratt
photographerurl: https://unsplash.com/@anniespratt
---

The probabilistic social graph, as I defined it, is well-nigh [impossible to compute to any degree of certainty](https://shaisachs.github.io/2017/09/24/probabilistic-social-graph.html). Finding a good training set, identifying retrievable features, computing reliable probabilities even in the world of perfect information, even defining the relationships we seek to find - these are thorny, ambiguous problems. It's no easy task to get it perfectly right! But to an engineer, the perfect should not be an enemy of the good: is there a way to compute a good probabilistic social graph?

## Some relationships are easier than others

In the definition of the probabilistic social graph, we are looking to compute the function `P(a, b, i)` - the probability that people `a` and `b` are related by relationship type `i`: `i` could be friendship, a professional relationship, a weak tie like having been classmates, etc.

Well, it turns out that not all relationships are created equal, especially when it comes to predicting relationships. In particular, let's think about family relationships: marriages and births, and the probability that two people are related by these relationships.

Married couples have a certain pattern: both partners tend to be within the same age range, they tend to be in broadly similar socioeconomic strata, they tend to live fairly close to one another (before they get married, that is). What is even better is that at the point they get married, they sign a public document that makes the whole thing official. From the point of view of machine learning, they create a wonderful training set that gives us a pretty reliable picture of which people, exactly, get married. The database of marital certificates is not always available for a variety of reasons. Some states simply don't make those records available, some states make them difficult to obtain for a variety of records (e.g., the certificates are not held centrally by the state, but locally in each county's registrar's office; and so on.)
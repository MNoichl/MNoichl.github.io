---
layout: page
title: Homework No. 12
has_children: false
parent: DH, Romanov, 2019
---

# Topic modelling the *Daily Dispatch*

What is really obvious about the process of topic-modelling with different pre-defined numbers of topics is how much of a difference it makes. Surprisingly, in my experimentations, on the whole the smaller number of topics seemed to yield way better results: While under the larger sample the topic of *war*, identified by words like *state*, *general*, *battle*, etc. was split into three topics with only minor differences, in the model with the  smaller `num_topics` they were neatly moved into one. Also, in the larger model, for some reason the topic of slavery, identifiable by words like *slave*, *negro*, *arrested*, *stealing*, had gone completely missing, as well as death (*death*, *died*, *church*, *god*). I played also around a little bit with the other parameters of the `gensim` implementation, and every little change seemed to make quite a difference.

On the whole I am not sure how comfortable this makes me with the results by Rob Nelson. Some of the topics he identifies seem to be very consistent. For example the ads for hiring seem to be cleanly identified by the model. With this one in particular I was wondering whether he externally validated the topic, by comparing it to the XML-tags in the text. I was also very surprised by how well the model seemed to identify humor, something that would seem like one of the last things which computers should be able to identify.

Other topics, like e.g. 'accidents, in particularily fires', seem way more noisy. Few of the example-sentences reach high topic-scores, and those that do seem to be mainly driven by the two words *accident* and *fire*, which is not very exciting to learn. This makes me wonder whether there should be some sort of topic-quality-indicator presented alongside the topic, which tells us how 'clean' a topic is, compared to the others. It would be also interesting to include that value into the visualizations.

I also wonder why, for forty topics, I received *very* different results compared to those of Nelson. While there was some overlap, and several topics matched really well, it seemed to me that on the whole, that from my results a very different (and somewhat lower quality) picture would emerge.
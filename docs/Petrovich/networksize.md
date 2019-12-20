---
layout: page
title: Importance of Scale
has_children: false
nav_order: 5
---

# [Draft] An argument for scale in (computational) intellectual history

In his comments on my recent post at this blog (LINK), Eugenio raised the interesting question of how the structure that we arive at through bibliometric methods changes, if we make changes to our sample 
I will frame this question slightly different, and try to give some indication about what I belief to be the right answer to it, using again the dataset collected by Petrovich and Buonomo 2018.

The question I'm interested in, is in how well the network structure of the most read articles, which arguably will form the picture that most people have of their discipline, mirrors the structure of the whole network. If they do  mirror it adequately -- if networks of academic relations are self-similar -- we can learn a lot about the structure of the whole by studying only the best and the few. If on the other hand they don't, we are always in considerable danger of error when we make structural claims about a discipline without considering large datasets. 

With a *structural claim about a discipline* I mean any claim about the unity or dis-unity of a certain body of intellectual production, and claims about the distance or nearness between multiple such bodies. This also includes common claims about changes in those structures.

Some examples for such structural claims, which I recently came across, might be the following:

+ "Economists of education ignore sociologists of technology; cognitive scientists never use social studies of science; ethnoscience is far remote from pedagogy;" (Latour p.16)
+ "...a new and potentially more fruitful division is emerging within English speaking philosophy. In place of the old analytic–Continental split we now have the opposition between the naturalists and the neo-Kantians." (Papineau, 2003, cited after Glock, 2008, p. 258)
+ "Within the more recent literature [of Experimental philosophy], discussion of these questions has become increasingly interdisciplinary, with many of the key contributions turning to methods from cognitive neuroscience, developmental psychology, or computational cognitive science." (Knobe & Nichols, 2017)

One might at this point ask: Unity, distance, dissimilarity – regarding what measure? When these claims are made, this is often not entirely clear. And indeed there are multiple plausible candidates for such measures. One might for example be concerned about some kind of social distance – do people interact frequently? Do they have common acquaintances? Frequent the same institutions? But one might also think about something in the realm of what might be vaguely called intellectual distances, and which would include such things as stemming from the same intellectual tradition, engaging with the same thematic field or using the same, or related concepts. 

In this case, the measure can be stated precisly: I will be using bibliographic coupling, which counts the amount of sources, which two articles share, as an indicator for their similarity. When done for all articles in a dataset, this gives a weighted network, which can then be processed further. Below I have depicted such a network made from the most cited papers in the dataset of analytical philosophy used by Petrovich and Buonomo 2018 \?

![](205_nodes_75_citations_minimum_0_k_label.png)

What does the bibliographic coupling measure actually relate to? On the one hand it certainly has a social component to it, as citations 



A sensible way to test, how well small, but illustrious samples match up with the larger samples from which they are drawn, is to let both undergo the same clustering process, and then count how often a pair of articles that ends up in the same cluster in  one clustering solution, ends up in the same cluster in the other one. If all the pairs from the smaller sample end up together in the same clusters in the larger sample, the structures of both samples match up very well. (Unless something has gone wrong with the clustering along the way.

If on the other hand they only rarely match up, we should be very cautious in drawing inferences about the whole from structures which we noted in a small sample.



The number of clusters which our clustering-algorithm settles on is not the most relevant here: If it were for example to keep a set of articles in one sample together, but simply split that set into two in the other sample -- which might well be compatible with very similar structure -- this should not have a very large impact on the rand-index, as most pairs of nodes will still be kept together in their respective sub-clusters. I have checked my results with spectral clustering, which allows two define a constant number of clusters beforehand. It doesn't make a huge difference for the results, if anything, the rand-indices get smaller and the "channel" of high rand-indices narrows.






(n) Caveats 

more formal evaluation 

even larger scale, more runs

random controls


more datasets
# Literature


Glock, Hans-Johann. What is analytic philosophy? Cambridge University Press, 2008.

Knobe, Joshua and Nichols, Shaun, "Experimental Philosophy", The Stanford Encyclopedia of Philosophy (Winter 2017 Edition), Edward N. Zalta (ed.), URL = <https://plato.stanford.edu/archives/win2017/entries/experimental-philosophy/>.


Latour, Bruno. 2003. Science in Action: How to Follow Scientists and Engineers through Society. 11. print. Cambridge, Mass: Harvard Univ. Press.
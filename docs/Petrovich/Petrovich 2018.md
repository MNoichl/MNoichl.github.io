---
layout: page
title: Petrovich
has_children: false
---

# \[Draft\] A short and informal replication of Petrovich and Buonomo 2018

I recently came across this very interesting study by Petrovich and
Buonomo (2018), in which they analyze co-citation networks for the last
three decades of analytic philosophy. After a bit of conversation with
Eugenio, I thought that I would do a little quasi-replication of their
results, to take the slightly different methods I'm trying out right now
for a little spin.

So I downloaded the sample Petrovich and Buonomo used from the web of
science. It consists of the years 1985-2014 from the following 5
journals: \*

The question that Petrovich and Buonomo are interested in is the
question whether analytic philosophy has become more diverse in these
thirty years. There various ways in which one could approach this
question. Petrovich and Buonomo go for visual inspection, and I will try
to give my own idea on that later. But, first and foremost Eugenio and
me were talking about formal evaluation of the co-citation graphs. In
what follows I am very much inspired by Tang, Cheng, and Chen (2017) who
present a recommendable longitudinal study of the digital humanities.

So the first thing I did was to try and get the transitivities for the
different samples.
[Transitivities](https://mathinsight.org/definition/transitivity_graph)
are a very basic measure of how much a graph tends to cluster. It
results from the number triangles in the graph (in our case three
sources, of which each combination was co-cited at least once) divided
by the number of triplets. A fully connected graph would score the
number 1 on this measure, while a completely unconnected graph would
result in a 0. For this little exercise I will use a sliding window
approach, in which I always consider 5 years together.

But we can make this a little more interesting by looking at the
modularity of the graph. Modularity is a measure which is dependent on a
given community structure of a graph. It compares the connectedness
within the identified communities with what would be expected, if the
links were distributed randomly, which is why it can be also used to
optimize a community-detection methods. A value above zero suggests,
that the edges within communities are more frequent than would be
expected by chance. I will use the Leiden-algorithm (Traag, Waltman, and
van Eck (2019)) to identify communities in the networks, and then
calculate their modularities relative to that. This will give us another
view into how solid groupings within the our sample are over time.

Another interesting value is how

After looking at these graph based measures, there is another
interesting thing we can do to get an idea about

Now for the most fun part, the visual inspection: A neat trick when
dealing with confusing networks is to lay out their minimum spanning
tree, instead of a usually zealously pruned version of the network
itself. I am using the wonderful tmap-library by Probst and Reymond
(n.d.), and will also use faerun, a visualization framework developed by
the same authors.

In the networks below we see the results. Because it would be annoying
to browse through 23 graphics, I will only show each of the three
decades, in the same way Petrovich and Buonomo do. To read the graphics
remember, that the minimum spanning tree-construction will try to put
the sources with the strongest connections next to each other, which is
why we have these little balls, usually around a primary source of mayor
importance, with which all the others are co-cited. But the algorithm
sometimes has to do trade-offs, so we can not expect every node to be
linked to its respective nearest neighbour.

I've been running the YAKE-keyword algorithm on the abstracts and titles
of the citing papers associated with the communities, so we can learn a
little bit more about them. Be mindful, that we have only titles for the
first decade, which is why keyword quality here is low.

It's supposed to be interactive. If it's not, maybe try it out at this
link.

<div>

<iframe src="20052014.html" width="700" height="700">
</iframe>

</div>

This seems to agree with general trends in philosophy. From a larger
dataset I had around (used in this visualization) I have extracted

![](a09b8624c4a37dec07e9ff333abca794.png)

## Remaining questions & further work


There are several things I am unsure about in the above. For example I'm
not sure whether the inner workings of YAKE might make it bad at
selecting keywords for this specific purpose. I have been very pleased
working with it, because it really seems pretty good at getting useful
keywords. Also it would seem prudent to

There seems to be some evidence that bibliographic coupling-networks are
better at

## Literature

Petrovich, Eugenio, and Valerio Buonomo. 2018. "Reconstructing Late
Analytic Philosophy. A Quantitative Approach." *Philosophical Inquiries*
6 (1): 151--82. <https://doi.org/10.4454/philinq.v6i1.184>.

Probst, Daniel, and Jean-Louis Reymond. 2019 "Visualization of Very
Large High-Dimensional Data Sets as Minimum Spanning Trees," 27.

Tang, Muh-Chyun, Yun Jen Cheng, and Kuang Hua Chen. 2017. "A
Longitudinal Study of Intellectual Cohesion in Digital Humanities Using
Bibliometric Analyses." *Scientometrics* 113 (2): 985--1008.
<https://doi.org/10.1007/s11192-017-2496-6>.

Traag, V. A., L. Waltman, and N. J. van Eck. 2019. "From Louvain to
Leiden: Guaranteeing Well-Connected Communities." *Scientific Reports* 9
(1): 5233. <https://doi.org/10.1038/s41598-019-41695-z>.

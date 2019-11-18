---
layout: page
title: Homework No. 6
has_children: false
parent: DH, Romanov, 2019
---


# Homework no. 6

# Downloading the *Daily Dispatch*
First we need to import some libraries: pandas, numpy, (now that I think about it, I think I didn't even need those), beautifulsoup to parse html, requests to do requests (duh) and re for regular expressions.


```python
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import re
```

Then we load the basic website. I have downloaded it, but that would not be necessary.


```python
soup = BeautifulSoup(open("Richmond.html",encoding='utf-8'))
```

We loop over every link that belongs to the class 'aResultsHeader', which is what is used for the search results. We save the address of the link (with a little modification, to get the whole file), and the text it uses.


```python
linklist = []
linktexts = []
for link in soup.findAll('a', attrs={'class': 'aResultsHeader'}):
    linktexts.append(link.text)
    linklist.append(link.get('href').replace('text?','http://www.perseus.tufts.edu/hopper/dltext?'))
```

Then we just loop over our links, download the xml for each of them, and name the file after the text of the link:
* The Daily Dispatch: November 1, 1860., [Electronic resource].xml
* The Daily Dispatch: November 2, 1860., [Electronic resource].xml
* The Daily Dispatch: November 3, 1860., [Electronic resource].xml
* ...


```python
for link, article  in zip(linklist,linktexts):
    
    filename = str(article)+'.xml'
    print(filename)
    with open(filename, 'wb') as f:
        f.write(requests.get(link).content)
```
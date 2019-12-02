---
layout: page
title: Homework No. 7
has_children: false
parent: DH, Romanov, 2019
---


# Homework no. 7

# Splitting the *Daily Dispatch*
First we import some libraries:

```python
import pandas as pd
import numpy as np
import re
import os
from tqdm import tqdm, tnrange, tqdm_notebook

```

Then we loop over each file in the appropriate directory, replace all xml-tags by using a regex and save the resulting plaintext in another directory, replacing the .xml-ening with .txt.

```python
directory = 'richmond'
directory_clean_text =  'cleaned_richmond_full'
for filename in tqdm_notebook(os.listdir(directory)[0:100]):
    if filename.endswith(".xml"): 
        with open(os.path.join(directory, filename), 'r',encoding='utf8') as f:
            cleaned_article = re.sub('<[^>]*>', '', f.read())
            with open(os.path.join(directory_clean_text, str(filename.replace('.xml','.txt'))), 'w',encoding='utf8') as towrite:
                towrite.write(cleaned_article)
```

To get the individual articles we follow the same procedure as above, but split every dispatch into articles on 'div3', and then loop over the individual articles:

```python
directory = 'richmond'
directory_clean_text =  'cleaned_richmond'
for filename in tqdm_notebook(os.listdir(directory)[0:100]):
    if filename.endswith(".xml"): 
        with open(os.path.join(directory, filename), 'r',encoding='utf8') as f:
            article_list = re.split('<div3 type=\"article\".*>', f.read())
            article_id = 0
            for a in article_list[1:]:
                article = re.split('<\/div3>',a)[0]
                cleaned_article = re.sub('<[^>]*>', '', article)
                with open(os.path.join(directory_clean_text, str(filename.replace('.xml','') +'_'+ str(article_id)+'.txt')), 'w',encoding='utf8') as towrite:
                    towrite.write(cleaned_article)
                article_id = article_id + 1
```
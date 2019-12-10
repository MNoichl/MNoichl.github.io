---
layout: page
title: Homework No. 8
has_children: false
parent: DH, Romanov, 2019
---


# Homework no. 8

# *Daily Dispatch* to .tsv
After the same imports as last week, we define a little function that strips off .xml tags from any string we pass to it. Then we loop over every file. We split at the markers for articles `<div3 type=` and then take the first of these items, and split it at `<date value\=\"`. The next then letters that come after this are the date we are interested in, and so we save it to the variable `date`. Then we loop over the individual articles, splitting off the first tiny bit, which was left from the `<div3`-tag, and keeping it, as it denotes the article type. In a similar fashion we get the content of the head and the article, to which we apply theremove_xml-function.

Then all variables of interest are appended to a dictionary we defined earlier. When the loop has concluded, we convert the dictionary to a dataframe, check whether everything looks nice, and then save it off as a tab-seperated file.


```python
def remove_xml(x):
    return re.sub('<[^>]*>', '', x)

directory = 'richmond'
results = {}
count = 0

for filename in tqdm_notebook(os.listdir(directory)):
    if filename.endswith(".xml"): 
        with open(os.path.join(directory, filename), 'r',encoding='utf8') as f:
            article_data = []
            article_list = re.split('<div3 type=', f.read())
            date = re.split('<date value\=\"',article_list[0])[1][0:10]

            for a in article_list[1:]:
                article_type = re.split('\"',a)[1]
                article_header = remove_xml('<' +re.split('<\/head>',a)[0]).replace('\n','%%%%%')
                article = remove_xml(re.split('<\/div3>',a)[0]).replace('\n','%%%%%')
                results[count] = [date, article_type, article_header,article]
                count += 1
                
results_df = pd.DataFrame.from_dict(results, orient='index', columns=['date', 'article_type', 'article_header','article'] )
results_df.to_csv('results.tsv', sep='\t',escapechar ='\\')

```


# Python-Progress:

![2019-12-10](2019-12-10)
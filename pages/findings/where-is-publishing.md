# Where is this research published, communicated and discussed?

### Where are the top 10 places for publishing data-related research as a whole?
To understand where the research is published, communicated and discussed we utilised the Lens dataset, which enables us to look at the type of publication, the journal and the publisher. Unfortunately 360Giving and Gateway to Research do not have relevant data to allow us to answer these questions. The Lens dataset is primarily made up of journal articles, accounting for 75% of the total. The remaining documents are mostly book chapters and conference articles. 

```yaml table
data: data/lens_publications.csv
autowidth: true
order:
  - [1, 'desc']
columns:
  - data: source title
  - data: publications
  - data: citations
```
*Data Sourced from The Lens*

The Lens dataset contains 273 different publishers, with 48 publications missing data. However, it is worth noting that the dataset is relatively noisy. There are many single-article journals – 205 of the 273 journals only accounting for single articles in the dataset. Social Science Research network is the most popular journal in this ‘data-related’ research dataset, publishing 22 articles over the last two years. The top journals are based in the US, UK and Canada, matching with the locations of historically prestigious universities. One interesting aspect of the results is the difference in citation from the publications in each journal. Despite featuring the most publications, the 22 articles in the Social Science Research Network were only cited three times in total. On the other hand, the 12 articles from the Journal of Medical Internet Research were cited 385 times. However given the discrepancy we can assume there may be some bad data in the dataset. 

```yaml table
data: data/lens_publishers.csv
autowidth: true
order:
  - [1, 'desc']
columns:
  - data: publisher
  - data: publications
  - data: citations
```
*Data Sourced from The Lens*

Regarding publishers there is a much smaller spread, with 118 different publishers across the 565 articles with 84 publications missing data. Similarly with the journal data above, the data is messy. There are several entries for different publishers, for example, there are six different entries from Elsevier each with a slightly different set of words. In the next iteration of this report, further manual cleaning of the data would help paint a clearer picture of the publishers in this dataset. Elsevier BV is the top publisher, with 49 articles published in the two years covered by this dataset. The following 10 publishers range from Springer International Publishing with 45 publications, down to SAGE Publications with 15, showing a much shorter tail to the data compared to looking at journals. Regarding citations, Springer International Publishing has a surprisingly small 34 citations for its 45 publications, while Cambridge University Press (not in the top 10) has 248 for only two publications. 

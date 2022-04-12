# How much funding is being directed at each of the 10 keywords from ‘Data 2020’?
The second question this project wanted to answer was ‘how much funding is being directed at each of the 10 keywords from the ODI’s  [Data 2020](https://theodi.org/article/data-2020/)  project?’. Here we don’t focus on funders, but rather on the 10 keywords which were used as search terms for the initial discovery of the three datasets. Again, to answer this question we use data from 360Giving and Gateway to Research, as the Lens does not have the relevant financial data. As discussed in the methods section, for the sake of simplicity, we are defining ‘data-related research’ as a cluster of ten keywords:

* Data ethics
* Data sharing
* Misinformation
* Data infrastructure
* Digital economy
* Value of data
* Data rights
* Data literacy
* Digital trade
* Automated decision making

### Total amount of funding for each keyword in 360Giving (2012–2021)

```yaml table
data: data/360giving_keywords.csv
autowidth: true
order:
  - [2, 'desc']
columns:
  - data: keyword
  - data: amount
  - data: grants
  - data: average amount
```

Looking at the amount of funding each of our 10 keywords received, ‘Data Sharing’ is clearly the most popular, receiving 75% of the funding in the dataset, and accounting for two thirds of the grants. This is perhaps unsurprising given the broad nature of the keyword in comparison to some of the others. ‘Automated decision making’, ‘digital trade’ and ‘data infrastructure’ did not feature in the 360Giving dataset. On average, projects looking at the ‘value of data’ and ‘digital economy’ received higher value grants than any other keywords except ‘data sharing’. This appears to be a result of a number of high value projects from the Cabinet Office.

### Total amount of funding for each keyword in Gateway to Research (from 2020-2022)

```yaml table
data: data/gtr_keywords.csv
autowidth: true
order:
  - [2, 'desc']
columns:
  - data: keyword
  - data: amount
  - data: projects
```
*This project was listed in Gateway to Research as having £0 in the funding amount.*

Within Gateway to Research we see a slightly different story. While the largest number of projects funded in the Gateway to Research dataset were around topics of ‘Data sharing’, projects on the topic of ‘digital economy’ received nearly double the funding in total. ‘Data infrastructure’ is also well funded here, thanks to significant funding from the Economic and Social Research Council. On the other side, ‘Data literacy’ did not receive any funding, and ‘data rights’, ‘value of data’, ‘automated decision making’, and ‘data ethics’ received very little. There was one project under ‘digital trade’ but it was listed as having £0 funding – which we take to be a limit or error in the Gateway to Research data. Lastly, it is worth noting again that a decision was made to remove projects related to misinformation due to unreliable search results. 

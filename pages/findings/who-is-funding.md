# Who is funding data-related research (as a whole)
The second question was: ‘Who is funding data-related research in each of the three datasets we are using?’ For this question we wanted to look at the top 10 funders based on a series of different metrics. Unfortunately, the Lens does not have suitable financial data to support answering this question, so we used 360Giving and Gateway to Research here. We look at the total amount of money that each funder had put towards data-related research, and the quantity of grants they had provided. 

### Total number of grants in 360Giving (2012–2022)

```yaml table
data: data/360giving_funders.csv
autowidth: true
order:
  - [2, 'desc']
columns:
  - data: funder
  - data: amount
  - data: grants
```

Within the 360Giving dataset, there is approximately £30m of funding for data-related research across 72 grants. Wellcome  is the largest funder of data-related research in the 360Giving dataset, by both value and number of the grants. Its grants make up approximately 62% of the total value of funding within the dataset. The largest grant of nearly £2.5m went to the  [The Global Alliance for Genomics and Health](https://www.ga4gh.org/)  to support ‘Setting the Standards for Genomics and Health-Related Data Sharing’, while the smallest was just over £4,200 to an unlisted individual to support the ‘Development of Operational Guidance for Epidemics Ethics’ demonstrating the breadth of support Wellcome offers to the health sector. Interestingly, the third largest funder (by value) in the dataset only provided one grant. The Geospatial Commission (via the Cabinet Office) awarded £2,409,375 to the  [Greater London Authority](https://www.london.gov.uk/)  to pilot a national data-sharing platform on the location and condition of underground assets.

Finally, it’s worth noting that as a proportion of the total funding these organisations deliver which have been collected via 360Giving, our ‘data-related research’ dataset remains a very small minority. None of the funders in the table below devote more than 1% of their funding to projects in this dataset.

### Number of projects and amount of money per funder in Gateway to Research (2020–2022)

```yaml table
data: data/gtr_funders.csv
autowidth: true
order:
  - [2, 'desc']
columns:
  - data: funder
  - data: amount
  - data: projects
```

Within the Gateway to Research dataset there were 78 grants worth £86,255,21 in total. The distribution of funders differs from the 360Giving dataset in that there are two large funders Innovate UK, the UK’s national innovation agency, and The Engineering and Physical Sciences Research Council (EPSRC), which both support around 23 projects, with a total value of around £28m. On the other end of the scale, The Biotechnology and Biological Sciences Research Council (BBSRC), only supports two projects, with a value of £332,068.

To put these total numbers in context, according to Gateway to Research data, between 2020 and 2022 these funders awarded a total of £7,391,655,257 over 24,531 projects.  

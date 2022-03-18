
# Who is conducting ‘data-related research’?


## Who are the top 10 ~research organisations~ conducting research in this area as a whole?

### For this question we are looking at data-related research as a whole - rather than at individual keywords - based on different metrics.
### Who are the top 10 research organisations in this area by total amount of funding received?
### Who are the top research organisations in this area based on the total number of projects won?

## 360Giving

```yaml table
data: data/360giving_researchers.csv
autowidth: true
order:
  - [3, 'desc']
columns:
  - data: organisation
  - data: grants
  - data: amount
  - data: years
  - data: min-year
  - data: max-year
```

## Gateway to Research projects
### Top 20 in order of amount funded
### Caveat: not all projects have an amount of funding

```yaml table
data: data/gtr_researchers.csv
autowidth: true
order:
  - [1, 'desc']
columns:
  - data: organisation
  - data: amount
  - data: projects
```

## Discussion of these findings and any necessary caveats, clarification or context
* ### [xxx]
* ### Producing a table of top authors by number of publications or citations would have been possible - either as a whole or for each keyword - but we decided not to because of reasons…

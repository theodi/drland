

# Who is funding ‘data-related research’ (as a whole)
* For this question we chose to focus on the top 10-20 funders based on a series of different metrics
	* Parameters
		* What: data-related research - ie the ten keywords
		* When: 2020-2021/22
		* Where: UK
	* Metrics
		* Total amount of money;
		* number of grants/ projects; 
		* total number of publications funded
	* Caveats, clarifications and context
		* The different databases don’t contain the same data/ columns
			* 360Giving doesn’t have publications
			* Funding data is harder to analyse within Lens for a given country
			* Project-level data for funders is spotty

### Total amount of money for grants in 360Giving / Total number of grants in 360Giving

```yaml table
data: data/360giving_funders.csv
width: 800
order:
  - [2, 'desc']
columns:
  - data: funder
  - data: amount
  - data: grants
```

Within the 360Giving data set, there is approximately £30 million of funding for data related research across 72 grants.

### Number of projects and amount of money per funder in GtR

```yaml table
data: data/gtr_funders.csv
width: 600
order:
  - [2, 'desc']
columns:
  - data: funder
  - data: amount
  - data: projects
```

### Of the list of top UK funders, who are most occurring funders and what number of citations within our Lens dataset?
* Filter by citations
* Work down until we’ve identified 10 distinct funders
* Standardise the names if there are any variations
* Tally up the number of citations for each of those funders within the top 100
* (recognising it is an extremely small sample)
* (citations is a way of gauging impact, therefore, this is, in a way, top funder by impact)
* [xxx INSERT: table/chart xxx]

### Discussion of these findings and any necessary caveats, clarification or context
* [xxx]

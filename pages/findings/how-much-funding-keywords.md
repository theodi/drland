
# How much funding is being directed at each of the ten keywords from ‘Data 2020’?

* For this question we chose to focus not on individual funders, but on the total amount of funding (and projects?) for each of the ten keywords/topics that make up our initial sketch of ‘data-related research’
	* As discussed in the methods section, for the sake of simplicity, we are defining ‘data-related research’ as a cluster of ten keywords drawn from the ten ‘hot topics’ in  [Data 2020](https://theodi.org/article/data-2020/) .
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
### Total amount of funding for each keyword in 360Giving (from 2012-2021)
* For 360Giving we are looking at grants awarded in the **ten years from 2012-2021** (ie since the founding of the ODI)

```yaml table
data: data/360giving_keywords.csv
autowidth: true
order:
  - [2, 'desc']
columns:
  - data: keyword
  - data: amount
  - data: grants
```

### Total amount of funding for each keyword in Gateway to Research (from YEAR-YEAR)
* (For GtR we are looking projects that started in the last two years, 2020-2022)
* **Important caveat**: including the keyword “misinformation” ballooned the returned results from the low hundreds up to 40,000 for reasons we could not understand. So we left it out. 

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

### Total citations for each keyword in Lens (from YEAR-YEAR)

```yaml table
data: data/lens_keywords.csv
autowidth: true
order:
  - [2, 'desc']
columns:
  - data: keyword
  - data: citations
  - data: publications
```

### Discussion of these findings and any necessary caveats, clarification or context
* [xxx]

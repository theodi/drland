# Has the amount of funding for data-related research changed over the last decade?
To analyse funding trends over time, we examined the funding portfolios over the last 10 years of two of the funders we interviewed during the qualitative phase of the project. We examined two government funders, ESRC and Innovate UK, as they had the most projects in Gateway to Research. We chose to focus on only two funders because we did not have time to analyse the portfolios of all the organisations we interviewed, and because some of the funders we spoke to do not publish funding data in a way that facilitates the type of analysis we wanted to conduct. Below we outline the questions we asked and our findings.

## Total funding for ESRC and Innovate UK data-related research over ten years

```yaml table
data: data/gtr_esrc_iuk.csv
autowidth: true
order:
  - [2, 'desc']
columns:
  - data: funder
  - data: amount
  - data: projects
```

Using our keyword search in Gateway to Research, and then doing our labelling process, we found ESRC and Innovate UK have funded 131 data-related projects between 2012 and 2022 with £244,766,406 in funding (although 10 projects had a listed funding amount of £0).

To put these amounts in context, ESRC and Innovate UK from 2011 to 2022 together funded 24,530 projects with a total funding amount of £7,391,655,257 (1,213 projects had no funding values).

### Breakdown of ESRC and Innovate UK funding by year
We looked at whether the funding amounts and number of projects for data-related research increases within our dataset for ESRC and Innovate UK. For the funding amount, the answers seem inconclusive, although this could be down to missing funding information. However, for the number of data-related projects funded it does seem to increase somewhat over recent years, particularly with Innovate UK funding.

```yaml image
path: ../../assets/esrc_iuk_funding.png
width: fit
height: unset
class: border
```

```yaml image
path: ../../assets/esrc_iuk_projects.png
width: fit
height: unset
class: border
```

## Who were the main recipients of ESRC and Innovate UK funding?

### ESRC funding
We can see that ESRC primarily focuses on funding universities. However, there are two exceptions with the Northern Ireland Stats Res Agency and a Behavioural Insights Team.

Again, we see Gateway to Research’s data limitations, with five projects having £0 funding.

```yaml table
data: data/esrc_fundees.csv
autowidth: true
order:
  - [1, 'desc']
columns:
  - data: fundee
  - data: amount
  - data: projects
```

### Innovate UK funding
Digital Catapult dominates the funding received from Innovate UK, with an award of £75 million. However, looking at the results this seems to be funding for the centre as a whole and not for individual projects. However, much of Digital Catapult work would be data related.

What’s different from ESRC funded projects is that a lot of the funding goes to businesses and private limited companies. However, Glasgow and Edinburgh universities are also some of the top recipients of funding. Also there’s a wider spread of funding, with grants in the tens of thousands being awarded frequently.

```yaml table
data: data/iuk_fundees.csv
autowidth: true
order:
  - [1, 'desc']
columns:
  - data: fundee
  - data: amount
  - data: projects
```

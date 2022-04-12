# Who is conducting data-related research?
Next, we asked: ‘who is conducting data-related research?’ – in this case thinking about the organisations receiving grants or support. Here we look at both the total amount of funding received, and the total amount of projects. Again, the analysis below only utilises data from 360Giving and Gateway to Research, due to the fact that the Lens only details the authors of different reports, but not their institutions. It was decided to not delve deeper into the researchers working in this space in this project, but it remains an area for further study. 

### Who are the top 10 research organisations conducting research in this area as a whole?
To answer this question, we looked at data-related research as a whole – rather than at individual keywords – based on different metrics. More specifically, we are asking:
* Which are the top 10 research organisations in this area by total amount of funding received? 
* Which are the top research organisations in this area based on the total number of projects won? 

#### 360Giving

```yaml table
data: data/360giving_researchers.csv
autowidth: true
order:
  - [1, 'desc']
columns:
  - data: organisation
  - data: amount
  - data: grants
```

In the 360Giving data, the top funded organisations are heavily weighted towards UK-based academic institutions. The University of Oxford received the highest amount of funding, and the most projects over the last 10 years. The 10 grants to the University of Oxford come entirely from the Wellcome Trust and are all focused on health-data-related research. The remainder of the funding in the 360Giving dataset is quite evenly dispersed across a number of different institutions, including the European Bioinformatics Institute and the Greater London Authority. 

#### Gateway to Research

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

Within the Gateway to Research dataset, the University of Edinburgh received the most funding (approximately £33m) as well as the highest number of projects (seven). Of the seven grants, there is one outlier. The University received a grant from Innovate UK for a sum of approximately £22m to establish the ‘Global Open Finance Centre of Excellence in Central Scotland to safely unlock the potential of customer data as a force to improve lives’. As with the 360Giving dataset, the organisations in the top 10 are dominated by UK academic institutions, with the Alan Turing Institute and the Scottish Government the only exceptions. 

The heavy presence of academia in these tables is perhaps unsurprising. However, the lack of civil society organisations is more telling. Other than the Alan Turing Institute, none of the other major data-focused civil society organisations feature near the top of these lists, despite all receiving substantial government and philanthropic support. This indicates one of the limitations with these datasets in answering these kinds of questions about data-related research. 

Producing a table of top authors by number of publications or citations would have been possible – either as a whole or for each keyword – but we decided not to because of the format of the author data in the Lens. The data on authors is a string, with each author separated by a comma. While this type of analysis would be straightforward on other software, working with such data in Google Sheets proved difficult. As such, we prioritised working on the different fields of study (which were in a similar form), rather than looking into the authors.
# What are the most-cited articles for data-related-research in The Lens (2020-2022)?

Next we wanted to understand what the topic articles within data-related research were over the past two years. For this question we were interested in the top articles across all of our 10 data-related keywords as well as what the top articles were for each of those keywords. 

```yaml table
data: data/lens_cited_articles.csv
autowidth: true
order:
  - [1, 'desc']
columns:
  - data: title
  - data: keyword
  - data: citations
```
*Data Sourced from The Lens*

### Total citations for each keyword in The Lens (Jan 2020–Feb 2022)

```yaml table
data: data/lens_cited_keywords.csv
autowidth: true
order:
  - [1, 'desc']
columns:
  - data: keyword
  - data: citations
  - data: publications
```
*Data Sourced from The Lens*

These two tables show the top articles in the Lens dataset based on citation count. Of the 20 most-cited articles within the Lens dataset it is perhaps not surprising that so many are related to ‘data sharing’ and ‘misinformation’. Data sharing was one of the most general terms within our set of keywords and misinformation has been relevant throughout the Covid-19 pandemic. Zooming out, the total number of publications and citation count by keyword paint a familiar picture. ‘Data sharing’ and ‘misinformation’ are the most common keywords by some distance. While ‘digital trade’ and ‘digital rights’ are by some distance the least common.

We think there are two reasons for the vast spread of these keywords. Firstly, in the cleaning and culling process, we found it easier to target relevant articles with specific but widely used terminology, like ‘digital economy’, or ‘data ethics’. Whereas it was quite difficult for incredibly broad terms like ‘data sharing’ or ‘misinformation’, which meant that more edge cases made it into the dataset. Secondly, broader terms like ‘data sharing’ and ‘misinformation’ returned many more hits than more specific or emerging keywords like ‘data rights’, and ‘digital trade’, further compounding the first point.

Given the popularity of these two keywords – ‘data sharing’ and ‘misinformation’, we used the VOSviewer software to look more closely at the landscape for research of the publications tagged with these keywords. The map for ‘data sharing’ is very similar to the map for the entire dataset, indicating the breadth of content that a broad search term like ‘data sharing’ encompases. On the other hand, misinformation is much more focused on the pandemic, with a big cluster of big circles dedicated to it. 

### **Data sharing** (320 publications)

 [Explore the ‘data sharing’ diagram here](https://app.vosviewer.com/?json=https://drive.google.com/uc?id=1wjWg9HMhsZXg0tPXkaK_bS3p5Tuc43yS)

```yaml image
path: ../../assets/vosviewer-data-sharing.png
width: fit
height: unset
class: border
```

### **Misinformation** (119 publications) 

[Explore the ‘misinformation’ diagram here](https://app.vosviewer.com/?json=https://drive.google.com/uc?id=1rcZTK9w7m5y76iHJbWoPhZDanIx2QGxm)  

```yaml image
path: ../../assets/vosviewer-misinformation.png
width: fit
height: unset
class: border
```

### Airtable views for each data-related keyword
The links below are reading lists (hosted in Airtable, an online relational database app) of the most-cited academic articles for each of our 10 data-related keywords over the past two years with the results ranked by the number of citations. We hope people who are interested in specific data-related topics will find them useful as curated reading lists. 

*  [Automated decision-making](https://airtable.com/shrlbsyfJD6IzxNKU) 
*  [Data ethics](https://airtable.com/shr0EurVsZf7ktfip) 
*  [Data infrastructure](https://airtable.com/shrv4LKlv87SibgWT) 
*  [Data literacy](https://airtable.com/shrsENkJRDev0Ty2x) 
*  [Data rights](https://airtable.com/shr1R06YLYdY2NVMC) 
*  [Data sharing](https://airtable.com/shrToVz7WmRih9OuY) 
*  [Digital economy](https://airtable.com/shrMavIcDihLkFZrF) 
*  [Digital trade](https://airtable.com/shrCjPGM3vz9IADCp) 
*  [Misinformation](https://airtable.com/shrh7wUWDiQd8IGaJ) 
*  [Value of data](https://airtable.com/shrmFFlfbJJMPCgH4) 

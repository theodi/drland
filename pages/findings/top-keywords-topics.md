# What are the top keywords and topics within data-related research?
### Top ‘fields of study’ for each of the 10 keywords in the Lens dataset

Using the ‘fields of study’ in the Lens dataset, we have defined the top 10 fields of study relevant to each of our 10 keywords. We believe this can help people interested in specific topics to better target their searches. For instance, ‘automated decision making’ is not a field of study contained within our dataset. But the list of top five fields of study related to the articles we tagged as ‘automated decision making’ can be used by people interested in automated decision-making to target their searches to capture relevant articles. Similarly, ‘data rights’ does not appear as a field of study in our dataset, but ‘digital rights’ does. People interested in ‘data rights’ should consider searching for ‘digital rights’ instead.

### An expanded list of ‘fields of study’ based on the Lens dataset

At the start of this project we chose 10 keywords from ‘Data 2020’ to serve as a stand-in for ‘data-related research’. We knew they represented only a small portion of the entire landscape, but they enabled us to begin collecting relevant funding details and publications from a diverse range of relevant topics. Once we had our dataset of 649 relevant articles, we used the ‘fields of study’ attached to each article to expand our list of data-related topics and keywords. The table below contains 3,239 distinct fields of study that are relevant for data-related research, ranked by the number of times that the field of study appeared in our dataset (each publication had at least five fields of study attributed to it). The fields of study represent the broad contours of the field of data-related research. 

Since the fields of study are widely used and standardised across the system of academic publishing, they can be used to target searches much more efficiently and reproducibly than our initial list of keywords. As we conduct further deep dives into new data-related keywords and topics we will continue adding to this list. The fields of study are categorised as:
* **First-order topics**: keywords that a directly relevant to the exploration of data, its value, management, uses and impacts – for example ‘the internet’ or ‘information privacy’
* **Secondary topics**: keywords that are not directly relevant for data-related research, but may be when combined with other relevant keywords – for example ‘research ethics’ or ‘sustainability’
* **Tertiary topics**: keywords that are only of tangential interest to data-related research, though they may appear often in combination with more relevant keywords – for example, ‘Covid-19’ or ‘Perception’
* **Research areas/departments**: keywords that are less about a topic and more about a specific branch of study or inquiry – for example‘ psychology’ or ‘chemistry’
* **Areas of works/challenges**: keywords that are more related to initiatives or challenges people are working to address – for example, ‘climate change’ or ‘sustainable development’
* **Methods**: keywords that are forms of research – for example ‘randomized controlled trial’ or ‘qualitative research’.

```yaml table
data: data/lens_field_of_study.csv
autowidth: true
order:
  - [2, 'desc']
columns:
  - data: field-of-study
  - data: categorisation
  - data: count
```
*Data sourced from The Lens*

Airtable [containing the top fields of study contained in the Lens dataset](https://airtable.com/shrFimne7d1FfrShz) .

The table below shows the distribution of fields of study across the 10 keywords from this research. To take a look at the different results, please filter the table by the keywords at the top of each column. There is a strong correlation between the fields of study and the keywords for most of the 10. For those with limited results, like Data Rights, this is more limited. 

```yaml table
data: data/lens_field_of_study_keywords.csv
order:
  - [2, 'desc']
columns:
  - data: field-of-study
  - data: total
  - data: data-ethics
  - data: data-sharing
  - data: misinformation
  - data: data-infrastructure
  - data: digital-economy
  - data: value-of-data
  - data: data-rights
  - data: data-literacy
  - data: digital-trade
  - data: automated-decision-making
```
*Data sourced from The Lens.*
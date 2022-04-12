# How dispersed is the field of data-related research?
First, we tried to identify the extent to which the field of data-related research is fragmented and dispersed. Our interviews suggested that there is indeed an emerging field of data-related research, but they also suggested that the relevant research, publications and funding are dispersed across several more established fields and areas of study. 

### Network diagram based on our corpus of 587 articles in the Lens that contain our 10 data-related keywords
We used  [VOSviewer](https://www.vosviewer.com/), a software tool for constructing and visualising bibliometric networks, to map the ‘data-related research’ field based on the Lens dataset. Using the DOIs from our dataset, VOSviewer extracted the necessary information about each publication using the OpenAlex API. The software then develops a map of circles with connecting lines to show the interconnectedness of the concepts within the datasets. Larger circles indicate more occurrences within the dataset, thicker lines between the circles mean that there are more articles which are tagged with both concepts, and the different colours are different clusters, which indicates interrelated topics. The diagram shows the rough landscape of data-related research, with data-related research spread across a range of areas of inquiry. We first created a network based on bibliographic data based on the co-occurence of concepts covered by the publications, which are based on the Microsoft Academic fields of study and have a built-in hierarchy. This clustered topics together around:

* Computer science, including topics like artificial intelligence, data sharing and internet of things.
* Social media and misinformation, including topics like political science, fake news and social psychology.
* The Covid-19 pandemic, including topics like vaccination and virology.
* Medicine, including topics like public health, health care and research ethics.
* Business, including topics like knowledge management, and digital transformation
* The internet, including topics like world wide web, and information retrieval. 

The first four fields in the above list are very distinct. They are much more interconnected than they are connected with other clusters. In comparison, the fields of business and the internet are more dispersed, and intertwined with the four other main fields. 

```yaml image
path: ../../assets/vosviewer-dispersed-field-1.png
width: fit
height: unset
class: border
```

[View the interactive diagram of ‘data-related research’ field based on the Lens dataset](https://app.vosviewer.com/?json=https://drive.google.com/uc?id=1jjs4_b4plgfwx1HDhgXJoGvStyhPDA7V)

The diagram below is based on text data, and shows a slightly different story. Using the DOIs to pull titles and abstracts from the OpenAlex API, VOSviewer then clusters words mentioned in these sections together based on co-occurrence (meaning multiple terms appear in the same abstract or title). In this map there are four distinct clusters:
* Technology and frameworks (in green)
* Pandemic and misinformation (in red)
* Research language (in blue)
* Collaboration (in yellow)

This map presents a less clear picture of the landscape of data-related research for the Lens dataset, as a result of counting co-occurrences of terms rather than looking at distinct concepts. As such, common words for abstracts, like ‘framework’ or ‘theme’ feature heavily, but don’t help us to understand the field as a whole. 

```yaml image
path: ../../assets/vosviewer-dispersed-field-2.png
width: fit
height: unset
class: border
```

[View the interactive diagram of ‘data-related research’ field based on text data](https://app.vosviewer.com/?json=https://drive.google.com/uc?id=1JSCO_fhBpxPNAxb0XM_MZhfrZjMKyDh5)

# Discussion and future work

# Trends we've identified in data-related research/ interesting points

* Anything surprising or that confirms our suspicions? 
* The pandemic’s impact on funding
* Are we able to gauge the Data 2020 predictions?
* Is this an us (ie ODI) problem?
	* Are we the only ones who are looking for visibility across all these areas?
	* Yes, across the wide breadth, but there seem to be overlaps between some of the keywords, topics, themes etc, and those are likely to be interesting to other orgs/people, eg
		* Data ethics, data literacy, data governance
		* AI for good, autonomous decision making, AI ethics, explainability

### QUESTIONS TO ANSWER: How many different ‘fields of study’ and areas of research is ‘data-related’ research spread across?
* **ONE**: Using the ‘fields of study’ in the Lens dataset, is it possible to produce a list of all the fields of study in our culled dataset, ranked by the number of times that the field of study appeared in our dataset? **DONE**
	* This should help us expand our list of ten ‘data-related’ keywords (which were admittedly chosen semi at random based on the contents of Data 2020) to a larger set of 20-30 fields of study that can be used to define the WIP boundaries of data-related research.
	* It should also help us replace any of the ten keywords that may have a better, more standardised field of study that we should be searching for.
		* For instance, ‘data rights’ does not appear as a field of study in our dataset, but ‘digital rights’ does. Possibly data rights is not an established field of study. Going forward, we could search for digital rights instead
	* We could then continue this process in the future by searching for other relevant keywords that seem to be missing from our list, download the related articles, cull them to ensure they are relevant, then add any new relevant fields of study to our growing list of standardised fields of study within the emerging field of ‘data-related research’
* **TWO**: Using the fields of study in the Lens dataset, is it possible to define the top 5-10 fields of study relevant to each of our ten keywords? eg for those articles tagged as ‘automated decision-making’, what are the top 5-10 fields of study?
	* This would be helpful to better target searches for topics that do not have clear keywords or search terms. For instance, ‘automated decision making’ is not a field of study in our dataset. Knowing the top five fields of study related to the articles we tagged as ‘automated decision making’ would potentially help people interested in automated decision-making to target their search to capture relevant articles.
* **THREE**: Using the ‘fields of study’ from the Lens dataset, is it possible to visualise the wide landscape of academic research (math(s), physics, chemistry, biology, social science, arts and humanities, etc) and then show the amount of ‘data-related research’ being conducted within each of those areas? 
	* Basically a cluster diagram similar to this one about meta-research (research on research) being conducted in different fields…

```yaml image
path: https://github.com/theodi/drland/blob/main/assets/clusters.png?raw=true
width: 50%
height: unset
class: border
```

Possibly using  [this free(?) tool](https://www.vosviewer.com/)  recommended to us by RORI
* Short of this, even a list of fields of study related to different areas of academic research would be useful - eg a list showing fields of study related to math(s), biology, computer science, social science, economics, arts and humanities, etc

# Potential uses for different audiences

* Researchers
* Funders
* Users of research
* Policymakers
* Research on research

# Gaps and how to fill them

* *Basically a repeat of the gap-related points from the short summary report (see section below)*

# Ideas for further work (basically an internal/external sales pitch for funding to continue work on this area)

* **Overall pitch**
* There is a problem here, and we don’t know the answer, but we are committed to following up, including through further research, collaborations and playing a role as a convener… 
* **Filling in the landscape outside of government-funded academic research**
	* In the short term, further work to track funding within academia across different funders, regions, types of funding for specific topics. 
		* Sites like 360Giving and Gateway to Research provide some of this functionality, but not a wide enough view. How could this be improved?
	* In the medium term, further work could focus on the non-academic world to confirm whether:
		* It is *~possible~* to fill some of these gaps, eg by going directly to non-academic research orgs to link funding, projects and outputs
			* What other orgs are trying to map grey literature? Are these services useful?
				* Overton
				* Dimensions includes some policy/government reports
				* Altmetrics tracks some relevant aspects
		* It is *~useful~* to fill these gaps to get a more holistic view of research about data - eg being able to trace research about data from funding to output for more than just academic orgs. Can academic and non-academic be combined in an easy/meaningful way?
		* It is *~difficult~* to fill these gaps, possibly because it is time consuming with fewer systems in place
		* (aka Dr Land 2.0 - The Squeakquel) 
	* In the long term, the ODI could explore how to convene different parties and stakeholders from inside/outside academic to work to fill in the gap around ‘grey literature’
		* Convene events and workshops with relevant stakeholders
			* Eg an event with the members which is partly about gauging whether they also see a challenge and what they think might be the solutions… 
		* Explore options for adopting and adapting standards used within academia to track research outside of academia
		* Explore options for tracking non-academic research beyond of the standard methods used within academia
		* To lead by example, the ODI could publish **its own** reports and outputs in a way that is aligned with or interoperable with existing academic systems, eg by:
			* Identifying whether workable systems, schemas and publishing standards exist to publish, catalogue and connect its own to academic research
			* Demonstrating the value of doing this
			* Working with other non-academic orgs to understand their views on the matter and possibly co-designing ways of moving forward, eg by pushing the adoption of publishing standards and/or cataloguing outputs from non-academic orgs to submit them to sites like Lens Scholar
* **Work to produce a semi-automated way of searching databases like Lens and OpenAlex**
	* Every article in Lens has a list of relevant keywords and fields of study. Since we hand-culled the datasets, they should be relevant. 
	* Meaning we now have a fairly expansive set of keywords and fields of study that can serve as a starting point to define the rough boundaries of ‘data-related research’. 
		* We also have lists of fields of study for each of our ten keywords
	* We should be able to repurpose those lists to help us - and others - to search for ‘data-related research more efficiently and effectively, eg
		* For someone interested in data ethics we might be able to point them to:
			* The top 10 keywords to include with their search in order to narrow down the results and reject unuseful articles
			* The top related academic disciplines/ fields of study
			* Areas of overlap with other concepts or keywords
			* The top journal articles to focus on
			* The top research organisations working in that field
* **Making our datasets and/or infrastructure available externally**
	* OPTIONAL: An ~~interactive dashboard~~ or simply a spreadsheet that interested parties can use to conduct their own research in this area 		* The data we use should be available to download 
			* Assuming the platforms share data with appropriate licenses (Lens might be quite restrictive?)
		* Visualisations should also be reusable
		* An airtable with some of our datasets that is open and viewable

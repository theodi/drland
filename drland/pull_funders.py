import os
import csv
from dotenv import load_dotenv

import filepaths
from lens import Lens

def results_to_rows(results) -> list:
    rows = []
    for i in results:
        print(i)
        row = {'title': i['title']}
        row['funders'] = '| '.join([j['org'] for j in i['funding']]) 
        # breakpoint()
        print(row)
        rows.append(row)
    return rows

query = {
    "query": {
        "bool": {
            "must": [
                {"match": {"has_funding": True}},
                {"bool": {
                    "should": [
                        {"match_phrase": {"title": "data infrastructure"}},
                        {"match_phrase": {"abstract": "data infrastructure"}},
                        {"match_phrase": {"title": "data sharing"}},
                        {"match_phrase": {"abstract": "data sharing"}},
                        {"match_phrase": {"title": "open data"}},
                        {"match_phrase": {"abstract": "open data"}},
                        {"match_phrase": {"title": "personal data"}},
                        {"match_phrase": {"abstract": "personal data"}},
                        {"match_phrase": {"abstract": "data ethics"}},
                        {"match_phrase": {"title": "data ethics"}},
                        {"match_phrase": {"abstract": "data ethics"}},
                    ]
                }},
            ]
        }
    },
    "include": ["title", "funding"],
    # "stemming": False
}


load_dotenv()
token = os.environ.get("LENS_TOKEN")
lens = Lens(token)

results = lens.query(query)
print()
csv_rows = results_to_rows(results)

# # write out
# with open(filepaths.DATA_RESEARCH_FUNDERS_FILEPATH, 'w') as fileout:
#     writer = csv.DictWriter(f, fieldnames=["fruit", "count"])
#     writer.writeheader()

with open(filepaths.DATA_RESEARCH_FUNDERS_FILEPATH, 'w') as f:
    fieldnames = csv_rows[0].keys()
    writer = csv.DictWriter(f, fieldnames=fieldnames) 
    writer.writeheader() 
    for i in csv_rows:
        writer.writerow(i)

# print(csv_rows)
# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(csv_rows)


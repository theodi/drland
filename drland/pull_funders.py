import os
import csv
from dotenv import load_dotenv

import filepaths
from lens import Lens

def results_to_rows(results, include:bool=False, exclude:bool=False) -> list:

    with open(filepaths.FUNDERS_INCLUDE, "r") as file_in:
        funders_include = file_in.read().splitlines()

    with open(filepaths.FUNDERS_EXCLUDE, "r") as file_in:
        funders_exclude = file_in.read().splitlines()

    rows = []
    for i in results:
        row = {}

        title = i['title']
        # this is going in to a .csv file - so replace commas with spaces
        title = title.replace(',', ' ')
        row['title'] = title
    
        funders = [j['org'] for j in i['funding']] 
        funders = list(set(funders))
        add_to_results = True
        if include:
            overlap = list(set.intersection(set(funders_include), set(funders)))
            if len(overlap) == 0: add_to_results = False 
        
        if exclude:
            funders_less = list(set(funders) - set(funders_exclude))
            if len(funders_less) == 0: add_to_results = False 


        if add_to_results:
            # funders list has to fit in one cell
            row['funders'] = '| '.join(funders)
            rows.append(row)

    return rows

def write_out_results_csv(csv_rows: list, outfile: str):
    with open(outfile, 'w') as file_out:
        fieldnames = csv_rows[0].keys()
        writer = csv.DictWriter(file_out, fieldnames=fieldnames) 
        writer.writeheader() 
        for i in csv_rows:
            writer.writerow(i)

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

print('getting results...')
results = lens.query(query)

print('writing all results...')
csv_rows = results_to_rows(results)
write_out_results_csv(csv_rows, filepaths.WORKS_RESULTS)

print('writing all include results...')
csv_rows = results_to_rows(results, include=True)
write_out_results_csv(csv_rows, filepaths.WORKS_RESULTS_INCLUDE)

print('writing all exclude results...')
csv_rows = results_to_rows(results, exclude=True)
write_out_results_csv(csv_rows, filepaths.WORKS_RESULTS_EXCLUDE)

# import json
# with open(filepaths.DATA_RESEARCH_FUNDERS_FILEPATH_JSON, 'w', encoding='utf-8') as f:
#     json.dump(results, f, ensure_ascii=False, indent=4)




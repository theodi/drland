import os
import csv
import collections

import dotenv

import filepaths
from lens import Lens

def lens_results_to_rows(results, include:bool=False, exclude:bool=False) -> list:

    with open(filepaths.FUNDERS_INCLUDE, "r") as file_in:
        funders_include = file_in.read().splitlines()

    with open(filepaths.FUNDERS_EXCLUDE, "r") as file_in:
        funders_exclude = file_in.read().splitlines()

    rows = []
    for i in results:
        row = {}
        # this is going in to a .csv file - so replace commas with spaces
        row['title'] = i['title'].replace(',', ' ')
        row['year published'] = i['year_published']

        funders = [j['org'] for j in i['funding'] if 'org' in j] 
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

def results_rows_to_top_funders(results_rows: list) -> list:
    all_funders = []
    funders_rows = []
    for i in results_rows:
        row_funders = i['funders'].split('| ')
        all_funders += row_funders

    funders_count = collections.Counter(all_funders)
    for funder, count in funders_count.most_common():
        funders_rows.append({'funder': funder, 'works count': count})

    return funders_rows

def write_out_rows_to_csv(csv_rows: list, outfile: str):
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
                {"range": {
                        "year_published": {
                            "gte": "2011",
                            "lte": "2021"
                        }
                    }
                }
            ]
        }
    },
    "include": ["title", "funding", "year_published"],
    # "stemming": False
}


dotenv.load_dotenv()
lens = Lens(os.environ.get("LENS_TOKEN"))
print('getting results...')
lens_results = lens.query(query)

print('writing all results...')
results_rows = lens_results_to_rows(lens_results)
funders_rows = results_rows_to_top_funders(results_rows)
write_out_rows_to_csv(results_rows, filepaths.WORKS_RESULTS)
write_out_rows_to_csv(funders_rows, filepaths.TOP_FUNDERS_RESULTS)

print('writing all include results...')
results_rows = lens_results_to_rows(lens_results, include=True)
funders_rows = results_rows_to_top_funders(results_rows)
write_out_rows_to_csv(results_rows, filepaths.WORKS_RESULTS_INCLUDE)
write_out_rows_to_csv(funders_rows, filepaths.TOP_FUNDERS_RESULTS_INCLUDE)

print('writing all exclude results...')
results_rows = lens_results_to_rows(lens_results, exclude=True)
funders_rows = results_rows_to_top_funders(results_rows)
write_out_rows_to_csv(results_rows, filepaths.WORKS_RESULTS_EXCLUDE)
write_out_rows_to_csv(funders_rows, filepaths.TOP_FUNDERS_RESULTS_EXCLUDE)

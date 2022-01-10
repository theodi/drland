import os
import json
from dotenv import load_dotenv

from lens import Lens


# query = "data ethics"


query = {
    # "query": {
    #     "bool":{
    #         "should": [
    #             {"match_phrase": {"title": "data ethics"}},
    #             {"match_phrase": {"abstract": "data ethics"}},
    #             {"match_phrase": {"keyword": "data ethics"}},
    #             {"match_phrase": {"field_of_study": "data ethics"}}
    #         ],
    #     },
    #     "must": {"match": {"has_funding": "true"}}
    # },

    # {

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
    #  },
    # "size": 1,
    # "sort": [
    #        {
    #             "year_published": "desc"
    #        }
    # ],
    # "include": ["title", "doi"]
# }
# query = {
#     "query": {
#         "terms": {
#             "pmid": ["14297189", "17475107"]
#         }
#     }
# }

load_dotenv()
token = os.environ.get("LENS_TOKEN")
lens = Lens(token)
response = lens.query(query)

print("Status code: ", response.status_code)
# print("Printing Entire Post Request")
# print(response.json())

import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(response.json())

# from pathlib import Path
# import filepaths

# results_filepath = Path(filepaths.ROOT_DIR) / 'data' / 'results.json'
# with open(results_filepath, 'w') as outfile:
#     json.dump(response.json(), outfile)

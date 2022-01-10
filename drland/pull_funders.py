import os
import json
from dotenv import load_dotenv

from lens import Lens


# query = "data ethics"
query = {
    "query": {
        "match_phrase":{
            "title": ["data ethics", "data governance"]
        }
    },
    "include": ["title", "doi"]
}
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

from pathlib import Path
import filepaths

results_filepath = Path(filepaths.ROOT_DIR) / 'data' / 'results.json'
with open(results_filepath, 'w') as outfile:
    json.dump(response.json(), outfile)

import os
import json
from dotenv import load_dotenv

from lens import Lens

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
response = lens.query(query)

print("Status code: ", response.status_code)
import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(response.json())

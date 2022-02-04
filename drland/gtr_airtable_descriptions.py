import os

import dotenv
import pyairtable
import requests

import api
from api import Gateway
dotenv.load_dotenv()

def add_descriptions_to_gateway_airtable():
    airtable_api_key = os.environ.get("AIRTABLE_API_KEY")
    gateway_base_id = os.environ.get("GATEWAY_BASE_ID")
    table = pyairtable.Table(airtable_api_key, gateway_base_id, 'GtR - Projects - 2020-2022 - 9 keywords')
    
    update_records = []
    for record in table.all():
        url = 'https://gtr.ukri.org/gtr/api/projects/' + record['fields']['ProjectId']
        response = requests.get(url, headers={'Accept': 'application/vnd.rcuk.gtr.json-v7'})

        response_json = response.json()
        update_record = {'id': record['id'], 'fields': {'Description': response_json['abstractText']}}
        update_records.append(update_record)
    
    table.batch_update(update_records)

if __name__ == "__main__":
    add_descriptions_to_gateway_airtable()

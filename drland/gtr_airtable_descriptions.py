'''
When data is downloaded from the Gateway to Research website it doesn't include the descriptions of the projects.
This is a small script to pull those descriptions from the GtR API and then use the Airtable API to write those
descriptions to the dataset. 
'''

import os

import dotenv
import pyairtable
import requests

import api
from api import Gateway
dotenv.load_dotenv()

def add_descriptions_to_gateway_airtable():
    airtable_api_key = os.environ.get("AIRTABLE_API_KEY")
    gateway_base_id = os.environ.get("GATEWAY_IUK_ERSRC_BASE_ID")
    table = pyairtable.Table(airtable_api_key, gateway_base_id, 'GtR - ESRC+IUK - 2011-2022')
    
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

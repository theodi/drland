'''
Train a simple ML classifier over Lens data to judge whether an article is relevant
to data-related research.
Output the results to the terminal 
'''

import os
import random

import dotenv
import pyairtable
import spacy

import filepaths

def create_dataset_from_airtable():
    dotenv.load_dotenv()
    airtable_api_key = os.environ.get("AIRTABLE_API_KEY")
    lens_base_id = os.environ.get("LENS_BASE_ID")
    table = pyairtable.Table(airtable_api_key, lens_base_id, 'Lens Dataset - Master')

    text_data = []
    print('pulling Airtable data...')
    for record in table.all(fields=['Title', 'Abstract', 'Include']):
        try:
            text = record['fields']['Title'] + ' ' + record['fields']['Abstract']
            label = record['fields']['Include']
        except KeyError:
            continue            
        text_data.append((text, label))

    random.shuffle(text_data)

    print('creating datasets...')
    num_train = int(len(text_data) * 0.8)
    train_docbin = dataset_to_docbin(text_data[:num_train])
    train_docbin.to_disk(filepaths.LENS_TRAINING_DATA)
    valid_docbin = dataset_to_docbin(text_data[num_train:])
    valid_docbin.to_disk(filepaths.LENS_VALID_DATA)
    

def dataset_to_docbin(dataset):
    # nlp = spacy.load('en_core_web_trf') 
    nlp = spacy.load('en_core_web_sm') 
    docbin = spacy.tokens.DocBin()
    for doc, label in nlp.pipe(dataset, as_tuples=True):
        doc.cats["Yes"] = int(label == 'Yes')
        doc.cats["No"] = int(label == 'No')
        docbin.add(doc)
    return docbin

if __name__ == "__main__":
    create_dataset_from_airtable()
    # build_ml_pipeline()
    # train_model()
    # test_model()
    # output_results()

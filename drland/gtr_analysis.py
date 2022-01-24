import pandas as pd 
import humanize

import filepaths
import api

# gateway = api.Gateway()
# params = {
#     "f": "pro.t", "f": "pro.a",   
#     "q": "\"data governance\"", 
#     "q": "\"data ethics\"",
#     "q": "\"data sharing\""
# }

def get_top_funders():
    projects_df = pd.read_csv(filepaths.GTR_PROJECTS)
    print('top funders by # of projects')
    print(projects_df['FundingOrgName'].value_counts())
    
    print('\n\n')
    print('top funders by funding amount of projects')
    for (funder, count) in projects_df['FundingOrgName'].value_counts().items():
        funding_amount = int(projects_df[projects_df['FundingOrgName'] == funder]['AwardPounds'].sum())
        funding_amount = "£" + humanize.intcomma(funding_amount)
        print(funder, funding_amount)

if __name__ == "__main__":
    # results = gateway.search_projects(params)
    get_top_funders()
    pass

# projects_df = pd.read_csv(filepaths.GTR_PROJECTS)
# keywords = ['data ethics', 'data sharing', 'misinformation', 'data infrastructure', 'digital economy', 'Value of data', 'data rights', 'data literacy', 
#             'digital trade', 'automated decision making']
# projects_df[
#     (projects_df['Title'].str.contains('|'.join(keywords), na=False, case=False, regex=True)) |
#     (projects_df['Title'].str.contains('|'.join(keywords), na=False, case=False, regex=True))
# ]

# "data ethics" OR "data sharing" OR "misinformation" OR "data infrastructure" OR "digital economy" OR "Value of data" OR "data rights" OR "data literacy" OR "digital trade" OR "automated decision making"

# pass
# import pdb; pdb.set_trace()
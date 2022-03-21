import requests

class Gateway:
    projects_url = 'https://gtr.ukri.org/gtr/api/projects/'
    page_size = 100

    def search_projects(self, params: dict) -> list:
        results = []

        headers = {'Accept': 'application/vnd.rcuk.gtr.json-v7'}
        params["s"] = Gateway.page_size
        params["p"] = 0

        results = []        
        complete = False
        while not complete:  
            params["p"] += 1
            response = requests.get(Gateway.projects_url, params=params, headers=headers)
            response_json = response.json()

            results += response_json['project']
            print('got results', response_json['page'], response_json['totalPages'])
            if response_json['page'] == response_json['totalPages']:
                complete = True
            
        return results


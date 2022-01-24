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
            
            print(complete)
        
        return results


class Lens:
    search_url = 'https://api.lens.org/scholarly/search/'
    page_size = 1000
    
    def __init__(self, token: str) -> None:
        self.token = token

    def query(self, query: dict)-> list: 
        headers = {'Authorization': self.token, 'Content-Type': 'application/json'}
        query['size'] = Lens.page_size
        query['scroll'] = "1m"
        # query['scroll_id'] = self.page_size

        results = []
        complete = False
        while not complete:  
            response = requests.post(Lens.search_url, json=query, headers=headers)
            response_json = response.json()

            try:
                results += response_json['data']
            except Exception as e:
                print(e)
                breakpoint()

            query['scroll_id'] = response_json['scroll_id']
            
            if 'size' in query: del query['size']

            if len(results) == response_json['total']:
                complete = True
        
        return results

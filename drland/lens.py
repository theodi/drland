import requests

class Lens:
    search_url = 'https://api.lens.org/scholarly/search/'
    page_size = 1000
    
    def __init__(self, token: str) -> None:
        self.token = token

    def query(self, query: dict)-> list: 
        headers = {'Authorization': self.token, 'Content-Type': 'application/json'}
        query['size'] = Lens.page_size

        results = []
        response = requests.post(Lens.search_url, json=query, headers=headers)
        results += response.json()['data']
        return results

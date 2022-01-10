import requests

class Lens:
    search_url = 'https://api.lens.org/scholarly/search/'
    # page_size = 1000
    
    def __init__(self, token: str) -> None:
        self.token = token

    def query(self, query: dict)-> requests.Response: 

        response = requests.get(
            Lens.search_url, 
            params={"query": query, "token": self.token}
        )
        return response 

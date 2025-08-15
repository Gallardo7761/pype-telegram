import requests

class Anime:
    def __init__(self):
        self.base_url = f"https://api.waifu.pics/"
    
    def get(self, type: str, category: str) -> None:
        if type != "nsfw" and type != "sfw":
            raise Exception("Type not supported!")

        if not isinstance(category, str):
            raise Exception("Category must be a string!")
        
        response = requests.get(f"{self.base_url}/{type}/{category}")
        if response.status_code != 200:
            raise Exception("Failed to retrieve data from API!")

        return response.json()["url"]
    
    def sfw(self, category: str) -> str:
        return self.get("sfw", category)

    def nsfw(self, category: str) -> str:
        return self.get("nsfw", category)
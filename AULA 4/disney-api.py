import requests
from json import loads as json_loads

BASE_URL = 'https://api.disneyapi.dev'
FETCH = 'character'

class Disney:

    def __init__(self, id:int):
        self.id:int = id
        info = self.chamar_personagem()
        self.url:str = info.get('url')
        self.name:str = info.get('name')
        self.image_url:str = info.get('imageUrl')
        self.films:list[str] = info.get('films')
        self.short_films:list[str] = info.get('shortFilms')
        self.tv_shows:list[str] = info.get('tvShows')
        self.video_games:list[str] = info.get('videoGames')
        self.park_attractions:list[str] = info.get('parkAttractions')
        self.allies:list[str] = info.get('allies')
        self.enemies:list[str] = info.get('enemies')
    
    def chamar_personagem(self) -> dict:
        response:requests = requests.get(f'{BASE_URL}/{FETCH}/{self.id}')
        raw_content:bytes = response.content
        parsed_content:dict = json_loads(raw_content)['data']
        return dict(parsed_content)

if __name__ == '__main__':
    try:
        for n in range(1, 9000):
            id = n
            char = Disney(id)
            if char.name is not None:
                print(f'{id}:{char.name}')
                print(f'''
                    Nome: {char.name}
                    Imagem: {char.image_url}
                    Filmes:
                    {char.films}
                    Video Games:
                    {char.video_games}
                    ''')
               

                 
    except KeyboardInterrupt:
        exit()
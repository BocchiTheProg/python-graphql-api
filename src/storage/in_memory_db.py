from typing import List
from src.models.game import Game
from src.models.developercompany import DeveloperCompany

developers: List[DeveloperCompany] = [
    DeveloperCompany(id=1, name="CD Projekt Red", country="Poland"),
    DeveloperCompany(id=2, name="Rockstar Games", country="USA"),
    DeveloperCompany(id=3, name="Hoyoverse", country="PRC")
]

games: List[Game] = [
    Game(id=1, title="The Witcher 3", genre="RPG", release_year=2015, developer_id=1),
    Game(id=2, title="Cyberpunk 2077", genre="RPG", release_year=2020, developer_id=1),
    Game(id=3, title="GTA V", genre="Action", release_year=2013, developer_id=2),
    Game(id=4, title="Genshin Impact", genre="RPG, Adventure", release_year=2020, developer_id=3),
    Game(id=5, title="Honkai: Star Rail", genre="TBS", release_year=2023, developer_id=3),
]
import strawberry
from typing import Optional
from src.storage.in_memory_db import games
from src.storage.in_memory_db import developers
from src.models.game import Game
from src.models.developercompany import DeveloperCompany
from src.graphql.types import GameType
from src.graphql.types import DeveloperType


@strawberry.type
class Mutation:

    # Games Mutations

    @strawberry.mutation
    def create_game(
        self,
        title: str,
        genre: str,
        release_year: int,
        developer_id: int,
    ) -> GameType:

        new_id = max([g.id for g in games], default=0) + 1

        game = Game(
            id=new_id,
            title=title,
            genre=genre,
            release_year=release_year,
            developer_id=developer_id,
        )

        games.append(game)

        return GameType(**game.model_dump())

    @strawberry.mutation
    def update_game(
        self,
        id: int,
        title: Optional[str] = None,
        genre: Optional[str] = None,
    ) -> Optional[GameType]:

        game = next((g for g in games if g.id == id), None)

        if not game:
            return None

        if title:
            game.title = title

        if genre:
            game.genre = genre

        return GameType(**game.model_dump())

    @strawberry.mutation
    def delete_game(self, id: int) -> bool:

        game = next((g for g in games if g.id == id), None)

        if not game:
            return False

        games.remove(game)
        return True
    
    # Developer Companies Mutations

    @strawberry.mutation
    def create_developer(
        self,
        name: str,
        country: str,
    ) -> DeveloperType:

        new_id = max([d.id for d in developers], default=0) + 1

        developer = DeveloperCompany(
            id=new_id,
            name=name,
            country=country,
        )

        developers.append(developer)

        return DeveloperType(**developer.model_dump())

    @strawberry.mutation
    def update_developer(
        self,
        id: int,
        name: Optional[str] = None,
        country: Optional[str] = None,
    ) -> Optional[DeveloperType]:

        developer = next((d for d in developers if d.id == id), None)

        if not developer:
            return None

        if name:
            developer.name = name

        if country:
            developer.country = country

        return DeveloperType(**developer.model_dump())

    @strawberry.mutation
    def delete_developer(self, id: int) -> bool:

        developer = next((d for d in developers if d.id == id), None)

        if not developer:
            return False

        games.remove(developer)
        return True
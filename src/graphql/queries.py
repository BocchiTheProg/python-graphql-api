import strawberry
from typing import List, Optional
from src.storage.in_memory_db import games, developers
from src.graphql.types import GameType, DeveloperType


@strawberry.type
class Query:

    @strawberry.field
    def games(self) -> List[GameType]:
        return [GameType(**g.model_dump()) for g in games]

    @strawberry.field
    def game(self, id: int) -> Optional[GameType]:
        g = next((g for g in games if g.id == id), None)
        if g:
            return GameType(**g.model_dump())
        return None

    @strawberry.field
    def developers(self) -> List[DeveloperType]:
        return [DeveloperType(**d.model_dump()) for d in developers]

    @strawberry.field
    def developer(self, id: int) -> Optional[DeveloperType]:
        d = next((d for d in developers if d.id == id), None)
        if d:
            return DeveloperType(**d.model_dump())
        return None
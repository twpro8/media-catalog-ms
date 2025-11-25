from typing import Protocol


class SupportsToDict(Protocol):
    def to_dict(self) -> dict: ...


class SupportsEntity(Protocol):
    __dict__: dict


class DataMapper[TModel: SupportsToDict, TEntity: SupportsEntity]:
    model: type[TModel]
    entity: type[TEntity]

    @classmethod
    def to_entity(cls, obj: TModel) -> TEntity:
        return cls.entity(**obj.to_dict())

    @classmethod
    def from_entity(cls, entity_obj: TEntity) -> TModel:
        return cls.model(**entity_obj.__dict__)

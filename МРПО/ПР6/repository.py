from abc import ABC, abstractmethod
import json
from typing import Type, TypeVar, Generic, List

T = TypeVar('T')

class AbstractRepository(ABC, Generic[T]):
    @abstractmethod
    def add(self, entity: T) -> None:
        pass

    @abstractmethod
    def get(self, entity_id: int) -> T:
        pass

    @abstractmethod
    def list(self) -> List[T]:
        pass

    @abstractmethod
    def delete(self, entity: T) -> None:
        pass

class JsonRepository(AbstractRepository[T]):
    def __init__(self, entity_type: Type[T], file_path: str):
        self.entity_type = entity_type
        self.file_path = file_path

    def add(self, entity: T) -> None:
        data = self._load()
        data.append(entity.__dict__)
        self._save(data)

    def get(self, entity_id: int) -> T:
        data = self._load()
        entity_data = next((item for item in data if item['id'] == entity_id), None)
        if entity_data:
            return self.entity_type(**entity_data)
        return None

    def list(self) -> List[T]:
        data = self._load()
        return [self.entity_type(**item) for item in data]

    def delete(self, entity: T) -> None:
        data = self._load()
        data = [item for item in data if item['id'] != entity.id]
        self._save(data)

    def _load(self) -> List[dict]:
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save(self, data: List[dict]) -> None:
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)
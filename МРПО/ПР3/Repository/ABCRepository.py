from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    @abstractmethod
    def add(self, item):
        raise NotImplementedError

    @abstractmethod
    def remove(self, item):
        raise NotImplementedError
        return True

    @abstractmethod
    def get_all(self):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id):
        raise NotImplementedError

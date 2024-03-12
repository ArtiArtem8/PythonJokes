from .ABCRepository import AbstractRepository
from ..Classes.Client import Client


# noinspection PyMissingConstructor
class ClientRepository(AbstractRepository):
    """Repository for managing clients."""

    def remove(self, item):
        pass

    def get_all(self):
        pass

    def __init__(self):
        self.clients = []

    def add(self, client: Client):
        self.clients.append(client)

    def get_by_id(self, client_id: int) -> Client:
        for client in self.clients:
            if client.id == client_id:
                return client
        raise ValueError("Client not found")
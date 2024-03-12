from .ABCRepository import AbstractRepository
from ..Classes.Client import Client
from dataclasses import field, dataclass

@dataclass
class ClientRepository(AbstractRepository):
    """Repository for managing clients."""
    clients: list[Client] = field(default_factory=list)

    def remove(self, item):
        pass

    def get_all(self):
        pass


    def add(self, client: Client):
        self.clients.append(client)

    def get_by_id(self, client_id: int) -> Client:
        for client in self.clients:
            if client.id == client_id:
                return client
        raise ValueError("Client not found")
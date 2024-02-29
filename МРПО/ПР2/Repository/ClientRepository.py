from ..Classes.Client import Client


class ClientRepository:
    """Repository for managing clients."""
    def __init__(self):
        self.clients = []

    def add_client(self, client: Client):
        self.clients.append(client)

    def get_client_by_id(self, client_id: int) -> Client:
        for client in self.clients:
            if client.id == client_id:
                return client
        raise ValueError("Client not found")
import csv
import os

from clients.models import Client


class ClientService:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_client(self, client):
        with open(self.table_name, mode='a') as f:
            write = csv.DictWriter(f, fieldnames=Client.schema())
            write.writerow(client.to_dict())

    def list_clients(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=Client.schema())

            return list(reader)

    def update_client(self, update_client):
        clients = self.list_clients()

        updated_clients = []
        for client in clients:
            if client['uid'] == update_client.uid:
                updated_clients.append(update_client.to_dict())
            else:
                updated_clients.append(client)

        self._save_to_disk(updated_clients)

    def _save_to_disk(self, clients):
        tmp_table_name = self.table_name + '.tmp'
        with open(tmp_table_name, mode = 'w') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerows(clients)

        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)
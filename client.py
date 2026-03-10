class Client:
    def __init__(self, orm):
        self.orm = orm
        self.table = "clients"
        self.id_column = "id_client"

    def get_all(self):
        return self.orm.select_all(self.table)

    def create(self, data):
        return self.orm.insert(self.table, data)

    def update(self, client_id, data):
        return self.orm.update(self.table, data, client_id, self.id_column)

    def delete(self, client_id):
        return self.orm.delete(self.table, client_id, self.id_column)
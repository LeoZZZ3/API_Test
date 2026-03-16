from abc import ABC, abstractmethod

class BaseORM(ABC):
    @abstractmethod
    def select_all(self, table):
        pass

    @abstractmethod
    def insert(self, table, data):
        pass

    @abstractmethod
    def update(self, table, data, id_value, id_column):
        pass

    @abstractmethod
    def delete(self, table, id_value, id_column):
        pass

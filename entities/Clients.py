class Clients:
    def __init__ (self, id_client, prenom, nom, email, telephone, a_permis_bateau, created_at):
        self.__id_client = id_client
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.__email = email
        self.__a_permis_bateau = a_permis_bateau
        self.__created_at = created_at 
    def get_email(self):
        return self.__email

client1 = Clients(1, "Dupont", "Jean", "jean.dupont@example.com", "06 12 34 56 78", False, "2023-01-01")
print(client1.get_email())
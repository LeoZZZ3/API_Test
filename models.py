class Client:
    def __init__(self, id_client, nom, prenom, telephone, email, a_permis_bateau, created_at):
        self.id_client = id_client
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.email = email
        self.a_permis_bateau = a_permis_bateau
        self.created_at = created_at

    @staticmethod
    def from_tuple(row):
        return Client(*row) if row else None

    def to_dict(self):
        return vars(self)

class ModeleJetski:
    def __init__(self, id_modele, nom, marque, puissance_cv, capacite, permis_requis, caution, description, stock_total, created_at):
        self.id_modele = id_modele
        self.nom = nom
        self.marque = marque
        self.puissance_cv = puissance_cv
        self.capacite = capacite
        self.permis_requis = permis_requis
        self.caution = caution
        self.description = description
        self.stock_total = stock_total
        self.created_at = created_at

    @staticmethod
    def from_tuple(row):
        return ModeleJetski(*row) if row else None

    def to_dict(self):
        return vars(self)

class Reservation:
    def __init__(self, id_res, client_id, modele_id, jetski_no, debut, fin, duree, nb_pers, opt_photos, opt_gopro, opt_acc, commentaire, total, created_at):
        self.id_reservation = id_res
        self.client_id = client_id
        self.modele_id = modele_id
        self.jetski_numero = jetski_no
        self.debut = debut
        self.fin = fin
        self.duree_minutes = duree
        self.nb_personnes = nb_pers
        self.option_photos = opt_photos
        self.option_gopro = opt_gopro
        self.option_accompagnateur = opt_acc
        self.commentaire = commentaire
        self.montant_total = total
        self.date_creation = created_at

    @staticmethod
    def from_tuple(row):
        return Reservation(*row) if row else None

    def to_dict(self):
        return vars(self)

class Tarif:
    def __init__(self, id_tarif, modele_id, duree_minutes, prix, created_at):
        self.id_tarif = id_tarif
        self.modele_id = modele_id
        self.duree_minutes = duree_minutes
        self.prix = prix
        self.created_at = created_at

    @staticmethod
    def from_tuple(row):
        return Tarif(*row) if row else None

    def to_dict(self):
        return vars(self)
    
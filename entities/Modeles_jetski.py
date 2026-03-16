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
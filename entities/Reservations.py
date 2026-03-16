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
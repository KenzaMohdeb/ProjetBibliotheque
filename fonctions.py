import json

# Fonction pour charger la bibliothèque depuis le fichier JSON
def charger_bibliotheque():
    try:
        with open("bibliotheque.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Erreur de lecture du fichier JSON. Initialisation d'une nouvelle bibliothèque.")
        return []

# Fonction pour sauvegarder la bibliothèque dans un fichier JSON
def sauvegarder_bibliotheque(bibliotheque):
    with open("bibliotheque.json", "w", encoding="utf-8") as f:
        json.dump(bibliotheque, f, indent=4, ensure_ascii=False)

# Fonction pour afficher tous les livres
def afficher_livres(bibliotheque):
    if not bibliotheque:
        print("Aucun livre dans la bibliothèque.")
        return
    for livre in bibliotheque:
        lu = "Lu" if livre["Lu"] else "Non Lu"
        note = livre["Note"] if livre["Note"] is not None else "Aucune"
        print(f"ID: {livre['ID']} - Titre: {livre['Titre']} - Auteur: {livre['Auteur']} - Année: {livre['Année']} - Statut: {lu} - Note: {note}")

# Fonction pour ajouter un livre
def ajouter_livre(bibliotheque):
    titre = input("Titre du livre : ")
    auteur = input("Auteur du livre : ")
    annee = int(input("Année de publication : "))
    id_unique = len(bibliotheque) + 1  # ID unique basé sur la taille de la liste
    livre = {
        "ID": id_unique,
        "Titre": titre,
        "Auteur": auteur,
        "Année": annee,
        "Lu": False,
        "Note": None
    }
    bibliotheque.append(livre)
    print(f"Le livre '{titre}' a été ajouté.")

# Fonction pour supprimer un livre
def supprimer_livre(bibliotheque):
    id_livre = int(input("Entrez l'ID du livre à supprimer : "))
    livre_a_supprimer = next((livre for livre in bibliotheque if livre["ID"] == id_livre), None)
    if livre_a_supprimer:
        confirmation = input(f"Êtes-vous sûr de vouloir supprimer le livre '{livre_a_supprimer['Titre']}' ? (o/n) ")
        if confirmation.lower() == 'o':
            bibliotheque.remove(livre_a_supprimer)
            print("Livre supprimé.")
        else:
            print("Suppression annulée.")
    else:
        print("Livre introuvable.")

# Fonction pour rechercher un livre
def rechercher_livre(bibliotheque):
    mot_cle = input("Entrez un mot-clé pour la recherche (dans le titre ou l'auteur) : ").lower()
    livres_trouves = [livre for livre in bibliotheque if mot_cle in livre['Titre'].lower() or mot_cle in livre['Auteur'].lower()]
    
    if livres_trouves:
        for livre in livres_trouves:
            print(f"ID: {livre['ID']} - Titre: {livre['Titre']} - Auteur: {livre['Auteur']}")
    else:
        print("Aucun livre trouvé.")

# Fonction pour marquer un livre comme lu
def marquer_comme_lu(bibliotheque):
    id_livre = int(input("Entrez l'ID du livre que vous avez lu : "))
    livre = next((livre for livre in bibliotheque if livre["ID"] == id_livre), None)
    if livre:
        livre["Lu"] = True
        livre["Note"] = int(input("Entrez une note sur 10 : "))
        livre["Commentaire"] = input("Entrez un commentaire (optionnel) : ")
        print(f"Le livre '{livre['Titre']}' est marqué comme lu.")
    else:
        print("Livre introuvable.")

# Fonction pour afficher les livres lus ou non lus
def afficher_livres_lus_ou_non_lus(bibliotheque):
    choix = input("Voulez-vous afficher les livres (1) Lus ou (2) Non lus ? Entrez 1 ou 2 : ")
    if choix == '1':
        livres = [livre for livre in bibliotheque if livre["Lu"]]
        titre = "Livres lus"
    elif choix == '2':
        livres = [livre for livre in bibliotheque if not livre["Lu"]]
        titre = "Livres non lus"
    else:
        print("Choix invalide.")
        return

    print(f"\n{titre} :")
    if not livres:
        print("Aucun livre trouvé.")
    else:
        for livre in livres:
            note = livre["Note"] if livre["Note"] is not None else "Aucune"
            print(f"ID: {livre['ID']} - Titre: {livre['Titre']} - Auteur: {livre['Auteur']} - Année: {livre['Année']} - Note: {note}")

# Fonction pour trier les livres
def trier_livres(bibliotheque):
    print("\nTrier par :")
    print("1. Année")
    print("2. Auteur")
    print("3. Note")
    choix = input("Choix (1-3) : ")

    if choix == '1':
        livres_tries = sorted(bibliotheque, key=lambda x: x['Année'])
    elif choix == '2':
        livres_tries = sorted(bibliotheque, key=lambda x: x['Auteur'].lower())
    elif choix == '3':
        livres_tries = sorted(bibliotheque, key=lambda x: (x['Note'] is None, x['Note']))
    else:
        print("Choix invalide.")
        return

    print("\nLivres triés :")
    for livre in livres_tries:
        note = livre["Note"] if livre["Note"] is not None else "Aucune"
        print(f"ID: {livre['ID']} - Titre: {livre['Titre']} - Auteur: {livre['Auteur']} - Année: {livre['Année']} - Note: {note}")


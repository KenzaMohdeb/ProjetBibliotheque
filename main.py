import json
from functions import *

def menu():
    bibliotheque = charger_bibliotheque()

    while True:
        print("\nBienvenue dans votre bibliothèque personnelle !")
        print("1. Afficher tous les livres")
        print("2. Ajouter un livre")
        print("3. Supprimer un livre")
        print("4. Rechercher un livre")
        print("5. Marquer un livre comme lu")
        print("6. Afficher les livres lus ou non lus")
        print("7. Trier les livres")
        print("8. Sauvegarder et quitter")

        choix = input("Choisissez une option (1-8) : ")

        if choix == '1':
            afficher_livres(bibliotheque)
        elif choix == '2':
            ajouter_livre(bibliotheque)
        elif choix == '3':
            supprimer_livre(bibliotheque)
        elif choix == '4':
            rechercher_livre(bibliotheque)
        elif choix == '5':
            marquer_comme_lu(bibliotheque)
        elif choix == '6':
            afficher_livres_lus_ou_non_lus(bibliotheque)
        elif choix == '7':
            trier_livres(bibliotheque)
        elif choix == '8':
            sauvegarder_bibliotheque(bibliotheque)
            print("Bibliothèque sauvegardée. À bientôt !")
            break
        else:
            print("Choix invalide.")


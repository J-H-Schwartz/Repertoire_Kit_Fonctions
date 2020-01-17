# coding: utf-8
from repertoire_utils.repertoire_action import verification_existance_contact, ajouter_numero, \
    modification_numero, recherche_contact, supprimer_numero
from terminaltables import DoubleTable

repertoire = [{'NOM': 'MICHAEL', 'NUMERO': '1111111111', 'ADRESSE': 'blabla@mfloe.com'},
              {'NOM': 'LINDA', 'NUMERO': '2222222222', 'ADRESSE': 'blbblb@zvrez.com'},
              {'NOM': 'SANDRA', 'NUMERO': '3333333333', 'ADRESSE': 'fzefzzcz@fzv.com'},
              {'NOM': 'SANDRA2', 'NUMERO': '4444444444', 'ADRESSE': 'fzgzgvdsz@fzv.com'},
              {'NOM': 'SANDRA3', 'NUMERO': '555555555', 'ADRESSE': 'aaeaczzcz@fzv.com'}]
resultat = []


# Fonction Afficher_Repertoire

def afficher_repertoire(repertoire):
    tableau_contacts = [
        ["-Nom:", "-Numero:", "-Adresse:"],
    ]
    for contact in repertoire:
        tableau_contacts.append([contact['NOM'], contact['NUMERO'], contact['ADRESSE']])
    tableau_contacts = sorted(tableau_contacts)
    tableau = DoubleTable(tableau_contacts)
    tableau.inner_row_border = True
    print(tableau.table)


# Fonction Ajout contact

def ajout_contact(repertoire):
    while True:
        nom = input("Entrez le nom du contact à ajouter ou tapez Entrée pour revenir au menu principal: ").upper()
        resultat = verification_existance_contact(repertoire, nom)
        if resultat:
            print("Ce contact existe déja.")
            continue
        if nom == "":
            continue
        numero = input("Entrez le numéro du contact à ajouter: ").upper()
        adresse = input("Entrez l'adresse du contact à ajouter: ")
        ajouter_numero(nom, numero, adresse, repertoire)
        print("Le contact a bien été ajouté.")
        return


# Fonction Modification de contact

def modification(repertoire):
    destination = ""
    while True:
        modification = ""
        nom = input("Entrez le nom du contact à modifier ou tapez Entrée pour revenir au menu précédent: ").upper()
        resultat = verification_existance_contact(repertoire, nom)
        if nom == "":
            print("Retour au menu précédent.")
            break
        if not resultat:
            print("Ce contact n'existe pas.")
            continue
        else:
            destination = input("Que voulez-vous modifier ? (N)uméro / (A)dresse: ").upper()
        if destination == "N":
            modification = input("Entrez le nouveau numéro: ").upper()
            destination = 'NUMERO'
            break
        elif destination == "A":
            modification = input("Entrez la nouvelle adresse: ")
            destination = 'ADRESSE'
            break
        else:
            print("Commande non reconnue. Recommencez.")
            continue
    try:
        resultat = modification_numero(repertoire, nom, destination, modification)
        if resultat:
            print("Le contact a été modifié.")
            return
        else:
            print("Aucune modification effectuée.")
            return
    except NameError:
        return


# Fonction Recherche Contact

def recherche_de_contact(repertoire):
    resultat = []
    while True:
        choix = input("Rechercher par : (N)om  /  Numero(0) / (P)récédent").upper()
        if choix == "0" or choix == "N":
            champ = input("Entrez votre recherche: ").upper()
            if choix == "0":
                argument = {"numero": champ}
            if choix == "N":
                argument = {"nom": champ}
            if champ == "":
                print("Commande non reconnue. Recommencez")
                continue
            resultat = recherche_contact(repertoire=repertoire,
                                         type_de_recherche=choix, **argument)
            return resultat
        elif choix == "P":
            return resultat
        else:
            print("Commande non reconnue. Recommencez.")


# Fonction Suppression

def supprimer(repertoire):
    while True:
        nom = input("Entrez le nom du contact à supprimer ou tapez Entrée pour revenir au menu: ").upper()
        if nom == "":
            return
        resultat = supprimer_numero(repertoire, nom)
        if resultat:
            print("Le contact a été supprimé.")
            return
        else:
            print("Ce contact n'existe pas.")


# Début.

def main():
    while True:
        choix = input("(L)ister (R)echercher (A)jouter (M)odifier (S)upprimer (Q)uitter")
        choix = choix.upper()

        # Afficher répertoire.

        if choix == "L":
            afficher_repertoire(repertoire)

        # Ajouter contact.

        elif choix == "A":
            ajout_contact(repertoire)

        # Modification.

        elif choix == "M":
            modification(repertoire)

        # Recherche contact.

        elif choix == "R":
            resultat = recherche_de_contact(repertoire)
            if len(resultat) < 1:
                print("La recherche n'a donné aucun résultat.")
                continue
            else:
                afficher_repertoire(resultat)

        # Suppression contact.

        elif choix == "S":
            supprimer(repertoire)

        # Quitter programme.

        elif choix == "Q":
            print("Programme quitté.")
            break

        # Si aucun choix valide, reposer la question.

        else:
            print("Commande non reconnue. Recommencez.")
            continue


if __name__ == "__main__":
    main()
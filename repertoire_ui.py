# coding: utf-8
from repertoire_utils.repertoire_action import verification_contact, ajouter_personne, \
    modification_contact, chercher_personne, supprimer_personne
import repertoire_utils_text as repertoire_utils
from terminaltables import DoubleTable


# Fonction tri alphabetique
# def tri_upper(key='NOM_UPPER'):
#    return 'NOM_UPPER'


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

def ajout_contact_ui(repertoire):
    while True:
        nom = input("Entrez le nom du contact à ajouter ou tapez Entrée pour revenir au menu principal: ")
        resultat = verification_contact(repertoire, nom)
        if resultat:
            print("Ce contact existe déja.")
            continue
        if nom == "":
            continue
        numero = input("Entrez le numéro du contact à ajouter: ")
        adresse = input("Entrez l'adresse du contact à ajouter: ")
        ajouter_personne(repertoire, nom, numero, adresse)
        print("Le contact a bien été ajouté.")
        return


# Fonction Modification de contact

def modification_contact_ui(repertoire):
    champ = ""
    while True:
        modification = ""
        nom = input("Entrez le nom du contact à modifier ou tapez Entrée pour revenir au menu précédent: ")
        resultat = verification_contact(repertoire, nom)
        if nom == "":
            print("Retour au menu précédent.")
            break
        if not resultat:
            print("Ce contact n'existe pas.")
            continue
        else:
            champ = input("Que voulez-vous modifier ? (N)uméro / (A)dresse: ")
        if champ.upper() == "N":
            modification = input("Entrez le nouveau numéro: ")
            champ = 'NUMERO'
            break
        elif champ.upper() == "A":
            modification = input("Entrez la nouvelle adresse: ")
            champ = 'ADRESSE'
            break
        else:
            print("Commande non reconnue. Recommencez.")
            continue
    try:
        resultat = modification_contact(repertoire, nom, champ, modification)
        if resultat:
            print("Le contact a été modifié.")
            return
        else:
            print("Aucune modification effectuée.")
            return
    except NameError:
        return


# Fonction Recherche Contact

def recherche_de_contact_ui(repertoire):
    resultat = []
    while True:
        choix = input("Rechercher par : (N)om  /  Numero(0) / (P)récédent")
        if choix.upper() == "0" or choix.upper() == "N":
            champ = input("Entrez votre recherche: ")
            argument = {}
            if choix.upper() == "0":
                argument = {"numero": champ}
            if choix.upper() == "N":
                argument = {"nom": champ}
            if champ == "":
                print("Commande non reconnue. Recommencez")
                continue
            resultat = chercher_personne(repertoire, type_de_recherche=choix, **argument)
            return resultat
        elif choix.upper() == "P":
            return resultat
        else:
            print("Commande non reconnue. Recommencez.")


# Fonction Suppression

def supprimer_contact_ui(repertoire):
    while True:
        nom = input("Entrez le nom du contact à supprimer ou tapez Entrée pour revenir au menu: ")
        if nom == "":
            return
        confirmation = input("Êtes-vous sûr de vouloir supprimer " + nom + " de votre répertoire ? (O)ui / (N)on : ")
        if confirmation.upper() == "O":
            resultat = supprimer_personne(repertoire, nom)
            if resultat:
                print("Le contact a été supprimé.")
                return
            else:
                print("Ce contact n'existe pas. Vérifiez l'orthographe et recommencez.")
        else:
            print("Suppression abandonnée. Retour au menu précédent.")
            return


# Fonction principale du répertoire.

def main():
    while True:
        repertoire = repertoire_utils.get_rep()
        choix = input("(L)ister (R)echercher (A)jouter (M)odifier (S)upprimer (Q)uitter")
        choix = choix.upper()

        # Afficher répertoire.

        if choix.upper() == "L":
            afficher_repertoire(repertoire)

        # Ajouter contact.

        elif choix.upper() == "A":
            ajout_contact_ui(repertoire)

        # Modification.

        elif choix.upper() == "M":
            modification_contact_ui(repertoire)

        # Recherche contact.

        elif choix.upper() == "R":
            resultat = recherche_de_contact_ui(repertoire)
            if len(resultat) < 1:
                print("La recherche n'a donné aucun résultat.")
                continue
            else:
                afficher_repertoire(resultat)

        # Suppression contact.

        elif choix.upper() == "S":
            supprimer_contact_ui(repertoire)

        # Quitter programme.

        elif choix.upper() == "Q":
            print("Programme quitté.")
            break

        # Si aucun choix valide, reposer la question.

        else:
            print("Commande non reconnue. Recommencez.")
            continue


if __name__ == "__main__":
    main()

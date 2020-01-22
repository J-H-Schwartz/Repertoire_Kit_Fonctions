# coding: utf-8
from repertoire_utils.repertoire_action import verification_contact, ajouter_personne, \
    modification_numero, chercher_personne, supprimer_personne
import repertoire_utils_text as repertoire_utils
from terminaltables import DoubleTable


resultat = []


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

def ajout_contact():
    while True:
        nom = input("Entrez le nom du contact à ajouter ou tapez Entrée pour revenir au menu principal: ")
        resultat = verification_contact(nom)
        if resultat:
            print("Ce contact existe déja.")
            continue
        if nom == "":
            continue
        numero = input("Entrez le numéro du contact à ajouter: ")
        adresse = input("Entrez l'adresse du contact à ajouter: ")
        ajouter_personne(nom, numero, adresse)
        print("Le contact a bien été ajouté.")
        return


# Fonction Modification de contact

def modification():
    champ = ""
    while True:
        modification = ""
        nom = input("Entrez le nom du contact à modifier ou tapez Entrée pour revenir au menu précédent: ")
        resultat = verification_contact(nom)
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
        resultat = modification_numero(nom, champ, modification)
        if resultat:
            print("Le contact a été modifié.")
            return
        else:
            print("Aucune modification effectuée.")
            return
    except NameError:
        return


# Fonction Recherche Contact

def recherche_de_contact():
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
            resultat = chercher_personne(type_de_recherche=choix, **argument)
            return resultat
        elif choix.upper() == "P":
            return resultat
        else:
            print("Commande non reconnue. Recommencez.")


# Fonction Suppression

def supprimer():
    while True:
        nom = input("Entrez le nom du contact à supprimer ou tapez Entrée pour revenir au menu: ")
        if nom == "":
            return
        resultat = supprimer_personne(nom)
        if resultat:
            print("Le contact a été supprimé.")
            return
        else:
            print("Ce contact n'existe pas.")


# Fonction principale du répertoire.

def main():
    repertoire = repertoire_utils.get_rep()
    while True:
        choix = input("(L)ister (R)echercher (A)jouter (M)odifier (S)upprimer (Q)uitter")
        choix = choix.upper()

        # Afficher répertoire.

        if choix.upper() == "L":
            afficher_repertoire(repertoire)

        # Ajouter contact.

        elif choix.upper() == "A":
            ajout_contact()

        # Modification.

        elif choix.upper() == "M":
            modification()

        # Recherche contact.

        elif choix.upper() == "R":
            resultat = recherche_de_contact()
            if len(resultat) < 1:
                print("La recherche n'a donné aucun résultat.")
                continue
            else:
                afficher_repertoire(resultat)

        # Suppression contact.

        elif choix.upper() == "S":
            supprimer()

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

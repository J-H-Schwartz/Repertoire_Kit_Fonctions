# coding: utf-8
from terminaltables import DoubleTable

repertoire = [{'NOM': 'MICHAEL', 'NUMERO': '1111111111', 'ADRESSE': 'blabla@mfloe.com'},
              {'NOM': 'LINDA', 'NUMERO': '2222222222', 'ADRESSE': 'blbblb@zvrez.com'},
              {'NOM': 'SANDRA', 'NUMERO': '3333333333', 'ADRESSE': 'fzefzzcz@fzv.com'},
              {'NOM': 'SANDRA2', 'NUMERO': '4444444444', 'ADRESSE': 'fzgzgvdsz@fzv.com'},
              {'NOM': 'SANDRA3', 'NUMERO': '555555555', 'ADRESSE': 'aaeaczzcz@fzv.com'}]
resultat = []


# Fonction vérification existance contact

def verification_existance_contact(repertoire, nom):
    for item in repertoire:
        if nom == item['NOM']:
            return True


# Fonction Afficher répertoire

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


# Fonction Ajouter numéro

def ajouter_numero(nom, numero, adresse):
    repertoire.append({"NOM": nom, "NUMERO": numero, "ADRESSE": adresse})


# Fonction Suppression numéro

def supprimer_numero(repertoire, nom):
    for contact, element in enumerate(repertoire):
        if nom == element['NOM']:
            del repertoire[contact]
            return True
    return False


# Fonction Recherche

def recherche_contact(repertoire, nom="defaut", numero="defaut", type_de_recherche="defaut"):
    contact_trouve = []
    champ = ''
    entree_recherchee = ""
    for item in repertoire:
        if type_de_recherche == "N":
            champ = 'NOM'
            entree_recherchee = nom
        elif type_de_recherche == "0":
            champ = 'NUMERO'
            entree_recherchee = numero
        if entree_recherchee in item[champ]:
            contact_trouve.append({'NOM': item['NOM'], 'NUMERO': item
                                   ['NUMERO'], 'ADRESSE': item['ADRESSE']})
    return contact_trouve


# Fonction modification numéro.

def modification_numero(repertoire, contact, destination, modification):
    for contacts in repertoire:
        if contact == contacts['NOM']:
            contacts[destination] = modification
            return True
    return False


# Début.

while True:
    choix = input("(L)ister (R)echercher (A)jouter (M)odifier (S)upprimer (Q)uitter")
    choix = choix.upper()

    # Afficher répertoire.

    if choix == "L":
        afficher_repertoire(repertoire)

    # Ajouter contact.

    elif choix == "A":
        nom = input("Entrez le nom du contact à ajouter ou tapez Entrée pour revenir au menu principal: ").upper()
        resultat = verification_existance_contact(repertoire, nom)
        if resultat:
            print("Ce contact existe déja.")
            continue
        if nom == "":
            continue
        numero = input("Entrez le numéro du contact à ajouter: ").upper()
        adresse = input("Entrez l'adresse du contact à ajouter: ")
        ajouter_numero(nom, numero, adresse)
        print("Le contact a bien été ajouté.")

    # Modification.

    elif choix == "M":
        destination = ""
        while True:
            modification = ""
            nom = input("Entrez le nom du contact à modifier ou tapez Entrée pour revenir au menu précédent: ").upper()
            resultat = verification_existance_contact(repertoire, nom)
            if nom == "":
                print("Retour au menu précédent.")
                break
            if resultat:
                break
            print("Ce contact n'existe pas.")
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
            else:
                print("Aucune modification effectuée")
        except NameError:
            continue

    # Recherche contact.

    elif choix == "R":
        resultat = []
        while True:
            choix = input("Rechercher par : (N)om  /  Numero(0) / (P)récédent").upper()
            if choix == "0":
                numero = input("Entrer un numéro à rechercher : ").upper()
                resultat = recherche_contact(repertoire=repertoire, numero=numero,
                                             type_de_recherche=choix)
                break
            elif choix == "N":
                nom = input("Entrez votre recherche: ").upper()
                resultat = recherche_contact(repertoire=repertoire, nom=nom,
                                             type_de_recherche=choix)
                break
            elif choix == "P":
                break
            else:
                print("Commande non reconnue. Recommencez.")
        afficher_repertoire(resultat)

    # Suppression contact.

    elif choix == "S":
        while True:
            nom = input("Entrez le nom du contact à supprimer ou tapez Entrée pour revenir au menu: ").upper()
            if nom == "":
                break
            resultat = supprimer_numero(repertoire, nom)
            if resultat:
                print("Le contact a été supprimé.")
            else:
                print("Ce contact n'existe pas.")
            break

    # Quitter programme.

    elif choix == "Q":
        print("Programme quitté.")
        break

    # Si aucun choix valide, reposer la question.

    else:
        print("Commande non reconnue. Recommencez.")
        continue

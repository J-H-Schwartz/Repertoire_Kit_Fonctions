# coding: utf-8

nom_a_rechercher = "-1"
numero_a_rechercher = "-1"
contact_existant = False
repertoire = [{'NOM': 'MICHAEL', 'NUMERO': '1111111111', 'ADRESSE': 'blabla@mfloe.com'},
              {'NOM': 'LINDA', 'NUMERO': '2222222222', 'ADRESSE': 'blbblb@zvrez.com'},
              {'NOM': 'SANDRA', 'NUMERO': '3333333333', 'ADRESSE': 'fzefzzcz@fzv.com'},
              {'NOM': 'SANDRA2', 'NUMERO': '4444444444', 'ADRESSE': 'fzgzgvdsz@fzv.com'},
              {'NOM': 'SANDRA3', 'NUMERO': '555555555', 'ADRESSE': 'aaeaczzcz@fzv.com'}]
recherche = []


# Fonction vérification existance contact

def verification_existance_contact(repertoire_listing, nom_a_verifier):
    for i in range(len(repertoire_listing)):
        if nom_a_verifier == repertoire_listing[i]['NOM']:
            return True


# Fonction Afficher répertoire

def afficher_repertoire(repertoire_listing):
    for element in repertoire_listing:
        print(element['NOM'], element['NUMERO'], element['ADRESSE'])


# Fonction Ajouter numéro

def ajouter_numero(nom_nouveau_contact, numero_nouveau_contact, adresse_nouveau_contact):
    repertoire.append({"NOM": nom_nouveau_contact, "NUMERO": numero_nouveau_contact,
                       "ADRESSE": adresse_nouveau_contact})


# Fonction Suppression numéro

def supprimer_numero(repertoire_cible, nom_contact_suppression):
    for element in range(len(repertoire_cible)):
        if nom_contact_suppression == repertoire_cible[element]['NOM']:
            del repertoire_cible[element]
            break


# Fonction Recherche

def recherche_contact(repertoire_recherche, nom_recherche="defaut", numero_recherche="defaut",
                      type_de_recherche="defaut"):
    contact_trouve = []
    for i in range(len(repertoire_recherche)):
        if type_de_recherche == "N":
            if nom_recherche in repertoire_recherche[i]['NOM']:
                contact_trouve.append({'NOM': repertoire_recherche[i]['NOM'], 'NUMERO': repertoire_recherche[i]
                                      ['NUMERO'], 'ADRESSE': repertoire_recherche[i]['ADRESSE']})
        elif type_de_recherche == "0":
            if numero_recherche in repertoire_recherche[i]['NUMERO']:
                contact_trouve.append({'NOM': repertoire_recherche[i]['NOM'], 'NUMERO': repertoire_recherche[i]
                                       ['NUMERO'], 'ADRESSE': repertoire_recherche[i]['ADRESSE']})
    return contact_trouve


# Fonction modification numéro.

def modification_numero(repertoire_modification):
    modif = False
    modification = ""
    while True:
        nom_a_modifier = input("Entrez le nom du contact à modifier ou tapez P pour revenir au menu "
                               "précédent: ").upper()
        verification_existance_nom = verification_existance_contact(repertoire_modification, nom_a_modifier)
        if verification_existance_nom:
            break
        print("Ce contact n'existe pas.")

    if nom_a_modifier == "P":
        print("Retour au menu précédent.")
        return
    while True:
        destination = input("Que voulez-vous modifier ? (N)uméro / (A)dresse: ").upper()
        if destination == "N":
            modification = input("Entrez le nouveau numéro: ").upper()
            destination = 'NUMERO'
            break
        elif destination == "A":
            modification = input("Entrez la nouvelle adresse: ").upper()
            destination = 'ADRESSE'
            break
        else:
            print("Commande non reconnue. Recommencez.")
            continue
    for elements in range(len(repertoire_modification)):
        if nom_a_modifier == repertoire_modification[elements]['NOM']:
            repertoire_modification[elements][destination] = modification
            modif = True
            break
    if modif:
        print("Le contact a été modifié.")
    else:
        print("Aucune modification effectuée")


# Début.

while True:
    choix = input("(L)ister (R)echercher (A)jouter (M)odifier (S)upprimer (Q)uitter")
    choix = choix.upper()


# Afficher répertoire.

    if choix == "L":
        afficher_repertoire(repertoire)


# Ajouter contact.

    elif choix == "A":
        nouveau_contact = input("Entrez le nom du contact à ajouter ou (P)récedent: ").upper()
        contact_existant = verification_existance_contact(repertoire, nouveau_contact)
        if contact_existant:
            print("Ce contact existe déja.")
            continue
        if nouveau_contact == "P":
            continue
        nouveau_numero = input("Entrez le numéro du contact à ajouter: ").upper()
        nouvelle_adresse = input("Entrez l'adresse du contact à ajouter: ")
        ajouter_numero(nouveau_contact, nouveau_numero, nouvelle_adresse)


# Modification.

    elif choix == "M":
        modification_numero(repertoire)


# Recherche contact.

    elif choix == "R":
        recherche = []
        while True:
            choix_recherche = input("Rechercher par : (N)om  /  Numero(0)").upper()
            if choix_recherche == "0":
                numero_a_rechercher = input("Entrer un numéro à rechercher ou (P)récedent: ").upper()
                recherche = recherche_contact(repertoire_recherche=repertoire, numero_recherche=numero_a_rechercher,
                                              type_de_recherche=choix_recherche)
                break
            elif choix_recherche == "N":
                nom_a_rechercher = input("Entrez votre recherche: ").upper()
                recherche = recherche_contact(repertoire_recherche=repertoire, nom_recherche=nom_a_rechercher,
                                              type_de_recherche=choix_recherche)
                break
            else:
                print("Commande non reconnue. Recommencez.")
        afficher_repertoire(recherche)


# Suppression contact.

    elif choix == "S":
        while True:
            suppression = input("Entrez le nom du contact à supprimer ou (P)récedent: ").upper()
            try:
                if suppression == "P":
                    break
                supprimer_numero(repertoire, suppression)
                print("Le contact a été supprimé.")
                break
            except KeyError:
                print("Ce contact n'existe pas. Recommencez.")


# Quitter programme.

    elif choix == "Q":
        print("Programme quitté.")
        break


# Si aucun choix valide, reposer la question.

    else:
        print("Commande non reconnue. Recommencez.")
        continue

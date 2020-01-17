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
    for item in repertoire_listing:
        if nom_a_verifier == item['NOM']:
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
    for i, element in enumerate(repertoire_cible):
        if nom_contact_suppression == element['NOM']:
            del repertoire_cible[i]
            break


# Fonction Recherche

def recherche_contact(repertoire_recherche, nom_recherche="defaut", numero_recherche="defaut",
                      type_de_recherche="defaut"):
    contact_trouve = []
    champ = ''
    entree_recherchee = ""
    for item in repertoire_recherche:
        if type_de_recherche == "N":
            champ = 'NOM'
            entree_recherchee = nom_recherche
        elif type_de_recherche == "0":
            champ = 'NUMERO'
            entree_recherchee = numero_recherche
        if entree_recherchee in item[champ]:
            contact_trouve.append({'NOM': item['NOM'], 'NUMERO': item
                                   ['NUMERO'], 'ADRESSE': item['ADRESSE']})
    return contact_trouve


# Fonction modification numéro.

def modification_numero(repertoire_modification):
    modif = False
    modification = ""
    while True:
        nom_a_modifier = input("Entrez le nom du contact à modifier ou tapez Entrée pour revenir au menu "
                               "précédent: ").upper()
        verification_existance_nom = verification_existance_contact(repertoire_modification, nom_a_modifier)
        if verification_existance_nom:
            break
        print("Ce contact n'existe pas.")

    if nom_a_modifier == "":
        print("Retour au menu précédent.")
        return
    while True:
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
    for contacts in repertoire_modification:
        if nom_a_modifier == contacts['NOM']:
            contacts[destination] = modification
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
        nouveau_contact = input("Entrez le nom du contact à ajouter ou tapez Entrée pour revenir au menu "
                                "principal: ").upper()
        contact_existant = verification_existance_contact(repertoire, nouveau_contact)
        if contact_existant:
            print("Ce contact existe déja.")
            continue
        if nouveau_contact == "":
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
            choix_recherche = input("Rechercher par : (N)om  /  Numero(0) / (P)récédent").upper()
            if choix_recherche == "0":
                numero_a_rechercher = input("Entrer un numéro à rechercher : ").upper()
                recherche = recherche_contact(repertoire_recherche=repertoire, numero_recherche=numero_a_rechercher,
                                              type_de_recherche=choix_recherche)
                break
            elif choix_recherche == "N":
                nom_a_rechercher = input("Entrez votre recherche: ").upper()
                recherche = recherche_contact(repertoire_recherche=repertoire, nom_recherche=nom_a_rechercher,
                                              type_de_recherche=choix_recherche)
                break
            elif choix_recherche == "P":
                break
            else:
                print("Commande non reconnue. Recommencez.")
        afficher_repertoire(recherche)

    # Suppression contact.

    elif choix == "S":
        while True:
            suppression = input("Entrez le nom du contact à supprimer ou tapez Entrée pour revenir au menu: ").upper()
            try:
                if suppression == "":
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

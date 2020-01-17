nom_a_rechercher = "-1"
numero_a_rechercher = "-1"
repertoire = {}
recherche = {}


# Fonction Afficher répertoire

def afficher_repertoire(repertoire_listing):
    for item in repertoire_listing:
        print("Nom : {} / Numéro : {}".format(item, repertoire[item]))


# Fonction Ajouter numéro

def ajouter_numero(nom_nouveau_contact, numero_nouveau_contact):
    repertoire.update({nom_nouveau_contact: numero_nouveau_contact})


# Fonction Suppression numéro

def supprimer_numero(nom_contact_suppression):
    repertoire.pop(nom_contact_suppression)


# Fonction Recherche

def recherche_contact(repertoire_recherche, nom_recherche="defaut", numero_recherche="defaut",
                      type_de_recherche="defaut"):
    contact_trouve = {}
    for key in repertoire_recherche:
        if type_de_recherche == "N":
            if nom_recherche in key:
                contact_trouve.update({key: repertoire_recherche.get(key, "Aucun numéro.")})
        elif type_de_recherche == "0":
            liste_numeros = repertoire_recherche.items()
            for item in liste_numeros:
                if numero_recherche in item[1]:
                    contact_trouve.update({item[0]: item[1]})
    return contact_trouve


# Fonction modification numéro.

def modification_numero(repertoire_modification):
    modif = False
    nom_a_modifier = input("Entrez le nom du contact à modifier ou tapez P pour revenir au menu précédent: ").upper()
    if nom_a_modifier == "P":
        print("Retour au menu précédent.")
        return
    modification_du_numero = input("Entrez le nouveau numéro: ").upper()
    for key in repertoire_modification.keys():
        if nom_a_modifier in key:
            repertoire_modification[key] = modification_du_numero
            modif = True
    if modif:
        print("Le numéro a été modifié.")
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
        if nouveau_contact in repertoire:
            print("Ce contact existe déja.")
            continue
        if nouveau_contact == "P":
            continue
        nouveau_numero = input("Entrez le numéro du contact à ajouter : ").upper()
        ajouter_numero(nouveau_contact, nouveau_numero)


# Modification.

    elif choix == "M":
        modification_numero(repertoire)


# Recherche contact.

    elif choix == "R":
        choix_recherche = input("Rechercher par : (N)om  /  Numero(0)").upper()
        if choix_recherche == "0":
            numero_a_rechercher = input("Entrer un numéro à rechercher ou (P)récedent: ").upper()
            recherche = recherche_contact(repertoire_recherche=repertoire, numero_recherche=numero_a_rechercher,
                                          type_de_recherche=choix_recherche)
        elif choix_recherche == "N":
            nom_a_rechercher = input("Entrez votre recherche: ").upper()
            recherche = recherche_contact(repertoire_recherche=repertoire, nom_recherche=nom_a_rechercher,
                                          type_de_recherche=choix_recherche)
        for word in recherche:
            print("Nom: {}  Numéro: {}".format(word, recherche[word]))


# Suppression contact.

    elif choix == "S":
        while True:
            suppression = input("Entrez le nom du contact à supprimer ou (P)récedent: ").upper()
            try:
                if suppression == "P":
                    break
                supprimer_numero(suppression)
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
        continue

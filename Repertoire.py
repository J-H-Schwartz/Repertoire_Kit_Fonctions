import re
nom_contact = "NOM"
numero_contact = "NUMERO"
recherche = 0
repertoire = {nom_contact: numero_contact}


# Fonction Afficher répertoire

def afficher_repertoire():
    for item in repertoire:
        print("Nom : {} / Numéro : {}".format(item, repertoire[item]))


# Fonction Ajouter numéro

def ajouter_numero(nom_nouveau_contact, numero_nouveau_contact):
    repertoire.update({nom_nouveau_contact: numero_nouveau_contact})


# Fonction Suppression numéro

def supprimer_numero(nom_contact_suppression):
    repertoire.pop(nom_contact_suppression)


# Fonction Recherche par numero

def recherche_contact_par_numero(repertoire_recherche, numero_recherche):
    liste_numeros = repertoire_recherche.items()
    for item in liste_numeros:
        if item[1] == numero_recherche:
            return item[0]
        else:
            return 0


# Fonction Recherche par nom

def recherche_contact_par_nom(repertoire_recherche, nom_recherche):
    if nom_recherche in repertoire_recherche:
        print("Nom: " + nom_recherche + " / " + "Numéro: " + repertoire_recherche[nom_recherche])
        return 1
    else:
        return 0


# Fonction modification numéro

def modification_numero(repertoire_modification):
    modif = False
    nom_a_modifier = input("Entrez le nom du contact à modifier ou tapez P pour revenir au menu précédent: ")
    nom_a_modifier = nom_a_modifier.upper()
    if nom_a_modifier == "P":
        print("Retour au menu précédent.")
        return
    modification_du_numero = input("Entrez le nouveau numéro: ")
    for key in repertoire_modification.keys():
        if nom_a_modifier in key:
            repertoire_modification[key] = modification_du_numero
            modif = True
    if modif:
        print("Le numéro a été modifié.")
    else:
        print("Aucune modification effectuée")


while True:
    choix = input("Que souhaitez vous faire ? Tapez L pour afficher le répertoire, A pour ajouter un contact, M pour"
                  " modifier un contact, S pour supprimer un contact, R pour rechercher un contact, ou Q pour"
                  " quitter le programme: ")
    choix = choix.upper()
    if choix == "L":
        afficher_repertoire()
    elif choix == "A":
        nouveau_contact = input("Entrez le nom du contact à ajouter ou tapez P pour revenir au menu précédent : ")
        nouveau_contact = nouveau_contact.upper()
        verification_contact_existant = recherche_contact_par_nom(repertoire, nouveau_contact)
        if verification_contact_existant == 1:
            print("Ce contact existe déja.")
            continue
        if nouveau_contact == "P":
            continue
        nouveau_numero = input("Entrez le numéro du contact à ajouter : ")
        ajouter_numero(nouveau_contact, nouveau_numero)
    elif choix == "M":
        modification_numero(repertoire)
    elif choix == "R":
        choix_recherche = input("Tapez N pour rechercher par nom, ou 0 pour rechercher par numéro: ")
        choix_recherche = choix_recherche.upper()
        if choix_recherche == "0":
            numero_a_recherche = input("Entrer un numéro à rechercher ou tapez P pour revenir au menu précédent: ")
            numero_a_recherche = numero_a_recherche.upper()
            recherche = recherche_contact_par_numero(repertoire, numero_a_recherche)
        elif choix_recherche == "N":
            nom_a_rechercher = input("Entrez votre recherche: ")
            nom_a_rechercher = nom_a_rechercher.upper()
            recherche = recherche_contact_par_nom(repertoire, nom_a_rechercher)
        if recherche == 0:
            print("Ce contact n'existe pas.")
            continue
    elif choix == "S":
        while True:
            suppression = input("Entrez le nom du contact à supprimer, tapez P pour revenir au menu précédent: ")
            suppression = suppression.upper()
            try:
                if suppression == "P":
                    break
                supprimer_numero(suppression)
                print("Le contact a été supprimé.")
                break
            except:
                print("Ce contact n'existe pas. Recommencez.")
    elif choix == "Q":
        print("Programme quitté.")
        break
    else:
        continue

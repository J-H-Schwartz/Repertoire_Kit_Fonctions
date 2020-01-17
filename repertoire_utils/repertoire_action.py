# coding: utf-8


# Fonction vérification existance contact

def verification_existance_contact(repertoire, nom):
    for item in repertoire:
        if nom == item['NOM']:
            return True


# Fonction Ajouter numéro

def ajouter_numero(nom, numero, adresse, repertoire):
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


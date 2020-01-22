# coding: utf-8


# Fonction vérification existance contact

def verification_existance_contact(repertoire, nom):
    for item in repertoire:
        if nom.upper() == item['NOM'].upper():
            return True


# Fonction Ajouter numéro

def ajouter_personne(nom, numero, adresse, repertoire):
    repertoire.append({"NOM": nom, "NUMERO": numero, "ADRESSE": adresse, "NOM_UPPER": nom.upper()})


# Fonction Suppression numéro

def supprimer_personne(repertoire, nom):
    for contact, element in enumerate(repertoire):
        if nom.upper() == element['NOM'].upper():
            del repertoire[contact]
            return True
    return False


# Fonction Recherche

def chercher_personne(repertoire, nom="defaut", numero="defaut", type_de_recherche="defaut"):
    contact_trouve = []
    champ = ''
    entree_recherchee = ""
    for item in repertoire:
        if type_de_recherche.upper() == "N":
            champ = 'NOM'
            entree_recherchee = nom
        elif type_de_recherche.upper() == "0":
            champ = 'NUMERO'
            entree_recherchee = numero
        if entree_recherchee.upper() in item[champ].upper():
            contact_trouve.append({'NOM': item['NOM'], 'NUMERO': item
                                   ['NUMERO'], 'ADRESSE': item['ADRESSE']})
    return contact_trouve


# Fonction modification numéro.

def modification_numero(repertoire, contact, destination, modification):
    for contacts in repertoire:
        if contact.upper() == contacts['NOM'].upper():
            contacts[destination] = modification
            contacts['NOM_UPPER'] = modification.upper()
            return True
    return False


# coding: utf-8
import repertoire_utils_text as repertoire_utils


# Fonction vérification existance contact

def verification_contact(nom):
    contact_existant = repertoire_utils.verification_existance_contact(nom)
    return contact_existant


# Fonction Ajouter numéro

def ajouter_personne(nom, numero='defaut', adresse='defaut'):
    repertoire_utils.append_rep(nom, numero, adresse)


# Fonction Suppression numéro

def supprimer_personne(nom):
    suppression = repertoire_utils.del_rep(nom)
    return suppression


# Fonction Recherche

def chercher_personne(nom="defaut", numero="defaut", type_de_recherche="defaut"):
    contact_trouve = []
    champ = ''
    entree_recherchee = ""
    for item in repertoire_utils.get_rep():
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

def modification_numero(contact, destination, modification):
    for contacts in repertoire_utils.get_rep():
        if contact.upper() == contacts['NOM'].upper():
            contacts[destination] = modification
            contacts['NOM_UPPER'] = modification.upper()
            repertoire_utils.changes_save()
            return True
    return False


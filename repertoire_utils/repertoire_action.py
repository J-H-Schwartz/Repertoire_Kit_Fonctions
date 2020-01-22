# coding: utf-8
import repertoire_utils_dict as repertoire_utils


# Fonction appel repertoire:
def get_repertoire():
    repertoire = repertoire_utils.get_rep()
    return repertoire


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
    repertoire = get_repertoire()
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

def modification_numero(contact, destination, modification):
    repertoire = get_repertoire()
    for contacts in repertoire:
        if contact.upper() == contacts['NOM'].upper():
            contacts[destination] = modification
            contacts['NOM_UPPER'] = modification.upper()
            return True
    return False


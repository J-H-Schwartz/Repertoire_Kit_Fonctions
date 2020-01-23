# coding: utf-8
import repertoire_utils_text as repertoire_utils


# Fonction choix répertoire

def verification_existance_repertoire(nom_de_fichier):
    if repertoire_utils.existing_repertories_check(nom_de_fichier) == 0:
        return False
    else:
        return True


# Fonction vérification existance contact

def verification_existance_contact(repertoire, nom):
    contact_existant = repertoire_utils.verification_existance_contact(repertoire, nom)
    return contact_existant


# Fonction Ajouter numéro

def ajouter_personne(repertoire, nom, numero='defaut', adresse='defaut'):
    personne = {"NOM": nom, "NUMERO": numero, "ADRESSE": adresse, "NOM_UPPER": nom.upper()}
    repertoire_utils.append_rep(repertoire, personne)


# Fonction Suppression numéro

def supprimer_personne(repertoire, personne):
    suppression = repertoire_utils.del_rep(repertoire, personne)
    return suppression


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

def modification_contact(repertoire, contact, destination, modification):
    for contacts in repertoire:
        if contact.upper() == contacts['NOM'].upper():
            contacts[destination] = modification
            repertoire_utils.changes_save(repertoire)
            return True
    return False

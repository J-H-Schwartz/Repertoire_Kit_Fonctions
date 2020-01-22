# coding: utf-8
import json


# Fonction appel répertoire

def get_rep():
    with open("repertoire.txt", "r") as repertoire_text:
        repertoire = sorted(json.loads(repertoire_text.read()), key=lambda k: k["NOM_UPPER"])
    return repertoire


# Fonction vérification existance contact

def verification_existance_contact(repertoire, nom):
    for item in repertoire:
        if nom.upper() == item['NOM_UPPER']:
            return True


# Fonction Ajouter numéro

def append_rep(repertoire, personne):
    repertoire.append(personne)
    with open("repertoire.txt", "w") as repertoire_text:
        repertoire_text.write(json.dumps(repertoire))


# Fonction Suppression numéro

def del_rep(repertoire, personne):
    for contact in repertoire:
        if personne.upper() == contact['NOM'].upper():
            repertoire.remove(contact)
            with open("repertoire.txt", "w") as repertoire_text:
                repertoire_text.write(json.dumps(repertoire))
                return True
    return False


def changes_save(repertoire):
    with open("repertoire.txt", "w") as repertoire_text:
        repertoire_text.write(json.dumps(repertoire))

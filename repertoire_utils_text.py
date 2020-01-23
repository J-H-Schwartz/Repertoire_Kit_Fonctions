# coding: utf-8
import json
import os.path


# Fonction Choix Répertoire

def existing_repertories_check(nom_de_fichier):
    if os.path.isfile(nom_de_fichier):
        return True
    else:
        return False


# Fonction appel répertoire

def get_rep(repertoire_actif):
    with open(repertoire_actif, "r") as repertoire_text:
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

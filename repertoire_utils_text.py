# coding: utf-8
import json
with open("repertoire.txt", "r") as repertoire_text:
    repertoire_data = json.loads(repertoire_text.read())

print(repertoire_data)


# Fonction appel répertoire

def get_rep():
    return repertoire_data


# Fonction vérification existance contact

def verification_existance_contact(nom):
    for item in repertoire_data:
        if nom.upper() == item['NOM'].upper():
            return True


# Fonction Ajouter numéro

def append_rep(nom, numero, adresse):
    repertoire_data.append({"NOM": nom, "NUMERO": numero, "ADRESSE": adresse, "NOM_UPPER": nom.upper()})
    repertoire_text = open("repertoire.txt", "w")
    repertoire_text.write(str(repertoire_data).replace("\'", "\""))
    repertoire_text.close()


# Fonction Suppression numéro

def del_rep(nom):
    for contact, element in enumerate(repertoire_data):
        if nom.upper() == element['NOM'].upper():
            del repertoire_data[contact]
            repertoire_text = open("repertoire.txt", "w")
            repertoire_text.write(str(repertoire_data).replace("\'", "\""))
            repertoire_text.close()
            return True
    return False


def changes_save():
    repertoire_text = open("repertoire.txt", "w")
    repertoire_text.write(str(repertoire_data).replace("\'", "\""))
    repertoire_text.close()



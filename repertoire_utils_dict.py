# Code transféré sur repertoire_utils_text.

repertoire_data = []


# Fonction appel répertoire

def get_rep():
    repertoire = repertoire_data
    return repertoire


# Fonction vérification existance contact

def verification_existance_contact(nom):
    for item in repertoire_data:
        if nom.upper() == item['NOM'].upper():
            return True


# Fonction Ajouter numéro

def append_rep(nom, numero, adresse):
    repertoire_data.append({"NOM": nom, "NUMERO": numero, "ADRESSE": adresse, "NOM_UPPER": nom.upper()})


# Fonction Suppression numéro

def del_rep(nom):
    for contact, element in enumerate(repertoire_data):
        if nom.upper() == element['NOM'].upper():
            del repertoire_data[contact]
            return True
    return False



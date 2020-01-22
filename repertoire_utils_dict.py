repertoire_data = [{'NOM': 'michael', 'NUMERO': '1111111111', 'ADRESSE': 'blabla@mfloe.com', 'NOM_UPPER': "MICHAEL"},
              {'NOM': 'Linda', 'NUMERO': '2222222222', 'ADRESSE': 'blbblb@zvrez.com', 'NOM_UPPER': "LINDA"},
              {'NOM': 'SANDRA', 'NUMERO': '3333333333', 'ADRESSE': 'fzefzzcz@fzv.com', 'NOM_UPPER': "SANDRA"},
              {'NOM': 'sandra2', 'NUMERO': '4444444444', 'ADRESSE': 'fzgzgvdsz@fzv.com', 'NOM_UPPER': "SANDRA2"},
              {'NOM': 'Sandra3', 'NUMERO': '555555555', 'ADRESSE': 'aaeaczzcz@fzv.com', 'NOM_UPPER': "SANDRA3"}]


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



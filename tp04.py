import os
import sys


# Fonctions

def inputuser() -> str:
    """
    va demander à l'utilisateur les mots qu'il veut rechercher
    :return:le(s) mot(s) entrés par l'utilisateur
    """
    input_utilisateur: str = input("Entrez les mots que vous recherchez : ")

    return input_utilisateur


def decoupageinput(_input: str) -> list:
    """
    fonction qui servira à découper l'input de l'utilisateur dans une liste pour pouvoir la comparer à chaque texte
    :param _input: l'input entrée par l'utilisateur
    :return: l'input de l'utilisateur sous forme de liste
    """

    # caractères utilisés pour stock l'input dans notre liste
    list_carac_input: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                              's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'é', 'è', 'ê', 'à', 'ä', 'ü', 'ù', 'ô', 'ö',
                              'â', 'ï', 'ç', 'î']

    list_input: list = []
    mot_decoupe_input: str = ""
    # pour chaque mot dans notre input, celui-ci sera découpé et stocké dans notre liste
    for i in _input:
        i = i.lower()
        if i in list_carac_input:
            mot_decoupe_input += i
        else:
            if mot_decoupe_input == '':
                pass

            elif mot_decoupe_input not in list_input:
                list_input.append(mot_decoupe_input)
                mot_decoupe_input = ""

            else:
                pass
                mot_decoupe_input = ""

    # on rajoute le dernier mot dans notre liste avec un append supplémentaire
    list_input.append(mot_decoupe_input)

    return list_input


def textelecture(_texte: str) -> dict:
    """
    fonction qui va lire le fichier en cours, et stocker les différents mots que l'on veut dans un dictionnaire
    :param _texte: le texte à lire en cours
    :return: le dictionnaire rempli selon le texte qui a été lu
    """

    # initialisation de notre variable dictionnaire vide au début de la fonction + liste des caractères utiles que l'on va utiliser
    dico_text: dict = {}
    list_carac: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                        's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'é', 'è', 'ê', 'à', 'ä', 'ü', 'ù', 'ô', 'ö', 'â',
                        'ï', 'ç', 'î']

    # Ouverture et lecture du texte en cours + encodage en utf-8 pour éviter les caractères spéciaux
    with open(consolpath + "/" + _texte, "r", encoding='utf-8') as file:
        # chaque mot dans le texte sera lu et transformé en minuscule
        for i in file:
            i = i.lower()
            mot_decoupe: str = ""
            # lecture de chaque caractère par mot, avec la variable mot_decoupe, l'on va pouvoir commencer à récuper les charactères utiles à stocker dans notre dictionnaire
            for ch in i:

                if ch in list_carac:
                    mot_decoupe += ch

                # Si la variable mot_decoupe est vide (du aux espaces après les virgules), le mot sera stocké comme clé dans le dictionnaire, et sa valeur sera définie à 1
                else:
                    if mot_decoupe == '':
                        pass
                    elif mot_decoupe not in dico_text:
                        dico_text[mot_decoupe] = 1

                    # Si le mot est déjà présent dans notre dictionnaire, alors sa valeur augmentera simplement de 1
                    else:
                        dico_text[mot_decoupe] += 1
                    mot_decoupe = ""

    # Le dictionnaire de notre texte en cours sera renvoyé sous forme de variable dico_text
    return dico_text


def calculdistance(_input: list, _dicotexte: dict) -> float:
    """
    Fonction qui calculera la distance entre la liste input de l'utilisateur et le dictionnaire selon le texte en cours
    :param _input: l'input de l'utilisateur sous forme de liste créée précédement
    :param _dicotexte: le dictionnaire du texte en cours avec comme clé les différents mot, et le nombre de fois que le mot apparaît comme valeur
    :return: le résultat de la distance sous forme de float
    """

    # Initialisation des variables à 0 pour la somme des mot dans la liste ET dans le dico, ainsi que le nombre de mots dans le dico

    sommedistance: int = 0
    nb_mot_docu: int = 0

    # Pour chaque mot dans la liste, puis pour chaque clé (mot) dans le dictionnaire, si le mot correspond à la clé, alors la sommedistance augmentera de 1
    # On peut ainsi comparer l'input et le dictionnaire
    for i in _input:
        for cle2 in _dicotexte.keys():
            if i == cle2:
                sommedistance += _dicotexte[cle2]
            else:
                pass

    # Boucle simple servant à compter le nombre de mot présent dans le dictionnaire du texte, pour chaque clé, le nb de mot augmentera selon la valeur de la clé
    for cle in _dicotexte.keys():
        nb_mot_docu += _dicotexte[cle]

    # On peut ainsi retourner le calcul de la distance, avec un arrondi de 2
    return round((sommedistance / nb_mot_docu), 2)


# Déclaration et Initialisation des variables

# la variable dico sera le dictionnaire qui comportera 4 autres dictionnaires, chacun de ces dictionnaire dans le dico global comporte les données des textes 1 à 4
dico: dict = {}
list_input_main: list = []
mot_user: str

# variable servant à préciser le chemin dans la console
consolpath: str = sys.argv[1]

# Programme Principal

# Verifier si le chemin existe bien
if os.path.exists(consolpath):
    # On demande l'input à l'utilisateur
    mot_user = inputuser()
    distance: float
    # Tant que l'utilisateur ne saisit pas un input vide, le programme lui redemendera de saisir une valeur
    while mot_user:
        list_input_main = decoupageinput(mot_user)
        # Lecture du document 'textes', fichier par fichier se finissant en .txt
        for filename in os.listdir(consolpath):
            if filename.endswith(".txt"):
                # S'il s'agit d'un fichier txt, alors on pourra utiliser nos fonctions de création de dictionnaire selon le texte, et de calcul de la distance selon le texte
                dico[filename] = textelecture(filename)
                distance = calculdistance(list_input_main, dico[filename])

                # On affiche le résultat de la proximité entre l'input et le texte lu en cours
                print("Ce qui fait une proximité de {:.2f} au texte '{}'".format(distance, filename))
        # On redemande un input à l'utilisateur après les affichages des distances
        mot_user = inputuser()
else:
    print("Les fichiers n'existent pas !")

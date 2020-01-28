from outils import est_egal_a, coordonnee_x, coordonnee_y, creer_caisse, creer_case_vide, creer_cible, creer_image, \
    creer_mur, creer_personnage
import time
import os


# Fonctions à développer
def jeu_en_cours(caisses, cibles) -> bool:
    '''
    Fonction testant si le jeu est encore en cours et retournant un booléen comme réponse sur l'état de la partie.
    :param caisses: La liste des caisses du niveau en cours
    :param cibles: La liste des cibles du niveau en cours
    :return: True si la partie est finie, False sinon
    '''
    # Vérification des paramètres
    if caisses is None or cibles is None:
        return None

    nb_cibles: int = 0  # Compteur pour connaître le total des cibles
    for caisse in caisses:
        for cible in cibles:
            if caisse.x == cible.x and caisse.y == cible.y:
                nb_cibles += 1
    if nb_cibles == len(cibles):
        return True
    else:
        return False


def charger_niveau(joueur, caisses, cibles, murs, path):
    '''
    Fonction permettant de charger depuis un fichier.txt et de remplir les différentes listes permettant le
    fonctionnement du jeu (joueur, caisses, murs, cibles)
    :param joueur: liste des personnages
    :param caisses: liste des caisses
    :param cibles: liste des cibles
    :param murs: liste des murs
    :param path: Chemin du fichier.txt
    :return:
    '''
    # Vérification des paramètres
    if not os.path.isfile(path):
        return None
    elif joueur is None or caisses is None or cibles is None or murs is None:
        return None

    # Variables de départ
    c_dpt_x: int = DISTANCE_ENTRE_CASE // 2
    c_dpt_y: int = DISTANCE_ENTRE_CASE // 2

    # Déclaration de la coordonnée Y
    coord_y: int = Y_PREMIERE_CASE + c_dpt_y

    # Overture du fichier en mode lecture
    with open(path, 'r') as filin:
        # Lecture de chaque ligne du fichier
        for ligne in filin:
            # Calibrage des coordonnees X et Y
            coord_x = X_PREMIERE_CASE + c_dpt_x
            # Lecture et création de chaque élément de la ligne
            for element in ligne:
                if element == '#':
                    murs.append(creer_mur(coord_x, coord_y))
                elif element == '.':
                    cibles.append(creer_cible(coord_x, coord_y))
                elif element == '$':
                    caisses.append(creer_caisse(coord_x, coord_y))
                elif element == '@':
                    joueur.append(creer_personnage(coord_x, coord_y))

                # Calibrage de la coordonnée X à chaque intéraction
                coord_x = coord_x + DISTANCE_ENTRE_CASE
            # Calibrage de la coordonée Y a chaque intéraction
            coord_y = coord_y + DISTANCE_ENTRE_CASE


def mouvement(direction, can, joueur, murs, caisses, liste_image):
    '''
    Fonction permettant de définir les cases de destinations (il y en a 2 si le joueur pousse une caisse) selon la
    direction choisie.
    :param direction: Direction dans laquelle le joueur se déplace (droite, gauche, haut, bas)
    :param can: Canvas (ignorez son fonctionnement), utile uniquement pour créer_image()
    :param joueur: liste des joueurs
    :param murs: liste des murs
    :param caisses: liste des caisses
    :param liste_image: liste des images (murs, caisses etc...) détaillée dans l'énoncé
    :return:
    '''
    # Vérification des paramètres
    if direction is None or joueur is None or murs is None or caisses is None or liste_image is None:
        return None

    # Position du joueur
    position_x_joueur: int = coordonnee_x(joueur[0])
    position_y_joueur: int = coordonnee_y(joueur[0])

    if direction == "droite": # Si l'utilisateur clic à droite
        effectuer_mouvement(creer_case_vide(position_x_joueur + DISTANCE_ENTRE_CASE, position_y_joueur),
                            creer_case_vide(position_x_joueur + 2 * DISTANCE_ENTRE_CASE, position_y_joueur),
                            creer_caisse(position_x_joueur + DISTANCE_ENTRE_CASE, position_y_joueur),
                            caisses, murs, joueur, can,
                            (position_x_joueur + 2 * DISTANCE_ENTRE_CASE), position_y_joueur,
                            (position_x_joueur + DISTANCE_ENTRE_CASE), position_y_joueur, liste_image)
    elif direction == "gauche": # Si l'utilisateur clic à gauche
        effectuer_mouvement(creer_case_vide(position_x_joueur - DISTANCE_ENTRE_CASE, position_y_joueur),
                            creer_case_vide(position_x_joueur - 2 * DISTANCE_ENTRE_CASE, position_y_joueur),
                            creer_caisse(position_x_joueur - DISTANCE_ENTRE_CASE, position_y_joueur),
                            caisses, murs, joueur, can,
                            (position_x_joueur - 2 * DISTANCE_ENTRE_CASE), position_y_joueur,
                            (position_x_joueur - DISTANCE_ENTRE_CASE), position_y_joueur, liste_image)
    elif direction == "haut": # Si l'utilisateur clic en haut
        effectuer_mouvement(creer_case_vide(position_x_joueur, position_y_joueur - DISTANCE_ENTRE_CASE),
                            creer_case_vide(position_x_joueur, position_y_joueur - 2 * DISTANCE_ENTRE_CASE),
                            creer_caisse(position_x_joueur, position_y_joueur - DISTANCE_ENTRE_CASE),
                            caisses, murs, joueur, can,
                            position_x_joueur, (position_y_joueur - 2 * DISTANCE_ENTRE_CASE),
                            position_x_joueur, (position_y_joueur - DISTANCE_ENTRE_CASE), liste_image)
    elif direction == "bas": # Si l'utilisateur clic en bas
        effectuer_mouvement(creer_case_vide(position_x_joueur, position_y_joueur + DISTANCE_ENTRE_CASE),
                            creer_case_vide(position_x_joueur, position_y_joueur + 2 * DISTANCE_ENTRE_CASE),
                            creer_caisse(position_x_joueur, position_y_joueur + DISTANCE_ENTRE_CASE),
                            caisses, murs, joueur, can,
                            position_x_joueur, (position_y_joueur + 2 * DISTANCE_ENTRE_CASE),
                            position_x_joueur, (position_y_joueur + DISTANCE_ENTRE_CASE), liste_image)


def effectuer_mouvement(coordonnee_destination, coordonnee_case_suivante, ancienne_caisse, caisses, murs, joueur, can,
                        deplace_caisse_x, deplace_caisse_y, deplace_joueur_x, deplace_joueur_y, liste_image):
    '''
    Fonction permettant d'effectuer le déplacement ou de ne pas l'effectuer si celui-ci n'est pas possible. Voir énoncé
    "Quelques règles". Cette methode est appelée par mouvement.
    :param coordonnee_destination: variable CaseVide ayant possiblement des coordonnées identiques à une autre variable
    (murs, caisse, casevide)
    :param coordonnee_case_suivante: variable CaseVide ayant possiblement des coordonnées identiques à une autre variable
    (murs, caisse, casevide) mais représente la case après coordonnee_destination
    :param ancienne_caisse: variable utile pour supprimer l'ancienne caisse (après avoir déplacé celle-ci)
    :param caisses: liste des caisses
    :param murs: liste des murs
    :param joueur: liste des joueurs
    :param can: Canvas (ignorez son fonctionnement), utile uniquement pour créer_image()
    :param deplace_caisse_x: coordonnée à laquelle la caisse va être déplacée en x (si le joueur pousse une caisse)
    :param deplace_caisse_y: coordonnée à laquelle la caisse va être déplacée en y (si le joueur pousse une caisse)
    :param deplace_joueur_x: coordonnée en x à laquelle le joueur va être après le mouvement
    :param deplace_joueur_y: coordonnée en y à laquelle le joueur va être après le mouvement
    :param liste_image: liste des images (murs, caisses etc...) détaillée dans l'énoncé
    :return:
    '''
    # Vérification des paramètres
    if caisses is None or murs is None or joueur is None or deplace_caisse_x is None or deplace_caisse_y is None \
        or deplace_joueur_x is None or deplace_joueur_y is None or liste_image is None:
        return None

    # Booléens pour connaître la "nature" de la case destination ou la case qui suit la case destination
    case_dest_mur: bool = False
    case_suiv_mur: bool = False
    case_dest_caisse: bool = False
    case_suiv_caisse: bool = False

    for elt in murs:
        if est_egal_a(elt, coordonnee_destination):
            case_dest_mur = True
            break
    for elt in murs:
        if est_egal_a(elt, coordonnee_case_suivante):
            case_suiv_mur = True
            break
    for elt in caisses:
        if est_egal_a(elt, coordonnee_destination):
            case_dest_caisse = True
            break
    for elt in caisses:
        if est_egal_a(elt, coordonnee_case_suivante):
            case_suiv_caisse = True
            break

    # Selon les résultats obtenus plus haut, autorise le déplacement et fait les changements nécessaires sur les cases "touchées"
    if not case_dest_mur:
        if not (case_dest_caisse and (case_suiv_caisse or case_suiv_mur)):
            if case_dest_caisse:
                creer_image(can, deplace_caisse_x, deplace_caisse_y, liste_image[2])
                caisses.remove(ancienne_caisse)
                caisses.append(creer_caisse(deplace_caisse_x, deplace_caisse_y))

                creer_image(can, coordonnee_x(joueur[0]), coordonnee_y(joueur[0]), liste_image[6])
                joueur[0] = creer_personnage(deplace_joueur_x, deplace_joueur_y)
            else:
                creer_image(can, coordonnee_x(joueur[0]), coordonnee_y(joueur[0]), liste_image[6])
                joueur[0] = creer_personnage(deplace_joueur_x, deplace_joueur_y)


def chargement_score(scores_file_path, dict_scores):
    '''
    Fonction chargeant les scores depuis un fichier.txt et les stockent dans un dictionnaire
    :param scores_file_path: le chemin d'accès du fichier
    :param dict_scores:  le dictionnaire pour le stockage
    :return:
    '''
    # Vérification des paramètres
    if not os.path.isfile(scores_file_path) or dict_scores is None:
        return None

    ligne: str = ""
    scores: list = []
    niveau: int = 0

    # Ouverture du fichier en mode lecture
    with open(scores_file_path, 'r') as filin:
        for ligne in filin:
            ligne = ligne.strip() # Retire le dernier ";"
            niveau, scores = ligne.split(";", maxsplit=1) # Sépare le premier chiffre (niveau) et les scores dans une liste
            dict_scores[int(niveau)] = []
            for score in scores.split(";"): # Sépare chacun des scores de la liste séparés par ";"
                if len(score) > 0:
                    dict_scores[int(niveau)].append(int(score)) # Stocke chacun des scores dans le dictionnaire


def maj_score(niveau_en_cours, dict_scores) -> str:
    '''
    Fonction mettant à jour l'affichage des scores en stockant dans un str l'affichage visible
    sur la droite du jeu.
    ("Niveau x
      1) 7699
      2) ... ").
    :param niveau_en_cours: le numéro du niveau en cours
    :param dict_scores: le dictionnaire pour stockant les scores
    :return str: Le str contenant l'affichage pour les scores ("\n" pour passer à la ligne)
    '''
    # Vérification des paramètres
    if niveau_en_cours is None or dict_scores is None:
        return None

    affichage: str = ""
    compteur: int = 0
    affichage = "Niveau " + niveau_en_cours + "\n"

    # Après le "Niveau x", énumère tous les scores avec un retour à la ligne
    for elt in dict_scores[int(niveau_en_cours)]:
        compteur += 1
        affichage = affichage + str(compteur) + ") " + str(elt) + "\n"

    return affichage


def enregistre_score(temps_initial, nb_coups, score_base, dict_scores, niveau_en_cours) -> int:
    '''
    Fonction enregistrant un nouveau score réalisé par le joueur. Le calcul de score est le suivant :
    score_base - (temps actuel - temps initial) - (nombre de coups * valeur d'un coup)
    Ce score est arrondi sans virgule et stocké en tant que int.
    :param temps_initial: le temps initial
    :param nb_coups: le nombre de coups que l'utilisateurs à fait (les mouvements)
    :param score_base: Le score de base identique pour chaque partie
    :param dict_scores: Le dictionnaire stockant les scores
    :param niveau_en_cours: Le numéro du niveau en cours
    :return: le score sous forme d'un int
    '''
    # Vérification des paramètres
    if temps_initial is None or nb_coups is None or score_base is None or dict_scores is None or niveau_en_cours is None:
        return None

    # Nouveau score arrondi sans virgule et stocké en tant que int
    nouveau_score: int = int(round(score_base - (time.time() - temps_initial) - (nb_coups * VALEUR_COUP), 0))

    # Enregistrement du nouveau score dans le dictionnaire stockant les scores
    for i in range(len(dict_scores[int(niveau_en_cours)])):
        if nouveau_score >= dict_scores[int(niveau_en_cours)][i]:
            dict_scores[int(niveau_en_cours)].insert(i, nouveau_score)
            dict_scores[int(niveau_en_cours)].pop(len(dict_scores[int(niveau_en_cours)]) - 1)
            break

    return nouveau_score


def update_score_file(scores_file_path, dict_scores):
    '''
    Fonction sauvegardant tous les scores dans le fichier.txt.
    :param scores_file_path: le chemin d'accès du fichier de stockage des scores
    :param dict_scores: Le dictionnaire stockant les scores
    :return:
    '''
    # Vérification des paramètres
    if not os.path.isfile(scores_file_path) or dict_scores is None:
        return None

    # Ouverture du fichier en mode écriture
    with open(scores_file_path, 'w') as filout:
        for cle, val in dict_scores.items():
            filout.write(str(cle) + ";") # écrit le numéro du niveau
            for j in val:
                filout.write(str(j) + ";") # Parcourt la liste et écrit chacun des scores à la suite du niveau correspondant
            filout.write("\n") # Saut à la ligne avant de passer au niveau suivant


# Constantes à utiliser
DISTANCE_ENTRE_CASE = 32  # distance par rapport à l'autre case
VALEUR_COUP = 50
X_PREMIERE_CASE = 20
Y_PREMIERE_CASE = 20

# Ne pas modifier !
if __name__ == '__main__':
    os.system("fourni\simulateur.py")

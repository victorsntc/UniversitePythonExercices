"""
Dans cet exercice, nous nous familiarisons avec les manipulations de dictionnaires
sur une thématique de magasin en ligne.

«Chez Geek and sons tout ce qui est inutile peut s’acheter, et tout ce qui peut s’acheter est un peu trop cher.»

La base de prix des produits de Geek and sons est représentée en Python par un dictionnaire de type dict[str:float] avec :

— les noms de produits, de type str, comme clés
— les prix des produits, de type float, comme valeurs associées.


Question 1
Donner une expression Python pour construire la base des prix base_prix des produits correspondant à la table suivante :
-----------------------------------
| Nom du produit       | Prix TTC |
-----------------------------------
| Sabre laser          | 229.0    |
| Mitendo DX           | 127.30   |
| Coussin Linux        | 74.50    |
| Slip Goldorak        | 29.90    |
| Station Nextpresso   | 184.60   |
-----------------------------------

Déclarer la base des prix dans une fonction main()


Question 2
Donner une définition de la fonction "disponibilite" qui étant donné un nom de produit prod et une base de prix base_prix,
retourne True si le produit est présent dans la base, ou False sinon

Question 3
Donner une définition de la fonction prix_moyen qui, étant donné une base de prix base_prix (est-ce que la base contient au moins un produit ?),
retourne le prix moyen des produits disponibles

Par exemple :
prix_moyen(base_prix)
129.06

Question 4
Donner une définition de la fonction fourchette_prix qui, étant donné un prix minimum mini,
un prix maximum maxi et une base de prix base_prix, retourne l’ensemble des noms de produits disponibles dans cette
fourchette de prix

Par exemple :
fourchette_prix(50.0, 200.0, base_prix)
['Coussin Linux', 'Mitendo DX', 'Station Nextpresso']


Question 5
Le panier est un concept omniprésent dans les sites marchands, Geeks and sons n’échappe pas à la règle.
En Python, le panier du client sera représenté par un dictionnaire de type dict[str:int] avec :
— les noms de produits comme clés
— une quantité d’achat comme valeurs associées

Donner une expression Python correspondant à l’achat de 3 sabres lasers, de 2 coussins Linux et de 1 slip Goldorak.

Déclarer le panier dans la fonction main()


Question 6
Donner une définition de la fonction tous_disponibles qui, étant donné un panier d’achat panier et une base de prix base_prix,
retourne True si tous les produits demandés sont disponibles, ou False sinon

Question 7
Donner une définition de la fonction prix_achats qui, étant donné un panier d’achat panier et une base de prix base_prix,
retourne le prix total correspondant

Par exemple :
prix_achats(panier, base_prix)
865.9

Est-ce que tous les articles du paniers sont disponibles dans la base de produits ?

"""

def disponibilite(prod: str, base_prix: dict) -> bool:
    """
    retourne True si le produit est présent dans la base, ou False sinon
    :param prod: un produit
    :param base_prix: la base des prix des produits
    :return: retourne True si le produit est présent dans la base
    """
    if prod is None or base_prix is None:
        return None
    return prod in base_prix


def prix_moyen(base_prix: dict) -> float:
    """
    retourne le prix moyen des produits disponibles
    :param base_prix: la base des prix des produits
    :return: le prix moyen
    """
    if base_prix is None or len(base_prix) == 0:
        return None
    return sum(base_prix.values())/len(base_prix)


def fourchette_prix(mini, maxi, base_prix) -> list:
    """
    retourne l’ensemble des noms de produits disponibles dans cette fourchette de prix
    :param mini: un prix minimum mini
    :param maxi: un prix maximum
    :param base_prix: une base de prix
    :return: l’ensemble des produits
    """
    if mini < 0 or maxi < mini or base_prix is None:
        return None
    prods: list = []
    for k, v in base_prix.items():
        if v >= mini and v <= maxi:
            prods.append(k)
    return prods

def main():
    base_prix: dict = {"Sabre laser": 229.0,
                       "Mitendo DX": 127.30,
                       "Coussin Linux": 74.50,
                       "Slip Goldorak": 29.90,
                       "Station Nextpresso": 184.60}

    print(disponibilite("Mitendo DX", base_prix))
    print(disponibilite("Mitendo DZ", base_prix))
    print(disponibilite(None, base_prix))
    print(disponibilite("Mitendo DZ", None))

    print(prix_moyen(base_prix))

    print(fourchette_prix(50.0, 200.0, base_prix))


if __name__ == "__main__":
    main()
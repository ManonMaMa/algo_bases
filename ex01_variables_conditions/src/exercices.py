from __future__ import annotations


def somme(a: int, b: int) -> int:
    """Retourne la somme de deux entiers."""
    return a + b
    # TODO
    raise NotImplementedError


def produit(a: int, b: int) -> int:
    """Retourne le produit de deux entiers."""
    return a * b
    # TODO
    raise NotImplementedError


def est_pair(n: int) -> bool:
    """Vrai si le nombre est pair."""
    if n % 2 == 0:
        return True
    else: 
        return False
    # TODO
    raise NotImplementedError

def est_voyelle(lettre: str) -> bool:
    liste_voyelles=["a","e","i","o","u","y","A","E","I","O","U","Y"]
    if lettre in liste_voyelles:
        return True
    else:
        return False
    """Vrai si la lettre est une voyelle."""
    # TODO
    raise NotImplementedError

def calcul_reduction(prix: float, taux: float) -> float:
    if prix < 0:
        raise ValueError
    if prix == 0:
        return 0.0
    else:
        if taux >= 100:
            return 0.0
        else :
            return prix - (prix * taux /100)
    """Retourne le prix après remise (taux en pourcentage)."""
    # TODO


def est_bissextile(annee: int) -> bool:
    """Vrai si année bissextile (Grégorien).
    Une année est bissextile si elle est divisible par 4.
    Cependant, elle n'est pas bissextile si elle est divisible par 100, sauf si elle est aussi divisible par 400.
    Par exemple :
        - 2000 est bissextile (divisible par 400).
        - 1900 n'est pas bissextile (divisible par 100 mais pas par 400).
        - 2004 est bissextile (divisible par 4 mais pas par 100).
    """
    if annee % 400 == 0:
        return True
    else: 
        if annee % 100 == 0:
            return False
        else: 
            if annee % 4 == 0:
                return True
            else:
                return False 
    raise NotImplementedError

def racine_carree(x: float) -> float:
    import math
    if x < 0:
        raise ValueError
    else:
        return math.sqrt(x)
    """Retourne la racine carrée d'un nombre."""
    # TODO
    raise NotImplementedError

def maximum_trois(a: int, b: int, c: int) -> int:
    if a > b and a > c : 
        return a
    if b > a and b > c : 
        return b
    if c > b and c > a : 
        return c
    """Renvoie le maximum de trois valeurs sans utiliser max()."""
    # TODO
    raise NotImplementedError

def factorielle(n: int) -> int:
    """Retourne la factorielle d'un entier.
    1. Vérifier si n est un nombre négatif :
       - Si oui, lever une exception avec un message d'erreur approprié.
    2. Initialiser une variable résultat à 1.
    3. Pour chaque valeur i de 1 à n inclus :
       - Multiplier le résultat actuel par i.
    4. Retourner le résultat.
    """
    if n < 0:
        raise ValueError
    else: 
        resultat = 1
        for i in range(2,n+1):
            resultat = resultat * i
        return resultat
    # TODO
    raise NotImplementedError

def convertir_en_binaire(n: int) -> str:
    """Convertit un entier en représentation binaire."""
    import math
    if n == 0:
        return '0'
    else:
        result = '' 
        while n != 1:
            if n % 2 == 0:
                result = '0' + result
                n = n / 2
            else:
                result = '1' + result
                n = math.floor(n/2)
        result = '1' + result
        return result
    # TODO
    raise NotImplementedError


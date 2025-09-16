from __future__ import annotations


def somme_pairs(nums: list[int]) -> int:
    somme = 0
    for i in nums:
        if i % 2 == 0:
            somme = somme + i
    return somme
    # TODO: Implémentez la fonction pour calculer la somme de tous les nombres pairs de la liste donnée.


def compter_occurrences(items: list[int], valeur: int) -> int:
    nb_occurences = 0
    for i in items:
        if i == valeur:
            nb_occurences += 1
    return nb_occurences
    # TODO: Implémentez la fonction pour compter le nombre d'occurrences de `valeur` dans la liste `items`.


def table_multiplication(n: int) -> list[int]:
    i = 0
    liste_table = []
    while i != 10:
        i = i + 1
        r = n * i
        liste_table.append(r)
    return liste_table 
    # TODO: Implémentez la fonction pour retourner la table de multiplication de `n` (jusqu'à 10 inclus).


def trouver_maximum(nums: list[int]) -> int:
    u = nums[0]
    for i in nums:
        if i > u:
            u = i
    return u
    # TODO: Implémentez une fonction pour trouver et retourner la valeur maximale dans la liste.


def calculer_moyenne(nums: list[int]) -> float:
    somme = 0
    for i in nums:
        somme = somme + i
    if len(nums) == 0:
        return 0
    else:
        moyenne = somme / len(nums)
        return moyenne
    # TODO: Implémentez une fonction pour calculer et retourner la moyenne des valeurs dans la liste.


def compter_negatifs(nums: list[int]) -> int:
    count = 0
    for i in nums: 
        if i < 0: 
            count += 1
    return count
    # TODO: Implémentez une fonction pour compter et retourner le nombre d'entiers négatifs dans la liste.


def compter_mots(phrase: str) -> int:
    return len(phrase.split())
        # TODO: Implémentez une fonction pour compter le nombre de mots dans une chaîne de caractères donnée.


def trouver_plus_long(items: list[str]) -> str:
    mot_long = ""
    for mot in items:
        if len(mot) > len(mot_long):
            mot_long = mot
    return mot_long
    # TODO: Implémentez une fonction pour trouver et retourner le mot le plus long dans une liste de chaînes de caractères.


def convertir_majuscule(items: str) -> str:
    return items.upper()
    # TODO: Implémentez une fonction pour convertir toutes les chaînes de la liste en majuscules.


def compter_mots_commencant_par(items: str, lettre: str) -> int:
    liste = items.split()
    count = 0
    for i in liste:
        if i.startswith(lettre):
            count += 1
    return count
    # TODO: Implémentez une fonction pour compter les mots commençant par une lettre donnée.


def trouver_mot_finissant_par(items: str, suffixe: str) -> list[str]:
    liste = items.split()
    new_items = []
    for i in liste:
        if i.endswith(suffixe):
            new_items.append(i)
    return new_items
    # TODO: Implémentez une fonction pour trouver tous les mots qui se terminent par un suffixe donné dans la liste.


def compter_caracteres(s: str, char: str) -> int:
    return s.count(char)
        # TODO: Implémentez une fonction pour compter le nombre d'occurences du caractère char et retourner le nombre total.


def inverser_chaine(s: str) -> str:
    return s[::-1]
    # TODO: Implémentez une fonction pour inverser et retourner la chaîne de caractères donnée.


def trouver_occurrences_chaine(s: str, c: str) -> int:
    # TODO: Implémentez une fonction pour compter les occurrences d'un caractère donné dans une chaîne.
    raise NotImplementedError

# tuples
def somme_pairs_tuples(nums: tuple[int, ...]) -> int:
    # TODO: Implémentez la fonction pour calculer la somme de tous les nombres pairs dans un tuple donné.
    raise NotImplementedError


def compter_occurrences_tuples(items: tuple[int, ...], valeur: int) -> int:
    # TODO: Implémentez la fonction pour compter le nombre d'occurrences d'une valeur dans un tuple donné.
    raise NotImplementedError


def table_multiplication_tuples(n: int) -> tuple[int, ...]:
    # TODO: Implémentez la fonction pour retourner la table de multiplication (jusqu'à 10 inclus) sous forme de tuple.
    raise NotImplementedError


def trouver_maximum_tuples(nums: tuple[int, ...]) -> int:
    # TODO: Implémentez une fonction pour trouver et retourner le nombre maximum d'un tuple.
    raise NotImplementedError


def calculer_moyenne_tuples(nums: tuple[int, ...]) -> float:
    # TODO: Implémentez une fonction pour calculer et retourner la moyenne des nombres dans un tuple.
    raise NotImplementedError

# sets

def somme_pairs_sets(nums: set[int]) -> int:
    # TODO: Implémentez la fonction pour calculer la somme de tous les nombres pairs dans un set donné.
    raise NotImplementedError

def compter_occurrences_sets(items: set[int], valeur: int) -> int:
    # TODO: Cette fonction vérifiera simplement si `valeur` existe puisque les sets ne permettent pas les doublons.
    raise NotImplementedError


def table_multiplication_sets(n: int) -> set[int]:
    # TODO: Implémentez une fonction pour retourner la table de multiplication (jusqu'à 10 inclus) sous forme de set.
    raise NotImplementedError


def trouver_maximum_sets(nums: set[int]) -> int:
    # TODO: Implémentez une fonction pour trouver et retourner le nombre maximum d'un set.
    raise NotImplementedError


def compter_negatifs_sets(nums: set[int]) -> int:
    # TODO: Implémentez une fonction pour compter et retourner le nombre de nombres négatifs dans un set.
    raise NotImplementedError

# dictionnaires

def ajouter_element(d: dict, cle: str, valeur: any) -> dict:
    # TODO: Implémentez une fonction pour ajouter une clé et sa valeur dans un dictionnaire.
    raise NotImplementedError


def supprimer_element(d: dict, cle: str) -> dict:
    # TODO: Implémentez une fonction pour supprimer une clé et sa valeur d'un dictionnaire.
    raise NotImplementedError


def fusionner_dictionnaires(d1: dict, d2: dict) -> dict:
    # TODO: Implémentez une fonction qui fusionne deux dictionnaires et renvoie le résultat.
    # Les valeurs de `d2` remplaceront celles de `d1` en cas de doublons.
    raise NotImplementedError


def inverser_dictionnaire(d: dict) -> dict:
    # TODO: Implémentez une fonction pour inverser un dictionnaire, échangeant les clés et les valeurs.
    # Note: Si des valeurs duplicatées existent, une erreur ou un comportement spécifique doit être défini.
    raise NotImplementedError


def compter_valeurs(d: dict) -> int:
    # TODO: Implémentez une fonction pour compter combien de paires clé-valeur sont dans le dictionnaire.
    raise NotImplementedError


def trouver_valeur_maximale(d: dict) -> any:
    # TODO: Implémentez une fonction pour trouver et retourner la valeur la plus grande dans un dictionnaire.
    raise NotImplementedError


def trouver_cle_par_valeur(d: dict, valeur: any) -> list[str]:
    # TODO: Implémentez une fonction pour retourner une liste de toutes les clés correspondant à une valeur donnée.
    raise NotImplementedError


def verifier_cle_existe(d: dict, cle: str) -> bool:
    # TODO: Implémentez une fonction qui vérifie si une clé existe dans le dictionnaire.
    raise NotImplementedError


def valeurs_uniques(d: dict) -> set:
    # TODO: Implémentez une fonction qui retourne toutes les valeurs uniques dans un dictionnaire sous forme de set.
    raise NotImplementedError


def mettre_a_jour_valeur(d: dict, cle: str, nouvelle_valeur: any) -> dict:
    # TODO: Implémentez une fonction pour mettre à jour une valeur associée à une clé existante ou en ajouter une nouvelle.
    raise NotImplementedError

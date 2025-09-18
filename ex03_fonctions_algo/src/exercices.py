from __future__ import annotations

# Prise en main
# Exemples simples : Création d'une fonction et appel
def print_hello_world() -> None:
    # Une fonction qui affiche "Hello, world!"
    return "Hello, World!"


def reverse_string(param: str) -> str:
    # Une fonction qui renverse une chaîne donnée en entrée.
    return param[::-1]


def to_uppercase(param: str) -> str:
    # Une fonction qui transforme une chaîne en majuscules.
    return param.upper()


def count_substring(param: str, sub: str) -> int:
    # Une fonction qui compte le nombre d'occurrences d'une sous-chaîne dans une chaîne.
    return param.count(sub)

def list_length(param: list[int]) -> int:
    # Une fonction qui retourne le nombre d'éléments dans une liste d'entiers.
    return len(param)


def max_in_list(param: list[int]) -> int:
    # Une fonction qui retourne le plus grand élément dans une liste d'entiers.
    return max(param)


# Fonctions classiques
def pgcd(a: int, b: int) -> int:
    while b != 0:
        c = a
        a = b
        b = c % b
    return a
    # À FAIRE : Calculer le plus grand commun diviseur (PGCD) de deux entiers.
    # Utiliser l'algorithme d'Euclide en itératif.
    # L'algorithme d'Euclide fonctionne en répétant la division euclidienne entre deux nombres a et b :
    # - Tant que b n'est pas nul, remplacer a par b et b par le reste de la division euclidienne de a par b.
    # - Lorsque b devient nul, le PGCD est la valeur actuelle de a.
    # Une division euclidienne consiste à diviser deux nombres entiers a et b (b ≠ 0) pour obtenir un
    # quotient q et un reste r, tels que : a = b * q + r, avec 0 ≤ r < |b|.


def fibonacci(n: int) -> int:
    i = 2
    nb_fi = 1
    nb_fi_old = 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    while i <= n:
        nb_fi_new = nb_fi_old + nb_fi
        nb_fi_old = nb_fi
        nb_fi = nb_fi_new
        i = i + 1
    return nb_fi_new

    # La suite de Fibonacci est une suite de nombres où chaque terme est la somme des deux termes précédents,
    # en commençant par 0 et 1. Par exemple : 0, 1, 1, 2, 3, 5, 8, ... 13, 21, 34, 55
    # À FAIRE : Calculer le nième nombre de Fibonacci de manière itérative.


def crible_eratosthene(n: int) -> list[int]:
    liste_nb_premier = [bool]
    i = 0
    while i <= n:
        liste_nb_premier.append(True)
        i += 1
    liste_nb_premier[0] = False
    liste_nb_premier[1] = False

    p = 2
    while p <= n:
        if liste_nb_premier[p] == True:
            m = p + 1
            while m <= n:
                if m % p == 0:
                    liste_nb_premier[m] = False
                m += 1
        p += 1

    liste_premiers = []
    t = 0
    while t <= n:
        if liste_nb_premier[t] == True:
            liste_premiers.append(t)
        t += 1

    # À FAIRE : Implémenter le crible d'Ératosthène pour générer tous les nombres premiers jusqu'à n.
    # Étapes :
    # 1. Créer une liste booléenne de taille n+1 initialement à True, où l'indice représente un nombre.
    # 2. Les indices 0 et 1 doivent être marqués comme False (0 et 1 ne sont pas premiers).
    # 3. Parcourir les entiers p de 2 à √n (inclus).
    # 4. Si p est premier (booléen True), alors marquer tous ses multiples (p*p jusqu'à n) comme False.
    # 5. Extraire les indices marqués True dans la liste et les retourner sous forme de liste de nombres premiers.


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    div = 5
    while div * div <= n:
        if n % div == 0:
            return False
        if n % (div + 2) == 0:
            return False
        div += 6
    return True
    # À FAIRE : Vérifier si un nombre est premier à l'aide de vérifications itératives.
    # Instructions détaillées :
    # 1. Si n est inférieur ou égal à 1, retourner False (les nombres <= 1 ne sont pas premiers).
    # 2. Si n est 2 ou 3, retourner True (2 et 3 sont des nombres premiers).
    # 3. Si n est divisible par 2 ou 3, retourner False (les multiples de 2 et 3 ne sont pas premiers).
    # 4. Utiliser une boucle pour tester les divisibilités d'autres nombres potentiels :
    #    - Initialiser un diviseur potentiel à 5.
    #    - Continuer tant que le carré du diviseur est <= n.
    #    - Si n est divisible par le diviseur ou diviseur + 2, retourner False.
    #    - Incrémenter le diviseur de 6 à chaque tour (car les nombres premiers > 3 sont de la forme 6k ± 1).
    # 5. Si aucune des conditions précédentes n'a permis d'établir que n n'est pas premier, retourner True.


def is_palindrome(s: str) -> bool:
    p = s.replace(" ","")
    z = p.lower()
    if z == z[::-1]:
        return True
    else:
        return False
    # Un palindrome est une chaîne qui se lit de la même manière à l'endroit et à l'envers.
    # À FAIRE : Vérifier si une chaîne donnée est un palindrome en utilisant l'itération.


def binary_search(arr: list[int], target: int) -> int:
    # À FAIRE : Implémenter une recherche binaire sur une liste triée pour trouver la valeur cible.
    # Retourner l'indice de la cible si trouvée, sinon retourner -1.
    raise NotImplementedError


# Fonctions récursives
def gcd_recursive(a: int, b: int) -> int:
    if a >= b :
        r = a
        while r > 0:
            r = a % b
            if r > 0:
                a = b
                b = r
        return b
    # À FAIRE : Calculer le PGCD de deux entiers récursivement en utilisant l'algorithme d'Euclide.

def fibonacci_recursive(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    # À FAIRE : Calculer le nième nombre de Fibonacci de manière récursive.
    raise NotImplementedError


def is_prime_recursive(n: int, divisor: int = 2) -> bool:
    if n <= 1:
        return False
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True
    # À FAIRE : Vérifier si un nombre est premier en utilisant la récursion.
    # Cas de base : n <= 1 n'est pas premier. Pour n > 1, si divisible par divisor, n'est pas premier.
    # Sinon, incrémenter divisor et vérifier récursivement.

def is_palindrome_recursive(s: str) -> bool:
    if len(s) <= 1:
        return True

    if s[0] == s[-1]:
        return is_palindrome_recursive(s[1:-1])
    else:
        return False
    # À FAIRE : Vérifier si une chaîne donnée est un palindrome en utilisant la récursion.
    # Cas de base : Une chaîne de longueur 0 ou 1 est un palindrome.
    # Étape récursive : Comparer le premier et le dernier caractère et vérifier la sous-chaîne.

def factorial_recursive(n: int) -> int:
    # À FAIRE : Calculer la factorielle d'un nombre en utilisant la récursion.
    # Cas de base : n == 0 retourne 1. Étape récursive : n * factorial(n-1).
    if n == 0: 
        return 1
    return n * factorial_recursive(n-1)

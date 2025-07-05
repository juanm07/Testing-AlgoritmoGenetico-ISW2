import sys
from random import sample
from typing import Tuple


def selection(fitness_by_individual: dict, tournament_size: int) -> Tuple[list[str], float]:
    """
    fitness_by_individual: Diccionario que contiene a los individuos de la población como keys y su fitness como valores.
    tournament_size: Tamaño del torneo (entero positivo).
    """
    winner = None
    
    #  (Tournament selection)
    participantes = list(fitness_by_individual.keys())
    seleccionados = sample(participantes, tournament_size)
    mejor_fitness = sys.maxsize
    for individuo in seleccionados:
        if fitness_by_individual[individuo] < mejor_fitness:
            mejor_fitness = fitness_by_individual[individuo]
            winner = individuo

    return (list(winner), fitness_by_individual[winner])

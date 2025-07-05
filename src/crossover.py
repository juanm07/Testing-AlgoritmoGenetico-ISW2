from random import randint
from typing import List, Tuple


def crossover(parent1: List[str], parent2: List[str]) -> Tuple[List[str], List[str]]:
    offspring1 = None
    offspring2 = None
    # TODO: COMPLETAR
    size_parent1 = len(parent1)
    size_parent2 = len(parent2)
    crossover_point = min(size_parent1, size_parent2)//2 + 1    #Punto medio del padre más corto, así me aseguro de que haya mezcla
    offspring1 = parent1[:crossover_point]+parent2[crossover_point:]
    offspring2 = parent2[:crossover_point]+parent1[crossover_point:]

    return offspring1, offspring2

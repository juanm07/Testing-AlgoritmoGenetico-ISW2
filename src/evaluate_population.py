from typing import List

from src.get_fitness_cgi_decode import get_fitness_cgi_decode

def evaluate_population(population: List[List[str]]) -> dict:
    fitness = {}
    
    for individual in population:
        fitness_level = get_fitness_cgi_decode(individual)
        fitness[tuple(individual)] = fitness_level

    return fitness

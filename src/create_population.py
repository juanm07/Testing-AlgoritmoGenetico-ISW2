import random
import string
from random import choice
from string import printable
from typing import List


def get_random_character():
    return random.choice(string.printable)


def create_test_case() -> str:
    size = random.choice(range(11))
    test_case = ""
    while size != 0:
        test_case += get_random_character()
        size -= 1
    return test_case


def create_individual() -> List[str]:
    individual = []
    size = random.choice(range(1,16))
    while size !=0:
        individual.append(create_test_case())
        size -= 1
    return individual


def create_population(population_size) -> List[List[str]]:
    population = []
    while population_size != 0:
        population.append(create_individual())
        population_size -= 1
    return population

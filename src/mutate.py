from random import choice
from typing import List

from src.create_population import create_test_case, get_random_character


def add_character(test_case: str) -> str:
    
    if len(test_case) == 0:
        place_to_add = 0
    else:
        place_to_add = choice(range(len(test_case)))
    character_to_add = str(get_random_character())
    test_case = str(test_case[:place_to_add]) + character_to_add + str(test_case[place_to_add:])
    return test_case


def remove_character(test_case: str) -> str:
   
    place_to_skip = choice(range(len(test_case)-1))
    test_case = test_case[:place_to_skip] + test_case[place_to_skip+1:]
    return test_case


def modify_character(test_case: str) -> str:
    
    place_to_add = choice(range(len(test_case)))
    character_to_add = str(get_random_character())
    test_case = str(test_case[:place_to_add]) + character_to_add + str(test_case[place_to_add+1:])
    return str(test_case)


def add_test_case(individual: List[str]) -> List[str]:
    
    individual.append(create_test_case)
    return individual


def remove_test_case(individual: List[str]) -> List[str]:
    
    individual.pop()
    return individual


def modify_test_case(individual: List[str]) -> List[str]:
    
    has_mutated = False
    test_case_to_modify = choice(individual)
    while not has_mutated:
        modification_choice = choice(range(3))
        match modification_choice:
                case 0:
                    if len(test_case_to_modify) < 10:
                        add_character(test_case_to_modify)
                        has_mutated = True
                case 1:
                    if len(test_case_to_modify) > 1:
                        remove_character(test_case_to_modify)
                        has_mutated = True
                case 2:
                    if len(test_case_to_modify) > 0:
                        modify_character(test_case_to_modify)
                        has_mutated = True
        #Todo test case puede caer en alguno de estos casos. No hay riesgo de loop infinito
    return individual


def mutate(individual: List[str]) -> List[str]:
    
    has_mutated = False
    while not has_mutated:
        mutation_choice = choice(range(3))
        match mutation_choice:
            case 0:
                if len(individual) < 15:
                    add_test_case(individual)
                    has_mutated = True
            case 1:
                if len(individual) > 1:
                    remove_test_case(individual)
                    has_mutated = True
            case 2:
                if len(individual) > 0:
                    modify_test_case(individual)
                    has_mutated = True
        #Todo individuo puede caer en alguno de estos casos. No hay riesgo de loop infinito
    return individual


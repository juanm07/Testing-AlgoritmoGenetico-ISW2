from typing import List

from src.evaluate_condition import clear_maps
from src.cgi_decode_instrumented import cgi_decode_instrumented
from src.evaluate_condition import distances_false,distances_true

def get_fitness_cgi_decode(test_suite: List[str]) -> float:
    # Borro la información de branch coverage de ejecuciones anteriores
    # Recuerden que los diccionarios true_distances y false_distances son globales
    clear_maps()

    fitness = 0
    for test in test_suite:
        try:
            cgi_decode_instrumented(test)
        except:
            fitness = fitness #no me importa si tira una excepcion
    for key in distances_false:
        d_false = distances_false[key]
        d_true = distances_true[key]
        if d_true != 0:
            d_true = d_true/(d_true+1)
        if d_false !=0:
            d_false = d_false/(d_false+1)
        fitness += d_true
        fitness += d_false
    fitness += (5 - len(distances_false)) * 2  #Los branches que no están en los diccionarios no fueron alcanzados.
                                                #sumo +1 por cada uno ya que no se ejecutó
    return fitness
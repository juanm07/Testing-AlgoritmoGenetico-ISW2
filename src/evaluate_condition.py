import sys
from typing import Dict, Union

# Inicializar mappings globales
distances_true: Dict[int, int] = {}
distances_false: Dict[int, int] = {}


def update_maps(condition_num: int, d_true: int, d_false: int):
    global distances_true, distances_false

    if condition_num in distances_true.keys():
        distances_true[condition_num] = min(
            distances_true[condition_num], d_true)
    else:
        distances_true[condition_num] = d_true

    if condition_num in distances_false.keys():
        distances_false[condition_num] = min(
            distances_false[condition_num], d_false)
    else:
        distances_false[condition_num] = d_false


def clear_maps():
    global distances_true, distances_false
    distances_true.clear()
    distances_false.clear()


def get_true_distance(condition_num: int) -> Union[int, None]:
    global distances_true
    if condition_num in distances_true.keys():
        return distances_true[condition_num]
    else:
        return None


def get_false_distance(condition_num: int) -> Union[int, None]:
    global distances_false
    if condition_num in distances_false.keys():
        return distances_false[condition_num]
    else:
        return None


def has_reached_condition(condition_num: int) -> bool:
    global distances_true, distances_false
    return condition_num in distances_true.keys() or condition_num in distances_false.keys()


def evaluate_condition(condition_num: int, op: str, lhs: Union[str, Dict, int], rhs: Union[str, Dict, int]) -> bool:
    result = False
    distance_true = 0
    distance_false = 0
    if(not (type(lhs)== str and type(rhs) == str and len(lhs) == len(rhs) == 1
            or type(lhs) == str and type(rhs)== dict
            or type(lhs) == int and type(rhs) == int)):
        return False        #chequeo que sea uno de los casos posibles
    match op:       #Calculo distancias true y false segun el tipo de operacion basandonos en los ejemplos dados en la consigna
        case "Eq":
            result = (lhs == rhs)
            if result:
                distance_true = 0
                distance_false = 1
            else:
                if(type(lhs)== str and type(rhs) == str):
                    distance_true = abs(ord(lhs) - ord(rhs))
                    distance_false = 0
                elif (type(lhs) == str and type(rhs)== dict):
                    distance_true = get_distance_closest_key(lhs,rhs)
                    distance_false = 0

                else:
                    distance_true = abs(lhs - rhs)
                    distance_false = 0

        case "Ne":
            result = (lhs != rhs)
            if result:
                if(type(lhs) == str and type(rhs) == str):
                    distance_true = 0
                    distance_false = abs(ord(lhs)-ord(rhs))

                elif (type(lhs) == str and type(rhs)== dict):
                    distance_true = 0
                    distance_false = get_distance_closest_key(lhs,rhs)
                else:    
                    distance_true = 0
                    distance_false = abs(lhs - rhs)
            else:
                distance_true = 1
                distance_false = 0

        case "Lt":
            result = (lhs < rhs)
            if result:
                if(type(lhs) == str and type(rhs) == str):
                    distance_true = 0
                    distance_false = abs(ord(lhs)-ord(rhs))
                else:
                    distance_true = 0
                    distance_false = abs(lhs - rhs)
            else:
                if(type(lhs) == str and type(rhs) == str):
                    distance_true = abs(ord(lhs) - ord(rhs)) + 1
                    distance_false = 0
                else:
                    distance_true = abs(lhs - rhs) + 1
                    distance_false = 0

        case "Gt":
            result = (lhs > rhs)
            if result:
                if(type(lhs) == str and type(rhs) == str):
                    distance_true = 0
                    distance_false = abs(ord(lhs)-ord(rhs))
                else:    
                    distance_true = 0
                    distance_false = abs(lhs - rhs)
            else:
                if(type(lhs) == str and type(rhs) == str):
                    distance_true = abs(ord(lhs) - ord(rhs)) + 1
                    distance_false = 0
                else:    
                    distance_true = abs(lhs - rhs) + 1  
                    distance_false = 0

        case "Le":
            result = (lhs <= rhs)
            if result:
                if(type(lhs) == str and type(rhs) == str):
                    distance_true = 0
                    distance_false = abs(ord(lhs) - ord(rhs)) + 1
                else:
                    distance_true = 0
                    distance_false = abs(lhs - rhs) + 1
            else:
                if(type(lhs) == str and type(rhs) == str):
                    distance_true = abs(ord(lhs)-ord(rhs))
                    distance_false = 0
                else:
                    distance_true = abs(lhs - rhs)
                    distance_false = 0

        case "Ge":
            result = (lhs >= rhs)
            if result:
                if(type(lhs) == str and type(rhs) == str):
                    distance_true = 0
                    distance_false = abs(ord(lhs)-ord(rhs)) + 1
                else:
                    distance_true = 0
                    distance_false = abs(lhs - rhs) + 1
            else:
                if(type(lhs) == str and type(rhs) == str):
                    distance_true = abs(ord(lhs)-ord(rhs))
                    distance_false = 0
                else:
                    distance_true = abs(lhs - rhs)
                    distance_false = 0

        case "In":
            result = (lhs in rhs)
            if result:
                distance_true = 0
                distance_false = 1
            else:
                distance_true = get_distance_closest_key(lhs, rhs)
                distance_false = 0

    update_maps(condition_num, distance_true, distance_false)
    return result

def get_distance_closest_key(key: str, dic: Dict) -> int:
    key_value = ord(key)
    closest_key = sys.maxsize
    for k in dic:
        distance = abs(key_value - ord(k))
        if distance < closest_key:
            closest_key = distance
    return closest_key

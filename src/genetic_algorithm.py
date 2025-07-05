from random import random
from typing import List

from src.create_population import create_population
from src.crossover import crossover
from src.evaluate_population import evaluate_population
from src.mutate import mutate
from src.selection import selection

class GeneticAlgorithm():
    def __init__(self):
        self.population_size = 100
        self.tournament_size = 5
        self.p_crossover = 0.70
        self.p_mutation = 0.20

        self.generation = 0
        self.best_individual = None
        self.fitness_best_individual = None

    def get_best_individual(self):
        return self.best_individual
    
    def get_fitness_best_individual(self):
        return self.fitness_best_individual
    
    def get_generation(self):
        return self.generation

    def generate_crossovers(self, population: List[List[str]], fitness_by_individual: dict) -> List[List[str]]:
        
        new_population = []
        while len(new_population) < self.population_size:
            p1 = selection(fitness_by_individual, self.tournament_size)[0]
            p2 = selection(fitness_by_individual, self.tournament_size)[0]      #Hay chance de que ambos padres sean el mismo. Lo permitimos ya que aún así los hijos pueden mutar y generar nuevos individuos
            h1, h2 = crossover(p1, p2)      
            new_population.append(h1)
            new_population.append(h2)
        return new_population

    def generate_mutations(self, population: List[List[str]]) -> List[List[str]]:

        new_population = []
        for individual in population:
            new_population.append(individual)
            chance = random()
            if chance < self.p_mutation:
                new_population[-1] = mutate(individual)
        return new_population

    def covered_all_branches(self, fitness_individual: float) -> bool:
        
        return fitness_individual == 0     #fitness += 1 por cada branch no ejecutado. fitness = 0 --> todos los branches ejecutados

    def run(self):
        # Generar y evaluar la poblacion inicial
        population = create_population(self.population_size)
        fitness_by_individual = evaluate_population(population)

        # Imprimir el mejor valor de fitness encontrado
        best_fitness_and_individual = min(zip(fitness_by_individual.values(), fitness_by_individual.keys()))
        print("Mejor fitness de generacion", self.generation, ":", best_fitness_and_individual[0])
        self.best_individual = list(best_fitness_and_individual[1])
        self.fitness_best_individual = best_fitness_and_individual[0]

        # Continuar mientras la cantidad de generaciones es menor que 1000
        # y no haya ningun individuo que cubra todos los objetivos

        while (self.generation < 1000 and not self.covered_all_branches(self.fitness_best_individual)): 

            # Producir una nueva poblacion en base a la anterior.
            # Usar selection, crossover y mutation.
            new_population = []
            new_population = self.generate_crossovers(population, fitness_by_individual)
            new_population = self.generate_mutations(new_population)

            # Una vez creada, reemplazar la poblacion anterior con la nueva
            self.generation += 1
            population = new_population

            # Evaluar la nueva poblacion e imprimir el mejor valor de fitness
            fitness_by_individual = evaluate_population(population)
            best_fitness_and_individual = min(zip(fitness_by_individual.values(), fitness_by_individual.keys()))
            print("Mejor fitness de generacion", self.generation, ":", best_fitness_and_individual[0])
            self.best_individual = best_fitness_and_individual[1]
            self.fitness_best_individual = best_fitness_and_individual[0]

        # retornar el mejor individuo de la ultima generacion
        return self.best_individual

#!./venv/bin/python
import unittest

from random import seed
from src.genetic_algorithm import GeneticAlgorithm
from src.get_fitness_cgi_decode import get_fitness_cgi_decode


class TestGeneticAlgorithm(unittest.TestCase):
    def test1(self):
        # TODO COMPLETAR
        seed(1)
        ga = GeneticAlgorithm()
        result = ga.run()
        self.assertLessEqual(ga.get_generation(), 1000)
        if ga.get_generation() != 1000:
            self.assertEqual(ga.get_fitness_best_individual(), 0)
            self.assertEqual(get_fitness_cgi_decode(ga.best_individual), 0)
        print("Test suite:", result)
        print("Generaciones creadas:", ga.get_generation())
        print("Branch coverage:", 100 - ga.get_fitness_best_individual()*10, "%") #fitness = 0 -> 100% branch coverage

    def test2(self):
        # TODO COMPLETAR
        seed("2DaUnErrorRarisimo")
        ga = GeneticAlgorithm()
        result = ga.run()
        self.assertLessEqual(ga.get_generation(), 1000)
        if ga.get_generation() != 1000:
            self.assertEqual(ga.get_fitness_best_individual(), 0)
        print("Test suite:", result)
        print("Generaciones creadas:", ga.get_generation())
        print("Branch coverage:", 100 - ga.get_fitness_best_individual()*10, "%")

    def test3(self):
        # TODO COMPLETAR
        seed(3)
        ga = GeneticAlgorithm()
        result = ga.run()
        self.assertLessEqual(ga.get_generation(), 1000)
        if ga.get_generation() != 1000:
            self.assertEqual(ga.get_fitness_best_individual(), 0)
        print("Test suite:", result)
        print("Generaciones creadas:", ga.get_generation())
        print("Branch coverage:", 100 - ga.get_fitness_best_individual()*10, "%")


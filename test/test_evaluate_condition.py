#!./venv/bin/python
import unittest
from src.evaluate_condition import evaluate_condition


class TestEvaluateCondition(unittest.TestCase):
    def testExample(self):
        # TODO COMPLETAR
        evaluate_condition(1, "Eq", "10", "20")
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertEqual(True, False)

    def testEq(self):
        result = evaluate_condition(1, "Eq", 10, 20)
        self.assertFalse(result)
        result = evaluate_condition(2, "Eq", 20, 20)
        self.assertTrue(result)

    def testNe(self):
        result = evaluate_condition(1, "Ne", 10, 20)
        self.assertTrue(result)
        result = evaluate_condition(2, "Ne", 20, 20)
        self.assertFalse(result)

    def testLt(self):
        result = evaluate_condition(1, "Lt", 10, 20)
        self.assertTrue(result)
        result = evaluate_condition(2, "Lt", 20, 20)
        self.assertFalse(result)
        result = evaluate_condition(3, "Lt", 30, 20)
        self.assertFalse(result)

    def testGt(self):
        result = evaluate_condition(1, "Gt", 10, 20)
        self.assertFalse(result)
        result = evaluate_condition(2, "Gt", 20, 20)
        self.assertFalse(result)
        result = evaluate_condition(3, "Gt", 30, 20)
        self.assertTrue(result)

    def testLe(self):
        result = evaluate_condition(1, "Le", 10, 20)
        self.assertTrue(result)
        result = evaluate_condition(2, "Le", 20, 20)
        self.assertTrue(result)
        result = evaluate_condition(3, "Le", 30, 20)
        self.assertFalse(result)

    def testGe(self):
        result = evaluate_condition(1, "Ge", 10, 20)
        self.assertFalse(result)
        result = evaluate_condition(2, "Ge", 20, 20)
        self.assertTrue(result)
        result = evaluate_condition(3, "Ge", 30, 20)
        self.assertTrue(result)

    def testIn(self):
        result = evaluate_condition(1, "In", "A", {"A":1, "B":2, "C":3})
        self.assertTrue(result)
        result = evaluate_condition(2, "In", "a", {"A": 1, "B": 2, "C": 3})
        self.assertFalse(result)
        result = evaluate_condition(1, "In", "A", {})
        self.assertFalse(result)
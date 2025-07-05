#!./venv/bin/python
import unittest
import src.cgi_decode
from src.cgi_decode_instrumented import cgi_decode_instrumented
from src.evaluate_condition import evaluate_condition, clear_maps, get_true_distance, get_false_distance,distances_false,distances_true


class TestEvaluateConditionForCgiDecodeInstrumented(unittest.TestCase):
    def test_1(self):
        clear_maps()
        res = cgi_decode_instrumented("test+uno")
        self.assertEqual(res, "test uno")
        self.assertEqual(distances_true, {1: 0, 2: 0, 3: 64})
        self.assertEqual(distances_false, {1: 0, 2: 0, 3: 0})
    def test_2(self):
        clear_maps()
        res = cgi_decode_instrumented("h%69")
        self.assertEqual(res,"hi")
        self.assertEqual(distances_true,{1: 0, 2: 6, 3: 0, 4: 0, 5: 0})
        self.assertEqual(distances_false,{1: 0, 2: 0, 3: 0, 4: 1, 5: 1})
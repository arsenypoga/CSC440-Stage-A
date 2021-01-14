"""
Written By: Arseny Poga
CourseL CSC440
"""

from unittest import TestCase
from arith import Arith


class ArithTest(TestCase):
    def test_add(self):
        # Add two positive numbers
        self.assertEqual(90, Arith.add(80, 10))

        # Add a positive and negative number
        self.assertEqual(469, Arith.add(-99, 568))

        # Add floating point numbers
        self.assertEqual(30.785, Arith.add(0.005, 30.78))

    def test_sub(self):
        # Substract two positive integers
        self.assertEqual(70, Arith.sub(80, 10))

        # Substract a negative number and a positive number
        self.assertEqual(-667, Arith.sub(-99, 568))

        # Substarct two floating point numbers
        self.assertEqual(-10.2, Arith.sub(20.5, 30.7))

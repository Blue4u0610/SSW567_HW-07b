# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

"""
Updated Mar 30, 2026

@author: Jinfeng Lan
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    # 1. Right Triangle
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(4, 5, 3), 'Right', '4,5,3 is a Right triangle')

    # 2. Equilateral
    def testEquilateralTriangle(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    # 3. Isoceles
    def testIsocelesTriangleA(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isoceles', '2,2,3 should be isoceles')

    def testIsocelesTriangleB(self):
        self.assertEqual(classifyTriangle(2, 3, 2), 'Isoceles', '2,3,2 should be isoceles')

    def testIsocelesTriangleC(self):
        self.assertEqual(classifyTriangle(3, 2, 2), 'Isoceles', '3,2,2 should be isoceles')

    # 4. Scalene
    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(10, 11, 12), 'Scalene', '10,11,12 should be scalene')

    # 5. Not a Triangle
    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1, 10, 12), 'NotATriangle', '1,10,12 is not a triangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1,2,3 is not a triangle (forms a line)')

    # 6. Invalid Input: boundaries and negative nums
    def testInvalidInputNegative(self):
        self.assertEqual(classifyTriangle(-1, 10, 10), 'InvalidInput', 'Negative numbers are invalid')

    def testInvalidInputZero(self):
        self.assertEqual(classifyTriangle(0, 10, 10), 'InvalidInput', 'Zero is invalid')

    def testInvalidInputOver200(self):
        self.assertEqual(classifyTriangle(201, 10, 10), 'InvalidInput', 'Values > 200 are invalid')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()


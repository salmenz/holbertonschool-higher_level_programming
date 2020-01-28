#!/usr/bin/python3
import unittest
import io
import sys
import json
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestArgs(unittest.TestCase):
    def Reset(self):
        """Reset nb_objects to 0 before each test"""
        Base.reset_nb_objects()

    def test_0_args(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_1_arg(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(69)

    def test_2_args(self):
        r1 = Rectangle(69, 1)
        self.assertEqual(r1.width, 69)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_3_args(self):
        r1 = Rectangle(69, 1, 2)
        self.assertEqual(r1.width, 69)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_4_args(self):
        r1 = Rectangle(69, 1, 2, 3)
        self.assertEqual(r1.width, 69)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 1)

    def test_5_args(self):
        r1 = Rectangle(69, 1, 2, 3, 4)
        self.assertEqual(r1.width, 69)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 4)

    def test_more_than_5_args(self):
        with self.assertRaises(TypeError):
            Rectangle(69, 1, 2, 3, 4, 5)

class TestArgContent(unittest.TestCase):
    def Reset(self):
        """Reset nb_objects to 0 before each test"""
        Base.reset_nb_objects()

    def test_width_string(self):
        with self.assertRaises(TypeError):
            Rectangle("69", 1)

    def test_height_string(self):
        with self.assertRaises(TypeError):
            Rectangle(69, "1")

    def test_x_string(self):
        with self.assertRaises(TypeError):
            Rectangle(69, 2, "1")

    def test_y_string(self):
        with self.assertRaises(TypeError):
            Rectangle(69, 2, 3, "1")

    def test_id_string(self):
        with self.assertRaise(TypeError):
            Rectangle(69, 2, 3, 4, "1")

    def test_neg_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-69, 1)

    def test_neg_height(self):
        with self.assertRaises(ValueError):
            Rectangle(69, -1)

    def test_neg_x(self):
        with self.assertRaises(ValueError):
            Rectangle(69, 1, -1)

    def test_neg_y(self):
        with self.assertRaises(ValueError):
            Rectangle(69, 1, 2, -1)


class Test_Area(unittest.TestCase):
    def Reset(self):
        """Reset nb_objects to 0 before each test"""
        Base.reset_nb_objects()

    def test_area_2_args(self):
        r1 = Rectangle(69, 1)
        self.assertEqual(r1.area(), 69)

    def test_area_5_args(self):
        r1 = Rectangle(69, 1, 2, 3, 4)
        self.assertEqual(r1.area(), 69)

    def test_wrong(self):
        r1 = Rectangle(69, 69)
        with self.assertRaises(TypeError):
            r1.area(4761)

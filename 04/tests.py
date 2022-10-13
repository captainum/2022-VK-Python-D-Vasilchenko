# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member
# pylint: disable=too-few-public-methods
# pylint: disable=attribute-defined-outside-init
# pylint: disable=unused-variable

import unittest

from parameterized import parameterized

from descriptors import CapitalString, Integer, PositiveInteger
from meta import Meta


class TestMetaClass(unittest.TestCase):
    def test_meta(self):
        class CustomClass(metaclass=Meta):
            x = 50

            def __init__(self, val=99):
                self.val = val

            def line(self):
                return self.custom_val - self.custom_x

            def __str__(self):
                return "Custom_by_metaclass"

        inst = CustomClass()

        self.assertEqual(inst.custom_val, 99)
        self.assertEqual(inst.custom_x, 50)
        self.assertEqual(inst.custom_line(), 49)
        self.assertEqual(str(inst), "Custom_by_metaclass")

        inst.dynamic = "added later"
        self.assertEqual(inst.custom_dynamic, "added later")

        self.assertFalse("x" in inst.__dict__)
        self.assertFalse("val" in inst.__dict__)
        self.assertFalse("line" in inst.__dict__)
        self.assertFalse("dynamic" in inst.__dict__)
        self.assertFalse("yyy" in inst.__dict__)
        self.assertFalse("x" in inst.__dict__)
        self.assertFalse("x" in CustomClass.__dict__)


class TestDescriptors(unittest.TestCase):
    @parameterized.expand(
        [
            "five",
            (5.0,),
            ((1, 2),),
        ]
    )
    def test_integer_descriptor_wrong_arg(self, param):
        def create_class():
            class Data:
                num = Integer(param)

        def set_attr():
            class Data:
                num = Integer(5)

            Data().num = param

        self.assertRaises(TypeError, create_class)
        self.assertRaises(TypeError, set_attr)

    @parameterized.expand(
        [
            (1,),
            (-1,),
            (0,),
        ]
    )
    def test_integer_descriptor_successful_creation(self, param):
        def create_class():
            class Data:
                num = Integer(param)

            return Data()

        self.assertIsInstance(create_class().num, Integer)

        inst = create_class()
        inst.num = param * -1
        self.assertEqual(inst.num, param * -1)

    @parameterized.expand(
        [
            "five",
            (5.0,),
            ((1, 2),),
        ]
    )
    def test_capital_string_descriptor_wrong_arg(self, param):
        def create_class():
            class Data:
                name = CapitalString(param)

        def set_attr():
            class Data:
                name = CapitalString("Hello")

            Data().name = param

        self.assertRaises(TypeError, create_class)
        self.assertRaises(TypeError, set_attr)

    @parameterized.expand(
        [
            ("Josh",),
        ]
    )
    def test_capital_string_descriptor_successful_creation(self, param):
        def create_class():
            class Data:
                name = CapitalString(param)

            return Data()

        self.assertIsInstance(create_class().name, CapitalString)

        inst = create_class()
        inst.num = param.upper()
        self.assertEqual(inst.num, param.upper())

    @parameterized.expand(
        [
            "five",
            (-5,),
            (0,),
            (5.0,),
            ((1, 2),),
        ]
    )
    def test_positive_integer_descriptor_wrong_arg(self, param):
        def create_class():
            class Data:
                num = PositiveInteger(param)

        def set_attr():
            class Data:
                num = PositiveInteger(10)

            Data().num = param

        self.assertRaises(TypeError, create_class)
        self.assertRaises(TypeError, set_attr)

    @parameterized.expand(
        [
            (1,),
        ]
    )
    def test_positive_integer_descriptor_successful_creation(self, param):
        def create_class():
            class Data:
                num = PositiveInteger(param)

            return Data()

        self.assertIsInstance(create_class().num, PositiveInteger)

        inst = create_class()
        inst.num = param * 117
        self.assertEqual(inst.num, param * 117)

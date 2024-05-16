import unittest
from hw3 import BlockErrors


class TestBlockErrors(unittest.TestCase):
    def test_error_ignored(self):
        try:
            err_types = {ZeroDivisionError, TypeError}
            with BlockErrors(err_types):
                a = 1 / 0
        except:
            self.fail()

    def test_thrown_above(self):
        with self.assertRaises(TypeError):
            err_types = {ZeroDivisionError}
            with BlockErrors(err_types):
                a = 1 / '0'

    def test_lots_blocs(self):
        try:
            outer_err_types = {TypeError}
            with BlockErrors(outer_err_types):
                inner_err_types = {ZeroDivisionError}
                with BlockErrors(inner_err_types):
                    a = 1 / '0'
        except:
            self.fail()

    def test_child_errors_ignored(self):
        try:
            err_types = {Exception}
            with BlockErrors(err_types):
                a = 1 / '0'
        except:
            self.fail()

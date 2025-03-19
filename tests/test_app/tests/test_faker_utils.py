# -*- coding: utf-8 -*-
from unittest import TestCase
from faker import Faker


class TestFakerUtils(TestCase):
    def test_f(self):
        from dj3fb import faker_utils
        from dj3fb.faker_utils import f

        f.pyint()
        self.assertTrue(isinstance(f, Faker))
        self.assertTrue(f is faker_utils.f)

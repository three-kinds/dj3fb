# -*- coding: utf-8 -*-
import os
import shutil
from django.conf import settings
from django.core.management import call_command
from django.test import TestCase


class T(TestCase):

    def test__run_common__directly(self):
        dir_name = os.path.join(settings.BASE_DIR, 'test_app/factories')
        if os.path.isdir(dir_name):
            shutil.rmtree(dir_name)

        self.assertFalse(os.path.isdir(dir_name))
        call_command('generate_factories')
        self.assertTrue(os.path.isdir(dir_name))

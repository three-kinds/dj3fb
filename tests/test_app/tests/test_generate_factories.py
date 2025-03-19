# -*- coding: utf-8 -*-
import os
import shutil
from django.conf import settings
from django.core.management import call_command
from django.test import TestCase


class T(TestCase):
    def test__run_common__directly(self):
        base_dir = os.path.join(settings.BASE_DIR, "test_app")
        target_dir = os.path.join(base_dir, "factories")
        bak_dir = os.path.join(base_dir, "bak_factories_for_test")

        if os.path.isdir(target_dir):
            shutil.rmtree(target_dir)

        self.assertFalse(os.path.isdir(target_dir))
        shutil.copytree(bak_dir, target_dir)
        self.assertEqual(len([name for name in os.listdir(target_dir) if name.endswith(".py")]), 2)
        call_command("generate_factories")
        self.assertEqual(len([name for name in os.listdir(target_dir) if name.endswith(".py")]), 7)

        shutil.rmtree(target_dir)
        shutil.copytree(bak_dir, target_dir)

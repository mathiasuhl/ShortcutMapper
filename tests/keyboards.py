import sys
import os
import unittest
import glob
import re
import unittest
from utils import BaseTestCase

# import our data common utility
sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(__file__), '..')))
import shmaplib

class TestKeyboardLayout(BaseTestCase):

    def setup(self):
        self.valid_keys = shmaplib.get_all_valid_keynames()
        self.keyboard_templates = glob.glob(os.path.join(shmaplib.DIR_PAGES_KEYBOARDS, '*.html'))

    def test_validate_keyboard_template_keynames(self):
        for p in self.keyboard_templates:
            with open(p, 'r') as template_file:
                contents = template_file.read()
                key_names = re.findall(r'.*button data-key="(.*?)"', contents)
                for keyname in key_names:
                    self.assert_in(keyname, self.valid_keys)

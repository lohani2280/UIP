import os
import sys
import shutil
import unittest
import time
from uiplib import utils


class UtilsTest(unittest.TestCase):

    def test_make_dir(self):
        testdir = os.path.join(os.path.expanduser("~"), '.test')
        utils.make_dir(testdir)
        self.assertTrue(os.path.exists(testdir))
        if sys.platform.startswith('linux'):
            self.assertEqual(oct(os.stat(testdir).st_mode)[-3:], '777')
        shutil.rmtree(testdir)

    def test_get_percentage(self):
        self.assertLessEqual(utils.get_percentage(1, 0, 0), 100)
        self.assertGreaterEqual(utils.get_percentage(1, 0, time.time()), 0)

    def test_check_version(self):
        with self.assertRaises(SystemExit):
            utils.get_current_version = lambda: (0, 0)
            utils.check_version()

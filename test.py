import os
from pathlib import Path
import unittest

from img_files import *


class TestTest(unittest.TestCase):

    def setUp(self):
        self.test_dir = 'img_test'
        self.source_files_path = os.path.join(self.test_dir, 'source_dir')
        os.mkdir(self.test_dir)
        os.mkdir(self.source_files_path)
        for x in range(90, 95):
            Path('{}/{}.png'.format(self.source_files_path, x)).touch()

    def tearDown(self):
        self.clean_files(self.test_dir)
        os.rmdir(self.test_dir)

    def test_renumbers_files_to_start_at_0(self):
        images = os.listdir(self.source_files_path)
        # --before
        self.assertEqual('90.png', images[0])
        self.assertEqual('91.png', images[1])
        self.assertEqual('92.png', images[2])
        self.assertEqual('93.png', images[3])
        self.assertEqual('94.png', images[4])
        # --after
        renumber_file_names(self.source_files_path)
        images = os.listdir(self.source_files_path)
        self.assertEqual('0.png', images[0])
        self.assertEqual('1.png', images[1])
        self.assertEqual('2.png', images[2])
        self.assertEqual('3.png', images[3])
        self.assertEqual('4.png', images[4])

    def test_renumber_files_will_place_renumbered_files_in_specified_location(self):
        new_path = os.path.join(self.test_dir, 'new_files')
        self.assertFalse(os.path.exists(new_path))
        # --create directory and place renumbered files in it
        renumber_file_names(self.source_files_path, destination=new_path)
        self.assertTrue(os.path.exists(new_path))
        images = os.listdir(new_path)
        self.assertEqual('0.png', images[0])
        self.assertEqual('1.png', images[1])
        self.assertEqual('2.png', images[2])
        self.assertEqual('3.png', images[3])
        self.assertEqual('4.png', images[4])

    def test_renumber_will_start_renumbering_at_passed_in_index(self):
        images = os.listdir(self.source_files_path)
        # --before
        self.assertEqual('90.png', images[0])
        self.assertEqual('91.png', images[1])
        self.assertEqual('92.png', images[2])
        self.assertEqual('93.png', images[3])
        self.assertEqual('94.png', images[4])
        # --after
        renumber_file_names(self.source_files_path, start_idx=50)
        images = os.listdir(self.source_files_path)
        self.assertEqual('50.png', images[0])
        self.assertEqual('51.png', images[1])
        self.assertEqual('52.png', images[2])
        self.assertEqual('53.png', images[3])
        self.assertEqual('54.png', images[4])

    def clean_files(self, start_path):
        for item in os.listdir(start_path):
            item_path = os.path.join(start_path, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            try:
                if os.path.isdir(item_path):
                    os.rmdir(item_path)
            except OSError:
                self.clean_files(item_path)
                os.rmdir(item_path)


if __name__ == '__main__':
    unittest.main()

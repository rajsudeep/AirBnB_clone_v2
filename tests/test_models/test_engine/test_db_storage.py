#!/usr/bin/python3
"""test for file storage"""
import unittest
import pep8
from os import getenv
from models.engine.file_storage import DBStorage
import MySQLdb


class TestDBStorage(unittest.TestCase):
    '''this will test the DBStorage'''

    @classmethod
    def setUpClass(self):
        """set up for test"""
        self.db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user='hbnb_test',
            passwd='hbnb_test_pwd',
            db='hbnb_test_db',
            charset='utf8'
        )
        self.cursor = self.db.cursor()
        self.storage = DBStorage()
        self.storage.reload()

    @classmethod
    def teardown(self):
        """at the end of the test this will tear it down"""
        self.cursor.close()
        self.db.close()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'db')
    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'db')
    def test_all(self):
        storage = DBStorage()
        storage.reload()
        old = len(storage.all())
        State(name="CA").save()
        storage.save()
        new = len(storage.all())
        self.assertIs(new, old + 1)

if __name__ == "__main__":
    unittest.main()

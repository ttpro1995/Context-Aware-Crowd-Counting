from unittest import TestCase
from .data_path import ShanghaiTechDataPath
import os


class TestShanghaiTechDataPath(TestCase):

    def test_get(self):
        self.test_root = "unittest_data/mock_shanghaitech"
        self.data = ShanghaiTechDataPath(root=self.test_root)
        print(self.data.get())

    def test_get_a(self):
        self.test_root = "unittest_data/mock_shanghaitech"
        self.data = ShanghaiTechDataPath(root=self.test_root)
        print(self.data.get_a())

    def test_get_b(self):
        self.test_root = "unittest_data/mock_shanghaitech"
        self.data = ShanghaiTechDataPath(root=self.test_root)
        print(self.data.get_b())

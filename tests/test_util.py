from trello_tl.util import align_str_len

import unittest

class TestUtil(unittest.TestCase):

    def test_align_str_len(self):
        s = " (20). MacTalk 《你  (12). 给自己写一份财产备             "
        sr = align_str_len(s, 20)
        print(sr + "|")
        assert True

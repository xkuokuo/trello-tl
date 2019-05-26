from trello_tl.util import align_str_len

import unittest

class TestUtil(unittest.TestCase):

    def test_align_str_len_only_english_char_same_length(self):
        s = "I say i like it."
        res = align_str_len(s, 16)
        self.assertEqual(res, "I say i like it.")

    def test_align_str_len_only_english_char_greater_length(self):
        s = "This is just a dummy english string"
        res = align_str_len(s, 15)
        self.assertEqual(res, "This is just a…")

    def test_align_str_len_only_english_char_shorter_length(self):
        s = "This is just"
        res = align_str_len(s, 15)
        self.assertEqual(res, "This is just   ")

    def test_align_str_len_only_chinese_char_same_length(self):
        s = "吃了么"
        res = align_str_len(s, 6)
        self.assertEqual(res, s)

    def test_align_str_len_only_chinese_char_shorter_length(self):
        s = "吃了么"
        res = align_str_len(s, 7)
        self.assertEqual(res, s + " ")

    def test_align_str_len_only_chinese_char_greater_length(self):
        s = "这是一段发自内心的废话"
        res = align_str_len(s, 14)
        self.assertEqual(res, "这是一段发自 …")

    def test_align_str_len_only_chinese_char_greater_length_2(self):
        s = "这是一段发自内心的废话"
        res = align_str_len(s, 15)
        self.assertEqual(res, "这是一段发自内…")

    def test_align_str_len_only_mix_char_same_len(self):
        s = "我说yes你说no"
        res = align_str_len(s, 13)
        self.assertEqual(res, s)

    def test_align_str_len_only_mix_char_shorter_len(self):
        s = "我说yes你说no"
        res = align_str_len(s, 14)
        self.assertEqual(res, s + " ")

    def test_align_str_len_only_mix_char_greater_len(self):
        s = "我说yes你说no"
        res = align_str_len(s, 12)
        self.assertEqual(res, s + "我说yes你说n…")

from trello_tl.entity import Card

import unittest

class TestEntities(unittest.TestCase):

    def test_card_creation(self):
        card = Card("hihihi")
        print(card.content)
        assert True

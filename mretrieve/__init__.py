from mretrieve import MRetrieve
from mretrieve.indexer import Indexer
import unittest


class TestMRetrieve(unittest.TestCase):
    def __init__(self):
        mretrieve = MRetrieve(Indexer.NONE)

    def test_gettitle(self):
        mretrieve = MRetrieve(Indexer.MANGADEX)
        mretrieve.gettitle()

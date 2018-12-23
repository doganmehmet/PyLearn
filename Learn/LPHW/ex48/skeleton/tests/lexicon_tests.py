from nose.tools import *

from ex48 import lexicon

def test_directories():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])

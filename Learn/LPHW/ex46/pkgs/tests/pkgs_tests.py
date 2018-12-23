from nose.tools import *
import pkgs

def setup():
    print("SETUP")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN", end = '')

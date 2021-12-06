""" Tests for goterm.py """

import os
from subprocess import getstatusoutput, getoutput

PRG = "./goterms.py"


# --------------------------------------------------
def run(terms, expected_file):
    """Run test"""

    assert os.path.isfile(expected_file)
    expected = open(expected_file).read().rstrip()
    rv, out = getstatusoutput(f"{PRG} {terms}")
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def test1():
    """bad test"""

    run("foo", "./expected/foo.out")


# --------------------------------------------------
def test2():
    """good test"""

    run("GO:0005739", "./expected/go.out")


# --------------------------------------------------
def test3():
    """good test file"""

    run("input/input1.txt", "./expected/output1.out")


# --------------------------------------------------
def test4():
    """bad test file"""

    run("input/input2.txt", "./expected/output2.out")

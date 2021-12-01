""" Tests for goterm.py """

import os
from subprocess import getstatusoutput, getoutput

PRG = "./goterms.py"
SAMPLE1 = "input/input1.txt"
SAMPLE2 = "input/input2.txt"


# --------------------------------------------------
def test_exists():
    """Program exists"""

    assert os.path.isfile(PRG)
    print(os.path.isfile(PRG))


# --------------------------------------------------
def run(terms, expected_file):
    """Run test"""

    assert os.path.isfile(expected_file)
    expected = open(expected_file).read().rstrip()
    rv, out = getstatusoutput(f"{PRG}, {terms}")
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

    run("SAMPLE1", "./expected/output1.out")


# --------------------------------------------------
def test4():
    """bad test file"""

    run("SAMPLE2", "./expected/output2.out")

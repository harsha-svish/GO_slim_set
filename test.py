""" Tests for goterm.py """

# pylint:disable=consider-using-with,unspecified-encoding

import os
from subprocess import getstatusoutput, getoutput

PRG = "./goterms.py"
SAMPLE1 = "input/input1.txt"
SAMPLE2 = "input/input2.txt"


# --------------------------------------------------
def run(seq, expected_file):
    """Run test"""

    assert os.path.isfile(expected_file)
    expected = open(expected_file).read().rstrip()
    rv, out = getstatusoutput(f"{PRG} {seq}")
    assert rv == 0
    assert out.strip() == expected


# --------------------------------------------------
def test1():
    """test"""

    run("foo", "./expected/foo.out")


# --------------------------------------------------
def test2():
    """test"""

    run("GO:0005739", "./expected/go.out")


# --------------------------------------------------
def test3():
    """test"""

    run("input/input", "./expected/AAAAA.out")


# --------------------------------------------------
def test4():
    """test"""

    run("ACGT", "./expected/ACGT.out")

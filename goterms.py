#!/usr/bin/env python3
"""
Author : shv <shv@localhost>
Date   : 2021-11-20
Purpose: Find GO terms for Go_basic_obo
"""

import argparse
import os
from goatools import obo_parser


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Go term obtainer",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("goid", metavar="str", help="GO text file")

    args = parser.parse_args()

    if os.path.isfile(args.goid):
        args.goid = open(args.goid).read()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    go_obo = os.path.join(os.getcwd(), "go-basic.obo")
    go_terms = obo_parser.GODag(go_obo)

    for goid in args.goid.splitlines():
        if goid not in go_terms:
            print(f'Invalid GO term "{goid}"')
        else:
            annot = go_terms[goid]
            print(go_terms[goid])


# --------------------------------------------------
if __name__ == "__main__":
    main()

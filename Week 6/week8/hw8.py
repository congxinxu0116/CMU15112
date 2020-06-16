#################################################
# hw8.py
#
# Your name:
# Your andrew id:
#################################################

import cs112_f19_week8_linter
import math, copy

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Functions for you to write
#################################################

#################################################
# Test Functions
#################################################

# ADD YOUR OWN TEST FUNCTIONS!!!

#################################################
# testAll and main
#################################################

def testAll():
    pass

def main():
    cs112_f19_week8_linter.lint()
    testAll()

if __name__ == '__main__':
    main()

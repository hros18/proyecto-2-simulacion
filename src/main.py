from .functions import *
from .system import FuzzyInferenceSystem

#Fuzzyfication

#Linguistic: Funding
inadequate = TrapezoidalFuzzyNumber(0, 0, 2, 3.1)
marginal = TriangularFuzzyNumber(2, 5, 8)
adequate = TrapezoidalFuzzyNumber(6, 7.8, 10, 10)

#Linguistic: Staffing
small = TrapezoidalFuzzyNumber(0, 0, 3, 5.6)
large = TrapezoidalFuzzyNumber(4, 6, 10, 10)

#Linguistic: Risk
low = TrapezoidalFuzzyNumber(0, 0, 3.5,4)
normal = TriangularFuzzyNumber(2, 5, 8)
high = TrapezoidalFuzzyNumber(6, 8, 10, 10)

rules = [
    (adequate , small, low),
    (adequate, large, low),
    (marginal, small, low),
    (marginal, large, normal),
    (inadequate, small, high),
    (inadequate, large, high)
]

if __name__ == '__main__':
    pass
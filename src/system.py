from .aggregation import *
from .set import fuzzySet
import numpy as np

class FuzzyInferenceSystem:

    def __init__(self, rules):
        self.rules = rules
        self.antecedents = []
        self.precedents = []

        for r in rules:
            self.antecedents.append(r[:-1])
            self.precedents.append(r[-1])

    def singleton_params(self, input):
        params = []
        for antc in self.antecedents:
            minimum = 10000000000000000000
            for s,i in zip(antc, inputs):
                minimum = min(minimum, s.func(i))
            params.append(min)
        return params

    def _common(f:fuzzySet,s:fuzzySet):
        left, right = join([f.domain, s.domain])
        maximum = -10000000000000000000
        for x in np.arange(left, sup + 1, 0.1):
            maximum = max(maximum, min(f.func(x), s.func(x)))
        return maximum
    
    def fuzzy_params(self, input):
        params = []
        for antc in self.antecedents:
            maxs = []
            for f,i in zip(antc, input):
                maxs.append(_common(f,i))
            params.append(min(maxs))
        return params
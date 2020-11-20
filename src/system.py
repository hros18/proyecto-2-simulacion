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

    def singleton_params(self, inputs):
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
    
    def fuzzy_params(self, inputs):
        params = []
        for antc in self.antecedents:
            maxs = []
            for f,i in zip(antc, inputs):
                maxs.append(_common(f,i))
            params.append(min(maxs))
        return params

    def _call_mamdani(params):
        pass

    def _call_larsen(params):
        pass

    def call_aggregation(method='mamdani', typ='singleton', inputs):
        if typ == 'singleton':
            params = self.singleton_params(inputs)
        elif type == 'fuzzy':
            params = self.fuzzy_params(inputs)
        else return TypeError('Type not found')

        #TODO finish set of params or degrees

        if method == 'mamdani':
            return self._call_mamdani(params)
        elif method == 'larsen':
            return self._call_larsen(params)
        else return TypeError('Method not found')


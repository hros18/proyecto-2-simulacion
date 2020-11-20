
class FuzzyInferenceSystem:

    def __init__(self, rules):
        self.rules = rules
        self.antecedents = []
        self.precedents = []

        for r in rules:
            self.antecedents.append(r[:-1])
            self.precedents.append(r[-1])

    
class Rule:
    def __init__(self, conditions, conclusion):
        self.conditions = conditions
        self.conclusion = conclusion


class ExpertSystem:
    def __init__(self):
        self.rules = []
        self.facts = set()

    def add_rule(self, rule):
        self.rules.append(rule)

    def add_fact(self, fact):
        self.facts.add(fact)

    def ask_user_for_fact(self, fact):
        response = input(f"Is it true that {fact}? (yes/no): ").strip().lower()
        if response == 'yes':
            self.add_fact(fact)

    def infer(self):
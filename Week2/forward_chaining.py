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
        new_facts = True
        while new_facts:
            new_facts = False
            for rule in self.rules:
                if all(condition in self.facts for condition in rule.conditions) and rule.conclusion not in self.facts:
                    self.facts.add(rule.conclusion)
                    new_facts = True
                    print(f"Inferred: {rule.conclusion}")
                elif any(condition not in self.facts for condition in rule.conditions):
                    for condition in rule.conditions:
                        if condition not in self.facts:
                            self.ask_user_for_fact(condition)
                            break # Ask one fact at a time

# Example usage
if __name__ == "__main__":
    # Create an expert system
    es = ExpertSystem()
    # Add rules
    es.add_rule(Rule(["it is sunny"], "wear sunglasses"))
    es.add_rule(Rule(["it is rainy"], "take an umbrella"))
    es.add_rule(Rule(["it is sunny", "it is the weekend"], "go to beach"))
    # Perform inference
    es.infer()
    # Print final facts
    for fact in es.facts:
        print(fact)


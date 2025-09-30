# Simple Expert System with Rule Base and Inference Engine

# Knowledge base: rules
rules = [
    {
        "conditions": {"fever": "yes", "cough": "yes"},
        "conclusion": "You might have the flu or a chest infection."
    },
    {
        "conditions": {"fever": "yes", "rash": "yes"},
        "conclusion": "You might have measles or another infection with rash."
    },
    {
        "conditions": {"cough": "yes", "fever": "no"},
        "conclusion": "You might have a common cold or allergies."
    },
    {
        "conditions": {"rash": "yes", "fever": "no"},
        "conclusion": "You might have an allergic reaction or skin condition."
    }
]

# Inference engine
def infer(facts):
    for rule in rules:
        match = True
        for key, value in rule["conditions"].items():
            if facts.get(key) != value:
                match = False
                break
        if match:
            return rule["conclusion"]
    return "I can’t determine a condition based on these symptoms. Please consult a doctor."

# Main program
def expert_system():
    print("Welcome to the Expert System!\n")

    # Collect facts
    facts = {}
    facts["fever"] = input("Do you have a fever? (yes/no): ").strip().lower()
    facts["cough"] = input("Do you have a cough? (yes/no): ").strip().lower()
    facts["rash"] = input("Do you have a skin rash? (yes/no): ").strip().lower()

    # Infer conclusion
    result = infer(facts)
    print("\n" + result)
    print("\n--- End of Expert System ---")

if __name__ == "__main__":
    expert_system()
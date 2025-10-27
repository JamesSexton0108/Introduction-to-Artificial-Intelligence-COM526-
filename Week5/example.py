from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import matplotlib.pyplot as plt
from torch.autograd import variable


# #### HELPFUL PROVIDED FUNCTIONS

# Credit: stack overflow - https://stackoverflow.com/questions/70625490/how-to-print-the-printing-full-cpd-from-pgmpy
def print_full(cpd):
    backup = TabularCPD._truncate_strtable
    TabularCPD._truncate_strtable = lambda self, x: x
    print(cpd)
    TabularCPD._truncate_strtable = backup


def print_cpds(bayes_model):
    for cpd in bayes_model.get_cpds():
         print_full(cpd)


def display_model(bayes_model):
    model_daft = model.to_daft()
    model_daft.render()
    plt.show()


# #### END OF HELPFUL PROVIDED FUNCTIONS

model = DiscreteBayesianNetwork([('Winter','Rain'),
                            ('Rain', 'Accident'),
                            ('Rain', 'Roadworks'),
                            ('Accident', 'TrafficJam'),
                            ('Roadworks', 'TrafficJam'),
                            ('RushHour', 'TrafficJam'),
                        ])

# Conditional probability distributions (CPDs)
cpd_winter = TabularCPD(variable='Winter', variable_card=2, values=[[0.75], [0.25]])

cpd_rain = TabularCPD(variable='Rain', variable_card=2,
                      values=[[0.7, 0.6],
                              [0.3, 0.4]],
                      evidence=['Winter'], evidence_card=[2])

cpd_accident = TabularCPD(variable='Accident', variable_card=2, values=[[0.89, 0.11], [0.11, 0.89]], evidence=['Rain'], evidence_card=[2])
cpd_rushhour = TabularCPD(variable='RushHour', variable_card=2, values=[[0.8125], [0.1875]])
cpd_roadworks = TabularCPD(variable='Roadworks', variable_card=2,
                          values=[[0.9, 0.95],
                                  [0.1, 0.05]],
                          evidence=['Rain'], evidence_card=[2])

cpd_trafficjam = TabularCPD(variable='TrafficJam', variable_card=2,
                            values=[[0.95, 0.60, 0.65, 0.30, 0.30, 0.10, 0.15, 0.03],
                                    [0.05, 0.40, 0.35, 0.70, 0.70, 0.90, 0.85, 0.97]],
                            evidence=['Accident', 'Roadworks','RushHour'], evidence_card=[2, 2,2])


# Add CPDs to the model and check validity
model.add_cpds(cpd_roadworks,cpd_winter,cpd_rushhour,cpd_rain, cpd_accident, cpd_roadworks, cpd_trafficjam)
assert model.check_model()

# Inference
inference = VariableElimination(model)
query_result = inference.query(variables=['TrafficJam'], evidence={'Winter': 0, 'RushHour': 0})

print(query_result)
#display_model(model)      # Uncomment to visually see your model
print_cpds(model)         # Uncomment to see the CPD tables for each node



import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

time = ctrl.Antecedent(np.arange(0, 36, 1), 'time')
complexity = ctrl.Antecedent(np.arange(0, 101, 1), 'complexity')
additional_study_hours = ctrl.Consequent(np.arange(0, 12, 0.5), 'additional_study_hours')

# Custom membership functions
time['short'] = fuzz.zmf(time.universe, 10, 12)
time['average'] = fuzz.trapmf(time.universe, [10, 12, 20, 25])
time['long'] = fuzz.smf(time.universe, 20, 32)

complexity['easy'] = fuzz.zmf(complexity.universe, 25, 50)
complexity['medium'] = fuzz.trapmf(complexity.universe, [40, 50, 70, 85])
complexity['hard'] = fuzz.smf(complexity.universe, 70, 80)

additional_study_hours['low'] = fuzz.zmf(additional_study_hours.universe, 0.5, 4)
additional_study_hours['medium'] = fuzz.trapmf(additional_study_hours.universe, [0.5, 4, 8, 10])
additional_study_hours['high'] = fuzz.smf(additional_study_hours.universe, 8, 10)

# Should you wish to view any of the membership functions
time.view()
complexity.view()

rule1 = ctrl.Rule(time['short'] | complexity['hard'], additional_study_hours['high'])
rule2 = ctrl.Rule(complexity['medium'], additional_study_hours['medium'])
rule3 = ctrl.Rule(time['long'] & complexity['easy'], additional_study_hours['low'])

hours_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
hours_sim = ctrl.ControlSystemSimulation(hours_ctrl)

hours_sim.input['time'] = 36
hours_sim.input['complexity'] = 10

hours_sim.compute()

print (hours_sim.output['additional_study_hours'])

# If you want to view the centroid
additional_study_hours.view(sim=hours_sim)
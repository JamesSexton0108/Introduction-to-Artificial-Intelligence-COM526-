from agent import Agent
import utils

class WaterStation(Agent):

    def __init__(self, position):
        super().__init__(position)

    def decide(self, percept):
        for k,v in percept.items():
            print(k,v)
            if utils.is_robot(v):
                return "refill",k,v
        return "wait",None,None


    def act(self, environment):
        cell = self.sense(environment)
        decision,cell,item = self.decide(cell)

        if decision == "refill":
            item.refill()
        else:
            pass


    def __str__(self):
        return '💧'

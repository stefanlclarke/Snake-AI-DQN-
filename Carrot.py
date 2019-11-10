import numpy as np
carrot = 100.
shock = -100.

class GameEnvironment(object):
    def __init__(self):
        self.carrotpos = np.random.randint(2)
        self.game_over = False
    
    def get_boardstate(self):
        ret = np.array([0,0])
        ret[self.carrotpos] = 1
        return ret
    
    def update_boardstate(self, move):
        if move == self.carrotpos:
            reward = carrot
        else:
            reward = shock
        self.carrotpos = np.random.randint(2)
        return reward, False
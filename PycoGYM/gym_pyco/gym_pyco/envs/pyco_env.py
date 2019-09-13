from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import gym
from gym.spaces.discrete import Discrete
from gym.spaces.box import Box
import copy

import numpy as np
from pycolab.engine import Engine


class PycoEnv(gym.Env):


    def __init__(self, game :Engine):
        self.origame = game
        self.game = game
        self.action_space = Discrete(game._nb_action)
        #self.observation_space = Box(low=0, high=255, shape=(game._rows, game._cols, 3), dtype=np.uint8)
        self.observation_space = Box(low=0, high=255, shape=(game._cols , game._rows,),dtype=np.uint8)
        self.reward_range = (0 , float('inf'))

    def reset(self):
        self.game = copy.deepcopy(self.origame)
        obs, reward, discount = self.game.its_showtime()
        return obs

    def step(self,action):
        obs, reward, discount = self.game.play(action)
        isover = self.game._game_over
        return obs, reward, isover, ()

    def render(self,mode='human'):
        print(self.game._board)

    def close(self):
        print('closing')
        game = None





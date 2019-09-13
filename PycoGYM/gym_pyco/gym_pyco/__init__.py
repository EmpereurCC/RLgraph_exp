name="gym_pyco"
from gym.envs.registration import register

register(
    id='gympyco-v1',
    entry_point='gympyco.envs:PycoEnv',
)

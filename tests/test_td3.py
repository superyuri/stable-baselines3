import os

import gym

from torchy_baselines import TD3

def test_pendulum():
    model = TD3('MlpPolicy', 'Pendulum-v0', policy_kwargs=dict(net_arch=[64, 64]), start_timesteps=100, verbose=1)
    model.learn(total_timesteps=500, eval_freq=100)
    model.save("test_save")
    model.load("test_save")
    os.remove("test_save.pth")
import gym

import game
from DQN.dqn_agent import DQNAgent
import torch
import numpy as np


def seed_torch(seed):
    torch.manual_seed(seed)
    if torch.backends.cudnn.enabled:
        torch.backends.cudnn.benchmark = False
        torch.backends.cudnn.deterministic = True


if __name__ == '__main__':
    # environment
    #env_id = "CartPole-v1"
    #env = gym.make(env_id)

    env = game.Game(5, 5)

    seed = 777
    np.random.seed(seed)
    seed_torch(seed)
    obs, info = env.reset(seed=seed)

    # parameters
    num_frames = 10000
    memory_size = 1000
    batch_size = 32
    target_update = 100
    epsilon_decay = 1 / 2000

    agent = DQNAgent(env, memory_size, batch_size, target_update, epsilon_decay)

    agent.train(num_frames)





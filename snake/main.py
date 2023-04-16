import sys
import time

import game
import numpy as np
import matplotlib.pyplot as plt

from snake import display

# Board size
size_x = 5
size_y = 5

tile_state_n = 2  # empty or not empty
actions_n = 4  # UP, DOWN, LEFT, RIGHT
states_n = tile_state_n ** (size_x * size_y)

q_table = np.zeros((states_n, actions_n))

actions = [*range(0, actions_n)]

# Hyperparameters
episodes = 1000  # Total number of episodes
learning_rate = 0.5  # Learning rate
discount_factor = 0.9  # Discount factor
exploration_prob = 1.0
exploration_prob_decay = 0.001
min_exploration_prob = 0.01

print('Q-table before training:')
print(q_table)
print("Q_table: ", "{:.2f}".format(sys.getsizeof(q_table) / (1024 ** 3)), "GB")  # print amount of memory that's allocated to q_table

# Training
for e in range(episodes):
    training_env = game.Game(size_x, size_y)
    state = training_env.get_state()
    done = False

    while not done:
        rand = np.random.uniform(0, 1)

        # If random number < epsilon, take a random action
        if rand < exploration_prob:
            action = np.random.choice(actions)
        else:
            action = np.argmax(q_table[state, :])

        new_state, reward, done = training_env.step(action)

        q_table[state, action] = q_table[state, action] + learning_rate * (reward + discount_factor * np.max(q_table[new_state, :]) - q_table[state, action])

        state = new_state

    # exploration_prob = max(exploration_prob - exploration_prob_decay, 0)  # linear decay
    exploration_prob = max(min_exploration_prob, np.exp(-exploration_prob_decay * e))

print()
print('Q-table after training:')
print(q_table)

episodes = 1

for _ in range(episodes):

    real_env = game.Game(size_x, size_y)

    state = real_env.get_state()
    done = False

    while not done:
        action = np.argmax(q_table[state, :])

        new_state, reward, done = real_env.step(action)
        print(display.display(real_env))

        time.sleep(1)

        state = new_state

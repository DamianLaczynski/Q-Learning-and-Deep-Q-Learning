import sys
import time

import game
import numpy as np
import matplotlib.pyplot as plt

from snake import display

size_x = 3
size_y = 3
tile_state_n = 2  # empty or not empty
actions_n = 4  # UP, DOWN, LEFT, RIGHT
states_n = tile_state_n ** (size_x * size_y)

training_env = game.Game(size_x, size_y)

display.display(training_env)

q_table = np.zeros((states_n, actions_n))

actions = [*range(0, actions_n)]

# Hyperparameters
episodes = 100000  # Total number of episodes
learning_rate = 0.5  # Learning rate
discount_factor = 0.9  # Discount factor
exploration_prob = 1.0  # Amount of randomness in the action selection
exploration_prob_decay = 0.001  # Fixed amount to decrease
min_exploration_prob = 0.01

# List of outcomes to plot
outcomes = []

print('Q-table before training:')
print(q_table)
print("Q_table: ", "{:.2f}".format(sys.getsizeof(q_table) / (1024 ** 3)), "GB")  # print amount of memory that's allocated to q_table

# Training
for e in range(episodes):
    state = training_env.get_state()
    done = False

    # By default, we consider our outcome to be a failure

    # Until the agent gets stuck in a hole or reaches the goal, keep training it
    while not done:
        # Generate a random number between 0 and 1
        rand = np.random.uniform(0, 1)

        # If random number < epsilon, take a random action
        if rand < exploration_prob:
            action = np.random.choice(actions)
        else:
            action = np.argmax(q_table[state, :])

        new_state, reward, done = training_env.step(action)

        # Update Q(s,a)
        q_table[state, action] = q_table[state, action] + learning_rate * (reward + discount_factor * np.max(q_table[new_state, :]) - q_table[state, action])

        # Update our current state
        state = new_state

        # If we have a reward, it means that our outcome is a success

    # Update epsilon
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

    # Until the agent gets stuck in a hole or reaches the goal, keep training it
    while not done:
        action = np.argmax(q_table[state, :])

        new_state, reward, done = real_env.step(action)
        print(display.display(real_env))

        time.sleep(1)

        # Update our current state
        state = new_state

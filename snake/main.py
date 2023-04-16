import sys
import time

import game
import gym
import numpy as np
import matplotlib.pyplot as plt

from snake import display

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     snakeGame = game.Game(10, 10)
#     snakeGame.start()

size_x = 5
size_y = 5
tile_state_n = 2  # empty or not empty
actions_n = 4  # UP, DOWN, LEFT, RIGHT
states_n = tile_state_n ** (size_x * size_y)

snakeGame = game.Game(size_x, size_y)

q_table = np.zeros((states_n, actions_n))

actions = [*range(0, actions_n)]

# Hyperparameters
episodes = 1000  # Total number of episodes
learning_rate = 0.5  # Learning rate
discount_factor = 0.9  # Discount factor
exploration_prob = 1.0  # Amount of randomness in the action selection
exploration_prob_decay = 0.001  # Fixed amount to decrease

# List of outcomes to plot
outcomes = []

print('Q-table before training:')
print(q_table)
print("Q_table: ", "{:.2f}".format(sys.getsizeof(q_table) / (1024 ** 3)), "GB")  # print amount of memory that's allocated to q_table

# Training
for _ in range(episodes):
    state = snakeGame.getBoard()
    done = False

    # By default, we consider our outcome to be a failure
    outcomes.append("Failure")

    # Until the agent gets stuck in a hole or reaches the goal, keep training it
    while not done:
        # Generate a random number between 0 and 1
        rand = np.random.uniform(0, 1)

        # If random number < epsilon, take a random action
        if rand < exploration_prob:
            action = np.random.choice(actions)
        else:
            action = np.argmax(q_table[state, :])

        new_state, reward, done = snakeGame.step(action)

        # Update Q(s,a)
        q_table[state, action] = q_table[state, action] + learning_rate * (reward + discount_factor * np.max(q_table[new_state, :]) - q_table[state, action])

        # Update our current state
        state = new_state

        # If we have a reward, it means that our outcome is a success
        if reward:
            outcomes[-1] = "Success"

    # Update epsilon
    exploration_prob = max(exploration_prob - exploration_prob_decay, 0)

print()
print('===========================================')
print('Q-table after training:')
print(q_table)

# Plot outcomes
plt.figure(figsize=(12, 5))
plt.xlabel("Run number")
plt.ylabel("Outcome")
ax = plt.gca()
ax.set_facecolor('#efeeea')
plt.bar(range(len(outcomes)), outcomes, color="#0A047A", width=1.0)
plt.show()

snakeGame2 = game.Game(size_x, size_y)

for _ in range(episodes):
    state = snakeGame2.getBoard()
    done = False

    # Until the agent gets stuck in a hole or reaches the goal, keep training it
    while not done:
        action = np.argmax(q_table[state, :])

        new_state, reward, done = snakeGame2.step(action)
        print(display.display(new_state))

        time.sleep(1)

        # Update our current state
        state = new_state

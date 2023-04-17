import json
import pickle
import sys
import time

import numpy as np

import game, display


def save_model(data, path):
    with open(path, 'wb') as fp:
        pickle.dump(data, fp)


def load_model(path):
    with open(path, 'rb') as fp:
        model = pickle.load(fp)

    return model


def train_model(size_x, size_y, tile_state_n, actions_n, episodes, learning_rate, discount_factor, exploration_prob_decay):
    states_n = tile_state_n ** (size_x * size_y)

    q_table = dict()

    # q_table = np.zeros((states_n, actions_n))

    actions = [*range(0, actions_n)]

    exploration_prob = 1.0
    min_exploration_prob = 0.01

    progress = 0
    progress_bar_len = 20

    print("Hyperparameters for training:")
    print("%dx%d [%d states]" % (size_x, size_y, tile_state_n))
    print("Learning rate:", learning_rate)
    print("Discount factor:", discount_factor)
    print("Exploration decay:", exploration_prob_decay)
    print("-> Q_table: ", "{:.2f}".format(sys.getsizeof(q_table) / (1024 ** 1)),
          "KB")  # print amount of memory that's allocated to q_table
    print()

    print("Training for %d episodes:" % (episodes))
    print("|" + "-" * progress_bar_len + "|")
    print("|", end='')

    # Training
    for e in range(episodes):

        if progress > episodes / progress_bar_len:
            progress = 0
            print("#", end='')

        progress += 1

        training_env = game.Game(size_x, size_y)
        state = training_env.get_state()
        done = False

        while not done:
            rand = np.random.uniform(0, 1)

            if not (state in q_table):
                q_table[state] = [0] * actions_n

            # If random number < epsilon, take a random action
            if rand < exploration_prob:
                action = np.random.choice(actions)
            else:
                action = np.argmax(q_table[state])

            new_state, reward, done = training_env.step(action)

            if not (new_state in q_table):
                q_table[new_state] = [0] * actions_n

            q_table[state][action] = q_table[state][action] + learning_rate * (
                        reward + discount_factor * np.max(q_table[new_state]) - q_table[state][action])

            state = new_state

        # exploration_prob = max(exploration_prob - exploration_prob_decay, 0)  # linear decay
        exploration_prob = max(min_exploration_prob, np.exp(-exploration_prob_decay * e))

    print("#|")

    return q_table


def play(size_x, size_y, episodes, q_table, show_display):
    scores = []

    for _ in range(episodes):

        real_env = game.Game(size_x, size_y)

        state = real_env.get_state()
        done = False

        while not done:

            if state in q_table:
                action = np.argmax(q_table[state])
            else:
                action = 0

            new_state, reward, done = real_env.step(action)

            if show_display:
                display.display(real_env)
                real_env.get_snake().print_direction()
                time.sleep(1)

            state = new_state

        scores.append(real_env.getScore())

    return scores
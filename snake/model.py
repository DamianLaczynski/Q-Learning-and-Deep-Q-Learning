import json
import sys
import time

import numpy as np
from matplotlib import pyplot as plt

import game, display
from IPython.display import clear_output
from typing import List


def save_model(data, path):
    print("Saving model...")
    np.save(path, data)


def load_model(path):
    print("Loading model...")
    model = np.load(path)

    return model


def train_model(size_x, size_y, tile_state_n, actions_n, episodes: int, learning_rate, discount_factor, exploration_prob_decay):
    states_n = tile_state_n ** (size_x * size_y)

    q_table = np.zeros((states_n, actions_n))

    actions = [*range(0, actions_n)]

    exploration_prob = 1.0
    min_exploration_prob = 0.01

    progress = 0
    progress_bar_len = 20

    print_hiperparateters(size_x, size_y, tile_state_n, learning_rate,
                          discount_factor, exploration_prob_decay, q_table, episodes, progress_bar_len)

    update_cnt = 0
    exploration_probs = []
    scores = []
    score = 0



    # Training
    for e in range(episodes):
        score = 0
        if progress > episodes / progress_bar_len:
            progress = 0
            print("#", end='')

        progress += 1

        training_env = game.Game(size_x, size_y)
        state = training_env.get_state_as_int()
        done = False

        while not done:
            rand = np.random.uniform(0, 1)

            # If random number < epsilon, take a random action
            if rand < exploration_prob:
                action = np.random.choice(actions)
            else:
                action = np.argmax(q_table[state, :])

            new_state, reward, done = training_env.step(action)

            score += reward
            if done:
                scores.append(score)

            q_table[state, action] = q_table[state, action] + learning_rate * (
                        reward + discount_factor * np.max(q_table[new_state, :]) - q_table[state, action])

            state = new_state

        # exploration_prob = max(exploration_prob - exploration_prob_decay, 0)  # linear decay
        exploration_prob = max(min_exploration_prob, np.exp(-exploration_prob_decay * e))
        exploration_probs.append(exploration_prob)




    print("#|")
    _plot(episodes, scores, epsilons=exploration_probs)
    return q_table

scores = []
def play(size_x, size_y, episodes, q_table, show_gameplay):
    for _ in range(episodes):

        real_env = game.Game(size_x, size_y)

        state = real_env.get_state_as_int()
        done = False

        while not done:
            action = np.argmax(q_table[state, :])

            new_state, reward, done = real_env.step(action)

            if show_gameplay:
                real_env.get_snake().print_direction()
                display.display(real_env)
                time.sleep(0.01)

            state = new_state

        scores.append(real_env.get_score())

    return scores


def print_hiperparateters(
        size_x,
        size_y,
        tile_state_n,
        learning_rate,
        discount_factor,
        exploration_prob_decay, 
        q_table,
        episodes,
        progress_bar_len):
    print("Hyperparameters for training:")
    print("%dx%d [%d states]" % (size_x, size_y, tile_state_n))
    print("Learning rate:", learning_rate)
    print("Discount factor:", discount_factor)
    print("Exploration decay:", exploration_prob_decay)
    print("-> Q_table: ", "{:.2f}".format(sys.getsizeof(q_table) / (1024 ** 3)),
          "GB")  # print amount of memory that's allocated to q_table
    print()

    print("Training for %d episodes:" % (episodes))
    print("|" + "-" * progress_bar_len + "|")
    print("|", end='')

def _plot(
        frame_idx: int,
        scores: List[float],
        losses: List[float] = None,
        epsilons: List[float] = None,
):
    """Plot the training progresses."""
    clear_output(True)
    plt.figure(figsize=(18, 5))
    plt.subplot(131)
    plt.title('frame %s. score: %s' % (frame_idx, np.mean(scores[-10:])))
    plt.plot(scores)
    """plt.subplot(132)
    plt.title('loss')
    plt.plot(losses)
    """
    if epsilons is not None:
        plt.subplot(133)
        plt.title('epsilons')
        plt.plot(epsilons)
    plt.show()



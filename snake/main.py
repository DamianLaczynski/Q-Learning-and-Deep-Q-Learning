import numpy as np

import model

q_table = model.train_model(size_x=5, size_y=5, tile_state_n=4, actions_n=4, episodes=100000,
                            learning_rate=0.1, discount_factor=0.01, exploration_prob_decay=0.0001)

model.save_model(q_table, "./model1.npy")

#q_table = model.load_model("./model1.npy")

print(q_table)

scores = model.play(size_x=5, size_y=5, episodes=1, q_table=q_table, show_gameplay=True)

print(np.median(scores))

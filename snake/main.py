import numpy as np

import model

q_table = model.train_model(size_x=20, size_y=20, tile_state_n=2, actions_n=4, episodes=1000,
                            learning_rate=0.1, discount_factor=0.1, exploration_prob_decay=0.01)

model.save_model(q_table, "./model1s.npy")

#q_table = model.load_model("./model1s.npy")

scores = model.play(size_x=20, size_y=20, episodes=1, q_table=q_table, show_display=True)

print(np.median(scores))


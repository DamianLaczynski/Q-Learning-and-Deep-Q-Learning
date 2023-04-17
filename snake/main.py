import model

q_table = model.train_model(size_x=5, size_y=5, tile_state_n=2, actions_n=4, episodes=1000,
                           learning_rate=0.5, discount_factor=0.5, exploration_prob_decay=0.001)

model.save_model(q_table, "./model1.npy")

#q_table = model.load_model("./model1.npy")

model.play(size_x=5, size_y=5, episodes=1, q_table=q_table)

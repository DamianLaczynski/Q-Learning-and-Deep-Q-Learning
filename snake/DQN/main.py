import game
from DQN.dqn_agent import DQNAgent

if __name__ == '__main__':

    # environment
    env = game.Game(5, 5)

    # parameters
    num_frames = 10000
    memory_size = 1000
    batch_size = 32
    target_update = 100
    epsilon_decay = 1 / 2000

    #agent
    agent = DQNAgent(env, memory_size, batch_size, target_update, epsilon_decay)

    #train
    agent.train(num_frames)

    #test
    agent.test()
    #TODO run game with trained model

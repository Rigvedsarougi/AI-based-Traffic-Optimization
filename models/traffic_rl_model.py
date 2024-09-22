import numpy as np

class TrafficRLModel:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.q_table = np.zeros((state_size, action_size))

    def choose_action(self, state):
        if np.random.rand() < 0.1: 
            return np.random.choice(self.action_size)
        else:
            return np.argmax(self.q_table[state])

    def update_q_table(self, state, action, reward, next_state):
        # Q-Learning update rule
        best_next_action = np.argmax(self.q_table[next_state])
        self.q_table[state, action] = (1 - 0.1) * self.q_table[state, action] + \
                                      0.1 * (reward + 0.99 * self.q_table[next_state, best_next_action])

if __name__ == "__main__":
    state_size = 5  
    action_size = 3  
    model = TrafficRLModel(state_size, action_size)
    state = 2
    action = model.choose_action(state)
    print(f"Chosen action: {action}")

import numpy as np

from src.policy.policy import Policy


class RandomPolicy(Policy):
    def __init__(self,
                 action_size: int = 5):
        super(RandomPolicy, self).__init__()
        self.action_size = action_size

    def get_name(self):
        return self.__class__.__name__

    def save(self, filename):
        pass

    def load(self, filename):
        pass

    def act(self, handle: int, state, eps=0.):
        return np.random.choice(self.action_size)

    def step(self, handle: int, state, action, reward, next_state, done):
        pass

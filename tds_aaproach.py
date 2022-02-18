'''import numpy as np

# 19 states (not including the ending state)
NUM_STATES = 19
START = 9
END_0 = 0
END_1 = 20


class ValueFunction:
    def __init__(self, alpha=0.1):
        self.weights = np.zeros(NUM_STATES + 2)
        self.alpha = alpha

    def value(self, state):
        v = self.weights[state]
        return v

    def learn(self, state, delta):
        self.weights[state] += self.alpha * delta

class RandomWalk:

    def __init__(self, start=START, end=False, lmbda=0.4, debug=False):
        self.actions = ["left", "right","up", "down"]
        self.state = start  # current state
        self.end = end
        self.lmbda = lmbda
        self.states = []
        self.reward = 0
        self.debug = debug
        self.rate_truncate = 1e-3

    def chooseAction(self):
        action = np.random.choice(self.actions)
        return action

    def takeAction(self, action):
        new_state = self.state
        if not self.end:
            if action == "left":
                new_state = self.state - 1
            else:
                new_state = self.state + 1
            if new_state in [END_0, END_1]:
                self.end = True
        self.state = new_state
        return self.state

    def giveReward(self, state):
        if state == END_0:
            return -1
        if state == END_1:
            return 1
        # other states
        return 0

def play(self, valueFunc, rounds=100):
    for _ in range(rounds):
        self.reset()
        action = self.chooseAction()

        self.states = [self.state]
        while not self.end:
            state = self.takeAction(action)  # next state
            self.reward = self.giveReward(state)  # next state-reward

            self.states.append(state)

            action = self.chooseAction()
        if self.debug:
            print("total states {} end at {} reward {}".format(len(self.states), self.state, self.reward))

        # end of game, do forward update
        T = len(self.states) - 1
        for t in range(T):
            # start from time t
            state = self.states[t]
            gtlambda = 0
            for n in range(1, T - t):
                # compute G_t:t+n
                gttn = self.gt2tn(valueFunc, t, t + n)
                lambda_power = np.power(self.lmbda, n - 1)
                gtlambda += lambda_power * gttn
                if lambda_power < self.rate_truncate:
                    break

            gtlambda *= 1 - self.lmbda
            if lambda_power >= self.rate_truncate:
                gtlambda += lambda_power * self.reward

            delta = gtlambda - valueFunc.value(state)
            valueFunc.learn(state, delta)

def gt2tn(self, valueFunc, start, end):
    # only the last reward is non-zero
    reward = self.reward if end == len(self.states) - 1 else 0
    state = self.states[end]
    res = reward + valueFunc.value(state)
    return res
'''


import numpy as np

# global variables
BOARD_ROWS = 27
BOARD_COLS = 27
WIN_STATE = (27, 26)
LOSE_STATE = (27, 25)
START = (0, 0)
DETERMINISTIC = True


class State:
    def __init__(self, state=START):
        self.board = np.zeros([BOARD_ROWS, BOARD_COLS])
        self.board[1, 1] = -1
        self.state = state
        self.isEnd = False
        self.determine = DETERMINISTIC

    def giveReward(self):
        if self.state == WIN_STATE:
            return 1
        elif self.state == LOSE_STATE:
            return -1
        else:
            return 0

    def isEndFunc(self):
        if (self.state == WIN_STATE) or (self.state == LOSE_STATE):
            self.isEnd = True

    def nxtPosition(self, action):
        """
        action: up, down, left, right
        -------------
        0 | 1 | 2| 3|
        1 |
        2 |
        return next position
        """
        if self.determine:
            if action == "up":
                nxtState = (self.state[0] - 1, self.state[1])
            elif action == "down":
                nxtState = (self.state[0] + 1, self.state[1])
            elif action == "left":
                nxtState = (self.state[0], self.state[1] - 1)
            else:
                nxtState = (self.state[0], self.state[1] + 1)
            # if next state legal
            if (nxtState[0] >= 0) and (nxtState[0] <= (BOARD_ROWS -1)):
                if (nxtState[1] >= 0) and (nxtState[1] <= (BOARD_COLS -1)):
                    if nxtState != (1, 1):
                        return nxtState
            return self.state

    def showBoard(self):
        self.board[self.state] = 1
        for i in range(0, BOARD_ROWS):
            print('-----------------')
            out = '| '
            for j in range(0, BOARD_COLS):
                if self.board[i, j] == 1:
                    token = '*'
                if self.board[i, j] == -1:
                    token = 'z'
                if self.board[i, j] == 0:
                    token = '0'
                out += token + ' | '
            print(out)
        print('-----------------')


# Agent of player
class Agent:

    def __init__(self):
        self.states = []
        self.actions = ["up", "down", "left", "right"]
        self.State = State()
        self.lr = 0.2
        self.exp_rate = 0.3

        # initial state reward
        self.state_values = {}
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                self.state_values[(i, j)] = 0  # set initial value to 0

    def chooseAction(self):
        # choose action with most expected value
        mx_nxt_reward = 0
        action = ""

        if np.random.uniform(0, 1) <= self.exp_rate:
            action = np.random.choice(self.actions)
        else:
            # greedy action
            for a in self.actions:
                # if the action is deterministic
                nxt_reward = self.state_values[self.State.nxtPosition(a)]
                if nxt_reward >= mx_nxt_reward:
                    action = a
                    mx_nxt_reward = nxt_reward
        return action

    def takeAction(self, action):
        position = self.State.nxtPosition(action)
        return State(state=position)

    def reset(self):
        self.states = []
        self.State = State()

    def play(self, rounds=10):
        i = 0
        while i < rounds:
            # to the end of game back propagate reward
            if self.State.isEnd:
                # back propagate
                reward = self.State.giveReward()
                # explicitly assign end state to reward values
                self.state_values[self.State.state] = reward  # this is optional
                print("Game End Reward", reward)
                for s in reversed(self.states):
                    reward = self.state_values[s] + self.lr * (reward - self.state_values[s])
                    self.state_values[s] = round(reward, 3)
                self.reset()
                i += 1
            else:
                action = self.chooseAction()
                # append trace
                self.states.append(self.State.nxtPosition(action))
                print("current position {} action {}".format(self.State.state, action))
                # by taking the action, it reaches the next state
                self.State = self.takeAction(action)
                # mark is end
                self.State.isEndFunc()
                print("nxt state", self.State.state)
                print("---------------------")

    def showValues(self):
        for i in range(0, BOARD_ROWS):
            print('----------------------------------')
            out = '| '
            for j in range(0, BOARD_COLS):
                out += str(self.state_values[(i, j)]).ljust(6) + ' | '
            print(out)
        print('----------------------------------')


if __name__ == "__main__":
    ag = Agent()
    ag.play(50)
    print(ag.showValues())

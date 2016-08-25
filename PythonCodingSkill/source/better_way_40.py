from collections import namedtuple

Query = namedtuple('Query', ('y', 'x'))

ALIVE = '*'
EMPTY = '-'


def count_neighbors(y, x):
    n_ = yield Query(y + 1, x + 0)  # 북쪽
    ne = yield Query(y + 1, x + 1)  # 북동쪽
    e_ = yield Query(y + 0, x + 1)
    se = yield Query(y - 1, x + 1)
    s_ = yield Query(y - 1, x + 0)
    sw = yield Query(y - 1, x - 1)
    w_ = yield Query(y + 0, x - 1)
    nw = yield Query(y + 1, x - 1)

    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbor_states:
        if state == ALIVE:
            count += 1
    return count

it = count_neighbors(10, 5)
q1 = next(it)
print('1 yield:', q1)
q2 = it.send(ALIVE)
print('2 yield:', q2)
q3 = it.send(ALIVE)
print('3 yield:', q3)
q4 = it.send(ALIVE)
print('4 yield:', q4)
q5 = it.send(ALIVE)
print('5 yield:', q5)
q6 = it.send(ALIVE)
print('6 yield:', q6)
q7 = it.send(ALIVE)
print('7 yield:', q7)
q8 = it.send(ALIVE)
print('8 yield:', q8)

try:
    count = it.send(EMPTY)
except StopIteration as e:
    print('Count: ', e.value)

Transition = namedtuple('Transition', ('y', 'x', 'state'))

def game_logic(state, neighbors):
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY    # 죽음: 너무 적음
        elif neighbors > 3:
            return EMPTY    # 죽음: 너무 많음
    else:
        if neighbors == 3:
            return ALIVE    # 되살아남
    return state


class Grid(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.row = []
        for _ in range(self.height):
            self.row.append([EMPTY] * self.width)

    def __str__(self):
        # ...
        pass

    def query(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def assign(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state




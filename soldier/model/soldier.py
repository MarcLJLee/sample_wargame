import numpy as np
import uuid
import random

class Soldier:
    _uid = ''
    _state = True
    _name = ''
    _ground = [[]]
    _location = {
        'position': np.array([0, 0, 0]),
        'direction': np.array([0, 0, 0])
    }
    _attribute = {
        'speed': 5
    }
    _maxhp = 1
    _hp = 1
    _attack = 1
    _speed = 1
    _sight = 1

    _killcount = 0

    def get_uid(self):
        return self._uid

    def __init__(self, name):
        self._name = name
        self._uid = uuid.uuid4()
        self._location = {
            'position': np.array([0, 0, 0]),
            'direction': np.array([0, 0, 0])
        }
        self.init_attr()

    def init_attr(self):
        self._maxhp = random.randint(5, 10)
        self._attack = random.randint(2, 3)
        self._speed = random.randint(1, 2)
        self._sight = random.randint(1, 3)

    def learn(self):
        print(f'{self._name} getting stronger')
        self._maxhp = self._maxhp + random.randint(2, 4)
        self._attack = self._attack + random.randint(1, 2)
        self._speed = self._speed + random.randint(0, 1)
        self._sight = self._sight + random.randint(0, 1)

    def attack(self, enemey):
        if enemey.attacked(self._attack):
            self.learn()
            self._killcount = self._killcount + 1
            print(f'{self.soldier_str()}')
            return True
        else:
            return False

    def attacked(self, attack):
        if self._hp < attack:
            print(f'{self._hp} / {self._maxhp} attacked by {attack}, {self._name} dead')
            return True
        else:
            self._hp - attack
            if random.randint(0, 20) > 19:
                print(f'{self._name} getting stronger')
                self._attack = self._attack + random.randint(1, 2)

            return False

    def tick(self):
        if self._maxhp > self._hp:
            self._hp = self._hp + 1

    def soldier_str(self):
        return f'soldier {self._name} ({self._uid}) kill: {self._killcount}, attck: {self._attack}, hp: {self._maxhp}, on {self._location.get("position")}'

    def set_ground(self, ground):
        self._ground = ground.get_field()
        position = self._location.get('position')
        position[0] = random.randint(0, len(self._ground) - 1)
        position[1] = random.randint(0, len(self._ground[0]) - 1)

        self._location['position'] = position


    def random_move(self):
        position = self._location.get('position')
        willx = position[0] + random.randint(-2, 2)
        willy = position[1] + random.randint(-2, 2)

        if willx < 0: willx = 0
        if willx > len(self._ground) - 1: willx = len(self._ground) - 1

        if willy < 0: willy = 0
        if willy > len(self._ground[0]) - 1: willy = len(self._ground[0]) - 1

        position[0] = willx
        position[1] = willy
        self._location['position'] = position
        self.tick()

    def get_location(self):
        return self._location

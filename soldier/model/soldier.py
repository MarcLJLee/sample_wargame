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

    _skill = []

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
        self._skill = []
        self.init_attr()

    def exchamp(self, name, uid, attack, maxhp, sight, speed, skill):
        self._name = name
        self._uid = uid
        self._attack = round(attack/20)
        self._maxhp = round(maxhp/20)
        self._sight = round(sight/20)
        self._speed = round(speed/10)
        self._skill = skill
        self._skill.append('ExChamp')

        print(f'ex-champion on the ground : {self.soldier_str()}')


    def set_skill(self, prob, skill_name):
        if random.randint(0, prob) > prob - 1:
            self._skill.append(skill_name)

    def has_skill(self, skill):
        try:
            value_index = self._skill.index(skill)
        except:
            value_index = -1
        return value_index > -1

    def init_attr(self):
        self._maxhp = random.randint(5, 10)
        self._attack = random.randint(2, 3)
        self._speed = random.randint(1, 2)
        self._sight = random.randint(2, 5)

        self.set_skill(500, 'Newtype')
        self.set_skill(100, 'Gosu')
        self.set_skill(100, 'Chaser')
        # self.set_skill(10, 'Coward')
        self.set_skill(300, 'Genius')
        self.set_skill(500, 'Luckyboy')
        self.set_skill(500, 'Master')
        self.set_skill(1000, 'Saiyan')
        self.set_skill(1000, 'Absorber')

        if self.has_skill('Newtype'):
            print(f'{self._name} is Newtype')
            self._sight = self._sight + random.randint(2, 5)
            self._speed = self._speed + random.randint(1, 2)

        if self.has_skill('Gosu'):
            print(f'{self._name} is Gosu')
            self._attack = random.randint(2, 3)
            self._maxhp = random.randint(5, 10)

        if self.has_skill('Luckyboy'):
            self._speed = self._speed + random.randint(3, 5)

        if self.has_skill('Master'):
            print(f'{self._name} is Master')
            self._maxhp = random.randint(50, 100)
            self._sight = self._sight + random.randint(10, 30)
            self._speed = self._speed + random.randint(10, 30)

        if self.has_skill('Saiyan'):
            print(f'{self._name} is Saiyan')
            self._maxhp = random.randint(50, 100)
            self._sight = self._sight + random.randint(10, 30)
            self._speed = self._speed + random.randint(20, 30)

        if self.has_skill('Absorber'):
            print(f'{self._name} is Absorber')

    def learn(self):
        # print(f'{self._name} getting stronger')
        self._maxhp = self._maxhp + random.randint(2, 4)
        self._attack = self._attack + random.randint(2, 4)
        self._speed = self._speed + random.randint(0, 1)
        self._sight = self._sight + random.randint(0, 1)

        if self.has_skill('Genius'):
            self._attack = self._attack + random.randint(1, 3)
            self._sight = self._sight + random.randint(0, 1)

        if self.has_skill('Newtype'):
            self._attack = self._attack + random.randint(1, 4)
            self._sight = self._sight + random.randint(2, 3)

        if self.has_skill('Gosu'):
            self._maxhp = self._maxhp + random.randint(2, 4)
            self._attack = self._attack + random.randint(1, 2)
            self._sight = self._sight + random.randint(1, 2)
            self._speed = self._speed + random.randint(2, 3)

        if self.has_skill('Chaser'):
            self._sight = self._sight + random.randint(0, 4)

        if self.has_skill('ChoSaiyan'):
            if self._speed > 150:
                self._speed = 150
        if self.has_skill('Saiyan'):
            if self._speed > 80:
                self._speed = 80
        elif self.has_skill('Chaser'):
            if self._speed > 50:
                self._speed = 50
        elif self.has_skill('Gosu'):
            if self._speed > 45:
                self._speed = 45
        elif self._speed > 40:
            self._speed = 40

    def get_skills(self):
        return self._skill

    def get_attack(self):
        return self._attack

    def get_hp(self):
        return self._maxhp

    def get_sight(self):
        return self._sight

    def get_speed(self):
        return self._speed

    def attack(self, enemy):
        if self.has_skill('Absorber') and random.randint(0, 2) > 1:
            print('Absorber acting')
            self._attack = self._attack + random.randint(1, enemy.get_attack())
            self._maxhp = self._maxhp + random.randint(1, enemy.get_hp())
            self._sight = self._maxhp + random.randint(1, enemy.get_sight())
            self._speed = self._maxhp + random.randint(1, enemy.get_speed())

            for skill in enemy.get_skills():
                if not self.has_skill(skill):
                    self._skill.append(skill)

        if enemy.attacked(self._attack):
            self.learn()
            self._killcount = self._killcount + 1
            if self._killcount > 10 and self._killcount % 10 == 0:
                print(f'{self.soldier_str()}')
            return True
        else:
            return False

        if enemy.has_skill('Gosu') and random.randint(0, 1) > 0:
            print(f'{enemy.get_name()} returns to enemy')
            enemy.attack(self)

    def attacked(self, attack):
        if self.has_skill('Newtype'):
            if random.randint(0, 100) < 70:
                if random.randint(0, 20) > 19:
                    # print(f'{self._name} getting stronger')
                    self._attack = self._attack + random.randint(1, 2)
                return False
        elif self.has_skill('Gosu'):
            if random.randint(0, 100) < 50:
                if random.randint(0, 20) > 19:
                    # print(f'{self._name} getting stronger')
                    self._attack = self._attack + random.randint(1, 2)
                return False
        elif self.has_skill('Luckyboy'):
            if random.randint(0, 100) < 95:
                if random.randint(0, 20) > 19:
                    # print(f'{self._name} getting stronger')
                    self._attack = self._attack + random.randint(1, 2)
                return False
        else:
            if random.randint(0, 100) < 20:
                if random.randint(0, 20) > 19:
                    # print(f'{self._name} getting stronger')
                    self._attack = self._attack + random.randint(1, 2)
                return False

        if self._hp < attack:
            # if len(self._skill) > 0 or self._killcount > 5:
            if self.has_skill('Saiyan') and random.randint(0, 2) > 0:
                print(f'{self._name} feels angry!')
                self._maxhp = self._maxhp + random.randint(1, attack)
                self._attack = self._attack + random.randint(1, attack)
                self._sight = self._sight + random.randint(2, 4)
                self._speed = self._speed + random.randint(1, 6)
                if random.randint(0, 5) > 4:
                    print(f'{self._name} is ChoSaiyan!')
                    self._skill.pop(self._skill.index('Saiyan'))
                    self._skill.append('ChoSaiyan')
                    self._maxhp = self._maxhp + random.randint(10, 80)
                    self._attack = self._attack + random.randint(10, 80)
                    self._sight = self._sight + random.randint(20, 40)
                    self._speed = self._speed + random.randint(30, 60)

                return False
            elif self.has_skill('ChoSaiyan') and random.randint(0, 4) > 0:
                print(f'{self._name} feels angry!')
                self._maxhp = self._maxhp + random.randint(round(attack/2), attack*2)
                self._attack = self._attack + random.randint(round(attack/2), attack*2)
                return False

            if self._killcount > 5:
                print(f'dead {self.soldier_str()}')
            # print(f'{self._hp} / {self._maxhp} attacked by {attack}, {self._name} dead')
            return True
        else:
            self._hp - attack
            if random.randint(0, 20) > 19:
                # print(f'{self._name} getting stronger')
                self._attack = self._attack + random.randint(1, 2)
                if self.has_skill('Saiyan'):
                    print(f'{self._name} feels angry')
                    self._maxhp = self._maxhp + random.randint(2, 20)
                    self._attack = self._attack + random.randint(1, 20)
                    self._sight = self._sight + random.randint(1, 2)
                    self._speed = self._speed + random.randint(2, 3)
                elif self.has_skill('ChoSaiyan'):
                    print(f'{self._name} feels angry')
                    self._maxhp = self._maxhp + random.randint(round(attack/2), attack*2)
                    self._attack = self._attack + random.randint(round(attack/2), attack*2)
                    self._sight = self._sight + random.randint(1, 2)
                    self._speed = self._speed + random.randint(2, 3)

            return False

    def tick(self):
        if self._maxhp > self._hp:
            self._hp = self._hp + 1

        if self.has_skill('Genius') and random.randint(0, 100) > 98:
            self.learn()
        elif random.randint(0, 100) > 99:
            self.learn()

    def soldier_str(self):
        return f'soldier {self._name} ({self._uid}) kill: {self._killcount}, attck: {self._attack}, hp: {self._maxhp}, sight: {self._sight}, speed: {self._speed}, on {self._location.get("position")}, {self._skill}'

    def get_name(self):
        return f'{self._name}'

    def set_ground(self, ground):
        self._ground = ground.get_field()
        position = self._location.get('position')
        position[0] = random.randint(0, len(self._ground) - 1)
        position[1] = random.randint(0, len(self._ground[0]) - 1)

        self._location['position'] = position

    def seeking(self, soldiers):
        my_location = self._location.get('position')
        for enemy in soldiers:
            if enemy.get_uid() != self.get_uid():
                enemy_location = enemy.get_location().get("position")
                if my_location[0] - self._sight <= enemy_location[0] and my_location[0] + self._sight >= enemy_location[0] and my_location[1] - self._sight <= enemy_location[1] and my_location[1] + self._sight >= enemy_location[1]:
                    # print(f'{self._name} is found, {enemy.get_name()}')
                    return enemy_location

        return None

    def action(self, soldiers):
        if self.has_skill('Chaser') or random.randint(0, 2) > 0:
            target_location = self.seeking(soldiers)
            if target_location is not None:
                self.move_to(target_location)
            else:
                self.random_move()
        else:
            self.random_move()

    def move_to(self, location):
        position = self._location.get('position')
        if abs(position[0] - location[0]) > self._speed:
            if position[0] < location[0]:
                willx = position[0] + self._speed
            else:
                willx = position[0] - self._speed
        else:
            willx = position[0] = location[0]

        if abs(position[1] - location[1]) > self._speed:
            if position[1] < location[1]:
                willy = position[1] + self._speed
            else:
                willy = position[1] - self._speed
        else:
            willy = position[1] = location[1]

        position[0] = willx
        position[1] = willy

        self._location['position'] = position
        self.tick()

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

    def get_champ(self):
        return f"'{self._name}', '{self._uid}', {self._attack}, {self._maxhp}, {self._sight}, {self._speed}, {self._skill}"

import numpy as np


class Ground:
    _width = 800
    _height = 800

    _field = []
    _objects = []

    _frame = 0

    def __init__(self):
        self._field = np.zeros((self._height, self._width))

    def get_field(self):
        return self._field

    def render(self):
        self._frame = self._frame + 1
        self._field = np.zeros((self._height, self._width))
        for obj in self._objects:
            location = obj.get_location()
            position = location.get('position')
            self._field[position[0], position[1]] = 1

        for obj in self._objects:
            for enemy in self._objects:
                if obj.get_uid() != enemy.get_uid():
                    my_location = obj.get_location().get("position")
                    enemy_location = enemy.get_location().get("position")
                    if my_location[0] == enemy_location[0] and my_location[1] == enemy_location[1]:
                        if len(self._objects) < 5:
                            print(f'{obj.get_name()} attacks {enemy.get_name()}')
                        if obj.attack(enemy):
                            self._objects.remove(enemy)
                            if len(self._objects) < 10:
                                print(f'Rank #{len(self._objects) +1} : {enemy.soldier_str()}')
                            if len(self._objects) % 50 == 0:
                                print(f'#{self._frame} : {len(self._objects)} soldiers on field.')

        if self._frame % 300 == 0:
            print(f'#{self._frame} : {len(self._objects)} soldiers on field.')

        # print(f'{self._field}')

    def add_object(self, soldier):
        self._objects.append(soldier)

    def get_objects(self):
        return self._objects

    def check_champ(self):
        if len(self._objects) == 1:
            print(f'champion comes {self._objects[0].soldier_str()}')
            print(f'{self._objects[0].get_champ()}')
            return True
        else:
            return False

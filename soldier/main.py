from soldier.model import ground, soldier
from faker import Faker
import time

print('In Progress')
_mainground = ground.Ground()
_soldiers = []
_faker = Faker()

for i in range(0, 500):
    new_soldier = soldier.Soldier(_faker.name())
    new_soldier.set_ground(_mainground)
    _soldiers.append(new_soldier)
    _mainground.add_object(_soldiers[i])

while True:
    objects = _mainground.get_objects()
    for soldier_data in objects:
        soldier_data.action(objects)

    _mainground.render()
    if _mainground.check_champ():
        break
    # time.sleep(0.1)

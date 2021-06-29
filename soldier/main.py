from soldier.model import ground, soldier
from faker import Faker
import time

print('In Progress')
_mainground = ground.Ground()
_soldiers = []
_faker = Faker()

# ex_champ
ex_champ = soldier.Soldier('Exchamp')
ex_champ.exchamp('Amanda Simpson', '66f4dc49-03fb-4d91-a9aa-ca73fc3a38f3', 566, 566, 448, 50, 20, ['Chaser'])
ex_champ.set_ground(_mainground)

_soldiers.append(ex_champ)
_mainground.add_object(_soldiers[0])

for i in range(0, 500):
    new_soldier = soldier.Soldier(_faker.name())
    new_soldier.set_ground(_mainground)
    _soldiers.append(new_soldier)
    _mainground.add_object(_soldiers[len(_soldiers) - 1])

while True:
    objects = _mainground.get_objects()
    for soldier_data in objects:
        soldier_data.action(objects)

    _mainground.render()
    if _mainground.check_champ():
        break
    # time.sleep(0.1)

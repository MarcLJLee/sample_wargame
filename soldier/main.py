from soldier.model import ground, soldier
from faker import Faker
import time

print('In Progress')
_mainground = ground.Ground()
_soldiers = []
_faker = Faker()

# ex_champ
ex_champ = soldier.Soldier('Exchamp')
ex_champ.exchamp('James Morris', 'a5c91147-78ca-41ec-b3fe-79cec76d2329', 583, 566, 486, 50, ['Chaser'])
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

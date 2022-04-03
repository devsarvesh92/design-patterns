from random import randint

from chair_factory import ChairFactory

chair_types = ['b', 's', 'm']
random_chair = chair_types[randint(0, 3)]
chair = ChairFactory().get_chair(random_chair)
print(chair.display())

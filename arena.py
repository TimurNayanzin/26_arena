import random

thing_names = ['кольцо', 'сапоги', 'перчатки']

person_names = ['aa', 'bb', 'cc']


class Thing:
    def __init__(self, name, protection, attack, health):
        """Initialize instance."""
        self.name = name
        self.protection = protection
        self.attack = attack
        self.health = health


class Person:
    def __init__(self, name, hp, base_attack, base_protection):
        """Initialize instance."""
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_protection = base_protection

#       def set_things(things)

#       def sub_life()


class Paladin(Person):
    def __init__(self, name, hp, base_attack, base_protection):
        """Initialize instance."""
        super().__init__(name, hp, base_attack, base_protection)
        self.hp = hp * 2
        self.base_protection = base_protection * 2


class Warrior(Person):
    def __init__(self, name, hp, base_attack, base_protection):
        """Initialize instance."""
        super().__init__(name, hp, base_attack, base_protection)
        self.base_attack = base_attack * 2


things = []
for _ in range(random.randint(10, 20)):
    name = random.choice(thing_names)
    protection = random.random() / 10
    attack = random.random()
    health = random.random()
    things.append(Thing(name, protection, attack, health))

persons = []
for _ in range(10):
    name = random.choice(person_names)
    hp = random.random() * 100
    base_attack = random.random() * 10
    base_protection = random.random() * 1
    if random.choice((0, 1)):
        persons.append(Paladin(name, hp, base_attack, base_protection))
    else:
        persons.append(Warrior(name, hp, base_attack, base_protection))

print(things)
print(persons)

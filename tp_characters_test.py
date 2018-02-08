import math
import random

class Character(object):

    def __init__(self, name, MAX_hp, base_speed, priority="Normal", mindset_multiplier=1.0, move=''):
        self.MAX_hp = MAX_hp
        self.base_hp = MAX_hp
        self.base_speed = base_speed
        self.priority = priority
        self.mindset_multiplier = mindset_multiplier
        self.name = name

        self.move_pool = {}

    def __repr__(self):
        return "{self.name} - {self.base_hp} / {self.MAX_hp} HP, {self.mindset_multiplier} mindset, {self.base_speed} speed".format(self=self)

class Move(object):

    def __init__(self, description="", self_damage=0, damage=0, mindset_multiplier=1.0, opponent_mindset_multiplier=1.0, speed_boost=0, opponent_speed_boost=0, priority="Normal"):
        self.__doc__ = description
        self.self_damage = self_damage
        self.damage = damage
        self.mindset_multiplier = mindset_multiplier
        self.opponent_mindset_multiplier = opponent_mindset_multiplier
        self.speed_boost = speed_boost
        self.opponent_speed_boost = opponent_speed_boost
        self.priority = priority

    def __call__(self, user=None, opponent=None):
        if user is not None:
            user.priority = self.priority
            user.mindset_multiplier *= self.mindset_multiplier
            user.base_speed += self.speed_boost
            user.base_hp -= math.floor(self.self_damage *
                                           user.mindset_multiplier)
            user.base_hp = min(max(user.base_hp, 0), user.MAX_hp)

        if opponent is not None:
            opponent.mindset_multiplier *= self.opponent_mindset_multiplier
            opponent.base_speed += self.speed_boost
            opponent.base_hp -= math.floor(self.damage *
                                           user.mindset_multiplier)
            opponent.base_hp = min(max(opponent.base_hp, 0), opponent.MAX_hp)

class Berserker(Character):

    def __init__(self):
        Character.__init__(self, "jan pi pakala nasa", 250, 75)
        self.move_pool = {"1": Move(" utala lili luka - tenpo lili la, ona li pakala 30 e jan ante.",
                                    damage=30, priority="Fast"),
                          "2": Move(" utala sijelo - tenpo suli la, ona li pakala 50 e jan ante li pakala 30 e sijelo sama",
                                    self_damage=30, damage=50, priority="Slow"),
                          "3": Move(" wawa sewi - wawa sama li kama sewi ( x 1.25 ).",
                                    mindset_multiplier=1.25)}

class Philosopher(Character):

    def __init__(self):
        Character.__init__(self, "jan pi sona mute", 220, 80)
        self.move_pool = {"1": Move(" sona pona - ona li pona 30 e sijelo sama",
                                    self_damage=-30),
                          "2": Move(" toki mute pi ike mute - ona li pakala 40 e jan ante.",
                                    damage=40),
                          "3": Move(" sona sewi - sona ona li kama sewi. (x 1.35)",
                                    mindset_multiplier=1.35)}

class Trickster2(Character):

    class Bag_o_tricks(Move):

        def __call__(self, user, opponent):
            self.damage = random.uniform(-1, 1) * 100
            self.self_damage = random.uniform(-1, 1) * 50
            Move.__call__(self, user, opponent)

    class Swapper(Move):

        def __call__(self, user, opponent):
            user.priority = self.priority
            user.base_hp, opponent.base_hp = opponent.base_hp, user.base_hp
            user.MAX_hp, opponent.MAX_hp = opponent.MAX_hp, user.MAX_hp

    def __init__(self):
        Character.__init__(self, "jan pi powe nasa", 175, 100)
        self.move_pool = {"1": Trickster2.Bag_o_tricks(" nasin nasa - ona li ante e [-100,100] pi jan ante e [-50,50] pi jan sama."),
                          "2": Move(" ike nasa - ona li ike e lawa pi jan ante (x 0.8) li pona e lawa sama (x 1.05)",
                                    mindset_multiplier=1.05, opponent_mindset_multiplier=0.8),
                          "3": Trickster2.Swapper(" sijelo ante - ona li ante sama e sijelo pi jan ante e sijelo pi jan sama.")}

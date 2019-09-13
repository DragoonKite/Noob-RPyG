from colorama import init, Fore
from Skills_And_Magic import *
init(strip=False)

class bcolors:
    HEADER = '\033[95n'
    OKBLUE = '\033[34m'
    OKGREEN = '\033[32m'
    WARNING = '\033[93n'
    FAIL = '\033[31m'
    ENDC = '\033[39m'


class Character:

    def __init__(self, name, item, lvl=1, base_hp=100, base_mp=35, base_atk=10, base_df=7, exp=0):
        self.lvl = lvl
        self.maxhp = base_hp
        self.hp = base_hp
        self.maxmp = base_mp
        self.mp = base_mp
        self.atkl = base_atk - 2
        self.atkh = base_atk + 2
        self.df = base_df
        self.exp = exp
        self.actions = ["Attack", "Skill", "Items", "Quit"]
        self.item = item
        self.name = name

    def name(self):
        return self.name + " is your name, adventurer"

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_lvl(self):
        return self.lvl

    def choose_action(self): #displays options for player
        i = 1
        print("\n" + self.name )
        print (bcolors.OKBLUE + "Actions" + bcolors.ENDC)
        for item in self.actions:
            print("      " + str(i) + ":", item)
            i += 1


class Knight(Character):
    def __init__(self, name, skills=["Block", "Cover", "Shiled Bash"], job_hp=100, job_mp=15, job_atk=5, job_df=7):
        Character.__init__(self, name, item=["Kite Shield", "Bastard Sword"])
        self.skills = skills
        self.hp += job_hp
        self.maxhp += job_hp
        self.mp += job_mp
        self.maxmp += job_mp
        self.atkh += job_atk
        self.atkl += job_atk
        self.df += job_df

    def get_self(self):
            return Character.name(self)

    def check_bag(self):
        i = 0
        for itm in self.item:
            print(str(i+1) + ") " + itm)
            i += 1

    def take_action(self):
        Character.choose_action(self)

    def use_skill(self):
        i = 0
        for skill in self.skills:
            print(str(i + 1) + ") " + skill)
            i += 1


class Soldier(Character):
    def __init__(self, name, skills=[], job_hp=90, job_mp=20, job_atk=7, job_df=5):
        Character.__init__(self, name, item=["Lance", "Round Shield"])
        self.skills = []
        self.skill_check()
        self.hp += job_hp
        self.maxhp += job_hp
        self.mp += job_mp
        self.maxmp += job_mp
        self.atkh += job_atk
        self.atkl += job_atk
        self.df += job_df

    def get_self(self):
            return Character.name(self)

    def check_bag(self):
        i = 1
        for itm in self.item:
            print(str(i) + ") " + str(itm))
            i += 1

    def take_action(self):
        Character.choose_action(self)

    def use_skill(self):
        i = 0
        for skill in self.skills:
            print(str(i + 1) + ") " + skill.name)
            i += 1

    def skill_check(self):
        for option in skill_tree:
            if self.atkl > option.minimum_stat:
                self.skills.append(option)
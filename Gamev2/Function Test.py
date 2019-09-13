import simplejson as json
import re
import os
from Class import *
from Items import *
from Skills_And_Magic import *
from colorama import init, Fore
init(strip=False)



'''if os.path.isfile("./game.json") and os.stat("./game.json").st_size != 0:
    old_file=open("./game.json","r+")
    data= json.loads(old_file.read())

    player=Person(data[0]["maxhp"], data[0]["maxmp"], int(data[0]["atkh"]-10), data[0]["def"], magic)
    player.hp = data[0]["hp"]
    player.mp = data[0]["mp"]

    enemy = Person(data[1]["maxhp"], data[1]["maxmp"], int(data[1]["atkh"] - 10), data[1]["def"], magic)
    enemy.hp = data[1]["hp"]
    enemy.mp = data[1]["mp"]

    print("Player Stats:", "HP:", player.hp, "/", player.maxhp, "MP:", player.mp,
    "/", player.maxmp, "Attack:", "low-", player.atkl, "high-", player.atkh,
    "Defense:", player.df)
    print("Enemy Stats:", "HP:", enemy.hp, "Attack:", enemy.atkl, enemy.atkh, "Defense:", enemy.df)
else:
    old_file = open("./game.json", "w+")
    player = Person(460, 65, 60, 34, magic)
    enemy = Person(1200, 65, 45, 25, magic)

    print("No file found, creating new file")
    print("Player Stats:", "HP:", player.hp, "MP:", player.mp, "Attack:", "low-", player.atkl, "high-", player.atkh,
          "Defense:", player.df)
    print("Enemy Stats:", "HP:", enemy.hp, "Attack:", enemy.atkl, enemy.atkh, "Defense:", enemy.df)'''

class bcolors:
    HEADER = '\033[95n'
    OKBLUE = '\033[34m'
    OKGREEN = '\033[32m'
    WARNING = '\033[93n'
    FAIL = '\033[31m'
    ENDC = '\033[39m'

Deadron = Knight("Deadron")
Kotatsu = Soldier("Kotatsu")
print(Kotatsu.use_skill())
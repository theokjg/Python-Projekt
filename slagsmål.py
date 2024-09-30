import random
playera = input("what is player a name? ")

playerA = 100
playerB = 100


while (playerA >0 and playerB >0):
    damage = random.randint(10,20)
    damage2 = random.randint(10,20)

    print(playera, "hits playerB with ", damage, "damage points")
    playerB = playerB - damage
    print("playerB hits", playera, "with", damage2, "damage points")
    playerA = playerA - damage

else:
    print("Game over")

if(playerA > 0):
    print(playera, "wins")

else:
    print("playerB wins")
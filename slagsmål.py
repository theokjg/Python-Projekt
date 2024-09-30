import random
namna = input("what is player a name? ")

playera = 100
playerb = 100


while (playera >0 and playerb >0 ):
    damage = random.randint(10,20)
    playera -= damage
    print (damage)
    print (namna,  "hits playerb with ", damage, "damage points")
    if(playera <= 0):
        print("playerb wins")
        break
      
    damage = random.randint(10,20)
    playerb -= damage
    print("playerB hits", namna, "with", damage, "damage points")
    if (playerb <= 0):
        print(namna, "wins")
        break


else:
    print("tied")




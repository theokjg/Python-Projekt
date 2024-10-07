Rättsvar = 0
Rsvar1 = "2"

print ("Vilket är Joels favorit fotbollslag?")
print ("1: Hammarby")
print ("X: AIK")
print ("2: Djurgården")

svar1 = input()

if(svar1 == Rsvar1):
    print ("Rätt svar")
    Rättsvar +=1
else:print ("Fel svar")

Rsvar2 = "X"

print ("Vad är Joels etnicitet?")
print ("1: Svensk")
print ("X: Kines")
print ("2: Thailändare")

svar2 = input()

if(svar2 == Rsvar2):
    print ("Rätt svar")
    Rättsvar +=1
else:print ("Fel svar")

Rsvar3 = "X"

print ("Vad är Joels favoritspel?")
print ("1: Football manager")
print ("X: Fortnite")
print ("2: Roblox")

svar3 = input()

if(svar3 == Rsvar3):
    print ("Rätt svar")
    Rättsvar +=1
else:print ("Fel svar")


print (f"Du fick {Rättsvar} rätt")
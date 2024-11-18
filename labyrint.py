def entrance(has_key):
    print("Du är i entrance. Det är en enkel hall med vita väggar och ett trägolv som knarrar under fötterna.")
    print("Härifrån kan du gå till flera olika rum.")
    print("1. Gå till living room")
    print("2. Gå till sunshine room")
    print("3. Gå till drafty room")
    choice = input("Ditt val (1/2/3): ")
    if choice == "1":
        living_room(has_key)
    elif choice == "2":
        sunshine_room(has_key)
    elif choice == "3":
        drafty_room(has_key)
    else:
        print("Ogiltigt val. Försök igen.")
        entrance(has_key)

def living_room(has_key):
    print("Du är i living room. Det är ett varmt och mysigt rum med en mjuk matta och en gammal soffa.")
    print("Ett fönster släpper in svagt ljus och gör rummet hemtrevligt.")
    print("1. Gå till entrance")
    print("2. Gå till drafty room")
    choice = input("Ditt val (1/2): ")
    if choice == "1":
        entrance(has_key)
    elif choice == "2":
        drafty_room(has_key)
    else:
        print("Ogiltigt val. Försök igen.")
        living_room(has_key)

def drafty_room(has_key):
    print("Du är i drafty room. Det är ett kallt och dragigt rum med spruckna väggar och ett golv täckt av damm.")
    print("Du hör vinden vina genom springorna.")
    if has_key:
        print("Du ser ett gömt nyckelhål i väggen.")
        print("1. Använd nyckeln och gå igenom dörren (avsluta spelet)")
    print("2. Gå till living room")
    print("3. Gå till sunshine room")
    print("4. Gå till entrance")
    if not has_key:
        print("5. Avsluta spelet")
    choice = input("Ditt val: ")
    if has_key and choice == "1":
        print("Du använder nyckeln och öppnar en hemlig dörr. Du har klarat spelet! Grattis!")
    elif choice == "2":
        living_room(has_key)
    elif choice == "3":
        sunshine_room(has_key)
    elif choice == "4":
        entrance(has_key)
    elif not has_key and choice == "5":
        print("Spelet avslutas. Hejdå!")
    else:
        print("Ogiltigt val. Försök igen.")
        drafty_room(has_key)

def sunshine_room(has_key):
    print("Du är i sunshine room. Det är ett ljust och luftigt rum med stora fönster som släpper in solljus.")
    print("Väggarna är målade i en varm gul nyans som fyller rummet med energi.")
    if not has_key:
        print("På ett bord ser du en glänsande nyckel.")
        print("1. Ta nyckeln")
    print("2. Gå till entrance")
    print("3. Gå till drafty room")
    choice = input("Ditt val: ")
    if choice == "1" and not has_key:
        print("Du plockar upp nyckeln. Den känns viktig.")
        sunshine_room(True)  # Nyckeln är nu hämtad
    elif choice == "2":
        entrance(has_key)
    elif choice == "3":
        drafty_room(has_key)
    else:
        print("Ogiltigt val. Försök igen.")
        sunshine_room(has_key)

# Starta spelet
print("Välkommen till spelet! Utforska rummen, hitta nyckeln och upptäck hemligheten.")
entrance(False)  # Spelet börjar utan nyckeln

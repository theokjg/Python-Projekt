def math():
    Rsvar = 7

    print ("x * 6 = 42")

    while True:
        try:
            gissning= int(input("Vad är x?"))
            break
        except ValueError:
            print("Ange en giltig siffra, försök igen")


    if gissning < Rsvar:
        print("För lågt, rätt svar är 7, då 7 * 6 = 42")
    elif gissning > Rsvar:
        print("För högt, rätt svar är 7, då 7 * 6 = 42")
    else:
        print("Rätt svar!")

math()
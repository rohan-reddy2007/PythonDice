import random
userinput = "Y"

while userinput == "Y":
    number = random.randint(1,6)
    if number == 1:
        print("[-----]")
        print("[--0--]")
        print("[-----]")

    if number == 2:
        print("[0----]")
        print("[-----]")
        print("[----0]")

    if number == 3:
        print("[0----]")
        print("[--0--]")
        print("[----0]")
        
    if number == 4:
        print("[0---0]")
        print("[-----]")
        print("[0---0]")

    if number == 5:
        print("[0---0]")
        print("[--0--]")
        print("[0---0]")

    if number == 6:
        print("[0-0-0]")
        print("[-----]")
        print("[0-0-0]")

    userinput = input("press 'Y' to roll again, 'END' to exit")
        

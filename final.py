import random as rand

crit = False

#difficulty loop
start = False
while start == False:
    ask = int(input("How hard do you want the game to be (1-5 is reccomended)?:"))
    check = str(input(f"You've chosen {ask} are you sure? (y/n):"))
    if check == "Y" or check == "y":
        start = True

def game():
    play = True
    global points
    points = 0

    while play == True:
        y = rand.randrange(1,5)
        #everything important
        if y == 1:
            global value 
            value = 10 + (ask*2) + (y*3) -1
            global hp
            hp = (y*10) + (ask*2)
            print(hp)
            print("you find a goblin")
            say = int(input("""
                Do you want to:
                1: Fight
                2: Run
                        """))
            #Nested combat loop 
            if say == 1:
                conn = input("Ok roll to hit")
                if conn == "":
                    while hp >= 1:
                        if con() == True and hp >= 0:
                            #updated the hp after damage
                            hp = com()
                            if hp <= 0:
                                print("You Killed it!")
                                points = points + value
                                y = rand.randrange(1,2)
                                break
                        elif con() == False:
                            con()
            elif say == 2:
                if points <= 10:
                    print("You ran away")
                    print(f"Points: {points}")
                    break
                elif points > 10:
                    print("You Return Victorious!")
                    print(f"Points: {points}")
                    break

        elif y == 2:
            value = 10 + (ask*2) + (y*3) -1
            hp = (y*10) + (ask*2)
            print(hp)
            print("you find a Skeleton")
            say = int(input("""
                Do you want to:
                1: Fight
                OR
                2: Run
                    """))
            #Nested combat loop 
            if say == 1:
                conn = input("Ok roll to hit")
                if conn == "":
                    while hp >= 1:
                        if con() == True and hp >= 0:
                            #updated the hp after damage
                            hp = com()
                            if hp <= 0:
                                print("You Killed it!")
                                points = points + value
                                y = rand.randrange(1,2)
                                break
                        elif con() == False:
                            con()
            elif say == 2:
                if points <= 10:
                    print("You ran away")
                    print(f"Points: {points}")
                    break
                elif points > 10:
                    print("You Return Victorious!")
                    print(f"Points: {points}")
                    break       

        elif y == 3:
            value = 10 + (ask*2) + (y*3) -1
            hp = (y*10) + (ask*2)
            print(hp)
            print("you find a Orc")
            say = int(input("""
                Do you want to:
                1: Fight
                2: Run
                    """))
            #Nested combat loop 
            if say == 1:
                conn = input("Ok roll to hit")
                if conn == "":
                    while hp >= 1:
                        if con() == True and hp >= 0:
                            #updated the hp after damage
                            hp = com()
                            if hp <= 0:
                                print("You Killed it!")
                                points = points + value
                                y = rand.randrange(1,2)
                                break
                        elif con() == False:
                            con()
            elif say == 2:
                if points <= 10:
                    print("You ran away")
                    print(f"Points: {points}")
                    break
                elif points > 10:
                    print("You Return Victorious!")
                    print(f"Points: {points}")
                    break
                
        elif y == 4:
            value = 10 + (ask*2) + (y*3) -1
            hp = (y*10) + (ask*2)
            print(hp)
            print("you find a Ogre")
            say = int(input("""
                Do you want to:
                1: Fight
                2: Run
                    """))
            #Nested combat loop 
            if say == 1:
                conn = input("Ok roll to hit")
                if conn == "":
                    while hp >= 1:
                        if con() == True and hp >= 0:
                            #updated the hp after damage
                            hp = com()
                            if hp <= 0:
                                print("You Killed it!")
                                points = points + value
                                y = rand.randrange(1,2)
                                break
                        elif con() == False:
                            con()
            elif say == 2:
                if points <= 10:
                    print("You ran away")
                    print(f"Points: {points}")
                    break
                elif points > 10:
                    print("You Return Victorious!")
                    print(f"Points: {points}")
                    break
     
#this returns the hp after combat
def com():
    say1 = input("YOU HIT!, roll for damage:")
    if say1 == "":
        dmg = rand.randrange(1,20)
        bonus = points/10
        if con() == True:                           
            hp1 = hp - (dmg + bonus)
            print(f"You did {dmg + bonus} damage!")
        elif con() == True and crit == True:
            dmg = dmg*2
            hp1 = hp - dmg
            crit = False
            print(f"You did {dmg + bonus} damage!")
        return hp1

#Checks if your attack hits or not
def con():
        #connect = rand.randrange(1,20)
        connect = 20
        if connect >= 5:
            return True
        elif connect == 20:
            crit = True
            return True
        else:
            retry = input("You missed :( roll again:")
            if retry == "":
                return False
            
game()

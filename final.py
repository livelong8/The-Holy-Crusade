import random as rand


start = False
while start == False:
    ask = int(input("How hard do you want the game to be (1-5)?:"))
    check = str(input(f"You've chosen {ask} are you sure? (y/n):"))
    if check == "Y" or check == "y":
        start = True


def game():
    #use later y = rand.randrange(0,3)
    y = 0
    if y == 0:
        points = 10
        hp1 = points + (ask*2)
        print(hp1)
        ann = print("you find a goblin")
        say = int(input("""
            Do you want to:
            1: Fight
            2: Run
                    """))
            #Nested combat loop
        if say == 1:
            combat()

def combat():
    while hp >= 0:
        con()
        if con() == True:
            hp = hp - damage()
            print(f"You did {damage()} damage!")
            return hp




def con():
    conn = input("Ok roll to hit")
    if conn == "":
        #use later connect = rand.randrange(1,20)
        connect = 20
        if connect >= 10:
            x = True
            return x
        else:
            x = False
            return x
            
 

def damage():
    say1 = input("YOU HIT!, roll for damage:")
    if say1 == "":
        dmg = rand.randrange(1,20)                            
        return dmg
    


def store():
    """

    conn = input("Ok roll to hit")
        if conn == "":
            #use later connect = rand.randrange(1,20)
            connect = 20
            if connect >= 10:
                #Damage
                say1 = input("YOU HIT!, roll for damage:")
                if say1 == "":
                    dmg = rand.randrange(1,20)
                    print(hp)
                    if hp <= 5 and hp > 0:
                        print(f"Dmg: {dmg}")
                        print("it looks badly hurt")
                        print(hp)
                        conn = input("Ok roll to hit")
                        if conn == "":
                        #use later connect = rand.randrange(1,20)
                            connect = 20
                            if connect >= 10:
                                say2 = input("YOU HIT!, roll for damage:")
                                if say2 == "":
                                    dmg = rand.randrange(1,20)                                        
                                    

                    elif hp <= 10 and hp >= 5:
                        print(f"Dmg: {dmg}")
                        print("It looks ok")
                        print(hp)
                        conn = input("Ok roll to hit")
                        if conn == "":
                            #use later connect = rand.randrange(1,20)
                            connect = 20
                            if connect >= 10:
                                say1 = input("YOU HIT!, roll for damage:")
                                if say1 == "":
                                    dmg = rand.randrange(1,20)                                
                                    hp = hp - dmg
                                    
                    elif hp >10:
                        print(f"Dmg: {dmg}")
                        print("Its fine")
                        print(hp)
                        conn = input("Ok roll to hit")
                        if conn == "":
                            #use later connect = rand.randrange(1,20)                                
                            connect = 20
                            if connect >= 10:
                                say1 = input("YOU HIT!, roll for damage:")
                                if say1 == "":
                                    dmg = rand.randrange(1,20)                            
                                    hp = hp - dmg
                    print(f"Dmg: {dmg}")
        
                    if hp <= 0:
                        print("kill check")
                        print("You killed it!")
                        hp = hp - dmg
            return hp    
    
    """


game()

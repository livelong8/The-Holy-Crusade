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
        hp = points + (ask*2)
        print(hp)
        ann = print("you find a goblin")
        say = int(input("""
            Do you want to:
            1: Fight
            2: Run
                    """))
            #Nested combat loop
        if say == 1:
            combat(say,hp)

def combat(say,hp):
    while say == 1 and hp >= 0:
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
                                say1 = input("YOU HIT!, roll for damage:")
                                if say1 == "":
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
                                    
                    else:
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
                        print("You killed it!")
                        return hp


               

game()
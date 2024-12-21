import random



class player:
    def __init__(self):
        self.hp=100
        self.power=1000
        self.defence=0
    
    def punch(self,enemy):
        if self.power<10:
            return False
        else:
            enemy.hp-=10
            self.power-=10
    
    def kick(self,enemy):
        if self.power<20:
            return False
        else:
            enemy.hp-=20
            self.power-=20

    def hp_checker(self):
        if self.hp==0:
            return False
        return True


class enemy:
    def __init__(self,level):
        self.level=level
        self.hp=100+level
        self.atk=5+level
        self.drop=1+level
    
    def attack(self,player):
        if player.hp<self.atk:
            return False
        else:
            player.hp-=self.atk
            iteam=random.randint(1,self.drop)
            if iteam==1:
                player.hp+=(10+(self.drop/2))
                return "You get HP boost"
            elif iteam==2:
                player.power+=(5+(self.drop/2))
                return "You get Power boost"
            elif iteam==3:
                player.hp+=20
                player.power+=10
                return "You get +20 HP And +10 Power boost"
            else:
                return "You get nothing :("
    
    def hp_checker(self):
        if self.hp<0:
            return False
        return True


rohit=player()
e1=enemy(1)

'''

while True:
    if rohit.hp_checker()==False:
            print("you lose")
            break
    elif e1.hp_checker()==False:
        print("You win")
        e1.level+=1
        e1=enemy(e1.level)
    else:
        a=int(input(" 1 to punch , 2 for kick  Enter choice  "))
        if a==1:
            if rohit.punch(e1)==False:
                print("Not Enough Power")
            else:
                rohit.punch(e1)
                iteam=e1.attack(rohit)
                print(iteam)
                print("------- You-------")
                print(f"HP :{rohit.hp} ")
                print(f"Power:  {rohit.power} \n")
                print("------- Enemy -------")
                print(f"HP : {e1.hp} \n")
        
        else:
            if rohit.kick(e1)==False:
                print("Not Enough Power")
            else:
                rohit.kick(e1)
                iteam=e1.attack(rohit)
                print(iteam)
                print("------- You-------")
                print(f"HP : {rohit.hp}")
                print(f"Power:  {rohit.power} \n")
                print("------- Enemy -------")
                print(f"HP : {e1.hp}\n")
        

'''

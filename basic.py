
class player:
    def __init__(self):
        self.hp=100
        self.power=100
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
    def __init__(self,hp,atk):
        self.hp=hp
        self.atk=atk
    
    def attack(self,player):
        if player.hp<self.atk:
            return False
        else:
            player.hp-=self.atk
    
    def hp_checker(self):
        if self.hp<0:
            return False
        return True


rohit=player()
e1=enemy(10,0)
while True:
    if rohit.hp_checker()==False:
            print("you lose")
            break
    elif e1.hp_checker()==False:
        print("You win")
        break
    else:
        a=int(input("Enter choice  "))
        if a==1:
            if rohit.punch(e1)==False:
                print("not enough power ")
            else:
                rohit.punch(e1)
                e1.attack(rohit)
                print(f" hp {rohit.hp} left")
                print(f"ur Power is {rohit.power} ")
                print(f"Enemy hp is {e1.hp} left")
        
        else:
            rohit.kick(e1)
            e1.attack(rohit)
            print(f"our hp is {rohit.hp} left")
            print(f"Enemy hp is {e1.hp} left")
        

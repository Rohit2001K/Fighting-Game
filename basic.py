
class player:
    def __init__(self):
        self.hp=100
        self.power=100
        self.defence=0
    
    def punch(self):
        if self.power<10:
            return False
        else:
            self.power-=10
    
    def kick(self):
        if self.power<20:
            return False
        else:
            self.power-=20

class enemy:
    def __init__(self,hp,atk):
        self.hp=hp
        self.atk=atk
    
    def attack(self,player):
        if player.hp<self.atk:
            return False
        else:
            player.hp-=self.atk


rohit=player()
e1=enemy(100,20)
while True:
    a=int(input("Enter choice  "))
    if a==1:
        rohit.punch()
        e1.attack(rohit)
        print(f"our hp is {rohit.hp} left")
        print(rohit.power)
    else:
        rohit.kick()
        print(rohit.power)
        

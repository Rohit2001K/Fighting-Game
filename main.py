import tkinter
from tkinter import *
from PIL import Image,ImageTk

from basic import player,enemy



class game:
    def __init__(self,root):
        self.root=root
        self.root.title("Game")
        self.root.geometry("1000x400")
        self.player=player()
        self.enemy=enemy(1)

        #user states showcase
        user_hp=Label(self.root,text=f"Your HP : {self.player.hp}",font=('Helvetica', 14),bg='green',fg='black').grid(row='1',column='1')
        user_power=Label(self.root,text=f"Your Power : {self.player.power}",font=('Helvetica', 14),bg='light blue',fg='black').grid(row='3',column='1')
        try:
            uicon = Image.open(r'images/placeholder_user.jpg')
            uicon = uicon.resize((300, 300))
            user_icon = ImageTk.PhotoImage(uicon)
            user_icon_label = Label(self.root, image=user_icon).grid(row=2, column=1)
            self.root.iconphoto(True, user_icon)

        except:
            user_icon_error = Label(self.root, text=f"Error in loading user_icon: {str(e)}", bg='red', fg='black').grid(row=1, column=3)

        # enemy showcase
        enemy_hp = Label(self.root, text=f"Enemy HP: {self.enemy.hp}", font=('Helvetica', 14), bg='Red', fg='black').grid(row=1, column=8)

        try:
            eicon = Image.open(r'images/placeholder_enemy.png')
            eicon = eicon.resize((300, 300))
            enemy_icon = ImageTk.PhotoImage(eicon)
            enemy_icon_label = Label(self.root, image=enemy_icon).grid(row=2, column=5)
            self.root.iconphoto(True, enemy_icon)

        except:
            enemy_icon_error = Label(self.root, text=f"Error in loading enemy_icon: {str(e)}", bg='red', fg='black').grid(row=2, column=5)






root=tkinter.Tk()
game(root)
root.mainloop()
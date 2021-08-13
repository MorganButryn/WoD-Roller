#!/usr/bin/python3
#Morgan Butryn
#2021-8-13

import random
import tkinter as tk

#screen class serves as template for future screens
class Screen(tk.Frame):
    current = 0
    def __init__(self):
        tk.Frame.__init__(self)

    def switch_frame():
        screens[Screen.current].tkraise()
    

class RollScreen(Screen):
    def __init__(self):
        Screen.__init__(self)

        self.lbl_dicepool = tk.Label(self, text="Dice pool (# of dice)", font=("20"))
        self.lbl_dicepool.grid(row = 0, sticky = "news")

        self.ent_dicepool = tk.Entry(self)
        self.ent_dicepool.grid(row = 1, sticky = "news")

#main
if __name__ == "__main__":
    root = tk.Tk()

    #screen size
    root.geometry("320x200")
    
    #screen title
    root.title("WoD Roller")

    #list of screens in program
    screens = [RollScreen()]
    
    for i in range(len(screens)):
        screens[i].grid(row = 0, column = 0, sticky = "news")
        
    Screen.current = 0
    Screen.switch_frame()
    
    root.grid_columnconfigure(0, weight = 1)
    root.grid_rowconfigure(0, weight = 1)
    root.mainloop()

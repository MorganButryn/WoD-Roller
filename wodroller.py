#!/usr/bin/python3
#Morgan Butryn
#created 2021-8-13
#last edit 2021-9-6

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
        self.lbl_dicepool.grid(row = 0, sticky = "nw")

        self.spn_dicepool = tk.Spinbox(self, from_ = 1, to = 99, width = 3)
        self.spn_dicepool.grid(row = 1, sticky = "nw")

        self.lbl_diff = tk.Label(self, text="Difficulty (# to beat)", font=("20"))
        self.lbl_diff.grid(row = 2, sticky = "nw")

        self.spn_diff = tk.Spinbox(self, from_ = 2, to = 10, width = 3)
        self.spn_diff.grid(row = 3, sticky = "nw")
        #sets starting value to 6
        for i in range(4):
            self.spn_diff.invoke("buttonup")

        self.bool_is_spec = tk.IntVar()
        
        self.chk_specialty = tk.Checkbutton(self, text = "Specialty applies", variable = self.bool_is_spec)
        self.chk_specialty.grid(row = 4, sticky = "nw")

        self.lbl_specialty = tk.Label(self, text="Specialty rules", font=("20"))
        self.lbl_specialty.grid(row = 5, sticky = "nw")

        self.var_spec_select = tk.IntVar()

        self.rad_revised = tk.Radiobutton(self, text="10s explode (Revised)", variable = self.var_spec_select, value = 1)
        self.rad_revised.grid(row = 6, sticky = "nw")
        self.rad_revised.invoke()

        self.rad_20th = tk.Radiobutton(self, text="10s count as 2 successes (20th Anniversary edition)", variable = self.var_spec_select, value = 2)
        self.rad_20th.grid(row = 7, sticky = "nw")

        self.btn_roll = tk.Button(self, text="ROLL!", command = self.roll)
        self.btn_roll.grid(row = 8, sticky = "news")

        self.txt_roll = tk.Text(self, height = 4, width = 18, state = "disabled")
        self.txt_roll.grid(row = 9, sticky = "news")

    
    
    def roll(self):
        result = []
        successes = 0
        is_botch = False
        for i in range(int(self.spn_dicepool.get())):
            result.append(d10())
            
            if result[-1] == 10 and self.bool_is_spec.get() == 1:
                if self.var_spec_select.get() == 1:
                    while result[-1] == 10:
                        successes += 1
                        result.append(d10())
                        if result[-1] >= int(self.spn_diff.get()):
                            successes += 1
                if self.var_spec_select.get() == 2:
                    successes += 2
                    
            elif result[i] >= int(self.spn_diff.get()):
                successes += 1
            elif result[i] == 1:
                successes -= 1
                
        self.txt_roll['state'] = "normal"
        self.txt_roll.delete('1.0', tk.END)
        self.txt_roll.insert('1.0', str(result)+"\n"+str(successes))
        self.txt_roll['state'] = "disabled"
        return
        

def d10():
        die = random.randint(1, 10)
        return die            
        
#main
if __name__ == "__main__":
    root = tk.Tk()

    #screen size
    root.geometry("300x300")
    
    #screen title
    root.title("WoD Roller")

    #list of screens in program
    screens = [RollScreen()]

    #applies grid to all screens
    for i in range(len(screens)):
        screens[i].grid(row = 0, column = 0, sticky = "news")
        
    Screen.current = 0
    Screen.switch_frame()
    
    root.grid_columnconfigure(0, weight = 1)
    root.grid_rowconfigure(0, weight = 1)
    root.mainloop()

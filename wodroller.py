#!/usr/bin/python3
#Morgan Butryn
#created 2021-8-13
#last edit 2022-9-14

import random
import tkinter as tk

#screen class serves as template for possible future screens
class Screen(tk.Frame):
    current = 0
    def __init__(self):
        tk.Frame.__init__(self)

    def switch_frame():
        screens[Screen.current].tkraise()
    

class RollScreen(Screen):
    def __init__(self):
        Screen.__init__(self)

        #widgets, organized in vertical order

        #dicepool
        self.lbl_dicepool = tk.Label(self, text="Dice pool (# of dice)", font=("20"))
        self.lbl_dicepool.grid(row = 0, sticky = "nw")

        self.spn_dicepool = tk.Spinbox(self, from_ = 1, to = 99, width = 3)
        self.spn_dicepool.grid(row = 1, sticky = "nw")

        #difficulty
        self.lbl_diff = tk.Label(self, text="Difficulty (# to beat)", font=("20"))
        self.lbl_diff.grid(row = 2, sticky = "nw")

        self.spn_diff = tk.Spinbox(self, from_ = 2, to = 10, width = 3)
        self.spn_diff.grid(row = 3, sticky = "nw")
        #sets starting value to 6
        for i in range(4):
            self.spn_diff.invoke("buttonup")

        #threshold
        self.lbl_threshold = tk.Label(self, text="Threshold (subracts # of successes)", font=("20"))
        self.lbl_threshold.grid(row = 4, sticky = "nw")

        self.spn_threshold = tk.Spinbox(self, from_ = 0, to = 10, width = 3)
        self.spn_threshold.grid(row = 5, sticky = "nw")

        #willpower
        self.lbl_will=tk.Label(self, text="Willpower (1 guaranteed extra success)", font=("20"))
        self.lbl_will.grid(row = 6, sticky = "nw")
        
        self.bool_will = tk.IntVar()

        self.chk_will = tk.Checkbutton(self, text = "Willpower spent", variable = self.bool_will)
        self.chk_will.grid(row = 7, sticky = "nw")

        #specialties
        self.lbl_specialty = tk.Label(self, text="Specialty rules", font=("20"))
        self.lbl_specialty.grid(row = 8, sticky = "nw")

        self.bool_specialty = tk.IntVar()
        
        self.chk_specialty = tk.Checkbutton(self, text = "Specialty applies", variable = self.bool_specialty)
        self.chk_specialty.grid(row = 9, sticky = "nw")

        self.var_spec_select = tk.IntVar()

        self.rad_revised = tk.Radiobutton(self, text="10s explode (Revised)", variable = self.var_spec_select, value = 1)
        self.rad_revised.grid(row = 10, sticky = "nw")
        self.rad_revised.invoke()

        self.rad_20th = tk.Radiobutton(self, text="10s count as 2 successes (20th Anniversary edition)", variable = self.var_spec_select, value = 2)
        self.rad_20th.grid(row = 11, sticky = "nw")

        #roll button
        self.btn_roll = tk.Button(self, text="ROLL!", command = self.roll)
        self.btn_roll.grid(row = 12, sticky = "news")

        self.txt_roll = tk.Text(self, height = 4, width = 18, state = "disabled")
        self.txt_roll.grid(row = 13, sticky = "news")

    
    
    def roll(self):
        result = []
        successes = 0
        threshold_counter = int(self.spn_threshold.get())
        no_botch = False
        for i in range(int(self.spn_dicepool.get())):
            result.append(d10())

            #specialty rules
            if result[-1] == 10 and self.bool_specialty.get() == 1:
                #revised
                if self.var_spec_select.get() == 1:
                    while result[-1] == 10:
                        successes += 1
                        result.append(d10())
                        if result[-1] >= int(self.spn_diff.get()):
                            successes += 1
                #20th
                if self.var_spec_select.get() == 2:
                    successes += 2
                    
            elif result[i] >= int(self.spn_diff.get()):
                if threshold_counter == 0:
                    no_botch = True
                    successes += 1
                else:
                    threshold_counter -= 1
            elif result[i] == 1:
                successes -= 1
        #willpower
        if self.bool_will.get() == 1:
            if successes < 1:
                successes = 1
            else:
                successes += 1
        #output
        self.txt_roll['state'] = "normal"
        self.txt_roll.delete('1.0', tk.END)
        self.txt_roll.insert('1.0', str(result)+"\n"+str(successes)+" successes")
        if not(no_botch) and successes < 0:
            self.txt_roll.insert('3.0', "\nBotch!")
        self.txt_roll['state'] = "disabled"
        return
        

def d10():
        die = random.randint(1, 10)
        return die            
        
#main
if __name__ == "__main__":
    root = tk.Tk()

    #screen size
    root.geometry("300x400")
    
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

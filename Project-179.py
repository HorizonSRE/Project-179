import tkinter as tk
import random

class game:
    def __init__(self):
        
    def updateGame(self):
        

    def __update_score(self, input_value):
        if input_value.lower() == self.color[self.random_number_for_color].lower():
            print(self.color[self.random_number_for_color])
            self.__score += random.randint(0, 10)
            self.label_score.config(text="Score: " + str(self.__score))

    def get_user_value(self, input_value):
        self.__update_score(input_value)

Root=Tk()
root.title("title")
root.geometry("400x400")


self.label_score = tk.Label(
    root,
    text="Score: 0",
    font=("Helvetica", 14),
    background="lightblue"
)
self.label_score.place(x=100, y=540)


self.input_value = tk.Entry(root, font=("Helvetica", 14))
self.input_value.place(x=250, y=555)

def getInput():
    value = self.input_value.get()
    obj.get_user_value(value)
    obj.updateGame()
    self.input_value.delete(0, tk.END)


button = tk.Button(
    root,
    text="Check",
    command=getInput,
    background="lightgreen",
    foreground="black",
    relief=tk.FLAT,
    padx=15,
    pady=10,
    font=("Helvetica", 12)
)
button.place(x=350, y=550)

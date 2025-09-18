import tkinter as tk
# Import necessary Tkinter constants
from tkinter import GROOVE, StringVar, Tk, Entry, Frame, Button, Label

class Calculator: # Corrected class name to start with a capital C (standard practice)
    
    # Corrected constructor: __init__ with double underscores, corrected method/variable names, corrected string for geometry
    def __init__(self, root): 
        self.root = root
        self.root.title("Advanced GUI Calculator") # Corrected tittle to title
        self.root.geometry("400x500") # Corrected 400*500 to 400x500
        self.root.resizable(False, False)

        self.expression = ""

        self.input_text = StringVar() # Corrected stringVar to StringVar

        # Corrected frame and Entry names to start with lowercase tk.Frame, tk.Entry, etc.
        self.input_frame = Frame(self.root, height=50, bg="lightgray")
        self.input_frame.pack(fill="both")
        
        self.input_field = Entry(self.input_frame, 
                                 font=('arial', 24, 'bold'),
                                 textvariable=self.input_text, # Corrected imput_text to input_text
                                 justify="right", bd=10, bg="white")
        self.input_field.pack(fill="both", padx=10, pady=20)

        self.buttons_frame = Frame(self.root) # Corrected frame to Frame
        self.buttons_frame.pack()

        self.create_buttons()

    # create_buttons is a method of the class, so it needs 'self'
    def create_buttons(self): 
        buttons = [
            ('C', '⌫', '%', '/'),
            ('7', '8', '9', '*'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('00', '0', '.', '=')
        ]

        for row in buttons:    
            row_frame = Frame(self.buttons_frame) # Corrected frame to Frame
            row_frame.pack(expand=True, fill="both") # Corrected true to True
            for btn_text in row:
                btn = Button(row_frame, 
                             text=btn_text, 
                             font=('arial', 18), # Corrected font tuple: ('arial, 18') -> ('arial', 18)
                             relief=GROOVE, # Corrected tk.GROOVE to GROOVE (imported above)
                             border=0, 
                             bg="#DDDCDC", 
                             activebackground="#D3CFCF", # Corrected activebackgroud to activebackground
                             command=lambda x=btn_text: self.on_button_click(x)) # Corrected seif.on_button_click to self.on_button_click
                btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "⌫":
            self.expression = self.expression[:-1] # Corrected exprssion to expression
        elif char == "=":
            try:
                # WARNING: eval() is unsafe. For a production calculator, use ast or a safe evaluator.
                result = str(eval(self.expression)) 
                self.expression = result
            except:
                self.expression = "Error"
        else:
            self.expression += str(char)

        # The indentation of this line was causing the logic to fail after '='
        self.input_text.set(self.expression) 

if __name__ == "__main__":
    root = Tk() # Corrected tk.Tk() to Tk() (imported above)
    Calculator(root)
    root.mainloop()
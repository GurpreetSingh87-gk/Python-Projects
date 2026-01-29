# Calculator App:-
# --------------

'''
import tkinter as tk

# Input function:-
# --------------

def press(key):
    entry.insert(tk.END, key)

# Clear Input function:-
# --------------------

def clear():
    entry.delete(0, tk.END)


# CE Input function:
# -----------------

def ce():
    entry.delete(0, tk.END)
    entry.insert(0, "0")
            
    
# Cut Input function:-
# ------------------

def cut():
    current = entry.get()
    
    if len(current) > 0:
        entry.delete(0, tk.END)
        entry.insert(0, current[:-1])
    
# Function to Calculate to Result:-
# -------------------------------

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.delete(0)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")



# Main GUI Window:-
# ---------------


root = tk.Tk()
root.title("Calculator App")
root.geometry("400x500")
#root.resizable(False, False)


# Creating Functions of Calculator:-
# --------------------------------

# Entry Widget:-
# ------------

entry = tk.Entry(root, font=("Arial", 32), relief="ridge", justify="right", bd=5)
entry.pack(fill=tk.X, padx=10, pady=20)

# Buttons Frame:-
# -------------

btn_frame = tk.Frame(root)
btn_frame.pack()

buttons = ["Clear","Cut","CE","/",
           "7","8","9","*",
           "4","5","6","-",
           "1","2","3","+",
           "%","0",".","="]    

row = 0
col = 0

# Buttons:-
# -------

for btn in buttons:

    def action(x=btn):
         if x == "=":
             calculate()
         elif x== "Clear":
             clear()
         elif x== "Cut":
             cut()
         elif x== "CE":
             ce()
         else:
             press(x)

    b = tk.Button(btn_frame, text=btn, width=7, height=2, font=("Arial", 14), command=action)

    b.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    
    if col == 4:
        col = 0
        row += 1

root.mainloop()

print(root)
'''















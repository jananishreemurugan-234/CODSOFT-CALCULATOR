import tkinter as tk
import math

# Function to handle button click
def click(event):
    global expression
    text = event.widget.cget("text")
   
    if text == "=":
        try:
            result = str(eval(expression))
            entry_var.set(result)
            expression = result
        except Exception:
            entry_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        entry_var.set("")
    elif text == "⌫":  # Backspace
        expression = expression[:-1]
        entry_var.set(expression)
    elif text == "x²":
        try:
            expression = str(float(expression) ** 2)
            entry_var.set(expression)
        except:
            entry_var.set("Error")
            expression = ""
    elif text == "√":
        try:
            expression = str(math.sqrt(float(expression)))
            entry_var.set(expression)
        except:
            entry_var.set("Error")
            expression = ""
    elif text == "%":
        try:
            expression = str(float(expression) / 100)
            entry_var.set(expression)
        except:
            entry_var.set("Error")
            expression = ""
    elif text == "sin":
        try:
            expression = str(math.sin(math.radians(float(expression))))
            entry_var.set(expression)
        except:
            entry_var.set("Error")
            expression = ""
    elif text == "cos":
        try:
            expression = str(math.cos(math.radians(float(expression))))
            entry_var.set(expression)
        except:
            entry_var.set("Error")
            expression = ""
    elif text == "tan":
        try:
            expression = str(math.tan(math.radians(float(expression))))
            entry_var.set(expression)
        except:
            entry_var.set("Error")
            expression = ""
    elif text == "log":
        try:
            expression = str(math.log10(float(expression)))
            entry_var.set(expression)
        except:
            entry_var.set("Error")
            expression = ""
    elif text == "ln":
        try:
            expression = str(math.log(float(expression)))
            entry_var.set(expression)
        except:
            entry_var.set("Error")
            expression = ""
    elif text == "eˣ":
        try:
            expression = str(math.exp(float(expression)))
            entry_var.set(expression)
        except:
            entry_var.set("Error")
            expression = ""
    elif text == "10ˣ":
        try:
            expression = str(10 ** float(expression))
            entry_var.set(expression)
        except:
            entry_var.set("Error")
            expression = ""
    else:
        expression += text
        entry_var.set(expression)

# Main window
root = tk.Tk()
root.title("Codsoft Scientific Calculator")
root.geometry("400x700")
root.resizable(False, False)
root.config(bg="#0AD9FD")

expression = ""
entry_var = tk.StringVar()

# Display Entry
entry = tk.Entry(root, textvar=entry_var, font="Arial 24 bold",
                 justify="right", bd=10, relief="sunken", bg="#ECF0F1", fg="black")
entry.pack(fill="both", ipadx=8, ipady=15, pady=15, padx=10)

# Button layout
buttons = [
    ["C", "⌫",],
    ["sin", "cos", "tan",],
    ["log","ln", "eˣ", "10ˣ"],
    ["x²", "√", "%","()"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    [".", "0", "=", "+"],
]

# Colors
colors = {
    "numbers": "#FD0990",   # Pink
    "operators": "#FDCF06", # Yellow
    "equal": "#FD0990",     # Pink
    "clear": "#FDCF06",     # Yellow
    "extra": "#FD0990",     # Pink
    "back": "#FD0990",      # Pink
    "trig": "#02D1FB",      # Aqua
    "logs": "#02D1FB"       # Aqua
}

for row in buttons:
    frame = tk.Frame(root, bg="#9DBBD8")
    frame.pack(expand=True, fill="both", padx=10, pady=5)
   
    for btn_text in row:
        if btn_text.isdigit():
            bg_color = colors["numbers"]
        elif btn_text in ["+", "-", "*", "/"]:
            bg_color = colors["operators"]
        elif btn_text == "=":
            bg_color = colors["equal"]
        elif btn_text == "C":
            bg_color = colors["clear"]
        elif btn_text == "⌫":
            bg_color = colors["back"]
        elif btn_text in ["sin", "cos", "tan"]:
            bg_color = colors["trig"]
        elif btn_text in ["log", "ln", "eˣ", "10ˣ"]:
            bg_color = colors["logs"]
        else:  # ., (), x², √, %
            bg_color = colors["extra"]
       
        button = tk.Button(frame, text=btn_text, font="Arial 16 bold",
                           relief="raised", bd=4, bg=bg_color, fg="white",
                           activebackground="#34495E", activeforeground="white")
        button.pack(side="left", expand=True, fill="both", padx=3, pady=3)
        button.bind("<Button-1>", click)

# Run the app
root.mainloop()
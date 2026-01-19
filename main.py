# L-System Fractal Architect
import tkinter as tk
import turtle
#creating main tkinter window
root =tk.Tk() #creating the main window
root.title("L-System Fractal Architect")
root.geometry("1000x700")
root.resizable(False,False) #prevent resizing
#adding canvas and embedding turtle using rawturtle 
canvas = tk.Canvas(root, width=700, height=700, bg="white") #area where graphics can be drawn
canvas.pack(side=tk.LEFT) #places canvas on the left side
screen = turtle.TurtleScreen(canvas) #uses this tkinter canvas as the screen
pen = turtle.RawTurtle(screen) #create the raw turtle object
#initial turtle settings
pen.speed(0) #fastest drawing
pen.hideturtle() #hides arrow for clean visuals
#creating the input dashboard(labels,entries,generate button)
controls = tk.Frame(root, padx=10, pady=10) #create frame for controls
controls.pack(side=tk.RIGHT, fill=tk.Y)
title_label = tk.Label(              #add title label
    controls,
    text="L-System Controls",
    font=("Arial", 14, "bold")
)
title_label.pack(pady=10)
tk.Label(controls, text="Axiom:").pack(anchor="w") #add axiom input
axiom_entry = tk.Entry(controls, width=30)
axiom_entry.pack(pady=5)
tk.Label(controls, text="Rules (Symbol:Replacement):").pack(anchor="w") #add rules input

rules_text = tk.Text(controls, width=30, height=6)
rules_text.pack(pady=5)
tk.Label(controls, text="Angle:").pack(anchor="w")#add angle input
angle_entry = tk.Entry(controls, width=30)
angle_entry.pack(pady=5)
tk.Label(controls, text="Iterations:").pack(anchor="w") #add iterations input
iterations_entry = tk.Entry(controls, width=30)
iterations_entry.pack(pady=5)
generate_button = tk.Button(          #add generate button
    controls,
    text="Generate",
    width=20
)
generate_button.pack(pady=15)

   
root.mainloop() #keeps the window open 


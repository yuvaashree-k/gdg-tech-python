# L-System Fractal Architect
import tkinter as tk
import turtle
root =tk.Tk() #creating the main window
root.title("L-System Fractal Architect")
root.geometry("1000x700")
root.resizable(False,False) #prevent resizing
canvas = tk.Canvas(root, width=700, height=700, bg="white") #area where graphics can be drawn
canvas.pack(side=tk.LEFT) #places canvas on the left side
screen = turtle.TurtleScreen(canvas) #uses this tkinter canvas as the screen
pen = turtle.RawTurtle(screen) #create the raw turtle object
#initial turtle settings
pen.speed(0) #fastest drawing
pen.hideturtle() #hides arrow for clean visuals
   
root.mainloop() #keeps the window open 


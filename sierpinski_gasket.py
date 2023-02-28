#!/usr/bin/env python3
import tkinter
import math
import random
import sys

if len(sys.argv) != 2:
  print("Give the number of plot points in the first argument.")
  print("Example: ./sierpinski_gasket.py 10000")
  exit()

number_of_points = int(sys.argv[1])

def plot_point(coordinate):
  x = coordinate[0]
  y = coordinate[1]
  canvas.create_oval(x-0.5, y-0.5, x+0.5, y+0.5, fill="black")

root = tkinter.Tk()
root.title("Test 1")
root.geometry("1000x1000")

canvas = tkinter.Canvas(root, bg = "white")
canvas.pack(fill = tkinter.BOTH, expand = True)

# vertices of the outmost triangle
vertices = ((100, 900), (900, 900), (500, 900-800/2*math.sqrt(3)))

for coordinate in vertices:
  plot_point(coordinate)

current_point = (600, 800)
for i in range(number_of_points):
  vertex = vertices[int(3*random.random())]
  current_point = ((current_point[0] + vertex[0])/2, (current_point[1] + vertex[1])/2)
  plot_point(current_point)

root.mainloop()

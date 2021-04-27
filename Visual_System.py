import random

from tkinter import ttk
from tkinter import *

from Rubiks_Cube.solver   import Solver
from Rubiks_Cube.cube     import Cube
from Rubiks_Cube.optimize import optimize_moves

def insert():
  string = cube_string.get()
  cube   = Cube(string)
  current_cube_output.set(string)
  cube_output.set(cube)

def random_cube():
  SOLVED_CUBE_STR = "OOOOOOOOOYYYGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBRRRRRRRRR"
  MOVES           = ["L", "R", "U", "D", "F", "B", "M", "E", "S"]
  scramble_moves  = " ".join(random.choices(MOVES, k=300))
  string          = current_cube_output.get()
  cube            = Cube(string)
  cube.sequence(scramble_moves)
  current_cube_output.set(cube.flat_str())
  cube_output.set(cube)

def Beginner():
  string = current_cube_output.get()
  cube   = Cube(string)
  solver = Solver(cube)

  solver.solveBeginner()
  current_cube_output.set(cube.flat_str())
  cube_output.set(cube)

  goal.set("""This is a complete Beginner solve solution,
  if you are trying to learn how to solve the Rubik's Cube,
  I would recommend using the smaller steps""")
  opt_moves.set(optimize_moves(solver.moves))
  if Checkbutton1.get() == 1:
    moves.set(opt_moves.get())

def Intermediate():
  string = current_cube_output.get()
  cube   = Cube(string)
  solver = Solver(cube)

  solver.solveIntermediate()
  current_cube_output.set(cube.flat_str())
  cube_output.set(cube)

  goal.set("""This is a complete Intermediate solve solution,
  if you are trying to learn how to solve the Rubik's Cube,
  I would recommend using the smaller steps""")
  opt_moves.set(optimize_moves(solver.moves))
  if Checkbutton1.get() == 1:
    moves.set(opt_moves.get())

def Expert():
  string = current_cube_output.get()
  cube   = Cube(string)
  solver = Solver(cube)

  solver.solveExpert()
  current_cube_output.set(cube.flat_str())
  cube_output.set(cube)

  goal.set("""This is a complete Expert solve solution,
  if you are trying to learn how to solve the Rubik's Cube,
  I would recommend using the smaller steps""")
  opt_moves.set(optimize_moves(solver.moves))
  if Checkbutton1.get() == 1:
    moves.set(opt_moves.get())

def White_Cross():
  string = current_cube_output.get()
  cube   = Cube(string)
  solver = Solver(cube)

  solver.white_cross()
  current_cube_output.set(cube.flat_str())
  cube_output.set(cube)

  goal.set("""The first stage is to make a white cross on the white face of the cube.
  You must find the four different edge cubies which contain a white
  facelet and set these in their correct positions.
  It is important that you take into account that the other colors of the
  edge cubies should also match their respective side center cubies """)
  opt_moves.set(optimize_moves(solver.moves))
  if Checkbutton1.get() == 1:
    moves.set(opt_moves.get())

def White_Cross_Corners():
  string = current_cube_output.get()
  cube   = Cube(string)
  solver = Solver(cube)

  solver.white_cross_corners()
  current_cube_output.set(cube.flat_str())
  cube_output.set(cube)

  goal.set("""The second stage is finishing the white face by placing the corner
  cubies containing a white facelet in their correct position,
  with taking the side face colors into account.""")
  opt_moves.set(optimize_moves(solver.moves))
  if Checkbutton1.get() == 1:
    moves.set(opt_moves.get())

def Second_Layer():
  string = current_cube_output.get()
  cube   = Cube(string)
  solver = Solver(cube)

  solver.second_layer()
  current_cube_output.set(cube.flat_str())
  cube_output.set(cube)

  goal.set("""The third stage is to finish the second layer.
  Find the correct edge cubie
  (one with two matching facelets colors for F)
  on the U layer of the cube and turn
  the U face in such a way that the edge cubie
  is above the F face and place thecubie in
  his respective place on the F face of the cube.""")
  opt_moves.set(optimize_moves(solver.moves))
  if Checkbutton1.get() == 1:
    moves.set(opt_moves.get())

def Yellow_Cross():
  string = current_cube_output.get()
  cube   = Cube(string)
  solver = Solver(cube)

  solver.yellow_cross()
  current_cube_output.set(cube.flat_str())
  cube_output.set(cube)

  goal.set("""The fourth stage is to create the yellow cross
  on the U face of the cube.
  There are four possible patterns at the start of this stage.
  One of these possible patterns is already a yellow cross,
  which means you can skip this stage and go to the fifth stage.""")
  opt_moves.set(optimize_moves(solver.moves))
  if Checkbutton1.get() == 1:
    moves.set(opt_moves.get())

def Yellow_Cross_Edges():
  string = current_cube_output.get()
  cube   = Cube(string)
  solver = Solver(cube)

  solver.yellow_cross_edges()
  current_cube_output.set(cube.flat_str())
  cube_output.set(cube)

  goal.set("""The fifth stage is switching the yellow edge cubies
  to their correct position, respective to the center cubies
  colors on each of the cube side faces.
  It is possiblethat all the edge cubies color already match
  with each respective center cubie color,
  in that case move on to stage six""")
  opt_moves.set(optimize_moves(solver.moves))
  if Checkbutton1.get() == 1:
    moves.set(opt_moves.get())

def Yellow_Cross_Corners_Place():
  string = current_cube_output.get()
  cube   = Cube(string)
  solver = Solver(cube)

  solver.yellow_cross_corners_place()
  current_cube_output.set(cube.flat_str())
  cube_output.set(cube)

  goal.set("""The sixth stage is getting the last four corner cubies
  in their correct position, respective to the sides face colors of the cube.
  The orientation of the corners does not matter in this stage,
  the only goal is getting  them  in  their  correct  position. """)
  opt_moves.set(optimize_moves(solver.moves))
  if Checkbutton1.get() == 1:
    moves.set(opt_moves.get())

def Yellow_Cross_Corners_Orientation():
  string = current_cube_output.get()
  cube   = Cube(string)
  solver = Solver(cube)

  solver.yellow_cross_corners_orientation()
  current_cube_output.set(cube.flat_str())
  cube_output.set(cube)

  goal.set("""The seventh and last stage is about the
  last four corner cubies orientation.
  All the cubies are in their correct location,
  thus orienting the last four corner cubies will solve the Rubik’s Cube.""")
  opt_moves.set(optimize_moves(solver.moves))
  if Checkbutton1.get() == 1:
    moves.set(opt_moves.get())

def F_2_L():
  string = current_cube_output.get()
  cube   = Cube(string)
  solver = Solver(cube)

  solver.F_2_L()
  current_cube_output.set(cube.flat_str())
  cube_output.set(cube)

  goal.set("""The thirth stage combines stages 2 and 3 from the Beginner Strategy.
  Instead of solving these two stages individually,
  the aim is to solve the stages simultaneously
  and as a result reducing the solve time considerably.
  In order to do this, the goal is to pair up the white
  corner cubie from stage 2 with the corresponding
  edge cubie from stage 3, before putting them in their correct position""")
  opt_moves.set(optimize_moves(solver.moves))
  if Checkbutton1.get() == 1:
    moves.set(opt_moves.get())

def Simple_PLL():
  string = current_cube_output.get()
  cube   = Cube(string)
  solver = Solver(cube)

  solver.yellow_cross_edges_PLL()
  solver.yellow_cross_corners_place_PLL()
  current_cube_output.set(cube.flat_str())
  cube_output.set(cube)

  goal.set("""The Fourt stage combines stages 5 and 6 from the Beginner Strategy
  The aim is to place all the edges and corners in their correct position.
  The beginners method uses a lot of repetition, this method solves it quicker""")
  opt_moves.set(optimize_moves(solver.moves))
  if Checkbutton1.get() == 1:
    moves.set(opt_moves.get())

def O_L_L():
  string = current_cube_output.get()
  cube   = Cube(string)
  solver = Solver(cube)

  solver.OLL()
  current_cube_output.set(cube.flat_str())
  cube_output.set(cube)

  goal.set("""The goal of this stage is to orientate all the cubies on the U face
  of the cube insuch a way that the entire U face is yellow.
  The side colors and the positions ofthe corner-
  and edge cubies do not matter, these will be fixed in a later stage""")
  opt_moves.set(optimize_moves(solver.moves))
  if Checkbutton1.get() == 1:
    moves.set(opt_moves.get())

def P_L_L():
  string = current_cube_output.get()
  cube   = Cube(string)
  solver = Solver(cube)

  solver.PLL()
  current_cube_output.set(cube.flat_str())
  cube_output.set(cube)

  goal.set("""This stage will combine moving the corner- and
  edge cubies simultaneously to their correct positions.
  The first step is to align the U face of the cube to match as
  many of the correct positionsas possible.""")
  opt_moves.set(optimize_moves(solver.moves))
  if Checkbutton1.get() == 1:
    moves.set(opt_moves.get())

def reset_moves():
  if Checkbutton1.get() == 1:
    moves.set(opt_moves.get())
  if Checkbutton1.get() == 0:
    moves.set("")

# Initial set up
window = Tk()
window.title("Tutoring System")
window.configure(bg='AntiqueWhite')

cube_string         = StringVar()
cube_output         = StringVar()
current_cube_output = StringVar()
moves               = StringVar()
goal                = StringVar()
opt_moves           = StringVar()

current_cube_output.set("OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR")
cube = Cube(current_cube_output.get())
cube_output.set(cube)

title_label    = Label(window, text = 'Rubik\'s Cube: Tutoring System', font=('roboto',25, 'bold'), bg="AntiqueWhite")
subtitle_label = Label(window, text = 'Created by: Floris van Voorst to Voorst (2021)', font=('roboto',15), bg="AntiqueWhite")

cube_label                = Label(window, text = 'Insert New Cube String', font=('roboto',10, 'bold'), bg="AntiqueWhite")
current_cube_label        = Label(window, text = 'Current Cube String:', font=('roboto',10, 'bold'), bg="AntiqueWhite")
current_cube_label_output = Label(window, textvariable = current_cube_output, font=('roboto',10, 'bold'), bg="AntiqueWhite")
cube_output_label         = Label(window, text = '2D Visualisation:', font=('roboto',10, 'bold'), bg="AntiqueWhite")
cube_print                = Label(window, textvariable = cube_output, font=('roboto',10, 'bold'), bg="AntiqueWhite")
moves_label               = Label(window, text = 'Moves to solve this stage:', font=('roboto',12, 'bold'), bg="AntiqueWhite")
moves_output_label        = Message(window, textvariable = moves, font=('roboto',12), bg="AntiqueWhite", width=400)
goal_label                = Label(window, text = 'Goal of this stage:', font=('roboto',12, 'bold'), bg="AntiqueWhite")
goal_output_label         = Message(window, textvariable = goal, font=('roboto',12), bg="AntiqueWhite", width=400, justify=CENTER)

cube_entry    = Entry(window, textvariable = cube_string, font = ('roboto',10,'normal'), width=75)
ins_button    = ttk.Button(window,text = 'Insert', command = insert)
random_button = ttk.Button(window,text = 'Random', command = random_cube)

beginner     = Label(window, text = 'Beginner Strategy', font=('roboto',13, 'bold'), bg="AntiqueWhite")
intermediate = Label(window, text = 'Intermediate Strategy', font=('roboto',13, 'bold'), bg="AntiqueWhite")
expert       = Label(window, text = 'Expert Strategy', font=('roboto',13, 'bold'), bg="AntiqueWhite")

full_solve_beginner                       = ttk.Button(window,text = 'Full Solve', command = Beginner)
white_cross_beginner                      = ttk.Button(window,text = 'White Cross', command = White_Cross)
white_corners_beginner                    = ttk.Button(window,text = 'White Cross Corners', command = White_Cross_Corners)
second_layer_beginner                     = ttk.Button(window,text = 'Second Layer', command = Second_Layer)
yellow_cross_beginner                     = ttk.Button(window,text = 'Yellow Cross', command = Yellow_Cross)
yellow_cross_edges_beginner               = ttk.Button(window,text = 'Yellow Edges', command = Yellow_Cross_Edges)
yellow_cross_corners_place_beginner       = ttk.Button(window,text = 'Yellow Corners Place', command = Yellow_Cross_Corners_Place)
yellow_cross_corners_orientation_beginner = ttk.Button(window,text = 'Yellow Corners Orientation', command = Yellow_Cross_Corners_Orientation)

full_solve_intermediate                       = ttk.Button(window,text = 'Full Solve', command = Intermediate)
white_cross_intermediate                      = ttk.Button(window,text = 'White Cross', command = White_Cross)
f2l_intermediate                              = ttk.Button(window,text = 'F2L', command = F_2_L)
yellow_cross_intermediate                     = ttk.Button(window,text = 'Yellow Cross', command = Yellow_Cross)
simple_pll_intermediate                       = ttk.Button(window,text = 'Simple PLL', command = Simple_PLL)
yellow_cross_corners_orientation_intermediate = ttk.Button(window,text = 'Yellow Corners Orientation', command = Yellow_Cross_Corners_Orientation)

full_solve_expert  = ttk.Button(window,text = 'Full Solve', command = Expert)
white_cross_expert = ttk.Button(window,text = 'White Cross', command = White_Cross)
f2l_expert         = ttk.Button(window,text = 'F2L', command = F_2_L)
oll_expert         = ttk.Button(window,text = 'OLL', command = O_L_L)
pll_expert         = ttk.Button(window,text = 'PLL', command = P_L_L)

Checkbutton1 = IntVar()
move_check  = ttk.Checkbutton(window, text = "Show me the required moves",
                             variable = Checkbutton1,
                             onvalue = 1,
                             offvalue = 0,
                             command = reset_moves)

# Grid Places
title_label.grid(row=0, column=1)
subtitle_label.grid(row=1, column=1)
cube_label.grid(row=2, column=0)
cube_entry.grid(row=2, column=1)
ins_button.grid(row=2, column=2)
random_button.grid(row=3, column=2)
cube_output_label.grid(row=4, column=0)
current_cube_label.grid(row=3, column=0)
current_cube_label_output.grid(row=3, column=1)
cube_print.grid(row=4, column=1)

beginner.grid(row=5, column=0)
full_solve_beginner.grid(row=6, column=0)
white_cross_beginner.grid(row=7, column=0)
white_corners_beginner.grid(row=8, column=0)
second_layer_beginner.grid(row=9, column=0)
yellow_cross_beginner.grid(row=10, column=0)
yellow_cross_edges_beginner.grid(row=11, column=0)
yellow_cross_corners_place_beginner.grid(row=12, column=0)
yellow_cross_corners_orientation_beginner.grid(row=13, column=0)

intermediate.grid(row=5, column=1)
full_solve_intermediate.grid(row=6, column=1)
white_cross_intermediate.grid(row=7, column=1)
f2l_intermediate.grid(row=8, column=1)
yellow_cross_intermediate.grid(row=9, column=1)
simple_pll_intermediate .grid(row=10, column=1)
yellow_cross_corners_orientation_intermediate.grid(row=11, column=1)

expert.grid(row=5, column=2)
full_solve_expert.grid(row=6, column=2)
white_cross_expert.grid(row=7, column=2)
f2l_expert.grid(row=8, column=2)
oll_expert.grid(row=9, column=2)
pll_expert.grid(row=10, column=2)

goal_label.grid(row=14, column=1)
goal_output_label.grid(row=15, column=1)
move_check.grid(row=17, column=1)
moves_label.grid(row=18, column=1)
moves_output_label.grid(row=19, column=1)

window.geometry("800x750")
window.mainloop()
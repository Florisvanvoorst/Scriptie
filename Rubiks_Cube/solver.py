import sys
import time
import random

from Rubiks_Cube          import cube
from Rubiks_Cube.maths    import Point
from Rubiks_Cube.optimize import optimize_moves

class Solver:
  def __init__(self, c):
    self.cube   = c
    self.colors = c.colors()
    self.moves  = []

  #Beginner Solve:
  def solveBeginner(self):
    self.white_cross()
    self.white_cross_corners()
    self.second_layer()
    self.yellow_cross()
    self.yellow_cross_edges()
    self.yellow_cross_corners_place()
    self.yellow_cross_corners_orientation()

  #Intermediate Solve:
  def solveIntermediate(self):
    self.white_cross()
    self.F_2_L()
    self.yellow_cross()
    self.yellow_cross_edges_PLL()
    self.yellow_cross_corners_place_PLL()
    self.yellow_cross_corners_orientation()

  #Expert Solve:
  def solveExpert(self):
    self.white_cross()
    self.F_2_L()
    self.OLL()
    self.PLL()

  def move(self, move_str):
    self.moves.extend(move_str.split())
    self.cube.sequence(move_str)

  def set_white_front(self):
    while self.cube.front_color() != "W":
      if self.cube.up_color() == "W":
        self.move("Xi")
      elif self.cube.down_color() == "W":
        self.move("X")
      else:
        self.move("Y")

  def white_cross(self):
    self.set_white_front()

    self.left_cubie  = self.cube.find_cubie(self.cube.left_color())
    self.right_cubie = self.cube.find_cubie(self.cube.right_color())
    self.up_cubie    = self.cube.find_cubie(self.cube.up_color())
    self.down_cubie  = self.cube.find_cubie(self.cube.down_color())

    left  = self.cube.find_cubie(self.cube.front_color(), self.cube.left_color())
    right = self.cube.find_cubie(self.cube.front_color(), self.cube.right_color())
    down  = self.cube.find_cubie(self.cube.front_color(), self.cube.down_color())
    up    = self.cube.find_cubie(self.cube.front_color(), self.cube.up_color())

    self._white_cross_solve(left, self.left_cubie, self.cube.left_color(), "L L", "E L Ei Li")
    self._white_cross_solve(right, self.right_cubie, self.cube.right_color(), "R R", "Ei R E Ri")
    self._white_cross_solve(down, self.down_cubie, self.cube.down_color(), "D D", "Mi D M Di")
    self._white_cross_solve(up, self.up_cubie, self.cube.up_color(), "U U", "M U Mi Ui")

  def _white_cross_solve(self, edge_cubie, face_cubie, face_color, move_1, move_2):
    if (edge_cubie.pos == (face_cubie.pos.x, face_cubie.pos.y, 1)
            and edge_cubie.colors[2] == self.cube.front_color()):
      return
    elif (edge_cubie.pos == (face_cubie.pos.x, face_cubie.pos.y, 1)):
      self.move(move_1)
      self.move(move_2)
      return

    if edge_cubie.pos.z == 0:
      if edge_cubie.pos.y == 1:
        if edge_cubie.pos.x == 1:
          self.move("R B Ri")
        elif edge_cubie.pos.x == -1:
          self.move("Li B L")
      elif edge_cubie.pos.y == -1:
        if edge_cubie.pos.x == 1:
          self.move("Ri B R")
        elif edge_cubie.pos.x == -1:
          self.move("L B Li")
    if edge_cubie.pos.z == 1:
      if edge_cubie.pos.y == 1:
        self.move("U U B")
      elif edge_cubie.pos.y == -1:
        self.move("D D B")
      elif edge_cubie.pos.y == 0:
        if edge_cubie.pos.x == 1:
          self.move("R R B")
        elif edge_cubie.pos.x == -1:
          self.move("L L B")

    if edge_cubie.pos.z == -1:
      while (edge_cubie.pos.x, edge_cubie.pos.y) != (face_cubie.pos.x, face_cubie.pos.y):
        self.move("B")

      if edge_cubie.colors[0] == face_color:
        self.move(move_1)
      elif edge_cubie.colors[1] == face_color:
        self.move(move_1)
      else:
        self.move(move_2)

  def white_cross_corners(self):
    self.left_cubie  = self.cube.find_cubie(self.cube.left_color())
    self.right_cubie = self.cube.find_cubie(self.cube.right_color())
    self.up_cubie    = self.cube.find_cubie(self.cube.up_color())
    self.down_cubie  = self.cube.find_cubie(self.cube.down_color())

    leftDown  = self.cube.find_cubie(self.cube.front_color(), self.cube.left_color(), self.cube.down_color())
    leftUp    = self.cube.find_cubie(self.cube.front_color(), self.cube.left_color(), self.cube.up_color())
    rightDown = self.cube.find_cubie(self.cube.front_color(), self.cube.right_color(), self.cube.down_color())
    rightUp   = self.cube.find_cubie(self.cube.front_color(), self.cube.right_color(), self.cube.up_color())

    self._white_corner_solve(leftDown, self.left_cubie, self.down_cubie, self.cube.front_color(), 1)
    self._white_corner_solve(leftUp, self.left_cubie, self.up_cubie, self.cube.front_color(), 2)
    self._white_corner_solve(rightDown, self.right_cubie, self.down_cubie, self.cube.front_color(), 3)
    self._white_corner_solve(rightUp, self.right_cubie, self.up_cubie, self.cube.front_color(), 4)

  def _white_corner_solve(self, corner_cubie, cubie_1, cubie_2, face_color, x):
    if corner_cubie.pos.z == 1:
      if corner_cubie.pos.y == 1:
        if corner_cubie.pos.x == 1:
          self.move("R Bi Ri")
        elif corner_cubie.pos.x == -1:
          self.move("Li B L")
      elif corner_cubie.pos.y == -1:
        if corner_cubie.pos.x == 1:
          self.move("Ri B R")
        elif corner_cubie.pos.x == -1:
          self.move("L Bi Li")

    if corner_cubie.pos.z == -1:
      while (corner_cubie.pos.x, corner_cubie.pos.y) != (cubie_1.pos.x, cubie_2.pos.y):
        self.move("B")

      if x == 1:
        self.move("Zi")
      elif x == 2:
        self.move("Z Z")
      elif x == 4:
        self.move("Z")

      if corner_cubie.colors[0] == face_color:
        self.move("Ri Bi R")
      elif corner_cubie.colors[1] == face_color:
        self.move("D B Di")
      else:
        self.move("Ri B B R B Ri Bi R")

      if x == 1:
        self.move("Z")
      elif x == 2:
        self.move("Z Z")
      elif x == 4:
        self.move("Zi")

  def second_layer(self):
    self.move("Xi")
    rightFront = self.cube.find_cubie(self.cube.right_color(), self.cube.front_color())
    rightBack  = self.cube.find_cubie(self.cube.right_color(), self.cube.back_color())
    leftFront  = self.cube.find_cubie(self.cube.left_color(), self.cube.front_color())
    leftBack   = self.cube.find_cubie(self.cube.left_color(), self.cube.back_color())

    self._second_layer_solve(rightFront, self.cube.right_color(), self.cube.front_color())
    self.move("Y")
    self._second_layer_solve(rightBack, self.cube.right_color(), self.cube.front_color())
    self.move("Y")
    self._second_layer_solve(leftBack, self.cube.right_color(), self.cube.front_color())
    self.move("Y")
    self._second_layer_solve(leftFront, self.cube.right_color(), self.cube.front_color())
    self.move("Y")

  def _second_layer_solve(self, edge_cubie, right_color, front_color):
    if edge_cubie.pos == [1, 0, 1] and edge_cubie.colors[2] == front_color:
      return

    if edge_cubie.pos == [1, 0, 1] and edge_cubie.colors[0] == front_color:
      self.move("U R Ui Ri Ui Fi U F Ui R Ui Ri Ui Fi U F")
      return

    elif edge_cubie.pos.y == 0:
      moves = 0
      while (edge_cubie.pos.x, edge_cubie.pos.z) != (1, 1):
        self.move("Y")
        moves += 1
      self.move("U R Ui Ri Ui Fi U F")
      for z in range(moves):
        self.move("Yi")

    if edge_cubie.pos.y == 1:
      if edge_cubie.colors[1] == right_color:
        while edge_cubie.pos.x != 1:
          self.move("U")
        self.move("U U R Ui Ri Ui Fi U F")
      elif edge_cubie.colors[1] == front_color:
        while edge_cubie.pos.x != 1:
          self.move("U")
        self.move(" Ui Fi U F U R Ui Ri")
      else:
        raise Exception("Mission failed")

  def yellow_cross(self):
    up_color = self.cube.up_color()

    if (self.cube[0, 1, 1].colors[1]  == up_color
       and self.cube[-1, 1, 0].colors[1] == up_color
       and self.cube[0, 1, -1].colors[1] == up_color
       and self.cube[1, 1, 0].colors[1]  == up_color):
      return

    elif (self.cube[0, 1, 1].colors[1] != up_color and
         self.cube[-1, 1, 0].colors[1] != up_color and
         self.cube[0, 1, -1].colors[1] != up_color and
         self.cube[1, 1, 0].colors[1]  != up_color):
      self.move("F U R Ui Ri Fi U F R U Ri Ui Fi")

    elif (self.cube[0, 1, 1].colors[1] == up_color and
         self.cube[0, 1, -1].colors[1] == up_color):
      self.move("U F R U Ri Ui Fi")

    elif (self.cube[-1, 1, 0].colors[1] == up_color and
         self.cube[1, 1, 0].colors[1]   == up_color):
      self.move("F R U Ri Ui Fi")

    elif (self.cube[-1, 1, 0].colors[1] == up_color and
         self.cube[0, 1, -1].colors[1]  == up_color):
      self.move("F U R Ui Ri Fi")
    elif (self.cube[0, 1, -1].colors[1] == up_color and
         self.cube[1, 1, 0].colors[1]   == up_color):
      self.move("Ui F U R Ui Ri Fi")
    elif (self.cube[1, 1, 0].colors[1] == up_color and
         self.cube[0, 1, 1].colors[1]  == up_color):
      self.move("U U F U R Ui Ri Fi")
    elif (self.cube[0, 1, 1].colors[1] == up_color and
         self.cube[-1, 1, 0].colors[1] == up_color):
     self.move("U F U R Ui Ri Fi")

  def yellow_cross_edges(self):
    upFront = self.cube.find_cubie(self.cube.up_color(), self.cube.front_color())
    upLeft  = self.cube.find_cubie(self.cube.up_color(), self.cube.left_color())
    upBack  = self.cube.find_cubie(self.cube.up_color(), self.cube.back_color())
    upRight = self.cube.find_cubie(self.cube.up_color(), self.cube.right_color())

    while upFront.pos != [0, 1, 1]:
      self.move("U")

    if upRight.pos != [1, 1, 0]:
      if upRight.pos == [-1, 1, 0]:
        self.move("U Ri U U R U Ri U R")
      if upRight.pos == [0, 1, -1]:
        self.move("Ri U U R U Ri U R U")

    if upLeft.pos != [-1, 1, 0]:
      self.move("U Ri U U R U Ri U R")

  def yellow_cross_corners_place(self):
    frontLeft  = self.cube.find_cubie(self.cube.front_color(), self.cube.left_color(), self.cube.up_color())
    frontRight = self.cube.find_cubie(self.cube.front_color(), self.cube.right_color(), self.cube.up_color())
    backLeft   = self.cube.find_cubie(self.cube.back_color(), self.cube.left_color(), self.cube.up_color())
    backRight  = self.cube.find_cubie(self.cube.back_color(), self.cube.right_color(), self.cube.up_color())

    if backLeft.pos != [1, 1, 1]:
      while backLeft.pos != [-1, 1, -1]:
        self.move("U R Ui Li U Ri Ui L")

      while frontRight.pos != [1, 1, 1]:
        self.move("Ri U L Ui R U Li Ui")

    else:
      self.move("Ri U L Ui R U Li Ui")
      while backLeft.pos != [-1, 1, -1]:
        self.move("U R Ui Li U Ri Ui L")

      while frontRight.pos != [1, 1, 1]:
        self.move("Ri U L Ui R U Li Ui")

  def yellow_cross_corners_orientation(self):
    frontLeft  = self.cube.find_cubie(self.cube.front_color(), self.cube.left_color(), self.cube.up_color())
    frontRight = self.cube.find_cubie(self.cube.front_color(), self.cube.right_color(), self.cube.up_color())
    backLeft   = self.cube.find_cubie(self.cube.back_color(), self.cube.left_color(), self.cube.up_color())
    backRight  = self.cube.find_cubie(self.cube.back_color(), self.cube.right_color(), self.cube.up_color())

    while frontRight.colors[1] != self.cube.up_color():
      self.move("Ri Di R D Ri Di R D")
    self.move("U")
    while backRight.colors[1] != self.cube.up_color():
      self.move("Ri Di R D Ri Di R D")
    self.move("U")
    while backLeft.colors[1] != self.cube.up_color():
      self.move("Ri Di R D Ri Di R D")
    self.move("U")
    while frontLeft.colors[1] != self.cube.up_color():
      self.move("Ri Di R D Ri Di R D")
    self.move("U")

  def F_2_L(self):
    self.move("Xi")
    leftFrontCorner  = self.cube.find_cubie(self.cube.down_color(), self.cube.left_color(), self.cube.front_color())
    leftBackCorner   = self.cube.find_cubie(self.cube.down_color(), self.cube.left_color(), self.cube.back_color())
    rightFrontCorner = self.cube.find_cubie(self.cube.down_color(), self.cube.right_color(), self.cube.front_color())
    rightBackCorner  = self.cube.find_cubie(self.cube.down_color(), self.cube.right_color(), self.cube.back_color())

    rightFrontEdge = self.cube.find_cubie(self.cube.right_color(), self.cube.front_color())
    rightBackEdge  = self.cube.find_cubie(self.cube.right_color(), self.cube.back_color())
    leftFrontEdge  = self.cube.find_cubie(self.cube.left_color(), self.cube.front_color())
    leftBackEdge   = self.cube.find_cubie(self.cube.left_color(), self.cube.back_color())

    self.F_2_L_solve(rightFrontCorner, rightFrontEdge, self.cube.right_color(), self.cube.front_color(), self.cube.down_color())
    self.move("Y")
    self.F_2_L_solve(rightBackCorner, rightBackEdge, self.cube.right_color(), self.cube.front_color(), self.cube.down_color())
    self.move("Y")
    self.F_2_L_solve(leftBackCorner, leftBackEdge, self.cube.right_color(), self.cube.front_color(), self.cube.down_color())
    self.move("Y")
    self.F_2_L_solve(leftFrontCorner, leftFrontEdge, self.cube.right_color(), self.cube.front_color(), self.cube.down_color())
    self.move("Y")

  def F_2_L_solve(self, corner_cubie, edge_cubie, right_color, front_color, down_color):
    if (corner_cubie.pos == [1, -1, 1] and corner_cubie.colors[2] == front_color):
      if (edge_cubie.pos == [1, 0, 1] and edge_cubie.colors[2] == front_color):
        return

    if corner_cubie.pos.y == -1:
      if corner_cubie.pos == [1, -1, -1]:
        self.move("Ri Ui R")
      elif corner_cubie.pos == [-1, -1, -1]:
        self.move("L U Li")
      elif corner_cubie.pos == [-1, -1, 1]:
        self.move("Li Ui L")
      elif corner_cubie.pos == [1, -1, 1]:
        if edge_cubie.pos.y == 0:
          if edge_cubie.pos == [1, 0, -1]:
            self.move("Y Fi U F U R Ui Ri Yi")
          elif edge_cubie.pos == [-1, 0, -1]:
            self.move("Y Y Fi U F U R Ui Ri Y Y")
          elif edge_cubie.pos == [-1, 0, 1]:
            self.move("Yi Fi U F U R Ui Ri Y")
          elif edge_cubie.pos == [1, 0, 1]:
            if corner_cubie.colors[2] == front_color:
              self.move("R Ui Ri D E Ri U U R U Ri U U R Di Ei")
            elif corner_cubie.colors[2] == right_color:
              if edge_cubie.colors[2] == front_color:
                self.move("R Ui Ri U R U U Ri U R Ui Ri")
              elif edge_cubie.colors[2] == right_color:
                self.move("R U Ri Ui R Ui Ri U D E Ri Ui R Di Ei")
            elif corner_cubie.colors[2] == down_color:
              if edge_cubie.colors[2] == front_color:
                self.move("R Ui Ri Ui R U Ri Ui R U U Ri")
              elif edge_cubie.colors[2] == right_color:
                self.move("R Ui Ri D E Ri Ui R Ui Ri Ui R Di Ei")

        if edge_cubie.pos.y == 1:
          if corner_cubie.colors[2] == front_color:
            if edge_cubie.colors[1] == right_color:
              while edge_cubie.pos != [0, 1, 1]:
                self.move("U")
              self.move("U R Ui Ri Ui Fi U F")
            elif edge_cubie.colors[1] == front_color:
              while edge_cubie.pos != [1, 1, 0]:
                self.move("U")
              self.move("Ui Fi U F U R Ui Ri")
          elif corner_cubie.colors[2] == right_color:
            if edge_cubie.colors[1] == right_color:
              while edge_cubie.pos != [0, 1, 1]:
                self.move("U")
              self.move("Fi U F Ui Fi U F")
            elif edge_cubie.colors[1] == front_color:
              while edge_cubie.pos != [1, 1, 0]:
                self.move("U")
              self.move("R U Ri Ui R U Ri")
          elif corner_cubie.colors[2] == down_color:
            if edge_cubie.colors[1] == right_color:
              while edge_cubie.pos != [0, 1, 1]:
                self.move("U")
              self.move("Fi Ui F U Fi Ui F")
            elif edge_cubie.colors[1] == front_color:
              while edge_cubie.pos != [1, 1, 0]:
                self.move("U")
              self.move("R Ui Ri U R Ui Ri")

    if corner_cubie.pos.y == 1:
      if edge_cubie.pos.y == 0:
        if edge_cubie.pos == [1, 0, -1]:
          self.move("Y Fi U F U R Ui Ri Yi")
        elif edge_cubie.pos == [-1, 0, -1]:
          self.move("Y Y Fi U F U R Ui Ri Y Y")
        elif edge_cubie.pos == [-1, 0, 1]:
          self.move("Yi Fi U F U R Ui Ri Y")
        elif edge_cubie.pos == [1, 0, 1]:
          while corner_cubie.pos != [1, 1, 1]:
            self.move("U")
          if edge_cubie.colors[2] == front_color:
            if corner_cubie.colors[2] == front_color:
              self.move("U Fi U F U Fi U U F")
            elif corner_cubie.colors[2] == right_color:
              self.move("R U Ri Ui R U Ri Ui R U Ri")
            elif corner_cubie.colors[2] == down_color:
              self.move("Ui R Ui Ri Ui R U U Ri")
          elif edge_cubie.colors[2] == right_color:
            if corner_cubie.colors[2] == front_color:
              self.move("U Fi Ui F Di Ei F U Fi D E")
            elif corner_cubie.colors[2] == right_color:
              self.move("R Ui Ri D E Ri U R Di Ei")
            elif corner_cubie.colors[2] == down_color:
              self.move("Ui R U Ri D E Ri Ui R Di Ei")

      if edge_cubie.pos.y == 1:
        while corner_cubie.pos != [1, 1, 1]:
          self.move("U")
        if corner_cubie.colors[1] == down_color:
          if edge_cubie.pos == [0, 1, 1]:
            if edge_cubie.colors[1] == front_color:
              self.move("R U Ri Ui Ui R U Ri Ui R U Ri")
            elif edge_cubie.colors[1] == right_color:
              self.move("Fi U U F U Fi Ui F")
          elif edge_cubie.pos == [-1, 1, 0]:
            if edge_cubie.colors[1] == front_color:
              self.move("U U R U Ri U R Ui Ri")
            elif edge_cubie.colors[1] == right_color:
              self.move("Ui Fi U U F Ui Fi U F")
          elif edge_cubie.pos == [0, 1, -1]:
            if edge_cubie.colors[1] == front_color:
              self.move("U R U U Ri U R Ui Ri")
            elif edge_cubie.colors[1] == right_color:
              self.move("U U Fi Ui F Ui Fi U F")
          elif edge_cubie.pos == [1, 1, 0]:
            if edge_cubie.colors[1] == front_color:
              self.move("R U U Ri Ui R U Ri")
            elif edge_cubie.colors[1] == right_color:
              self.move("Yi Ri Ui R U U Ri Ui R U Ri Ui R Y")
        elif corner_cubie.colors[1] == front_color:
          if edge_cubie.pos == [0, 1, 1]:
            if edge_cubie.colors[1] == front_color:
              self.move("Fi U F Ui Di Ei F U Fi D E")
            elif edge_cubie.colors[1] == right_color:
              self.move("U Fi U F Ui Fi Ui F")
          elif edge_cubie.pos == [-1, 1, 0]:
            if edge_cubie.colors[1] == front_color:
              self.move("Ui R U U Ri Ui R U U Ri")
            elif edge_cubie.colors[1] == right_color:
              self.move("Fi Ui F")
          elif edge_cubie.pos == [0, 1, -1]:
            if edge_cubie.colors[1] == front_color:
              self.move("Ui R U Ri Ui R U U Ri")
            elif edge_cubie.colors[1] == right_color:
              self.move("U Fi Ui F Ui Fi Ui F")
          elif edge_cubie.pos == [1, 1, 0]:
            if edge_cubie.colors[1] == front_color:
              self.move("U R Ui Ri")
            elif edge_cubie.colors[1] == right_color:
              self.move("Ui R U U Ri U Fi Ui F")
        elif corner_cubie.colors[1] == right_color:
          if edge_cubie.pos == [0, 1, 1]:
            if edge_cubie.colors[1] == front_color:
              self.move("U Fi U U F Ui R U Ri")
            elif edge_cubie.colors[1] == right_color:
              self.move("Ui Fi U F")
          elif edge_cubie.pos == [-1, 1, 0]:
            if edge_cubie.colors[1] == front_color:
              self.move("Ui R U Ri U R U Ri")
            elif edge_cubie.colors[1] == right_color:
              self.move("U Fi Ui F U Fi U U F")
          elif edge_cubie.pos == [0, 1, -1]:
            if edge_cubie.colors[1] == front_color:
              self.move("R U Ri")
            elif edge_cubie.colors[1] == right_color:
              self.move("U Fi U U F U Fi U U F")
          elif edge_cubie.pos == [1, 1, 0]:
            if edge_cubie.colors[1] == front_color:
              self.move("Ui R Ui Ri U R U Ri")
            elif edge_cubie.colors[1] == right_color:
              self.move("R Ui Ri U D E Ri Ui R Di Ei")

  def yellow_cross_edges_PLL(self):
    upFront = self.cube.find_cubie(self.cube.up_color(), self.cube.front_color())
    upLeft  = self.cube.find_cubie(self.cube.up_color(), self.cube.left_color())
    upBack  = self.cube.find_cubie(self.cube.up_color(), self.cube.back_color())
    upRight = self.cube.find_cubie(self.cube.up_color(), self.cube.right_color())

    while upBack.pos != [0, 1, -1]:
      self.move("U")

    while upRight.pos != [1, 1, 0]:
      self.move("Ri Ui R Ui Ri U U R")

    if upLeft.pos != [-1, 1, 0]:
      self.move("R U Ri U R U U Ri U")

  def yellow_cross_corners_place_PLL(self):
    frontLeft  = self.cube.find_cubie(self.cube.front_color(), self.cube.left_color(), self.cube.up_color())
    frontRight = self.cube.find_cubie(self.cube.front_color(), self.cube.right_color(), self.cube.up_color())
    backLeft   = self.cube.find_cubie(self.cube.back_color(), self.cube.left_color(), self.cube.up_color())
    backRight  = self.cube.find_cubie(self.cube.back_color(), self.cube.right_color(), self.cube.up_color())

    if backLeft.pos != [1, 1, 1]:
      while backLeft.pos != [-1, 1, -1]:
        self.move("U R Ui Li U Ri Ui L")
      if backLeft.pos == [-1, 1, 1]:
        self.move("U Ri U L Ui R U Li")
      elif backLeft.pos == [1, 1, -1]:
        self.move("U R Ui Li U Ri Ui L")

      if frontRight.pos == [1, 1, -1]:
        self.move("Ri U L Ui R U Li Ui")
      elif frontRight.pos == [-1, 1, 1]:
        self.move("U L Ui Ri U Li Ui R")
    else:
      self.move("Y Ri U L Ui R U Li Ui Yi")
      if frontRight.pos == [1, 1, -1]:
        self.move("Ri U L Ui R U Li Ui")
      elif frontRight.pos == [-1, 1, 1]:
        self.move("U L Ui Ri U Li Ui R")

  def OLL(self):
    up_color = self.cube.up_color()

    self.yellow_cross()

    leftFront  = self.cube.get_cubie(-1, 1, 1)
    leftBack   = self.cube.get_cubie(-1, 1, -1)
    rightFront = self.cube.get_cubie(1, 1, 1)
    rightBack  = self.cube.get_cubie(1, 1, -1)

    if (leftFront.colors[1] != up_color and
       rightFront.colors[1] != up_color and
       leftBack.colors[1]   != up_color and
       rightBack.colors[1]  != up_color):

      if (leftFront.colors[2] == up_color and
         leftBack.colors[2]   == up_color and
         rightFront.colors[2] == up_color and
         rightBack.colors[2]  == up_color):
        self.move("R U U Ri Ui R U Ri Ui R Ui Ri")

      if (leftFront.colors[0] == up_color and
         leftBack.colors[0]   == up_color and
         rightFront.colors[0] == up_color and
         rightBack.colors[0]  == up_color):
        self.move("R U Ri U R Ui Ri U R U U Ri")

      if (leftFront.colors[2] == up_color and
         leftBack.colors[2]   == up_color and
         rightFront.colors[0] == up_color and
         rightBack.colors[0]  == up_color):
        self.move("L Ui Ri U Li U R U Ri U R")

      if (leftFront.colors[0] == up_color and
         leftBack.colors[0]   == up_color and
         rightFront.colors[2] == up_color and
         rightBack.colors[2]  == up_color):
        self.move("R U U R R Ui R R Ui R R U U R")

      if (leftFront.colors[0] == up_color and
         leftBack.colors[2]   == up_color and
         rightFront.colors[0] == up_color and
         rightBack.colors[2]  == up_color):
        self.move("U L Ui Ri U Li U R U Ri U R Ui")

      if (leftFront.colors[2] == up_color and
         leftBack.colors[0]   == up_color and
         rightFront.colors[2] == up_color and
         rightBack.colors[0]  == up_color):
        self.move("Ui L Ui Ri U Li U R U Ri U R U")

    if ((leftFront.colors[1] == up_color and
       rightFront.colors[1]  != up_color and
       leftBack.colors[1]    != up_color and
       rightBack.colors[1]   != up_color) or
       (leftFront.colors[1]  != up_color and
       rightFront.colors[1]  == up_color and
       leftBack.colors[1]    != up_color and
       rightBack.colors[1]   != up_color) or
       (leftFront.colors[1]  != up_color and
       rightFront.colors[1]  != up_color and
       leftBack.colors[1]    == up_color and
       rightBack.colors[1]   != up_color) or
       (leftFront.colors[1]  != up_color and
       rightFront.colors[1]  != up_color and
       leftBack.colors[1]    != up_color and
       rightBack.colors[1]   == up_color)):

      if self.cube.get_cubie(1, 1, -1).colors[1] == up_color:
        self.move("U")

      if self.cube.get_cubie(-1, 1, -1).colors[1] == up_color:
        self.move("U U")

      if self.cube.get_cubie(-1, 1, 1).colors[1] == up_color:
        self.move("Ui")

      if (self.cube.get_cubie(-1, 1, 1).colors[2] == up_color and
         self.cube.get_cubie(-1, 1,-1).colors[0]  == up_color and
         self.cube.get_cubie(1, 1, -1).colors[2]  == up_color):
        self.move("Li U R Ui L U Ri")

      if (self.cube.get_cubie(-1, 1, 1).colors[0] == up_color and
         self.cube.get_cubie(-1, 1,-1).colors[2]  == up_color and
         self.cube.get_cubie(1, 1, -1).colors[0]  == up_color):
        self.move("Ri U U R U Ri U R")

    if ((leftFront.colors[1] == up_color and
       rightFront.colors[1]  == up_color and
       leftBack.colors[1]    != up_color and
       rightBack.colors[1]   != up_color) or
       (leftFront.colors[1]  == up_color and
       rightFront.colors[1]  != up_color and
       leftBack.colors[1]    == up_color and
       rightBack.colors[1]   != up_color) or
       (leftFront.colors[1]  != up_color and
       rightFront.colors[1]  != up_color and
       leftBack.colors[1]    == up_color and
       rightBack.colors[1]   == up_color) or
       (leftFront.colors[1]  != up_color and
       rightFront.colors[1]  == up_color and
       leftBack.colors[1]    != up_color and
       rightBack.colors[1]   == up_color) or
       (leftFront.colors[1]  == up_color and
       rightFront.colors[1]  != up_color and
       leftBack.colors[1]    != up_color and
       rightBack.colors[1]   == up_color) or
       (leftFront.colors[1]  != up_color and
       rightFront.colors[1]  == up_color and
       leftBack.colors[1]    == up_color and
       rightBack.colors[1]   != up_color)):

      if (self.cube.get_cubie(1, 1, 1).colors[1] == up_color and
         self.cube.get_cubie(-1, 1,-1).colors[1] == up_color):
        if (self.cube.get_cubie(-1, 1, 1).colors[0] == up_color and
           self.cube.get_cubie(1, 1, -1).colors[2]  == up_color):
          self.move("Ri Fi Li F R Fi L F")
        if (self.cube.get_cubie(-1, 1, 1).colors[2] == up_color and
           self.cube.get_cubie(1, 1, -1).colors[0]  == up_color):
          self.move("F Ri Fi R Mi U R Ui Ri M")

      if (self.cube.get_cubie(-1, 1, 1).colors[1] == up_color and
         self.cube.get_cubie(1, 1, -1).colors[1]  == up_color):
        self.move("U")
        if (self.cube.get_cubie(-1, 1, 1).colors[0] == up_color and
           self.cube.get_cubie(1, 1, -1).colors[2]  == up_color):
          self.move("Ri Fi Li F R Fi L F")
        if (self.cube.get_cubie(-1, 1, 1).colors[2] == up_color and
           self.cube.get_cubie(1, 1, -1).colors[0]  == up_color):
          self.move("F Ri Fi R Mi U R Ui Ri M")

      else:
        if (self.cube.get_cubie(-1, 1, 1).colors[1] != up_color and
           self.cube.get_cubie(-1, 1, -1).colors[1] != up_color):
          self.move("U U")

        if (self.cube.get_cubie(-1, 1, -1).colors[1] != up_color and
           self.cube.get_cubie(1, 1, -1).colors[1]   != up_color):
          self.move("U")

        if (self.cube.get_cubie(-1, 1, 1).colors[1] != up_color and
           self.cube.get_cubie(1, 1, 1).colors[1]   != up_color):
          self.move("Ui")

        if (self.cube.get_cubie(1, 1, 1).colors[2] == up_color and
           self.cube.get_cubie(1, 1, -1).colors[2] == up_color):
          self.move("Ri Fi L F R Fi Li F")

        if (self.cube.get_cubie(1, 1, 1).colors[0] == up_color and
           self.cube.get_cubie(1, 1, -1).colors[0] == up_color):
          self.move("U R R D Ri U U R Di Ri U U Ri")

  def PLL(self):
    self.PLL_solve()
    if self.cube.is_solved() == True:
      return

    tries = 0
    while (self.cube.is_solved() != True):
      self.move("Y")
      self.PLL_solve()
      tries += 1
      if (tries == 4 and self.cube.is_solved() != True):
        self.move("U")
        tries = 0

  def PLL_solve(self):
    frontLeftCorner  = self.cube.find_cubie(self.cube.front_color(), self.cube.left_color(), self.cube.up_color())
    frontRightCorner = self.cube.find_cubie(self.cube.front_color(), self.cube.right_color(), self.cube.up_color())
    backLeftCorner   = self.cube.find_cubie(self.cube.back_color(), self.cube.left_color(), self.cube.up_color())
    backRightCorner  = self.cube.find_cubie(self.cube.back_color(), self.cube.right_color(), self.cube.up_color())

    frontEdge = self.cube.find_cubie(self.cube.up_color(), self.cube.front_color())
    leftEdge  = self.cube.find_cubie(self.cube.up_color(), self.cube.left_color())
    backEdge  = self.cube.find_cubie(self.cube.up_color(), self.cube.back_color())
    rightEdge = self.cube.find_cubie(self.cube.up_color(), self.cube.right_color())

    if (frontEdge.pos == [0, 1, 1]  and
        leftEdge.pos  == [-1, 1, 0] and
        backEdge.pos  == [0, 1, -1] and
        rightEdge.pos == [1, 1, 0]):
      if (frontRightCorner.pos == [1, 1, -1] and
          backLeftCorner.pos   == [1, 1, 1]  and
          backRightCorner.pos  == [-1, 1, -1]):
        self.move("X Ri U Ri D D R Ui Ri D D R R Xi")

      if (frontRightCorner.pos == [-1, 1, 1] and
          frontLeftCorner.pos  == [1, 1, -1] and
          backRightCorner.pos  == [1, 1, 1]):
        self.move("Xi R Ui R D D Ri U R D D R R X")

      if (frontRightCorner.pos == [1, 1, -1]  and
          backRightCorner.pos  == [1, 1, 1]   and
          frontLeftCorner.pos  == [-1, 1, -1] and
          backLeftCorner.pos   == [-1, 1, 1]):
        self.move("Xi R Ui Ri D R U Ri U U Ei Ei Ri U R D Ri Ui R X")

    if (frontRightCorner.pos == [-1, 1, 1] and
        frontLeftCorner.pos  == [-1, 1, -1] and
        backLeftCorner.pos   == [1, 1, 1]):
      if (frontEdge.pos == [0, 1, -1] and
          leftEdge.pos  == [0, 1, 1]  and
          backEdge.pos  == [-1, 1, 0]):
        self.move("Ri Ui R Y R R U Ei Ri U R Ui R Ui E R R")
      elif (frontEdge.pos == [1, 1, 0] and
            leftEdge.pos  == [0, 1, 1] and
            rightEdge.pos == [-1, 1, 0]):
        self.move("R R Ui E R Ui R U Ri U Ei R R Y R Ui Ri")

    if (backRightCorner.pos == [-1, 1, -1] and
        frontLeftCorner.pos == [1, 1, -1]  and
        backLeftCorner.pos  == [-1, 1, 1]):
      if (frontEdge.pos == [-1, 1, 0] and
          leftEdge.pos  == [0, 1, -1] and
          backEdge.pos  == [0, 1, 1]):
        self.move("R U Ri Yi R R Ui E R Ui Ri U Ri U Ei R R")
      elif (rightEdge.pos == [-1, 1, 0] and
            leftEdge.pos  == [0, 1, -1] and
            backEdge.pos  == [1, 1, 0]):
        self.move("R R U Ei Ri U Ri Ui R Ui E R R Yi Ri U R")

    if (frontRightCorner.pos == [1, 1 ,1]   and
        frontLeftCorner.pos  == [-1, 1, 1]  and
        backLeftCorner.pos   == [-1, 1, -1] and
        backRightCorner.pos  == [1, 1, -1]):

      if (rightEdge.pos == [-1, 1, 0] and
          leftEdge.pos  == [0, 1, 1]  and
          frontEdge.pos == [1, 1, 0]):
        self.move("R R U R U Ri Ui Ri Ui Ri U Ri")

      if (rightEdge.pos == [0, 1, 1] and
          leftEdge.pos  == [1, 1, 0] and
          frontEdge.pos == [-1, 1, 0]):
        self.move("R Ui R U R U R Ui Ri Ui R R")

      if (rightEdge.pos == [-1, 1, 0] and
          leftEdge.pos  == [1, 1, 0]  and
          frontEdge.pos == [0, 1, -1] and
          backEdge.pos  == [0, 1, 1]):
        self.move("M M U M M U U M M U M M")

      if (rightEdge.pos == [0, 1, 1]  and
          leftEdge.pos  == [0, 1, -1] and
          frontEdge.pos == [1, 1, 0]  and
          backEdge.pos  == [-1, 1, 0]):
        self.move("M M U M M U Mi U U M M U U Mi U U")

    if (rightEdge.pos == [-1, 1, 0] and
        leftEdge.pos  == [1, 1, 0]):
      if (frontRightCorner.pos == [1, 1, -1] and
          backRightCorner.pos  == [1, 1, 1]):
        self.move("R U Ri Ui Ri F R R Ui Ri Ui R U Ri Fi")
      if (frontRightCorner.pos == [-1, 1, 1] and
          frontLeftCorner.pos  == [1, 1, 1]):
        self.move("Ri U U Ri Di Ei Ri Fi R R Ui Ri U Ri F R Ui F")

    if (frontEdge.pos == [0, 1, -1] and
        backEdge.pos  == [0, 1, 1]):
      if (frontRightCorner.pos == [-1, 1, -1] and
          backLeftCorner.pos   == [1, 1, 1]):
        self.move("L Ui R U U Li U Ri L Ui R U U Li U Ri U")
      if (backRightCorner.pos == [-1, 1, 1] and
          frontLeftCorner.pos == [1, 1, -1]):
        self.move("Ri U Li U U R Ui L Ri U Li U U R Ui L Ui")

    if (frontRightCorner.pos == [-1, 1, -1] and
        backLeftCorner.pos   == [1, 1, 1]):
      if (backEdge.pos == [-1, 1, 0] and
          leftEdge.pos == [0, 1, -1]):
        self.move("F R Ui Ri Ui R U Ri Fi R U Ri Ui Ri F R Fi")
      if (backEdge.pos  == [1, 1, 0] and
          rightEdge.pos == [0, 1, -1]):
        self.move("Ri U Ri Di Ei Ri Fi R R Ui Ri U Ri F R F")

    if (frontRightCorner.pos == [1, 1, -1] and
        backRightCorner.pos  == [1, 1, 1]  and
        frontEdge.pos        == [1, 1, 0]  and
        rightEdge.pos        == [0, 1, 1]):
      self.move("R U Ri Fi R U Ri Ui Ri F R R Ui Ri Ui")

    if (backRightCorner.pos == [-1, 1, -1] and
        backLeftCorner.pos  == [1, 1, -1]):
      if (backEdge.pos == [-1, 1, 0] and
          leftEdge.pos == [0, 1, -1]):
        self.move("Ri U Li U U R Ui Ri U U R L Ui")
      if (frontEdge.pos == [-1, 1, 0] and
          leftEdge.pos  == [0, 1, 1]):
        self.move("L U U Li U U L Fi Li Ui L U L F L L U")
      if (frontEdge.pos == [1, 1, 0] and
          rightEdge.pos == [0, 1, 1]):
        self.move("Ri U U R U U Ri F R U Ri Ui Ri Fi R R Ui")

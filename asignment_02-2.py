# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from cs1robots import *
load_world('worlds/ex36.rur.wld')
gshs = Robot()
gshs.set_trace(color='blue')

def turn_right():
    gshs.turn_left()
    gshs.turn_left()
    gshs.turn_left()

def turn_around():
    gshs.turn_left()
    gshs.turn_left()

def climb_up_1_stair():
    gshs.turn_left()
    gshs.move()
    gshs.turn_right()
    gshs.move()
    gshs.move()

def climb_up_4_stairs():
    climb_up_1_stair()
    climb_up_1_stair()
    climb_up_1_stair()
    climb_up_1_stair()

def exercise_1():
    gshs.move()
    gshs.turn_left()
    gshs.move()
    turn_right()
    gshs.move()
    turn_right()
    gshs.move()
    gshs.turn_left()

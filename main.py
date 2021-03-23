# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from cs1robots import *
load_world('worlds/harvest1.wld')
gshs = Robot()
gshs.set_trace('blue')

def turn_right():
    gshs.turn_left()
    gshs.turn_left()
    gshs.turn_left()
def move_1(n):
    for i in range(n) :
        gshs.move()
def turn_around():
    gshs.turn_left()
    gshs.turn_left()

def exercise_2(j, i):
    move_1(j)
    gshs.turn_left()
    move_1(i)
    gshs.pick_beeper()
    turn_around()
    move_1(i)
    turn_right()
    move_1(j)
    turn_around()

for i in range(6):
    for j in range(1, 7):
        exercise_2(j, i)
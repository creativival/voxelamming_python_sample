from turtle import Turtle, setup
from time import sleep

t = Turtle()

setup(600,400,None,None)

for _ in range(4):
    t.forward(100)  # 100歩前進
    t.right(90)     # 右に90度回転

sleep(10)
import math
import numpy as np
import random as rd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def mkFfield(x,y):
    fx = fxBase2
    fy = fyBase2 * y
    return fx, fy

def mkPoint(maxX,maxY):
    x = rd.uniform(-maxX,maxX)
    y = rd.uniform(-maxY,maxY)
    return x,y

interval1 = 30
fxBase1 = 30
fyBase1 = 10
fxBase2 = fxBase1/interval1
fyBase2 = fyBase1/interval1
n = 2
maxX = 0.2
maxY = 0.5


def step(points):
    for i in range(len(points)):
        x=points[i][0]
        y=points[i][1]
        vx = points[i][2]
        vy = points[i][3]
        fx, fy = mkFfield(x,y)
        points[i][2] = points[i][2]+fx
        points[i][3] = points[i][3]+fy
        points[i][0] = points[i][0]+points[i][2]
        points[i][1] = points[i][1]+points[i][3]
    for i in range(n):
        x, y = mkPoint(maxX, maxY)
        points.append([x, y, 0, 0])
    return points



fig, ax = plt.subplots()
point, = ax.plot([], [], "o", color="blue")

# 表示範囲
ax.set_xlim(-1, 30)
ax.set_ylim(-10, 10)


# 座標を更新する関数
def update(frame,points):
    global x, y

    points=step(points)
    new_x = []
    new_y = []
    for i in range(len(points)):
        new_x.append(points[i][0])
        new_y.append(points[i][1])
    point.set_data(new_x, new_y)
    return point,


# 500ms = 0.5秒ごとに更新

points = [[0, 0, 0, 0]]
ani = FuncAnimation(
    fig,
    update,
    fargs=(points,),
    interval=interval1
)

plt.show()
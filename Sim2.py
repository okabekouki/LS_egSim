import math
import numpy as np
import random as rd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def mkFfield(x,y):
    xc = x-FMx
    yc = y-FMy
    r = math.sqrt(xc**2+yc**2)
    rot = -FMrot + math.atan2(yc, xc)
    xc = r*math.cos(rot)
    yc = r*math.sin(rot)
    Area = math.fabs(cArea * xc**nArea)
    
    fx = cStr / (((math.fabs(yc)/(Area))**nF+1)*Area)
    fy = 0
    fr = math.sqrt(fx**2+fy**2)
    frot = math.atan2(fy, fx)
    rot = frot + FMrot
    fx = fr*math.cos(rot)
    fy = fr*math.sin(rot)
    return fx,fy

def mkPoint(maxX,maxY):
    x = rd.uniform(-maxX,maxX)
    y = rd.uniform(-maxY,maxY)
    vx = rd.uniform(minVX,maxVX)
    vy = rd.uniform(minVY,maxVY)
    return x,y,vx,vy

interval1 = 30
n = 2
maxX = 0.2
maxY = 0.5
maxVX = 1
minVX = 0.5
maxVY = 0.2
minVY = -0.2

cArea = 0.2
cStr = 0.5
FMx = 3
FMy = 5
FMrot = math.radians(-60)
nF = 3
nArea = 1

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
        x, y, vx, vy = mkPoint(maxX, maxY)
        points.append([x, y, vx, vy])
    return points



fig, ax = plt.subplots()

X, Y = np.meshgrid(
    np.linspace(-1,20,20),
    np.linspace(-20,2,20)
)

U = np.zeros_like(X)
V = np.zeros_like(Y)

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        U[i,j], V[i,j] = mkFfield(X[i,j],Y[i,j])

field = ax.quiver(X,Y,U,V)

point, = ax.plot([], [], "o", color="blue")

# 表示範囲
ax.set_xlim(-1, 20)
ax.set_ylim(-20, 2)


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
import math
import numpy as np
import random as rd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 力場パラメータ
cArea = [0.2,0.1]
cStr = [0.5,0.5]
FMx = [3,3]
FMy = [5,-5]
FMrot = [-60,60]
FMrot = [math.radians(i) for i in FMrot]
nF = 3
nArea = 1


def mkFbase(xc,yc,i):
    # i番目の力場放射器の力場を位置関係なく求める
    Area = math.fabs(cArea[i] * xc**nArea)
    Fx = cStr[i] / (((math.fabs(yc)/(Area))**nF+1)*Area)
    Fy = 0
    return Fx,Fy

def mkF1(x, y, i):
    # i番目のFMx,FMyにあるFMrotの向きの力場放射器を
    # x=0,y=0,x軸正の向きに放射されている座標系へ変換する
    dx = x - FMx[i]
    dy = y - FMy[i]

    theta = FMrot[i]
    cos_t = math.cos(-theta)
    sin_t = math.sin(-theta)
    R = np.array([[cos_t, -sin_t], [sin_t, cos_t]])

    xc, yc = R.dot(np.array([dx, dy]))
    Fx,Fy = mkFbase(xc,yc,i)
    
    Rin = np.array([[cos_t, sin_t], [-sin_t, cos_t]])
    Fx, Fy = Rin.dot(np.array([Fx, Fy]))
    return Fx,Fy

def mkF2(x,y):
    # i個の力場の重ね合わせを作る．
    F = np.array([0,0])
    for i in range(len(cStr)):
        F = F + np.array([mkF1(x,y,i)])
    return F

print(mkF2(1,2))
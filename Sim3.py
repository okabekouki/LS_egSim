import math
import numpy as np
import random as rd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 力場パラメータ
dim = 2

cArea = np.array([0.2,0.1])
cStr = np.array([0.5,0.5])
# FMは力場放射器のx,y,rotを持つ
FM = np.array([
    [3,5,-60],
    [3,-5,60]
    ], dtype=float)
FM[:,2] = np.radians(FM[:,2])
# print(FM)

nF = 3
nArea = 1


def mkFbase(r,i):
    # i番目の力場放射器の力場を位置関係なく求める
    Area = math.fabs(cArea[i] * r[0]**nArea) + 1e-6 #0除算対策
    R = math.sqrt(r[1]**2)
    F = np.array([cStr[i] / (((math.fabs(R)/(Area))**nF+1)*Area),
                  0])
    return F

def mkF1(r, i):
    # i番目のFMx,FMyにあるFMrotの向きの力場放射器を
    # x=0,y=0,x軸正の向きに放射されている座標系へ変換する
    dr = r - FM[i,:2]

    theta = FM[i,2]
    cos_t = math.cos(-theta)
    sin_t = math.sin(-theta)
    R = np.array([[cos_t, -sin_t], [sin_t, cos_t]])
    Rin = np.array([[cos_t, sin_t], [-sin_t, cos_t]])
    rc = R.dot(dr)
    F = mkFbase(rc,i)
    
    F = Rin.dot(F)
    return F

def mkF2(r):
    # i個の力場の重ね合わせを作る．
    F = np.array([0,0])
    for i in range(len(cStr)):
        F = F + mkF1(r,i)
    return F

r = np.array([1,2])
print(mkF2(r))
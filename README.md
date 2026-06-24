# LS_egSim
LS's engine simulation.

### sim1
sim1 is test file.
There is two dimension space.And some points move and thrust on it.

### sim2
「sim1では力場によって加速される点」が実現可能かを考えていたが，今回は力場の形状を現実に寄せる事を考えている．\\
$$F=\frac{1}{A} \frac{c}{(\frac{|y|}{A})^3+1}$$\\
という，
- x軸を中心軸とする力場
- 力場放射器からx軸方向に力場の広がりが減衰していくことを示す$A(x)$という関数
- 中心軸垂直な断面での力場勾配$F$の積分は$A(x)$に依存せず保存される．ただし二次元空間を想定．
- 中心軸垂直な断面での力場勾配$F$は中心からの距離$y$の三乗に反比例する．\\
などを満たしている．
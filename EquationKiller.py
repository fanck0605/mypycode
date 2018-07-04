# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    return x1, x2

a = float(input('请输入x的二次项系数：'))
b = float(input('请输入x的一次项系数：'))
c = float(input('请输入常数项系数：'))
x1, x2=quadratic(a, b, c)

print('x1 =',x1,', x2 =',x2)

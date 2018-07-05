# -*- coding: utf-8 -*-
#Copyright © 2018 Chuck

def errjg(x):
    if x>0:
        return x
    else:
        s = int(input('请您输入正确的成绩: '))
        return errjg(s)

s1 = errjg(int(input('请您输入上次的成绩: ')))
s2 = errjg(int(input('请您输入本次的成绩: ')))

up = (s2-s1)*100/s1
if up > 0:
    print('恭喜, 您的成绩提升了%.1f%%！' % up)
elif up < 0:
    dw = -up
    print('很不幸, 您的成绩下降了%.1f%%！' % dw)
else:
    print('不错，您的成绩保持不变！')

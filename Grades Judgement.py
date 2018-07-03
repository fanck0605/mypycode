# -*- coding: utf-8 -*-
#Copyright © 2018 Chuck

s1 = int(input('请输入您上次的成绩: '))
s2 = int(input('请输入您本次的成绩: '))

up = (s2-s1)*100/s1
if up < 0:
    dw = -up
    print('很不幸, 您的成绩下降了%.2f%%！' % dw)
else:
    if up > 0:
        print('恭喜, 您的成绩提升了%.2f%%！' % up)
    else:
        print('不错，您的成绩保持不变！')

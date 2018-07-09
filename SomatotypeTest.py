# -*- coding: utf-8 -*-
#Copyright © 2018 Chuck

print('欢迎测试！\n')

height = float(input('请输入您的身高(m): '))
weight = float(input('请输入您的体重(kg): '))

bmi = weight/(height*height)
print('\nBMI: %.1f' % bmi)
if bmi > 32:
    print('严重肥胖')
elif bmi > 28:
    print('肥胖')
elif bmi > 25:
    print('过重')
elif bmi > 18.5:
    print('正常')
else:
    print('过轻')

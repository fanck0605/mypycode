# -*- coding: utf-8 -*-
def trim(s):
#法一
#    i=0
#    j=len(s)
#    while s[i:i+1]==' ':
#        i+=1
#    while s[j-1:j]==' ':
#        j-=1
#    return s[i:j]
#法二
    while s[:1]==' ':
        s=s[1:]
    while s[-1:]== ' ':
        s=s[:-1]
    return s
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

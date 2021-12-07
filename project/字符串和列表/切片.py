'''
切片：字符串，列表
格式:字符串变量[start,end]
字符串变量[start,end,step] 默认是从左向右一个一个去元素
step:
1.步长
2.方向       step     正数      从左网页
            step     负数      从右往左
'''
s = 'ABCDEFG'

print(s[1:5]) # BCDE
print(s[:5])  # ABCDE
print(s[:])

x  = s[:]
print(x)
print(s)

print('*-' * 20)
print(s[:-1:2])
print(s[1::2])
print(s[::4])

print('*-' * 10)
print(s[0:6:-2]) #方向想同不能进行
print(s[6::-2])
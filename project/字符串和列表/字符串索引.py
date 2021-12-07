s1 = 'hello'
s2 = s1
s3 = 'hello'
s4 = 'hello1'

print(s1,s2,s3,s4)

print(id(s1))
print(id(s2))
print(id(s3))
print(id(s4))
#is 比较地址了，运算符
print(s1 is s4)

# 字符串 截取

s1 = 'ABCDEFG'

print(s1[3])
print(s1[-3])
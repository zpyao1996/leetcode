a=[[] for _ in range(5)]
print(a)

a='abcde'
a=a.strip('a')
print(a)
s='{name} is {age} years old'
s=s.format(name='Alfred',age=15)
print(s)

print(isinstance('abc',(str,bytes)))
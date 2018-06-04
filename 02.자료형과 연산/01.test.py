a = 3
b = 2
print(a + b);
print(a - b);
print(a * b);
print(a / b);
print(a % b);
print(a ** b);
print(a // b);

if a > 10:
    print(a + 10)
else:
    if a > 2:
        print(a * b)
    else:
        a = 5
        print('a == ', a)
print(a * b)
print(type(10))
print(type(10.1))
print(type('b'))

print(id(a))
a = 5;  # 상수객체 5를 참조한다 -> id가 변경됨

print(id(a))
print(id(b))

print(isinstance(a, int))
print(isinstance(a, float))
print("-------------------------")

# 같은 객체 공간 반환
c = d = []

print(id(c))
print(id(d))

# 다른 객체 공간 반환
c = []
d = []
print(id(c))
print(id(d))
print(type(c))
print(type(d))

print(c == d)   # True : 값 비교
print(id(c) == id(d))   # False : 고유번호 비교

c.append(1)
d.append(1)

print(id(c[0]))
print(id(d[0]))
print(id(1))

del a
print(dir())
print(globals())
print(locals())
# print(a)

print(1, 2, 3, sep='.', end='?'); print(1, 2, 3, sep='/', end='!');print(1, 2, 3, sep=',', end='g');


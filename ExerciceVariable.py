b = 10

def f1():
    global b
    b = 3

def f2(p,q) :
    global b
    return p + q + b

f1()
res = f2(1,2)
print(res)

x = ["apple", "banana", "lemon", "orange"]
del x[0]
print(x)

x = ["apple", "banana", "lemon", "orange"]
del x[3]
print(x)

x = ["apple", "banana", "lemon", "orange"]
del x[2]
print(x)



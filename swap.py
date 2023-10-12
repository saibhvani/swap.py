#swap program
x = 50
y = 100
temp = x
x = y
y = temp
print("value of x:", x)
print("value of y:", y)

x = 300
y = 500
temp = y
y = x
x = temp
print("value of x:", x)
print("value of y:", y)


#fibonnaic series

a = 5
b = 3
n = 10
i = 1
while i <= n:
    print(b)
    a = a + b
    b = a - b
    i += 1
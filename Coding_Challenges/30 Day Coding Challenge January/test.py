a = 1.5
b = -0.5
for C in range(100, 102):
    x = C
    n = 50
    for i in range(n):
        x = x * a + b
    print(x, end=" ")
    print(a**n * C + b*((a**n - 1) / a-1))

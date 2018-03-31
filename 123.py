def hailstone(n):
    yield n
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3+1
        n = int(n)
        yield n


for i in hailstone(10):
    print(i)

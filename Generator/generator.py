def gen(n):
    for i in range(n):
        yield i

g = gen(895)

print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
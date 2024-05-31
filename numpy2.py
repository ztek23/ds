import numpy as np

a = np.array([1, 2, 3, 4])
print(a[1:4])
print(a[:4])
print(a[1:])
print(a[1:4:2])
print(a[4:1:-1])
print(a[:-1])

multi = np.array([[4,5,6],[7,8,9],[1,2,3]])
print(multi[0:10:1])

print(a*2)

ab = np.array([5,7,8,9])
print(ab[ab%2==0])
print(ab[ab==5])
c = ab[ab==5]
print(c)
print(ab[[1,3]])
ab+=5
print(ab)
a+=ab
print(a)

def solve(a):
    return 2*a+3
y = solve(ab)
print(y)
print(np.random.permutation(np.arange(16)))
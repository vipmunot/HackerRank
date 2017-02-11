n,d = input().split(' ')
n = int(n)
d = int(d)
a = [int(v) for v in input().split(' ')]
def left_rotation(a,n,d):
    return a[d:] + a[:d]
result = left_rotation(a,n,d)
print(*result,sep=' ')
     
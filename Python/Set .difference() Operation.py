n = int(input())
s = set(map(int,input().split()))
m = int(input())
t = set(map(int,input().split()))
u = s.difference(t)
print(len(u))    
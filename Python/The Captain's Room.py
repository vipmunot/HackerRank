from collections import Counter
n = int(input())
a = list(map(int,input().split()))
count = Counter(a)
for keys,values in count.items():
    if values == 1:
        print(keys)
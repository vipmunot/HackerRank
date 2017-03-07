n = int(input())
s = list(map(int,input().split()))
for i in range(1,len(s)):
    curr = s[i]
    pos = i
    while pos>0 and s[pos-1]>curr:
        s[pos] = s[pos-1]
        pos -=1
        print (" ".join(map(str, s)))
    s[pos] = curr
print (" ".join(map(str, s)))   
    
    
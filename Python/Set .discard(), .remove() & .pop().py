n = int(input())
s = set(map(int, input().split())) 
lines = int(input())
for i in range(lines):
    query = input()
    if query == 'pop': s.pop()
    elif 'remove' in query:
        q = query.split()
        s.remove(int(q[1]))
    elif 'discard' in query:
        q = query.split()
        s.discard(int(q[1]))
        
print(sum(s)) 
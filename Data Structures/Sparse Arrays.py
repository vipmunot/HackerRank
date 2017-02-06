n = int(input())
arr = []
for i in range(n):
    arr.append(input())
q = int(input())    
for i in range(q):
    query = input()
    count = 0
    for j in range(len(arr)):
        if arr[j] == query:
            count +=1
    print(count)
    
    
def reveresed(number):
    a = str(number)[::-1]
    return(int(a))
i,j,k = input().strip().split(' ')
i,j,k = [int(i),int(j),int(k)]
lst = [x for x in range(i,j+1)]
result = 0
for i in range(len(lst)):
    if(abs(lst[i] - reveresed(lst[i]))%k == 0):
        result+=1
print(result)
    
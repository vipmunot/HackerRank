t=int(input())
for i in range(t):
    string =input()
    print (''.join([string[i] for i in range(0,len(string),2)])+" "+''.join([string[i] for i in range(1,len(string),2)]))
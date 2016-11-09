n = int(input())
phone = {}
for i in range(n):
    a = input().split(' ')
    phone[a[0]]=a[1]
i = 0
while True:
    try:
        name = str(input())
        # or a try-except statement depending on the kind of input
        if not name:
            break
        if name in phone.keys():
            string = name +'='+ str(phone[name])
            print(string)
            i += 1
        else:
            print("Not found")
            i += 1
    except:
        break
T = int(input())

while T>0:
    sen = input().split()
    flag = 0
    for word in sen:
        if word=="not":
            flag = 1
            break
    if flag==1:
        print("Real Fancy")
    else:
        print("regularly fancy")
    T=T-1

def encrypt(flag):
    
    flagList = list(flag)

    for i in range(0, len(flag)):
        flagList[i] = ord(flagList[i])*3

    n1=len(flag)//2
    f1=flagList[n1:0:-1]
    f1.insert(n1,flagList[0])
    f2=flagList[n1+1:len(flag)]
    f3=f1+f2
    return (f3)

flagRead = open("flag.txt", "r")
flag = flagRead.read()

print(encrypt(flag))


    

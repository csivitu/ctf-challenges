def decrypt(rev):
    rev1=rev[0:len(rev)//2+1]
    f1=rev1[::-1]
    f2=rev[len(rev)//2+1:]

    f3=f1+f2
    i=0
    for i in range(len(rev)):
        f3[i]=chr(f3[i]//3)

    return(''.join(f3))

rev = [285, 312, 348, 156, 348, 369, 306, 348, 297, 315, 345, 297, 357, 156, 345, 285, 339, 351, 147, 297, 321, 99, 375]

print(decrypt(rev))


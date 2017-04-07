"""
cryptography.py
Author: Emma Supattapone
Credit:***** >>> ***** ABBY FEYRER ***** <<< *****        (and Mr. Dennison)

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
nn=list(associations)

x = 1
while x == 1: 
    ham = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if ham == "e":
        y = input("Messege: ")
        g = input("Key: ")
        y = list(y)
        g = list(g)
        m = []
        for x in y:
            m.append(associations.find(x))
        n = []
        for x in g:
            n.append(associations.find(x))
        i=0
        j=0
        while i<len(m):
            b=m[i]+n[j]
            if b>=len(nn)-1:
                b=b-len(nn)
            m[i]=nn[b]
            i=i+1
            j=j+1
            if j >=len(n)-1:
                j=j-len(n)
        for x in m:
            print(x,end="")
        print(" ")
        x=1
    elif ham == "d":
        z = input("Message: ")
        g = input("Key: ")
        z = list(z)
        g = list(g)
        u = []
        for x in z:
            u.append(associations.find(x))
        n = []
        for x in g:
            n.append(associations.find(x))
        k=0
        j=0
        while k<len(u):
            t=u[k]-n[j]
            if t>=len(nn)-1:
                t=t-len(nn)
            u[k]=nn[t]
            k=k+1
            j=j+1
            if j >=len(n)-1:
                j=j-len(n)
        for x in u:
            print(x,end="")
        print(" ")
        x=1
    elif ham == "q":
#        print("Goodbye!")
#        print(" ")
        x = 2
    else:
        print("Did not understand command, try again.")
        x=1
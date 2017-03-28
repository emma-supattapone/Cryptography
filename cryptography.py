"""
cryptography.py
Author: Emma Supattapone
Credit: Abby Feyrer and Mr. Dennison

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
"""
x = 1
while x == 1: 
    ham = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if ham == "e":
        mesg = input("Message: ")
        mesg = list(mesg)
        mesg = str(mesg)
        mesge = associations.find(mesg)
        print(mesge)
        kye = associations.find(ky)
        print(kye)
    elif ham == "d":
        mesgg = input("Message: ")
        kyy = input("Key: ")
        print("decrypt")
    elif ham == "q":
        print("Goodbye!")
        x = 2
    else:
        print("Did not understand command, try again.")
"""

y = input("Messege: ")
g = input("Key: ")
y = list(y)
g = list(g)

m = []
for x in y:
    m.append(associations.find(x))
print(m)

n = []
for x in g:
    n.append(associations.find(x))
print(n)


i = len(y)
print(i)
j = len(g)
print(j)

if i > j:
    w = i / j
    mm = w * m
    print(mm)
    mn = zip(mm,n)
    print(list(mn))
elif j > i:
    k = j / i
    nn = k * n
    mn = zip(m,nn)
    print(list(mn))
else:
    mn = zip(m,n)
    print(list(mn))

#print(y)
#print(g)

u = 15 % 3
print(u)

#for e in g:
#    g = associations.find(e)
#print(g)

#associations[index]
#print(p)

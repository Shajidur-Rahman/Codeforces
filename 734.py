a = int(input())
b = input()

A = 0
D = 0

for i in range(0,a):
    if b[i] == "A":
        A = A+1
    else:
        D = D+1

if A>D:
    print("Anton")
elif D>A:
    print("Danik")
else:
    print("Friendship")
#https://www.acmicpc.net/problem/1929

def sosu(A):

    if 2 in A:
        print(2)
    for i in A:
        a=i+1-i//2
        for n in range(2,a):
            if i%n==0:break
            elif i//n<2:
                print(i)

A=[]
x,y=map(int,input().split())
for i in range(x,y+1):
    A.append(i)
sosu(A)

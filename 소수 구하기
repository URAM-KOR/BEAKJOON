#https://www.acmicpc.net/problem/1929

def sosu(A):
    for i in A:
        for n in range(2,i+1):
            if i%n == 0:
                if n==i:
                    print(i)
                else:break
            elif i//n != 1:
                continue
A=[]
x,y=map(int,input().split())
for i in range(x,y+1):
    A.append(i)
sosu(A)

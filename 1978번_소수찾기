#https://www.acmicpc.net/problem/1978

def sosu(A):
    B=[]
    for i in A:
        for n in range(2,i+1):
            if i%n == 0:
                if n==i:
                    B.append(i)
                else:break
            elif i//n != 1:
                continue
    return(print(len(B)))
A=[]
input()
for i in (map(int,input().split())):
    A.append(i)
sosu(A)

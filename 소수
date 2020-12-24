#https://www.acmicpc.net/problem/2581

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
    if len(B)==0:
        B=-1
        return print(B)
    else:return print((sum(B)),(min(B)),sep='\n')
A=[]

for i in range(int(input()),int(input())+1):
    A.append(i)
sosu(A)
 

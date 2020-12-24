#https://www.acmicpc.net/problem/1929

#https://www.acmicpc.net/problem/1929

A=[]
B=[]
a=()
x,y=map(int,input().split())
A = range(2, y + 1)
for i in range(x,y+1):
    B.append(i)
    if 1 in B:
        B.remove(1)
for j in range(len(A)):
    for k in B:
        if k%A[j]==0:
            if A[j] in B:
                a=A[j]
            B.remove(k)
            try:
                if A[j] not in B:
                    B.append(a)
            except:continue
print(A)
#print(A)

N = int(input())
A = list(map(int, input().split(' '))) 
B = list(map(int, input().split(' '))) 

a = []

for i in range (N):
    a.append(A[i] - B[i])
    result = " ".join(map(str,a))

print(result)

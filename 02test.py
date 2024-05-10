N, L = list(map(int, input().split()))

num = []
for a in range(L):
    num.append(list(map(int,input().split())))

num_transposed = [list(x) for x in zip(*num)]

M=[0]*L

for i in range (N):
   M[num_transposed[i].index(max(num_transposed[i]))] += 1

print(f"{M.index(max(M)) + 1} {(max(M))}")


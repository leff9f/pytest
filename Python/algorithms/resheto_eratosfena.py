N = 50000000
A = [True]*N
A[0] = A[1] = False
for k in range(2, N):
    if A[k]:
        for m in range(k*2, N, k):
            A[m] = False

for k in range(N):
    if A[k]:
        print(k)

with open('input.txt', 'r') as file:
    data = file.read().strip().split()

T = int(data[0])
inx = 1
results = []
for case in range(1, T + 1):
    N = int(data[inx])
    inx += 1 
    A = []
    for i in range(N):
        A.append(int(data[inx]))
        inx += 1
    max = 0
    for i in range(N - 1):
        if abs(A[i] - A[i + 1]) > max:
            max = abs(A[i] - A[i + 1])
    results.append(f"Case #{case}: {max}")

with open('output.txt', 'w') as file:
    file.write('\n'.join(results))
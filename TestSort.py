import time

arr = [1000, 1999, 342, 645, 545, 32, 15, 363, 25, 141, 2, 4,213,44,12,414,88,45,78]
print(arr)
start_time = time.time()
for i in range(0, len(arr)):
    print(arr[i], end=" ")

n1 = 0
s = 0
while n1 < len(arr):
    for n in range(0, len(arr) - 1):
        if arr[n] >= arr[n + 1]:
            swap = arr[n]
            arr[n] = arr[n + 1]
            arr[n + 1] = swap
            s = 1
        print(n1, arr)
    if (s == 0):
        break
    s = 0
    n1 = n1 + 1
print("\n")
print(arr)
end_time = time.time()
execution_time = start_time - end_time
print("\n time taken :", execution_time)

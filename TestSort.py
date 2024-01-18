arr = [1000, 1999, 342, 645, 545, 32, 15, 363, 25, 141, 2, 4]
print(arr)

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

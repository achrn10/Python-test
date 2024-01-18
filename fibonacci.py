val = input("Enter length of Fibonacci series : ")
lst = []
lst = [0,1]
n = 1
f = open("demofile2.txt", "a")
f.write("Now the file has more content!\n\n")

for i in range(1, int(val)-1):
    n = n + lst[i-1]
    lst.append (n)

f.write(str(lst)+ "\n")
print(lst)
f.close()

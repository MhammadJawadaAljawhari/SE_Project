#a
st = input("Enter integers separated by spaces: ")

L = [int(x) for x in st.split()]

isSorted = True
for i in range(1, len(L)):
    if L[i] < L[i-1]:
        isSorted = False
        break

if isSorted:
    print("YES: input is sorted")
else:
    print("NO: input is not sorted")

#b
n = int(input("Enter the number of integers: "))

isSorted = True
prev = int(input("Enter an integer: "))
for i in range(1, n):
    curr = int(input("Enter an integer: "))
    if curr < prev:
        isSorted = False
        break
    prev = curr

if isSorted:
    print("YES: input is sorted")
else:
    print("NO: input is not sorted")
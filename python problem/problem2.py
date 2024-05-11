#a
st1 = input("Enter the integers in the first sequence separated by spaces: ")

L1 = [int(x) for x in st1.split()]

st2 = input("Enter the integers in the second sequence separated by spaces: ")

L2 = [int(x) for x in st2.split()]

if len(L1) != len(L2):
    print("Sequences are not equal")
else:
    i = 0
    while i < len(L1) and L1[i] == L2[i]:
        i += 1
    if i == len(L1):
        print("Sequences are equal")
    else:
        print("Sequences are not equal")

#b

st1 = input("Enter the integers in the first sequence separated by spaces: ")

L1 = [int(x) for x in st1.split()]

st2 = input("Enter the integers in the second sequence separated by spaces: ")

L2 = [int(x) for x in st2.split()]

if L1 == L2:
    print("Sequences are equal")
else:
    print("Sequences are not equal")

#c
seq1_str = input("Enter the integers in the first sequence separated by spaces: ")
seq1 = seq1_str.split()
seq1 = [int(x) for x in seq1]

seq2_str = input("Enter the integers in the second sequence separated by spaces: ")
seq2 = seq2_str.split()
seq2 = [int(x) for x in seq2]

if len(seq1) != len(seq2):
    print("NO: Second sequence is not a permutation of the first")
else:
    seq1_counts = [0] * len(seq1)
    for i in range(len(seq2)):
        if seq2[i] not in seq1:
            print("NO: Second sequence is not a permutation of the first")
            break
        else:
            j = seq1.index(seq2[i])
            seq1_counts[j] += 1
    if seq1_counts.count(1) == len(seq1):
        print("YES: Second sequence is a permutation of the first")
    else:
        print("NO: Second sequence is not a permutation of the first")
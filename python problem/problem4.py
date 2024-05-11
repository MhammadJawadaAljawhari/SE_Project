s = input("Enter string: ")
n = len(s)
is_palindrome = True

for i in range(n//2):
    if s[i] != s[n-i-1]:
        is_palindrome = False
        break

if is_palindrome:
    print("YES palindrome")
else:
    print("NOT a palindrome")
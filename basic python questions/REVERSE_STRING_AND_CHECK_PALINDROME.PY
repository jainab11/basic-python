word = "madam"
rev = ""

for i in word:
    rev = i + rev

if rev == word:
    print("This is a palindrome")
else:
    print("Not a palindrome")

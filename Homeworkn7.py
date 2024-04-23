x = "level"
z = ""
result = True

for i in range(len(x),0,-1):
    z += x[i-1]

if z == x:
    print(x, "is palindrome")
else:
    print(x, "is not a palindrome")
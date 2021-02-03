n = int(input("Enter the number : "))
i = 2
j = 0
while i <= n/2 :
    if n % i == 0 :
        j = j + 1
        break
    i = i + 1

if j == 0 or n == 2:
    print("Prime number")
else:
    print("Not prime number")
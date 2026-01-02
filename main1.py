l = int(input("Enter a upper range"))
u = int(input("Enter a lower range"))
print("prime numbers are")
for num in range(l,u +1):
    if num > 1:
        for i in range(2,num):
            if(num % i) == 0:
                break
        else:
            print(num)
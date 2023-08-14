def PrimeChecker(number):
    prime = [2,3,5,7]
    if num in prime:
        print(f"{num} is a Prime.")
    else:
        primeCheck = True
        for n in prime:
            if (num%n == 0):
                print(f"{num} is not a Prime.")
                primeCheck =False
                break
        
        if (primeCheck):
            print(f"{num} is a Prime.")

def Prime_Check(number):
    is_prime = True
    for i in range(2,number):
        if number%i ==0:
            is_prime = False
    if is_prime:
        print("Prime")
    else:
        print("Not a Prime.")

num = int(input("Enter a number to check : "))
PrimeChecker(num)
Prime_Check(num)

    
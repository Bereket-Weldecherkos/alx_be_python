size = int(input("Enter the size of the pattern: "))
amount = size
while amount > 0:
    for count in range(size):
        print("*", end="")
    print()
    amount -= 1
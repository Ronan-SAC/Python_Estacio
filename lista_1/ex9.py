try:
    name = input("What's your name?: ")
    test1 = float(input("Insert test 1 note: "))
    test2 = float(input("Insert test 2 note: "))
    test3 = float(input("Insert test 3 note: "))
    average = (test1 + test2 + test3) / 3
    if average >= 6:
        print("Name: ", name)
        print("Average: ", average)
        print("Approved")
    else:
        print("Name: ", name)
        print("Average: ", average)
        print("Failed")
except ValueError:
    print("Invalid number")
# Program to check voting eligibility of 5 people

for i in range(1, 6):
    age = int(input("Enter age of person " + str(i) + ": "))

    if age >= 18:
        print("Person", i, "is eligible to vote.")
    else:
        print("Person", i, "is NOT eligible to vote.")

    print()   # blank line for readability
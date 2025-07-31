# Hour 2: Control Flow

#########Tutorial Begins############

''''
🔁 1. if, elif, else
    Python uses indentation instead of braces:
    
    x = 10
    if x > 10:
        print("Greater than 10")
    elif x == 10:
        print("Exactly 10")
    else:
        print("Less than 10")


🔄 2. while Loops
    
    count = 0
    while count < 5:
        print(f"Count is {count}")
        count += 1


🔂 3. for Loops with range()
    
    for i in range(5):  # 0 to 4
    print(i)
    
    One can also loop over lists, strings, etc.:
    for char in "Python":
        print(char)


🧰 4. Useful Loop Tools
    
    enumerate() — get index and value
    zip() — iterate over multiple sequences
    break, continue, pass
    names = ["Alice", "Bob", "Charlie"]
    for i, name in enumerate(names):
        print(f"{i}: {name}")

'''

#########Tutorial Ends############

'''
✅ Mini Exercise
Write a program that:

Asks the user for a number.
Prints whether it’s positive, negative, or zero.
Then prints all numbers from 1 to that number (if positive).

'''

# Mini Exercise Solution
try:
    number = int(input("Enter a number: "))
    if number > 0:
        print(f"{number} is Positive")
        for i in range(number):
            print(i+1)
    elif number < 0:
        print(f"{number} is Negative")
    elif number == 0:
        print(f"{number} is Zero")
except ValueError:
    print("Please enter an integer number.")

# Hour 2: Control Flow, Ends

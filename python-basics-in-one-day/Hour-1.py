# Hour 1: Python Basics

#########Tutorial Begins############

''''
🧪 1. Variables and Types
    Python is dynamically typed, so you don’t declare types:

    x = 10          # int
    pi = 3.14       # float
    name = "John"   # str
    is_valid = True # bool

You can check types using type():
    print(type(x))  # <class 'int'>


🖨️ 2. Printing and f-Strings
    name = "John"
    age = 35
    print(f"My name is {name} and I am {age} years old.")
    #This is Python’s version of Java’s System.out.printf()


📥 3. Input from User

    user_input = input("Enter something: ")
    print(f"You entered: {user_input}")


🧾 4. Indentation Instead of Braces
    Python uses indentation to define blocks:

    
    if x > 5:
        print("x is greater than 5")
    else:
        print("x is 5 or less")
'''

#########Tutorial Ends############

'''
✅ Mini Exercise

Try writing a small script that:
    - Asks for your name and age.
    - Prints a greeting with your name.
    - Tells you how old you’ll be in 5 years.
'''

# Mini Exercise Solution
username = input("Enter your name: ").strip()
print(f"Hello {username} ! ")
try:
	age = int(input("Enter your age: "))
	print(f"In 5 years you would be: {age + 5} years old.")
except ValueError:
    print("Please enter a valid age as a number.")

# Hour 1: Python Basics Ends

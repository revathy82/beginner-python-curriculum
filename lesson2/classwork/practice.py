# Problem 1
# Ask the user for their age.
# Calculate and print how many decades old they are, rounded to the nearest whole number.
age_input=input("Enter your age: 11")
age = int(age_input)
decades=round(age/10)
print("you are approximately",decades,"decades old")




# Problem 2
# Ask the user to enter a number.
# Print the result of multiplying that number by 5.
num_input=input("100")
number=float(num_input)
result=number*5
print("The result is:",result)


# Problem 3
# Use a for loop to print "I will learn Python!" 3 times.
for i in range(3):
    print("I will learn python!")


# Problem 4
# Ask the user for their name and age.
# Print their name and how old they will be one year in a single sentence.
name = input("enter your name: arya")
age = int(input("enter your age:11"))
# calculate age next year11
next_age=age+1
print (f"HELLO {name}, next year you will be {next_age} years old")

# Problem 5
# Use a for loop to print the numbers from 2 to 8, one per line.
for i in range (5,9):
    print(i)
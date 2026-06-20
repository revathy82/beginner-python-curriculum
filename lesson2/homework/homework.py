# Homework Problem 1
# Ask the user for two numbers.
# Print their quotient and remainder on separate lines.
number1=int(input("enter first number: "))
number2=int(input("enter second number: "))
quotient=number1/number2
remainder=number1%number2
print("Remainder is ", remainder)
print(f"Quotient is {quotient}")


# Homework Problem 2
# Ask the user for their favorite animal and favorite color.
# Print a sentence combining them like: "A blue tiger would be awesome!"
animal=input("favorite animal")
color=input("favorite color")
print(f"A {color} {animal} would be awesome!")


# Homework Problem 3
# Use a for loop to print all the even numbers from 0 to 10 (including 10).
for i in range(0,11,2):
    print(i)

for i in range(0,12):
    if(i%2 == 0):
        print(i)

# Homework Problem 4
# Ask the user how many push-ups they can do.
# Multiply it by 7 and print how many they could do in a week.
pushupcount=int(input("how many push-ups you can do?"))
weeklycount=pushupcount * 7
print(weeklycount)



# Homework Problem 5
# Use a for loop to print the square of each number from 1 to 6.
# (Example: 1*1=1, 2*2=4, etc.)

for i in range(1,7):
    print(i*i)

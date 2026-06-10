#Question:- user input age and number
#Program Code:-
X = input("Enter your Name:")
y = int(input("Enter your Age:"))

print("The User Name is:", X)
print("The user age in the next year will be:", y + 1)

#Question:- Even odd checker using if-else
#Program Code:-
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

#Question:- Greatest of two numbers
#Program Code:-
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

if x > y:
    print("The first number is greater")
elif y > x:
    print("The second number is greater")
else:
    print("Both numbers are equal")
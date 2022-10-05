# problem11Solution
# a Program to extract each digit from an integer in the reverse order.
num1 = 56464616
print("The number we have : ", num1)
while num1>0:
    digit = num1 % 10
    num1 = num1 //10
    print(digit,end=" ")
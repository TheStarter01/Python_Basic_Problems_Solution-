# problem1solution

num1 = int(input("Enter the First Number1 : ")) 
num2 = int(input("Enter the Second Number2 : "))

def function1(num1, num2):
    Product = num1 * num2
    if Product <=1000:
        return Product
    else:
        return num1 + num2
result = function1(num1, num2)
print(result)
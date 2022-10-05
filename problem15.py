# Problem15solution
#  a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
def firstfunction(base,exponent):
    num = exponent
    result = 1
    while num>0:
        result = result * base
        num = num -1 
    print("Final Result : ",result)
Base = int(input("Enter the Base : "))
Exponent = int(input("Enter the Exponent : "))
firstfunction(Base,Exponent)
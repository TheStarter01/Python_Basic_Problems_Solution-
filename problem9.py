#problem9Solution
# Check Palindrome Number
first_num = input("please enter a minimum 2 digit number : ")
new_Num = first_num[::-1]
if (first_num == new_Num):
    print("Yes! it's a  palindrome number.")
else: 
    print("No! it's not a palindrome number.")
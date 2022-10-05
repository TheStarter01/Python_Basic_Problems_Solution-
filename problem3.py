# problem3Solution
#  Print characters from a string that are present at an even index number
userString = input("Enter your string : ")
print("You enter : ", userString)
size = len(userString)
for i in range(0, size, 2):
    print("Even index letters are : " ,userString[i])
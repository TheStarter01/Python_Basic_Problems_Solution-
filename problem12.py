# proble12Solution
# Calculate income tax for the given income by user
income = int(input("Enter your income : "))
text = 0
if income <=10000:
    text = 0
elif income<=20000:
    x = income - 20000
    text = x *10/100
else:
    text = 0
    text = 10000 *10/100
    text = text + (income- 20000) *20/100
print("Total amount of income-text you will pay this month :",text)
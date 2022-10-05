# problem10Solution
# Create a new list from a two list using the following condition
list1 = [10, 20, 25, 30, 35]
print("list1 : ",list1)
list2 = [40, 45, 60, 75, 90]
print("list2 : ",list2)
list3 = []
for i in list1:
        if i%2 != 0:
            list3.append(i)
for j in list2:
        if j%2 == 0:
            list3.append(j)

print("New list : ",list3)
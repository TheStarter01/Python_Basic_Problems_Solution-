# problem14Soultion
# Print downward Half-Pyramid Pattern with Star
for i in range(6,0,-1) :
    print(i)
    for j in range(0,i-1):
        print("*", end = " ")
    print(" ")
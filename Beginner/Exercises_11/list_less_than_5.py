ages = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_ages=[]
index=0
while index < len(ages):
    if ages[index] < 5:
        new_ages.append(ages[index])

    index=index+1

print("old list: " + str(ages) + "\nnew list: " + str(new_ages))


# ages = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# new_ages=[]
# index=0
# while index < len(ages) and ages[index] < 5 :
#     new_ages.append(ages[index])
#     index=index+1
#
# print(new_ages)
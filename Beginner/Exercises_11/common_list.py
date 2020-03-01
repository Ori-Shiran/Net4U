a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
i=0
while i < len(a):
    if a[i] in b and a[i] not in c:
        c.append(a[i])
    i=i+1
print("New list with common numbers: " + str(c))

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []
# for i in a:
#     if (i in b) and (i not in c):
#         c.append(i)
# print("New list with common numbers: " + str(c))

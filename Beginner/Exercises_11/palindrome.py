var=input("Please eneter a palindrome")
i=0
while i < int(len(var)/2):
    if var[i] == var[-i-1]:
        i=i+1
    else:
        break
if i==int(len(var)/2):
    print("True")
else:
    print("sorry")

#### Sulotion in class###

# str1=input("Enter a string: ")
# if str1==str1[::-1]:
#     print("Ploingdrom")
# else:
#     print("not")

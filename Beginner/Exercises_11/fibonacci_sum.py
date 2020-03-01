a=1
b=1
n=int(input("Please enter how manny fibonacci elements to summarize: "))
for i in range(1,n):
    b=b+a
    a=b-a
    print(str(b)+", ")
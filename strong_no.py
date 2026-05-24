num=int(input("Enter number"))
facotr=0

for i in range(1,num+1//2):
    if num%i==0:
        facotr=facotr+i

if facotr==num:
    print("it is a perfact no")
else:
    print("not a perfact no")
num=int(input("Enter number"))
num1=int(input("Enter number"))

if num<num1:

    for i in range(num,num1+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            print(i)
else:
    print("first number always smaller for secound no")
    
num1=int(input("Enter First number"))
num2=int(input("Enter last number"))

if num1<num2:

    for num in range(num1,num2+1):
        temp=num
        temp1=num

        count=0
        while(temp>0):
            count+=1
            temp//=10
        aramstrong_no=0
        while (temp1>0):
            rem=temp1%10
            aramstrong_no=aramstrong_no+rem**count
            temp1//=10

        if aramstrong_no==num:
            print("it is a aramstrong_no",i)
        else:
            print("not is a aramstrong_no")

else:
    print("enter num1 alway's smaller into num2")
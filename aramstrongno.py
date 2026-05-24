num = int(input("Enter number"))
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
    print("it is a aramstrong_no")
else:
    print("not is a aramstrong_no")

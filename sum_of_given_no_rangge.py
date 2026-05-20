num1=int(input("Enter_number"))
num2=int(input("Enter_number"))
if num1<num2:
    sum_no=0
    for i in range(num1,num2+1):
        sum_no=sum_no+i
    print(sum_no)
else:
    print("please enter num2 is grater for num1")
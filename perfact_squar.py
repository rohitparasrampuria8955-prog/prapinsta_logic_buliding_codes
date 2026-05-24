num=int(input("Enter number "))

for i in range(1,num+1//2):
    if i*i==num:
        print("it is perfact_squar_no")
        break
    i+=1
else:
    print("not a perfact_squar_no")
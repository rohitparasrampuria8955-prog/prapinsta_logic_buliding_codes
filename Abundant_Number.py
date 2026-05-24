num = int(input("Enter number"))
factor_sum=0
i=1
while(i<num):
    if num%i==0:
        factor_sum +=i
    i+=1

print(factor_sum)

if factor_sum>num:
    print("its a abundant number")
else:
    print("not a abundant no")

num1 = int(input("Enter first number "))
num2 = int(input("Enter secound number "))

factor_sum_num1=0
factor_sum_num2=0

temp1=num1
temp2=num2

for i in range(1,temp1+1):
    if temp1%i==0:
        factor_sum_num1+=i

result1 = factor_sum_num1/num1

for i in range(1,temp2+1):
    if temp2%i==0:
        factor_sum_num2+=i
result2 = factor_sum_num2/num2

if result1 == result2:
    print("its a Friendly pair")
else:
    print("not a Friendly pair")



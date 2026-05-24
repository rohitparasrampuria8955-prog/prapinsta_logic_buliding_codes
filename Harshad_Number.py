num = int(input("Enter number"))
temp=num
dig_sum=0
while temp>0:
    rem=temp%10
    dig_sum=dig_sum+rem
    temp//=10
if num%dig_sum==0:
    print("it is a Harshad_number")
else:
    print(" not is a Harshad_number")

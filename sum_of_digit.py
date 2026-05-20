num = int(input("Enter number"))
digit_sum=0

while num>0:
    rem=num%10
    digit_sum = digit_sum + rem
    num//=10

print(digit_sum)
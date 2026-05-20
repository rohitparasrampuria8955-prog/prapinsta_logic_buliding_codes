num = int(input("Enter number"))
temp=num
rev_no=0

while temp>0:
    rem=temp%10
    rev_no=rev_no*10+rem
    temp//=10

if rev_no == num:
    print("palindrome no")
else:
    print("not a palindrome no")
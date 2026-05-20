num = int(input("Enter number"))
rev_no=0

while num>0:
    rem=num%10
    rev_no=rev_no*10+rem
    num//=10

print(rev_no)
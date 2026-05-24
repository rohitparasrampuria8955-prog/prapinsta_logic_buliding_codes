num = int(input("Enter number"))
square = num*num
sq_len=len(str(num))

last_digit= square%(10**sq_len)

if last_digit==num:
    print("automorphic_no")
else:
    print("not automorphic no")
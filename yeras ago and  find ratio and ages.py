given_data=input("given data n year ago and hence  find the ratio  enter 1 or  given extra n times equal to to n times enter 2 : ")
a=int(input("enter n years ago : "))
b=int(input("enter a is n times :"))
c = int(input("enter the hence years : "))
d=int(input("enter the a n times is equal : "))
if (given_data=="1"):
    e=abs((d*a)+(d*c)-a-c)/abs(b-d)
    print(f'ratio bxe + a = {(b*e)+a}')
    print(f'ratio e + a = {e+a}')
    print(f'ratio = {(b*e)+a} / {a+e}')
elif (given_data=="2"):
    e=int(input(" b is equal  n times"))
    f=abs((a*d*b)-(d*a)-(d*c))/((d*b)-(e))
    print(f' prasent age of person_2 = {f} years')
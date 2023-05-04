

a=int(input("enter age ratio : "))
b=int(input("enter age ratio : "))
c=int(input("enter the sum of ages : "))
d=int(input("enter the after years : "))
given_data=input("for  find the ratio enter 1 oe enter 2 for prasent ages of both : ")
if (given_data=="1"):
    e=(c)/(a+b)
    print(f' e = (  {c} ) / ( {a}+{b} )')
    print(f' ({a}x{e} = {a*e}) prsent age  person + {d} years ago  :  ({b}x{e} ={b*e}) prsent age  person + {d} years ago ')
    print((str((a*e)+d) + "/" +str((b*e)+d)))
elif (given_data=="2"):
    e=abs((a*d)-(b*c) - d)/(a+b)
    print(f' e = {a*d} - {b*c} - {d} / {a}+{b}')
    print(f'prasent age is {c}- {e} is = {c-e} years')
    print(f'prasent age person_2 is = {e} years')



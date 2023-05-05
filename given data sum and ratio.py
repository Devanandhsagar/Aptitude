

a=int(input("enter age ratio : "))
b=int(input("enter age ratio : "))
c=int(input("enter the sum of ages : "))
d=int(input("enter the after years : "))
given_data=input("find the ratio enter 1 or enter 2 for present ages of both : ")
if (given_data=="1"):
    e=(c)/(a+b)
    print(" e = ( c / (a + b ))")
    print(f' e = (  {c} ) / ( {a}+{b} )')
    print(f'Ratio =  ({a}x{e} = {a*e}) prsent age  person + {d} years ago  :  ({b}x{e} ={b*e}) prsent age  person + {d} years ago ')
    print( "Ratio  = "+(str((a*e)+d) + "/" +str((b*e)+d)))
elif (given_data=="2"):
    e=abs((a*d)-(b*c) - d)/(a+b)
    print (" e =  (( a x d ) - ( b x c ) - d ) / ( a + b )")
    print(f' e = {a*d} - {b*c} - {d} / {a}+{b}')
    print(f'prasent age is person_1 = {c}- {int(e)} is = {int(c-e)} years')
    print(f'prasent age person_2 is = {int(e)} years')



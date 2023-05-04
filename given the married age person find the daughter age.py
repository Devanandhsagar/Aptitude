given_data=input("given person_2 is yonest person_1 enter 1 or else 2")
a=int(input("enter the years ago : "))
b1=int((input("enter no times b_1 : ")))
b2=int((input("enter the times b_2 ")))
c1=float(input("enter the num ratio c_1 age or take c1 only return c_2 is 1 : "))
c2=float(input("enter the deno age ratio c_2 : "))
d=int(input("enter the years ago age : "))
b=float(b1/b2)
c=float(c1/c2)
e=int(round(a/(b-1)))
f=c*(e+a)
if (given_data=="2"):
    print(f' prasent age father is = {e}')
    print(f' daughters age {d} yeras ago =  f - d = {f-d} years ')
elif(given_data=="1"):
    print(f' person_2 age is  {e} - {c} ={e-c} years')
    
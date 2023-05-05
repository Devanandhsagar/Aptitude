## question 17 finding the difference of two persons
a=int(input("enter value for a : "))
b=int(input("enter value for b : "))
c=int(input("enter the hence year : "))
d=int(input("enter the ratio_1 : "))
e=int(input("enter the ratio_2 : "))
f=abs(((d)*(c)-(e)*(c))/((e)*(a)-(d)*(b)))
print(" f = ((d)*(c)-(e)*(c))/((e)*(a)-(d)*(b))")
print(f' f = ( { d * c } - {(e)*(c) }) / ({(e)*(a)} - {(d)*(b)} )')
print("f = " + str(f))
print("ans= (af-bf)")
print(" ans = (a-b)*f")
formula=(a-b)*f
print(formula)

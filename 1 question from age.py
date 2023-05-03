## 1 question from age
a=int(input("enter the persent ratio_1 : "))
b=int(input("enter the persent ratio_2 : "))
c=int(input("enter n years ago : "))
d=int(input("enter years ago ratio_1 : "))
e=int(input("enter years ago ratio_2 : "))
f=int(input("enter add year : "))
g=((e*c)-(d*c))/((e*a)-d)
print(str(g))
formula=(a*g)+f
print(str(a)+"x"+str(g)+str(f))
print(str(formula)+" years of person age")
## 1 question from age
a=int(input("enter the persent ratio_1 : "))
b=int(input("enter the persent ratio_2 : "))
c=int(input("enter n years ago : "))
d=int(input("enter years ago ratio_1 : "))
e=int(input("enter years ago ratio_2 : "))
check=input("(find the value a enter 1 and b for 2 )and ( for prasent age a enter 3 or b for enter 4) : ")
if (check=="1"):
    f=int(input("enter add year : "))
    g=((e*c)-(d*c))/((e*a)-b*d)
    print(str(g))
    formula=(a*g)+f
    print(str(a)+"x"+str(g)+"+"+str(f))
    print(str(formula)+" years of person age")
elif (check=="2"):
    f=int(input("enter hence ago year : "))
    g = abs((e * c) - (d * c)) / abs((e * a) - (d*b))
    print(str(g))
    formula=((b*g)-f)
    print(formula)
elif(check=="3"):
    g = ((e * c) - (d * c)) / ((e * a) - b*d)
    print(str(g))
    formula = abs(a * g)
    print(str(a) + "x" + str(g) )
    print(str(formula) + " years of person age")
elif (check=="4"):
    g = abs((e * c) - (d * c)) / abs((e * a) - (d*b))
    print(str(g))
    formula = abs(b* g)
    print(str(a) + "x" + str(g))
    print(str(formula) + " years of person age")

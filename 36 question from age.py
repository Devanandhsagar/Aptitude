## 36 finding the n years ago this ratio
a=int(input("enter present age : "))
b=int(input("enter prersent age : "))
c=int(input("enter the  ratio_1 : "))
d=int(input("enter thr ratio_2 : "))
e=abs((c*b)-(d*a))/(abs(c-d)) ## abs is absolute value if value is negative convert to the postive value
print("("+str(c)+"x"+str(b)+" - "+str(d)+"x"+str(a) +") / ("+str(c)+str(d)+")")
print(str(e)+" year ago")
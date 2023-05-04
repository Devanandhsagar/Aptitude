a=int(input("enter age avg : "))
b=int(input("enter years hence "))
c=int(input("enter the ratio a : "))
d=int(input("enter the ratio b : "))
a=a*2
e=((c*a)+(b*c)-(d*b))/(d+c)
print(f'( ( {c}x{a} + {b}x{c} - {d}x{b} / ({d}+{c} )')
print(f' psentage of daughter = {a-e} years')
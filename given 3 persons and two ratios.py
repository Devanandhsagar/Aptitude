given_data="given two ratio and thee persons data and sum"
check=input("enter if both ratio person_1 is simliar enter 1 or if person_2 is similar enter 2 or person_3 is similar enter 3")
person_1=0
person_2=0
person_3=0
sum_of_ages=int(input("enter sum of the three ages"))
val_1 = int(input("enter the value_1"))
val_2 = int(input("enter the value_2"))
val_3 = int(input("enter the value_3"))
val_4=int(input("enter the value"))
    if (check=="1"):
        person_1=float(1)
        person_2=float(val_2/val_1)
        person_3=float(val_4/val_3)
    elif (check=="2"):
        person_2=float(1)
        person_1=float(val_1/val_2)
        person_3=float(val_3/val_4)
    elif (check=="3"):
        person_3=float(1)
        person_1=float(val_1/val_2)
        person_2=float(val_3/val_4)
    lower=person_1+person_2+person_3
    upper=sum_of_ages
    value_of_x=int(upper/lower)
    person_call=input("enter 1 for person_1 and enter 2 person_2 and enter 3 person_3")
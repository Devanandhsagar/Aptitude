from fractions import Fraction
from math import sqrt
given_data=input("enter present or past or future : ")

if (given_data=="present"):
    person_1=int(input("enter the age ratio : "))
    person_2=int(input("enter the age ratio : "))
    year=int(input("enter year : "))
    person_1heance=int(input("enter person hence ratio : "))
    person_2heance=int(input("enter person hence ratio : "))
    upper=(((year)*(person_1heance))-((year)*(person_2heance)))
    if (upper<=0):
        upper=-(upper)
    else:
        upper=upper
    lower=(((person_2heance)*(person_1))-((person_1heance)*(person_2)))
    if (lower<=0):
        lower=-(lower)
    else:
        lower=lower
    value_of_x=upper/lower
    person_1_present_age=(person_1)*(value_of_x)
    person_2_present_age=(person_2)*(value_of_x)
    print("present age of person_1 : "+str(person_1_present_age))
elif (given_data == "past"):
    person_1 = int(input("enter the age ratio : "))
    person_2 = int(input("enter the age ratio : "))
    year = int(input("enter year : "))
    person_1ago = int(input("enter person ago ratio : "))
    person_2ago = int(input("enter person ago ratio : "))
    upper = (((year) * (person_1ago)) - ((year) * (person_2ago)))
    if (upper <= 0):
        upper = -(upper)
    else:
        upper = upper
    lower = (((person_2ago) * (person_1)) - ((person_1ago) * (person_2)))
    if (lower <= 0):
        lower = -(lower)
    else:
        lower = lower
    value_of_x = upper / lower
    person_1_past_age = (person_1) * (value_of_x)
    person_2_past_age = (person_2) * (value_of_x)
    print("past age person_1 : "+str(person_1_past_age-year))
elif (given_data== "Difference"):
    person_1 = int(input("enter the age ratio : "))
    person_2 = int(input("enter the age ratio : "))
    year = int(input("enter year : "))
    person_1heance = int(input("enter person hence ratio : "))
    person_2heance = int(input("enter person hence ratio : "))
    upper = (((year) * (person_1heance)) - ((year) * (person_2heance)))
    if (upper <= 0):
        upper = -(upper)
    else:
        upper = upper
    lower = (((person_2heance) * (person_1)) - ((person_1heance) * (person_2)))
    if (lower <= 0):
        lower = -(lower)
    else:
        lower = lower
    value_of_x = upper / lower
    person_1_present_age = (person_1) * (value_of_x)
    person_2_present_age = (person_2) * (value_of_x)
    print("Difference of two persons : "+str((person_1_present_age)-(person_2_present_age))+" years")
elif (given_data=="sum of persons given present ages find the heance age or ratio"):
    person_1 = int(input("enter the age ratio : "))
    person_2 = int(input("enter the age ratio : "))
    year = int(input("enter year : "))
    year_before_or_after=input("if year is hence or after enter the 1 else enter the 0 for both persent ages or enter -1 for ago or ratio for enter 2 : ")
    sum_ages = int(input("enter the sum : "))
    value_of_x=sum_ages/(person_1 + person_2)
    if (year_before_or_after== "1" ):
        print(((person_1*value_of_x))+year)
    elif (year_before_or_after=="0"):
        print(person_1 * value_of_x)
        print(person_2 * value_of_x)
    elif (year_before_or_after=="2"):
        ratio_1=(person_1 * value_of_x)+year
        ratio_2 = (person_1 * value_of_x) + year
        print(ratio_1/ratio_2)
    else :
        print(((person_1 * value_of_x)) - year)
elif (given_data=="sum of persons given after ages"):
    person_1 = int(input("enter the times of persons_2 : "))
    person_2 = int(input("enter the times nothing enter 1 : "))
    year = int(input("enter year : "))
    year_before_or_after=input("if year is hence or after enter the 1 else enter the 0 for both persent ages or enter -1 for ago : ")
    sum_ages = int(input("enter the sum : "))
    upper=abs((sum_ages+year)-(person_1 * year))
    lower=abs(person_2+(person_1*(person_2)))
    value_of_x=upper/lower
    if (year_before_or_after== "1" ):
        print(person_1*value_of_x)
    elif (year_before_or_after=="0"):
        print(sum_ages-(person_2*value_of_x))
        print(person_2 * value_of_x)
    else :
        print(((person_1 * value_of_x)))
elif (given_data=="product age and sum ages"):
    check=input("given only product age find the ratio enter 1 else 0 ")
    if (check=="1"):
        person_1=int(input("enter person_1"))
        person_2=int(input("enter person_2"))
        pr=int(input("enter the product of ages"))
        print(" value_of_x = sqrt (pr /(person_1 * person_2))")
        value_of_x=sqrt(pr/(person_1*person_2))
        after_year=int(input("enter year of hence : "))
        print(str((person_1*value_of_x)+after_year)+"/"+str((person_2*value_of_x)+after_year))
    elif (check=="0"):
        person_1=int(input("enter the age"))
        pr=int(input("enter the product"))
        sum=int(input("enter the sum age"))
        year_ago=int(input("enter year ago"))
        val_1=person_1
        val_2=year_ago
        val_3=sum - year_ago
        val_4=person_1
        a=val_1
        b=-((val_1*val_3)+(val_2*val_4))
        c=((val_2)*(val_3))+pr
        eq=(sqrt((b**2)-(4*((a)*(c)))))
        formula_1=(-b+eq)/2*a
        formula_2=(b-eq)/2*a
        if (formula_2>formula_1):
            print(formula_2)
        else:
            print(formula_1)
elif (given_data=="sum of three persons and ages ratio"):
    person_1 = int(input("enter the age ratio of persons_1 : "))
    person_2 = int(input("enter the age ratio of persons_2 : "))
    person_3=int(input("enter the age ratio of person_3 : "))
    year = int(input("enter year : "))
    persent_ages_of_persons= input(
        "if person_1 agw enter 1 or person_2 age enter 2 or person_3 age enter 3 : ")
    sum_ages = int(input("enter the sum : "))
    print(" upper = abs(sum_ages + (3*year))")
    upper = abs(sum_ages + (3*year))
    print("lower = (person_3) / (person_1 + person_1 +person_2)")
    lower = (person_3/(person_1 + person_3 +person_2))
    print("value_of_x = upper x lower")
    value_of_x = upper * lower
    print("value_of_x = "+str(value_of_x))
    if (persent_ages_of_persons=="1"):
        print(person_1*value_of_x)
    elif(persent_ages_of_persons=="2"):
        print(person_2*value_of_x)
    else:
        print(f' person_3 age is {value_of_x} years')
elif (given_data=="given persent age and after  age ratios find the n year ago"):
    person_1=int(input("enter the present age person_1"))
    person_2=int(input("enter the present age person_2"))
    person_1_after=int(input("enter the after person_1 ratio"))
    person_2_after=int(input("enter the after person-2 ratio"))
    upper=abs((person_1*person_2_after)-(person_2*person_1_after))
    lower=abs(person_1_after-person_2_after)
    value_of_x=upper/lower
    print(str(value_of_x)+"years ago")
elif (given_data=="find the diff years ago of two person and hence of persons"):
    person_1=int(input("enter the person_1"))
    person_2=int(input("enter the person_2"))
    person_1_year=int(input("enter the person hence enter -  value or +value"))
    person_2_year = int(input("enter the person hence enter -  value or +value"))
    person_1_year_ratio=int(input("enter the person year ratio persson_1"))
    person_2_year_ratio = int(input("enter the person year ratio person_2"))
    check=input("find the hence year give + value 1 or ago give _ value 2")
    year_ago_after_person_1=int(input("enter the year ago_person_1"))
    year_ago_after_person_2=int(input("enter the year ago person_2"))
    upper=abs((person_2_year_ratio*person_1_year) - (person_1_year_ratio*person_2_year))
    lower=abs((person_2_year_ratio*person_1)-(person_1_year_ratio*person_2))
    value_of_x=upper/lower
    ratio_1=((person_1*value_of_x)+year_ago_after_person_1)
    ratio_2 = ((person_2 * value_of_x) + year_ago_after_person_2)
    print(str(ratio_1)+"/"+str(ratio_2))

elif (given_data=="n years ago the ages no of times person_1"):
    n=int(input("enter n years ago : "))
    person_1=int(input("enter no of times person_2 : "))
    person_2=int(input("enter no of times  : "))
    year=int(input("enter year"))
    no_of_times=int(input("enter no of times person_1 is equal to person_2 : "))
    upper=abs((n+year)-(no_of_times*(n+year)))
    print("upper = ((n + year) - (no_of_times * (n + year)))")
    lower=abs((person_1)-(no_of_times*(person_2)))
    print("lower = ((person_1) - (no_of_times * (person_2)))")
    value_of_x=upper/lower
    print("value_of_x = upper / lower")
    check=input("enter sum of ages 1 or enter diff of ages 2 or enter both pesent ages 3 or enter persom_1 ages 4 or enter person_2 age 5 or enter year ago person_1 age 6 or enter year ago person_2 age 7 ")
    if (check=="1"):
        print("(person_1 + person_2) * value_of_x")
        print(abs(person_1+person_2)*value_of_x)
    elif (check=="2"):
        print("((person_1 - person_2) * value_of_x ))")
        print(abs((person_1-person_2)*value_of_x))
    elif (check=="3"):
        print("( person_1 * value_of_x ) + n")
        print((person_1*value_of_x)+n)
        print("((person_2 * value_of_x) + n)")
        print((person_2 * value_of_x)+n)
    elif (check=="4"):
        print("(person_1 * value_of_x) + n")
        print((person_1 * value_of_x)+n)
    elif(check=="5"):
        print("(person_2 * value_of_x) + n")
        print((person_2 * value_of_x)+n)
    elif(check=="6"):
        print("(person_1 * value_of_x) - n")
        print((person_1 * value_of_x)-n)
    else:
        if (check=="7"):
            print("(person_2 * value_of_x) - n")
            print((person_2 * value_of_x)-n)
        elif (check=="8"):
            ans=((person_1*value_of_x)+n)/((person_2*value_of_x)+n)
            print(str(ans)+" ratio taken in the decimal fraction")
elif (given_data=="n years ago the ages no of times both person"):
    n=int(input("enter n years ago : "))
    person_1=int(input("enter no of times persoon_1 : "))
    person_2=int(input("enter no of times in the person_2 : "))
    add_year=int(input("enter hence add year : "))
    no_of_times_1=int(input("enter no of times person_1 is : "))
    no_of_times_2 = int(input("enter no of times person_2 is : "))
    upper=abs((no_of_times_1*(n+add_year))-(no_of_times_2*(n+add_year)))
    print("upper=abs((no_of_times_1*(n+add_year))-(no_of_times_2*(n+add_year)))")
    lower=abs(no_of_times_1*(person_2)-(no_of_times_2*(person_1)))
    print("lower=abs(no_of_times_1*(person_2)-(no_of_times_2*(person_1)))")
    value_of_x=upper/lower
    print(" value_of_x = upper/ lower")
    check=input("enter sum of ages 1 or enter diff of ages 2 or enter both pesent ages 3 or enter persom_1 ages 4 or enter person_2 age 5 or enter year ago person_1 age 6 or enter year ago person_2 age 7 : ")
    if (check=="1"):
        print("((person_1 * value_of_x) + n) + ((person_2 * value_of_x) + n)")
        print(((person_1*value_of_x)+n)+((person_2*value_of_x)+n))
    elif (check=="2"):
        print("((person_1 * value_of_x) - (person_2 * value_of_x))")
        print(abs((person_1 * value_of_x) - (person_2 * value_of_x)))
    elif (check=="3"):
        print((person_1*value_of_x)+n)
        print((person_2 * value_of_x)+n)
    elif (check=="4"):
        print((person_1 * value_of_x)+n)
    elif(check=="5"):
        print((person_2 * value_of_x)+n)
    elif(check=="6"):
        print(person_1 * value_of_x)
    else:
        if (check=="7"):
            print(person_2 * value_of_x)
elif (given_data=="given two ratio and thee persons data and sum"):
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
    if person_call=="1":
        person_1=person_1*value_of_x
        print(str(person_1 )+ " years")
    elif person_call=="2":
        person_2=person_2*value_of_x
        print(str(person_2 )+" years")
    elif person_call=="3":
        person_3=person_3*value_of_x
        print(str(person_3)+" years")
elif given_data=="given difference and year ago age find the persent age":
    ago_years=int(input("enter the n year ago : "))
    diff=int(input("enter the difference : "))
    person_1=int(input("enter the ago age person_1 : "))
    person_2=int(input("enter the ago age person_2 : "))
    upper=diff
    lower=abs(person_1-person_2)
    value_of_x=upper/lower
    check=input("enter 1 person_1 and enter the 2 person_2")
    if check=="1":
        print(person_1*value_of_x)
    elif check=="2":
        print(person_2*value_of_x)
elif given_data=="given sum and persons age n years ago find the prasent age":
    person_1=int(input("enter the peson_1"))
    person_2= int(input("enter the peson_2"))
    person_3= int(input("enter the peson_3"))
    year_ago=int(input("enter the year ago"))
    sum_ages=int(input("enter the sum"))
    n_of_persons=int(input("enter the no of persons"))
    upper=sum_ages-(n_of_persons*year_ago)
    lower=person_1+person_2+person_3
    value_of_x=upper/lower
    check=input("enter 1 for person_1 and 2 for person_2 and 3 for person_3")
    if (check=="1"):
        print(person_1*value_of_x)
    elif (check=="2"):
        print(person_2*value_of_x)
    elif (check=="3"):
        print((person_3*value_of_x))
elif (given_data=="find the younest from the persons"):
    no_of_persons=int(input("enter the noof persons"))
    count=0
    increase_each=int(input("enter each"))
    sum_ages=int(input("enter the sum"))
    for i in range(1,no_of_persons):
        count+=i*increase_each
    print(" valu_of_x = (sum_ages - count) / no_of_persons")
    valu_of_x=(sum_ages-count)/no_of_persons
    print(valu_of_x)
elif (given_data=="years ago and the no of times equal to years"):
    year_ago=int(input("enter the year ago"))
    person_1=0
    no_of_equal=int(input("enter the no of equal the person_1"))
    upper=int(input("enter numerator value of person_2"))
    lower=int(input("enter denomenator value of person_2"))
    upper_value_of_x=year_ago
    lower_value_of_x=1-no_of_equal
    value_of_x=upper_value_of_x/lower_value_of_x
    person_1=value_of_x+year_ago
    person_2=(upper/lower)*value_of_x
    year_ago_person_age=int(input("enter the year ago person_2"))
    check=input("person_1 enter 1 or enter person_2 2")
    if (check=="1"):
        print(person_1-year_ago_person_age)
    elif (check=="2"):
        print(person_2-year_ago_person_age)
elif (given_data=="given three person ratio and diff 2 persons and find the other 2persons diff"):
    person_1=int(input("enter the person_1"))
    person_2 = int(input("enter the person_2"))
    person_3 = int(input("enter the person_3"))
    diff_two_persons=int(input("enter the diff of two persons"))
    check=input("enter two persons 1 and 2 take enter 1 or 2 and 3 enter 2 or 1 and 3 enter 3")
    value_of_x=0
    if (check==1):
        lower=abs(person_1-person_2)
        valu_of_x=diff_two_persons/lower
    elif(check=="2"):
        lower=abs(person_2-person_3)
        value_of_x=diff_two_persons
    elif (check=="3"):
        lower=abs(person_1-person_3)
        value_of_x=diff_two_persons











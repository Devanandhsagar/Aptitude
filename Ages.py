
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
    print("Difference of two persons : "+str((person_1_present_age)-(person_2_present_age)))
elif (given_data=="sum of persons given present ages"):
    person_1 = int(input("enter the age ratio : "))
    person_2 = int(input("enter the age ratio : "))
    year = int(input("enter year : "))
    year_before_or_after=input("if year is hence or after enter the 1 else enter the 0 for both persent ages or enter -1 for ago : ")
    sum_ages = int(input("enter the sum : "))
    value_of_x=sum_ages/(person_1 + person_2)
    if (year_before_or_after== "1" ):
        print(((person_1*value_of_x))+year)
    elif (year_before_or_after=="0"):
        print(person_1 * value_of_x)
        print(person_2 * value_of_x)
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

elif (given_data=="sum of three persons and ages ratio"):
    person_1 = int(input("enter the age ratio of persons_1 : "))
    person_2 = int(input("enter the age ratio of persons_2 : "))
    person_3=int(input("enter the age ratio of person_3 : "))
    year = int(input("enter year : "))
    persent_ages_of_persons= input(
        "if person_1 agw enter 1 or person_2 age enter 2 or person_3 age enter 3 : ")
    sum_ages = int(input("enter the sum : "))
    upper = abs(sum_ages - (3*year))
    lower = abs(person_1 + person_1 +person_2)
    value_of_x = upper / lower
    if (persent_ages_of_persons=="1"):
        print(person_1*value_of_x)
    elif(persent_ages_of_persons=="2"):
        print(person_2*value_of_x)
    else:
        print(person_3*value_of_x)







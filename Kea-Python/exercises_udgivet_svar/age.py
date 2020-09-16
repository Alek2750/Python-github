age=int(input("Enter your age: "))
year=2020
'''
print(age)
print("Your age + 100 years")
age_plus=age+100
print(age_plus)
'''

#print("You will be " + str(age + 100) + " years old, in 100 years.") 
#print("Your age in 100 years:", age + 100)
#print("You will be {} years old, in 100 years.".format(age+100))
#print("You will be {1} years old, in 100 years. And now is {0}".format(year, age+100))
print("You will be %d years in 100 years." % (age+100))

future_year=year+100-age
print("In the year {} you will be 100 years old".format(future_year))

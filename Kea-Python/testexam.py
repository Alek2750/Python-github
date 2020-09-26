name = "Alessandro Accaroli"

nameli = name.split(" ")

print(nameli[1])

with open ("testfile.txt", "w") as myfile:

    myfile.write("HELLO WORLD\n")
    myfile.write("192.168.0.1\n")
    myfile.write(name)


mylist = [2,1,5,6,7,54,5]

mysetlist = set(mylist)

print(mysetlist)
print(len(mysetlist))

#string to tuple list
mynumbers = "(1, 5), (8, 10)"
tuplist = list(eval(mynumbers))
print(str(tuplist))

#string to tuple
numbers = "1, 5,-5, 3, 8, 9"
resnum = eval(numbers)

print (resnum)

tup1 = ("HK", "HG", "Danmark")
tup2 = ("Fagforening", "Gym", "sygeforsikring")

if len(tup1) == len(tup2):
        res = dict(zip(tup1, tup2))

print (res)

mydict = {
    "ales0435@stud.kea.dk": 46,
    "coa@stud.kea.dk": 32
}

print(mydict["ales0435@stud.kea.dk"])
print(type(mydict))

#The try block will generate an error, because x is not defined:
try:
  print(x)
except:
  print("An exception occurred")

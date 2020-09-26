
# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.txt', 'w')

with open("myfile2.txt", "w") as myfile2:
    myfile2.write("Hello world 2")

# Get some info
print('Name: ', myFile.name)
print('Is Closed : ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I also\n like PHP')
myFile.close()

# Read from file, read(13) reads the first 13 chars
myFile = open('myfile.txt', 'r')
text = myFile.read()
text = myFile.read(13)
print(text)

# Read from file line by line, by looping
myFile = open("myfile.txt", "r")
for i in myFile:
    print(i)
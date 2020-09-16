word=input("Enter the search word: ")
line_no=1

file=open("log.txt", "r")
for line in file:
       if word.lower() in line.lower():
           print("{}:{}".format(line_no, line))
       line_no+=1


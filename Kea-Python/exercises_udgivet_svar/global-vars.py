z=10
print("z is ",z)

#fun() #this will give en error

def fun():
   global z
   z+=1
   print("z in the fun ", z)

fun()
print("z after ", z)

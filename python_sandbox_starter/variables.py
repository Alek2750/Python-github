"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x = 1          # int
y = 2.5        #float
name = "john"  #str
is_cool = True # boll

# multiple assignment
x, y, name, is_cool = (1, 2.5, 'john', True)

# Basic math
a = x + y

# Casting
x = str(x)
y = int(y)
z = float(y)

print (type(z), z)
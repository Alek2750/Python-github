# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# Using a constructor
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)

# Get value
print(fruits[1])

# Get the last value using negative indexing
print(fruits[-1])

# Can't change value
#fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get length
print(len(fruits))

# join() with tuples
mynumb = ("192","168","0","1")
s = "."
print(s.join(mynumb))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
# remove will give error if ele is not in the set, while discard does not.
fruits_set.remove('Grape')
#fruits_set.discard("Grape")

# Add duplicate
fruits_set.add('Apples')

# Add multiple items to the set, with update()
fruits2 = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits2.update(more_fruits)

# Clear set
fruits_set.clear()

# Delete
del fruits_set

#print(fruits_set)

# join() with set
mynumb1 = {"dany","alex","alek","charlie"}
s = "->"
print(s.join(mynumb1))

"""
Method	Description
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
"""
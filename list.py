students = ["david", "kioko", "kiamba", "ian", "dave", "ray" ]
print(students)
print(len(students))
print(type(students))

# the first item has index 0.
print(students[0])
#Negative indexing means start from the end
print(students[-1])

#The search will start at index 2 (included) and end at index 5 (not included).
print(students[2:5])
#By leaving out the start value, the range will start at the first item:
print(students[:4])

#By leaving out the end value, the range will go on to the end of the lis
print(students[2:])
print(students[-4:-1])

if "ian" in students:
  print("Yes, 'ian' is in the students list")

#Change list items
students[4] = "rose"
print(students)

#Change a Range of Item Values
students[2:4] = ["diego", "brian"]
print(students)

#If you insert more items than you replace
students[4:5] = ["Mike", "Rodgers"]
print(students)

#If you insert less items than you replace
students1 = ["imran", "tayabali"]
students1[1:3] = ["Jay"]
print(students1)

#Insert Items
students.insert(3, "bill")
print(students)

#To add an item to the end of the list, use the append() method
students.append("Ahmed")
print(students)

#To append elements from another list to the current list, use the extend() method.
students.extend(students1)
print(students)

#The remove() method removes the specified item.
students.remove("david")
print(students)

#The pop() method removes the specified index.
students.pop(6)
print(students)
#If you do not specify the index, the pop() method removes the last item.

#The del keyword also removes the specified index
del students[0]
print(students)
#The del keyword can also delete the list completely.

#The clear() method empties the list.The list still remains, but it has no content.
#students.clear()
#print(students)

#You can loop through the list items by using a for loop
for x in students:
  print(x)
 
 #You can also loop through the list items by referring to their index number.
for i in range(len(students)):
  print(students[i])

#Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by refering to their indexes.Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by refering to their indexes.
i = 0
while i < len(students):
  print(students[i])
  i = i + 1

#List Comprehension offers the shortest syntax for looping through lists
[print(x) for x in students]

#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in students:
  if "a" in x:
    newlist.append(x)
print(newlist)

#List objects have a sort() method that will sort the list alphanumerically, ascending, by default
students.sort()
print(students)

#To sort descending, use the keyword argument reverse = True
students.sort(reverse = True)
print(students)

#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
students2 = students.copy()
print(students2)

#join two lists
student3 = students + students1
print(student3)

#Another way to join two lists are by appending all the items from list2 into list1, one by one
for x in students1:
  students.append(x)

print(students)



























#Write a python program to merge two list? 
list1 = ["apple","grapes","cherry"]
list2 = ["waermelon","kiwi","mango"]
merged_list = list1 + list2
print(merged_list)


#Write a python program to delete element of given index in list ?
numbers = [3,5,6,8,9,11,14]
index = numbers.index(14)
print(index)


#Write a pytho program to delete given element from the list?

list = [10,20,-35,40,-55]
for i in list:
    if i <0:
     list.remove(i)
print(list)

#Write a python programe to check if the two list are having atleast one common element?


list1 = [1,3,4,5,4,6,7,6]
list2 = [8,9,10,4,6,11]
common_elements = []
for element in list1:
  for  element in list2:
      common_elements.append(element)
      if common_elements:
        print("common elements:", common_elements)
else:
  print(" no common elements found.")



#Write a python program to remove  specified column from the nestedlist?
list = [20,50,10,30,150]
for i in list :
  if i >100:
    list.remove(i)
    print(list)

#Write python program to convert a list of integers into single integer ?

list = [10,30,40,50]
for i in list:
  print(i,end = "")

#Write  a python programe to remove duplicates from the list ?

my_list = [1,3,4,5,4,6,7,6,7,8,9,10,9]
print(list(set(my_list)))

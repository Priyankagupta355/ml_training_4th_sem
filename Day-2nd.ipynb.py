# list 
""" features : 1. ordered
               2. mutable
                
                  """

lst = ["hello",22.34,22,1,True]
print(lst)
print(type(lst))
print(len(lst))

lst2 = ["green","red","blue","black","red"]
print(lst2.count("red"))                   # count the no. of strings
lst2.extend(["violet","white"])          # add elements/strings to the list
print(lst2)
 
print(lst2.index("red"))

#lst2.clear()    # clear the data of list , but list exixt as a void 
#print(lst2)

lst2.sort(reverse=True)
print(lst2)
lst2=lst2[ : : -1] 
print(lst2)

lst2.append("yellow")   # add element to the last
print(lst2)

lst2.insert(2,"grey")
print(lst2)

lst2.pop()  # remove the element either last or index wala
print(lst2)

lst2.remove()
print(lst2)

lst3 = lst2.copy()
print(lst3)
# note :- in case of duplication elements , it fetch or print from left to right or print which is accessed first


"""name = "surender"
age = 20
status = "unemployed" 

print(type(name))
print(type(age))
print(type(status))"""

"""print(type(print(1)))
print(type(1))
print(type(type))"""

## string & their methods  
company = "Upflair global tech"  # set of symbols defined between quotes
#print(type(company))

print(company.strip())  # remove spaces from both start and end
print(company.lstrip())  # remove spaces from left of string
print(company.rstrip())   # remove spaces from right of string

print(company.upper())  # print string in upper cases
print(company.lower())  # print string in lower cases

print(company.title())   # capitalise the 1st letter of every word
print(company.replace("Upflair global tech", "bye"))   # replace the word using parameters

print(company.count('l'))   # count the no. of time letter occurs

print(company.removeprefix("Upflair"))  # remove the prefix
print(company.removesuffix("tech"))    # remove the suffix
 
 ## slicing [start : stop : skip (optional) ]

print(company[0])  # print 0th index symbol
print(company[2]) 
print(company[-2]) 
print(company[2 : 10]) 
print(company[2 : 10 : 3]) 

demo = "123456789"
print(demo[2 : 8]) 
print(demo[2 : 8 : 2]) 
print(demo[2 : 8 : 3]) 

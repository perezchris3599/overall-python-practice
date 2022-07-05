#functions
#def function3(x, y):
#    return x + y
#e = function3(1, 2)
#print(e)

#dictionaries
d ={}
d["George"] = 24
d["Tom"] = 32
d["Jenny"] = 16

print(d["George"])

for key, value in d.items():
    print("key:")
    print(key)
    print("value:")
    print(value)
    print("")

#sets
a = set() #this is an empty set
print(a)

#adding one element in the set
a.add(1)
print(a)

a.add(2345)
print(a)

for x in a:
    print(x)

#removing duplicate values using sets
given_list1 = [1, 1, 3, 3, 3, 2, 4, 5, 6, 5, 6, 2, 7, 8, 9, 7, 8, 9, 10, 10, 7]
new_set1 = set()
for x in given_list1:
    new_set1.add(x)
print(new_set1)

#create a new list with unique elements from first list
new_list1 = list()
for x in new_list1:
    new_list1.append(x)
print(new_list1)

#adding things that arent numbers
b = set()
b.add('apple')
b.add('banana')
b.add(1)
b.add(7)
print(b)

#simple exercise, finding sum of unique elements
given_list2 = [1,3,4,1,3]
new_set2 = set()
for x in given_list2:
    new_set2.add(x)
total = 0
for x in new_set2:
    total += x
print (total)

#lists
a = [3, 10, -1]
print(a)
a.append("hello") #adding 2 to the list
print(a)
a.append([1, 2]) #Adding a list within the list
print(a)
a.pop()#deleting recently added data/last item in the list
print(a[0])#getting the first item in the list
a[0] = 100 #changing contents of the list
print(a)

#sample exercise, switch the first item in the list below with the last
b = ["windows", "mac", "linux"]
b[0], b[2] = b[2], b[0]
print(b)

#list comprehensions
a = [1, 3, 5, 7, 9, 11]
b = []
b.append(10)
b.append(20)
b.append(30)
b.append(40)
print(b)

#making double the numbers in a
c = []
for x in a:
    c.append(x * 2)
print(c)

#simpler syntax
d = [x * 2 for x in a]
print(d)

#another example
e1 = []
for x in range(1, 7):
    e1.append(x ** 2)
print(e1)
#simpler syntax
e2 = [x ** 2 for x in range(1, 7)]
print(e2)

#sample exercise
for x in range(6, 0, -1): #to count numbers from 6 in descending order
    print(x)
f1 = []
for x in range(6, 0, -1):
    f1.append(x**2)
print(f1)
#using list comprehension
f2 = [x**2 for x in range(6, 0, -1)]
print(f2)

#for loops
a = ["banana", "apple", "berry"]
#to print each of the above, youd usually do this;
print(a[0])
print(a[1])
print(a[2])
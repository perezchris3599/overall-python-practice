#functions
def function3(x, y):
    return x + y
e = function3(1, 2)
print(e)

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
print(a[0])
#getting the first item in the list
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
#the most efficient way ..using a for loop
for element in a:
    print(element)
    print(element)#this makes each element to be printed twice

#example 2
b = [20, 10, 5, 2.5]
for x in b:
    print(x)
#making the total of the items
b = [20, 10, 5, 2.5]
total = 0
for e in b:
    total = total + e
print(total)

#another way of getting total.. to print 1,2,3 4
c =list(range(1, 5))
print(c)

# using a for loop to create the above
for i in range(1, 5):
    print(i)

#getting total of the above
total2 = 0
for i in range(1, 5):
    total2 += i
print(total2)

#using range
print(list(range(1, 8)))
#getting total of the range
total3 = 0
for i in range(1, 8):
    if i % 3 == 0:
        total3 += i
print(total3)

#all multiples of 3,5 that are less than 100
print(list(range(1, 100)))
#solution
total = 0
for i in range(1, 100):
    if i % 3 == 0:
        total += i
    elif i % 5 == 0:
        total += i
print(total)

#another alternative to the above
total = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total += i
    print(total)

#more about for loops
a = ["one", "two", "three"]
for x in a:
    print(x)

#another method to do the above
for i in range(len(a)):
    for j in range(i + 1):
        print(a[i])

#finding the total of negative numbers in a list
given_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]

total2 = 0
j = len(given_list) - 1
while given_list[j] < 0:
    total2 += given_list[j]
    j -= 1
print(total2)

#while loops and the break statement
total2 = 0
j = 1
while j < 5:
    total2 += j
    j += 1
print(total2)

#finding the sum of only positive numbers in a list using the while loop
given_list = [5, 4, 4, 3, 1, -2, -3, -5]

total3 = 0
i = 0
while given_list[i] > 0:
    total3 += given_list[i]
    i += 1
print(total3)

#adding the break statement
given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
total4 = 0
for element in given_list2:
    if element <= 0:
        break
    total4 += element
print(total4)

#another alternative
total5 = 0
i = 0
while True:
    total5 += given_list2[i]
    i += 1
    if given_list2[i] <= 0:
        break
    print(total5)

#booleans
a =7
b = 5
if a > b:
    print("a is greater than b")
if True:
    print("a is greater than b")

    boolean_value = a > b
    print(boolean_value)

#another sample
def are_you_sad(is_rainy, has_umbrella):
    if is_rainy and not has_umbrella:
        return True
    else:
        return False

#another example
def are_you_sad(is_rainy, has_umbrella):
    return is_rainy and not has_umbrella
are_you_sad(True, False)
are_you_sad(True, True)
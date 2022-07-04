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

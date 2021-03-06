#functional programming in python
#pure functions
def do_Pure(data):
    return data * 2 #this returns the data multiplied by two

#functions are objects
def func1():
    return 1
def func2():
    return 2

#adding functions to dictionaries
my_funcs = {'a': func1, 'b':func2}
my_funcs['a']()
my_funcs['b']()

#closures and currying
def outer(outer_arg):
    def inner(inner_arg):
        return inner_arg + outer_arg
    return inner

func = outer(10)
func(5)

func.__closure__
func.__closure__[0]
func.__closure__[0].cell_contents

#partial functions
import functools
def func(a, b, c):
    return a, b, c

p_func = functools.partial(func, 10)
p_func(3, 4)

p_func = functools.partial(func, 10, 12)
p_func(3)

#recursion
def loop(n):
    for x in xrange(int(n)):
        a = 1 + 1

def recurse(n):
    if n <= 0:
        return
    a = 1 + 1
    recurse(int(n) -1)

#lambda
def use_callback(callback, arg):
    return callback(arg)

    use_callback(lambda arg: arg * 2, 10)

#instead of
def add(x, y):
    return x + y

#lambda does
lambda x, y: x + y

#another lambda example
#instead of
def mx(x, y):
    if x > y:
        return x
    else:
        return y
print(mx(8,5))

mx = lambda x, y: x if x >  y else y
print(mx(8, 5))

#map function
#instead of
List, [m, n, p]
function, f()

# map does
list, [f(m), f(n), f(p)]

#other map examples
def square (lst1):
    lst2 = []
    for num in lst1:
        lst2.append(num ** 2)
    return lst2

print square([4,3,2,1])

#map
n = [4, 3, 2, 1]
print (list(map(lambda x: x**2, n)))

#filter....for filtering items out of a sequence
def over_two(lst1):
    lst2 = [x for x in lst1 if x>2]
    return lst2

    print over_two([4,3,2,1])

#do
n = [4,3,2,1]
print(list(filter(lambda x: x>2, n)))

#reduce function
def mult (lst1):
    prod = lst1[0]
    for i in range(1, len(lst1)):
        prod *= lst[i]
    return prod

print mult([4,3,2,1])

#instead do
n = [4,3,2,1]
print (reduce(lambda x,y: x*y, n))
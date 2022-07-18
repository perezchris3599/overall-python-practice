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


# The value of what is being referenced by the variable has a type like int or float or str, but the variable itself has no type.
# The built-in type() function returns the data type of the object that is referenced by a particular variable.
# Notice that the type of the reference is bound dynamically as the program is executed.
# The built-in id() function returns a unique identifier of an object that is referenced by a particular variable.
# There is only a single int object 10 being created and both the variables x and y reference the same object. This is evident in that they both produce the same id.

#!/usr/bin/env python3
x = 10
tab = " \t"

print(x, tab, type(x), tab, id(x))
y = x
print(y, tab, type(y), tab, id(y))
x = 25.7
print(x, tab, type(x), tab, id(x))
x = "Hello"
print(x, tab, type(x), tab, id(x))

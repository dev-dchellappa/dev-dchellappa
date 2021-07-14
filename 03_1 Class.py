class Person:
    pass

p1 = Person()
p1.first_name = "David" 
p1.last_name = "Chellappa"
# Like simple variables, attributes of classes and instances are not declared ahead of time,
# but spring into existence the first time they are assigned values
# so here, the attributes first_name and last_name are create in the scope of p1 object, though the class does not have these members
# in this aspect, the Class in Python, like simple variables, is dynamic - it is not stongly typed like the Class in C++ or Java.

p2 = Person()
p2.age = 45

# print(p1.age) #this give an error 
#     print(p1.age)
# AttributeError: 'Person' object has no attribute 'age'
# python will first look for the member (either method or attrinute) in the instance. 
# if not available in instance, it will look for in the Class
# if not available in the Class, it will look for in teh super classes from left to right
# if not available, python will throu an error, and that's what is happening here

print(p2.age)
#print(p2.first_name) #this will give an error

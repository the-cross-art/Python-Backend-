def my_function(str1, str2):
    print(str1)
    print(str2)

my_function("This is the argument","This is the second argument")
my_function("imran","lololo")

def print_something(name="Someone",age="unknown"):
    print("My name is",name,"and my age is ",age)

print_something(age=20)

def print_people(*people):
    for person in people:
        print("This person is",person)

print_people("Nick", "Dan", "Jack", "King", "Smiley")

def do_math(num1,num2):
    return num1+num2

math1=do_math(5,7)
math2=do_math(11,34)
print(math2)
print("First sum is", math1, "and the second sum is",math2)
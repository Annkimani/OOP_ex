class Dog:

    # class attribute
    species = 'mammal'

    # intialize
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate
jake = Dog("jake", 7)
doug = Dog("doug", 4)
william = Dog("william", 5)

# determine the oldest dog
def get_biggest_number(*args):
    return max(args)

#output
print("the oldest dog is {} years old".format(get_biggest_number(jake.age, doug.age, william.age)))

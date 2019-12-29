class Tortuga:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print('Hello, I am the turtle {} and I am {} years old'.format(self.name, self.age))

if __name__ == '__main__':
    pet = Tortuga('Edison', 6)

    print('Age: {}'.format(pet.age))
    pet.say_hello()
class Animal:
    def sound(self):
        print("This animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("The dog barks")


class Cat(Animal):
    def sound(self):
        print("The cat meows")


dog = Dog()
dog.sound()

cat = Cat()
cat.sound()

animal = Animal()
animal.sound()

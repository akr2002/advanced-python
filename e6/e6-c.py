from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("This animal is sleeping")


class Dog(Animal):
    def sound(self):
        print("The dog barks")


class Cat(Animal):
    def sound(self):
        print("The cat meows")


dog = Dog()
dog.sound()
dog.sleep()

cat = Cat()
cat.sound()
cat.sleep()

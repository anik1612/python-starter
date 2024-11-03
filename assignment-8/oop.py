
# Let's explore the four pillars of Object-Oriented Programming (OOP) in Python with examples.

# 1. Encapsulation
# Encapsulation restricts direct access to some of an object's components and can prevent the accidental modification of data.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

# Creating an object of the BankAccount class
account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Balance: {account.get_balance()}")

# 2. Inheritance
# Inheritance allows a class to inherit attributes and methods from another class.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def display_battery_info(self):
        print(f"Battery size: {self.battery_size} kWh")

# Creating an object of the ElectricCar class
my_electric_car = ElectricCar("Tesla", "Model S", 2022, 100)
my_electric_car.display_info()
my_electric_car.display_battery_info()

# 3. Polymorphism
# Polymorphism allows methods to do different things based on the object it is acting upon.
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Using polymorphism
def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!

# 4. Abstraction
# Abstraction is the concept of hiding the complex reality while exposing only the necessary parts.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Creating an object of the Rectangle class
rectangle = Rectangle(5, 10)
print(f"Area of rectangle: {rectangle.area()}")

# Static, Private, and Public Members
class Example:
    public_var = "I am public"
    _protected_var = "I am protected"
    __private_var = "I am private"

    @staticmethod
    def static_method():
        print("This is a static method.")

    def get_private_var(self):
        return self.__private_var

# Accessing static method
Example.static_method()

# Accessing public, protected, and private variables
example = Example()
print(example.public_var)  # Accessible
print(example._protected_var)  # Accessible but should be treated as protected
print(example.get_private_var())  # Accessing private variable via a public method






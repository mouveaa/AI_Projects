# OOP Inheritance in Python
# Practice 4: Understanding Inheritance

print("=== Practice 4: Inheritance Basics ===")

# Base class (Parent class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"
    
    def make_sound(self):
        return f"{self.name} makes a sound"
    
    def info(self):
        return f"{self.name} is a {self.species}"

# Derived class (Child class) inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Call parent constructor using super()
        super().__init__(name, "Dog")
        self.breed = breed
    
    # Override parent method
    def make_sound(self):
        return f"{self.name} barks: Woof!"
    
    # Add new method specific to Dog
    def fetch(self):
        return f"{self.name} fetches the ball"
    
    # Override parent method and extend it
    def info(self):
        parent_info = super().info()
        return f"{parent_info} of breed {self.breed}"

class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name, "Cat")
        self.indoor = indoor
    
    def make_sound(self):
        return f"{self.name} meows: Meow!"
    
    def climb(self):
        return f"{self.name} climbs the tree"
    
    def info(self):
        parent_info = super().info()
        location = "indoor" if self.indoor else "outdoor"
        return f"{parent_info} ({location} cat)"

# Creating instances
generic_animal = Animal("Unknown", "Mystery")
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", indoor=True)

print("Generic Animal:")
print(generic_animal.info())
print(generic_animal.make_sound())

print("\nDog:")
print(dog.info())
print(dog.make_sound())
print(dog.fetch())
print(dog.eat())  # Inherited method

print("\nCat:")
print(cat.info())
print(cat.make_sound())
print(cat.climb())
print(cat.sleep())  # Inherited method

print("\n" + "="*50 + "\n")

# Practice 5: Multiple Inheritance
print("=== Practice 5: Multiple Inheritance ===")

class Flyable:
    def __init__(self):
        self.can_fly = True
    
    def fly(self):
        return "Flying through the sky"
    
    def land(self):
        return "Landing safely"

class Swimmable:
    def __init__(self):
        self.can_swim = True
    
    def swim(self):
        return "Swimming in water"
    
    def dive(self):
        return "Diving underwater"

# Multiple inheritance - Bird inherits from Animal, Flyable, and Swimmable
class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        # Call all parent constructors
        Animal.__init__(self, name, "Duck")
        Flyable.__init__(self)
        Swimmable.__init__(self)
    
    def make_sound(self):
        return f"{self.name} quacks: Quack!"
    
    def info(self):
        abilities = []
        if hasattr(self, 'can_fly') and self.can_fly:
            abilities.append("can fly")
        if hasattr(self, 'can_swim') and self.can_swim:
            abilities.append("can swim")
        
        base_info = super().info()
        if abilities:
            return f"{base_info} and {', '.join(abilities)}"
        return base_info

duck = Duck("Donald")
print(duck.info())
print(duck.make_sound())
print(duck.fly())
print(duck.swim())
print(duck.eat())  # From Animal

# Method Resolution Order (MRO)
print(f"\nDuck MRO: {Duck.__mro__}")

print("\n" + "="*50 + "\n")

# Practice 6: Abstract Base Classes and Method Overriding
print("=== Practice 6: Abstract Concepts ===")

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def info(self):
        return f"This is a {self.name}"

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def info(self):
        base_info = super().info()
        return f"{base_info} with width {self.width} and height {self.height}"

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius
    
    def info(self):
        base_info = super().info()
        return f"{base_info} with radius {self.radius}"

# Cannot instantiate abstract class
# shape = Shape("Generic")  # This would raise TypeError

rectangle = Rectangle(5, 3)
circle = Circle(4)

print(rectangle.info())
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")

print(f"\n{circle.info()}")
print(f"Area: {circle.area():.2f}")
print(f"Perimeter: {circle.perimeter():.2f}")

# Polymorphism - same method calls on different objects
shapes = [rectangle, circle]
print("\nPolymorphism in action:")
for shape in shapes:
    print(f"{shape.name}: Area = {shape.area():.2f}")
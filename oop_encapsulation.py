# OOP Encapsulation in Python
# Practice 7: Understanding Encapsulation and Data Hiding

print("=== Practice 7: Encapsulation Basics ===")

class Student:
    def __init__(self, name, age, student_id):
        # Public attributes (accessible from outside)
        self.name = name
        
        # Protected attribute (convention: single underscore)
        # Should not be accessed directly from outside, but can be
        self._age = age
        
        # Private attribute (name mangling: double underscore)
        # Cannot be accessed directly from outside
        self.__student_id = student_id
        
        # Private list to store grades
        self.__grades = []
    
    # Public method to access private data
    def get_student_id(self):
        return self.__student_id
    
    # Public method to modify private data with validation
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
            return f"Grade {grade} added successfully"
        else:
            return "Invalid grade. Must be between 0 and 100"
    
    # Public method to get private data
    def get_grades(self):
        return self.__grades.copy()  # Return a copy to prevent external modification
    
    # Public method to calculate average (using private data)
    def get_average(self):
        if self.__grades:
            return sum(self.__grades) / len(self.__grades)
        return 0
    
    # Protected method (convention)
    def _validate_age(self, age):
        return 0 <= age <= 150
    
    # Public method to set age with validation
    def set_age(self, age):
        if self._validate_age(age):
            self._age = age
            return f"Age updated to {age}"
        return "Invalid age"
    
    def get_age(self):
        return self._age
    
    def __str__(self):
        return f"Student: {self.name}, Age: {self._age}, ID: {self.__student_id}"

# Create student instance
student = Student("Alice", 20, "S12345")

print(student)
print(f"Name (public): {student.name}")
print(f"Age (protected): {student._age}")  # Accessible but shouldn't be used
print(f"Student ID (via method): {student.get_student_id()}")

# Try to access private attribute directly
try:
    print(f"Direct access to private ID: {student.__student_id}")
except AttributeError as e:
    print(f"Error accessing private attribute: {e}")

# Access private attribute using name mangling (not recommended)
print(f"Private ID via name mangling: {student._Student__student_id}")

# Add grades using public method
print(student.add_grade(85))
print(student.add_grade(92))
print(student.add_grade(105))  # Invalid grade

print(f"Grades: {student.get_grades()}")
print(f"Average: {student.get_average():.2f}")

print("\n" + "="*50 + "\n")

# Practice 8: Properties and Getters/Setters
print("=== Practice 8: Properties and Getters/Setters ===")

class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter for celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Calculated property for fahrenheit"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Setter for fahrenheit (converts to celsius)"""
        celsius_value = (value - 32) * 5/9
        if celsius_value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = celsius_value
    
    @property
    def kelvin(self):
        """Calculated property for kelvin"""
        return self._celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, value):
        """Setter for kelvin (converts to celsius)"""
        if value < 0:
            raise ValueError("Kelvin temperature cannot be negative")
        self._celsius = value - 273.15
    
    def __str__(self):
        return f"{self._celsius:.2f}°C / {self.fahrenheit:.2f}°F / {self.kelvin:.2f}K"

# Using properties
temp = Temperature(25)
print(f"Initial temperature: {temp}")

# Using property getter
print(f"Celsius: {temp.celsius}")
print(f"Fahrenheit: {temp.fahrenheit}")
print(f"Kelvin: {temp.kelvin}")

# Using property setter
temp.fahrenheit = 100  # Boiling point of water
print(f"After setting to 100°F: {temp}")

temp.kelvin = 0  # Absolute zero
print(f"After setting to 0K: {temp}")

# Validation in action
try:
    temp.celsius = -300  # Below absolute zero
except ValueError as e:
    print(f"Validation error: {e}")

print("\n" + "="*50 + "\n")

# Practice 9: Advanced Encapsulation with Descriptors
print("=== Practice 9: Advanced Encapsulation ===")

class ValidatedAttribute:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = f"_{name}"
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.name, None)
    
    def __set__(self, obj, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"Value must be at least {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"Value must be at most {self.max_value}")
        setattr(obj, self.name, value)

class Employee:
    # Using descriptors for validation
    salary = ValidatedAttribute(min_value=0, max_value=1000000)
    age = ValidatedAttribute(min_value=18, max_value=100)
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age  # Uses descriptor validation
        self.salary = salary  # Uses descriptor validation
        self.__employee_id = self._generate_id()
    
    def _generate_id(self):
        import random
        return f"EMP{random.randint(1000, 9999)}"
    
    @property
    def employee_id(self):
        return self.__employee_id
    
    def give_raise(self, amount):
        try:
            self.salary += amount
            return f"Salary increased by ${amount}. New salary: ${self.salary}"
        except ValueError as e:
            return f"Cannot give raise: {e}"
    
    def __str__(self):
        return f"Employee {self.name} (ID: {self.employee_id}), Age: {self.age}, Salary: ${self.salary}"

# Test the Employee class
emp = Employee("John Doe", 30, 50000)
print(emp)

print(emp.give_raise(10000))
print(emp)

# Test validation
try:
    emp.age = 150  # Too old
except ValueError as e:
    print(f"Age validation error: {e}")

try:
    emp.salary = -1000  # Negative salary
except ValueError as e:
    print(f"Salary validation error: {e}")

try:
    emp2 = Employee("Jane", 15, 30000)  # Too young
except ValueError as e:
    print(f"Age validation error during creation: {e}")

print("\n" + "="*50 + "\n")

# Practice 10: Composition and Encapsulation
print("=== Practice 10: Composition and Encapsulation ===")

class Engine:
    def __init__(self, horsepower, engine_type):
        self.__horsepower = horsepower
        self.__engine_type = engine_type
        self.__running = False
    
    def start(self):
        if not self.__running:
            self.__running = True
            return f"{self.__engine_type} engine started ({self.__horsepower} HP)"
        return "Engine is already running"
    
    def stop(self):
        if self.__running:
            self.__running = False
            return "Engine stopped"
        return "Engine is already stopped"
    
    @property
    def is_running(self):
        return self.__running
    
    @property
    def horsepower(self):
        return self.__horsepower
    
    def __str__(self):
        status = "running" if self.__running else "stopped"
        return f"{self.__engine_type} engine ({self.__horsepower} HP) - {status}"

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.__engine = engine  # Private composition
        self.__speed = 0
    
    def start_car(self):
        result = self.__engine.start()
        return f"Car starting... {result}"
    
    def stop_car(self):
        if self.__speed > 0:
            return "Cannot stop engine while car is moving. Stop the car first."
        result = self.__engine.stop()
        return f"Car stopping... {result}"
    
    def accelerate(self, speed_increase):
        if not self.__engine.is_running:
            return "Cannot accelerate. Engine is not running."
        
        max_speed = self.__engine.horsepower * 2  # Simple calculation
        new_speed = self.__speed + speed_increase
        
        if new_speed > max_speed:
            self.__speed = max_speed
            return f"Reached maximum speed: {max_speed} mph"
        else:
            self.__speed = new_speed
            return f"Accelerated to {self.__speed} mph"
    
    def brake(self, speed_decrease):
        self.__speed = max(0, self.__speed - speed_decrease)
        return f"Slowed down to {self.__speed} mph"
    
    @property
    def current_speed(self):
        return self.__speed
    
    def get_engine_info(self):
        return str(self.__engine)
    
    def __str__(self):
        return f"{self.make} {self.model} - Speed: {self.__speed} mph, Engine: {self.__engine}"

# Create a car with an engine
v8_engine = Engine(400, "V8")
car = Car("Ford", "Mustang", v8_engine)

print(car)
print(car.start_car())
print(car.accelerate(50))
print(car.accelerate(100))
print(car)
print(car.brake(30))
print(car.stop_car())  # Should fail - car is moving
print(car.brake(120))  # Stop the car
print(car.stop_car())  # Should succeed now
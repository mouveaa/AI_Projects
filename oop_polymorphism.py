# OOP Polymorphism in Python
# Practice 11: Understanding Polymorphism

print("=== Practice 11: Polymorphism Basics ===")

# Base class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return f"{self.name} makes a sound"
    
    def move(self):
        return f"{self.name} moves"

# Derived classes with overridden methods
class Dog(Animal):
    def make_sound(self):
        return f"{self.name} barks: Woof!"
    
    def move(self):
        return f"{self.name} runs"

class Cat(Animal):
    def make_sound(self):
        return f"{self.name} meows: Meow!"
    
    def move(self):
        return f"{self.name} prowls"

class Bird(Animal):
    def make_sound(self):
        return f"{self.name} chirps: Tweet!"
    
    def move(self):
        return f"{self.name} flies"

class Fish(Animal):
    def make_sound(self):
        return f"{self.name} blows bubbles"
    
    def move(self):
        return f"{self.name} swims"

# Polymorphism in action - same method call, different behavior
def animal_sounds_and_movements(animals):
    """Demonstrate polymorphism with a list of different animals"""
    for animal in animals:
        print(f"Sound: {animal.make_sound()}")
        print(f"Movement: {animal.move()}")
        print("-" * 30)

# Create different animals
animals = [
    Dog("Buddy"),
    Cat("Whiskers"),
    Bird("Tweety"),
    Fish("Nemo"),
    Animal("Generic")  # Base class
]

animal_sounds_and_movements(animals)

print("\n" + "="*50 + "\n")

# Practice 12: Duck Typing
print("=== Practice 12: Duck Typing ===")
print("'If it walks like a duck and quacks like a duck, then it's a duck'")

class Duck:
    def fly(self):
        return "Duck flies"
    
    def swim(self):
        return "Duck swims"
    
    def quack(self):
        return "Quack!"

class Airplane:
    def fly(self):
        return "Airplane flies"
    
    def land(self):
        return "Airplane lands"

class Boat:
    def swim(self):
        return "Boat floats on water"
    
    def dock(self):
        return "Boat docks"

class Robot:
    def fly(self):
        return "Robot hovers"
    
    def swim(self):
        return "Robot operates underwater"
    
    def quack(self):
        return "Beep beep! (robot quack)"

# Duck typing - objects with similar methods can be used interchangeably
def make_it_fly(flying_object):
    """Any object with a fly() method can be used"""
    return flying_object.fly()

def make_it_swim(swimming_object):
    """Any object with a swim() method can be used"""
    return swimming_object.swim()

def duck_activities(duck_like_object):
    """Function that works with any 'duck-like' object"""
    activities = []
    
    # Check if object has required methods before calling
    if hasattr(duck_like_object, 'fly'):
        activities.append(duck_like_object.fly())
    
    if hasattr(duck_like_object, 'swim'):
        activities.append(duck_like_object.swim())
    
    if hasattr(duck_like_object, 'quack'):
        activities.append(duck_like_object.quack())
    
    return activities

# Test duck typing
objects = [Duck(), Airplane(), Boat(), Robot()]

for obj in objects:
    print(f"{obj.__class__.__name__}:")
    activities = duck_activities(obj)
    for activity in activities:
        print(f"  - {activity}")
    print()

print("\n" + "="*50 + "\n")

# Practice 13: Operator Overloading
print("=== Practice 13: Operator Overloading ===")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # String representation
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    # Arithmetic operators
    def __add__(self, other):
        """Addition: v1 + v2"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        return NotImplemented
    
    def __sub__(self, other):
        """Subtraction: v1 - v2"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x - other, self.y - other)
        return NotImplemented
    
    def __mul__(self, other):
        """Multiplication: v1 * scalar or v1 * v2 (dot product)"""
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            # Dot product
            return self.x * other.x + self.y * other.y
        return NotImplemented
    
    def __truediv__(self, other):
        """Division: v1 / scalar"""
        if isinstance(other, (int, float)) and other != 0:
            return Vector(self.x / other, self.y / other)
        return NotImplemented
    
    # Comparison operators
    def __eq__(self, other):
        """Equality: v1 == v2"""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    
    def __lt__(self, other):
        """Less than: v1 < v2 (based on magnitude)"""
        if isinstance(other, Vector):
            return self.magnitude() < other.magnitude()
        return NotImplemented
    
    def __len__(self):
        """Length (magnitude) of vector"""
        return int(self.magnitude())
    
    def __abs__(self):
        """Absolute value (magnitude)"""
        return self.magnitude()
    
    # Utility methods
    def magnitude(self):
        """Calculate the magnitude of the vector"""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def normalize(self):
        """Return a normalized vector"""
        mag = self.magnitude()
        if mag == 0:
            return Vector(0, 0)
        return Vector(self.x / mag, self.y / mag)

# Test operator overloading
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 magnitude: {v1.magnitude():.2f}")
print(f"v2 magnitude: {v2.magnitude():.2f}")

print(f"\nv1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")
print(f"v1 / 2 = {v1 / 2}")
print(f"v1 * v2 (dot product) = {v1 * v2}")

print(f"\nv1 == v2: {v1 == v2}")
print(f"v1 < v2: {v1 < v2}")
print(f"len(v1): {len(v1)}")
print(f"abs(v1): {abs(v1):.2f}")

print("\n" + "="*50 + "\n")

# Practice 14: Polymorphism with Abstract Base Classes
print("=== Practice 14: Polymorphism with Abstract Classes ===")

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
    
    @abstractmethod
    def validate_payment(self, payment_info):
        pass
    
    def generate_receipt(self, amount, transaction_id):
        return f"Receipt: ${amount:.2f} - Transaction ID: {transaction_id}"

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # Simulate credit card processing
        transaction_id = f"CC_{hash(amount) % 10000}"
        return {
            'success': True,
            'transaction_id': transaction_id,
            'method': 'Credit Card'
        }
    
    def validate_payment(self, payment_info):
        # Simulate credit card validation
        card_number = payment_info.get('card_number', '')
        return len(card_number) == 16 and card_number.isdigit()

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # Simulate PayPal processing
        transaction_id = f"PP_{hash(amount) % 10000}"
        return {
            'success': True,
            'transaction_id': transaction_id,
            'method': 'PayPal'
        }
    
    def validate_payment(self, payment_info):
        # Simulate PayPal validation
        email = payment_info.get('email', '')
        return '@' in email and '.' in email

class BankTransferProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # Simulate bank transfer processing
        transaction_id = f"BT_{hash(amount) % 10000}"
        return {
            'success': True,
            'transaction_id': transaction_id,
            'method': 'Bank Transfer'
        }
    
    def validate_payment(self, payment_info):
        # Simulate bank account validation
        account_number = payment_info.get('account_number', '')
        return len(account_number) >= 8 and account_number.isdigit()

# Payment processing system using polymorphism
class PaymentSystem:
    def __init__(self):
        self.processors = {
            'credit_card': CreditCardProcessor(),
            'paypal': PayPalProcessor(),
            'bank_transfer': BankTransferProcessor()
        }
    
    def process_payment(self, payment_method, amount, payment_info):
        processor = self.processors.get(payment_method)
        if not processor:
            return {'success': False, 'error': 'Invalid payment method'}
        
        # Polymorphism in action - same method call, different implementations
        if not processor.validate_payment(payment_info):
            return {'success': False, 'error': 'Invalid payment information'}
        
        result = processor.process_payment(amount)
        if result['success']:
            receipt = processor.generate_receipt(amount, result['transaction_id'])
            result['receipt'] = receipt
        
        return result

# Test the payment system
payment_system = PaymentSystem()

# Test different payment methods
test_payments = [
    ('credit_card', 100.00, {'card_number': '1234567890123456'}),
    ('paypal', 75.50, {'email': 'user@example.com'}),
    ('bank_transfer', 200.00, {'account_number': '12345678'}),
    ('bitcoin', 50.00, {'wallet': 'abc123'}),  # Invalid method
    ('credit_card', 25.00, {'card_number': '123'})  # Invalid card
]

for method, amount, info in test_payments:
    print(f"Processing ${amount:.2f} via {method}:")
    result = payment_system.process_payment(method, amount, info)
    
    if result['success']:
        print(f"  ✓ Success - Method: {result['method']}")
        print(f"  {result['receipt']}")
    else:
        print(f"  ✗ Failed - {result['error']}")
    print()

print("\n" + "="*50 + "\n")

# Practice 15: Context Managers and Polymorphism
print("=== Practice 15: Context Managers and Polymorphism ===")

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing file: {self.filename}")
        if self.file:
            self.file.close()
        
        if exc_type:
            print(f"Exception occurred: {exc_val}")
        return False  # Don't suppress exceptions

class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connected = False
    
    def __enter__(self):
        print(f"Connecting to database: {self.connection_string}")
        self.connected = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Disconnecting from database")
        self.connected = False
        return False
    
    def execute_query(self, query):
        if self.connected:
            return f"Executed: {query}"
        return "Not connected to database"

# Using context managers polymorphically
def demonstrate_context_managers():
    # File context manager
    try:
        with FileManager("test.txt", "w") as f:
            f.write("Hello, World!")
            print("File written successfully")
    except Exception as e:
        print(f"File operation error: {e}")
    
    print()
    
    # Database context manager
    with DatabaseConnection("postgresql://localhost:5432/mydb") as db:
        result = db.execute_query("SELECT * FROM users")
        print(result)

demonstrate_context_managers()
# OOP Basics in Python
# Practice 1: Understanding Classes and Objects

print("=== Practice 1: Classes and Objects ===")

# A class is a blueprint for creating objects
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    # Constructor method (initializer)
    def __init__(self, name, age, breed):
        # Instance attributes (unique to each object)
        self.name = name
        self.age = age
        self.breed = breed
    
    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"
    
    # Instance method with parameters
    def describe(self):
        return f"{self.name} is a {self.age} year old {self.breed}"
    
    # Method that modifies state
    def have_birthday(self):
        self.age += 1
        return f"Happy birthday {self.name}! Now {self.age} years old."

# Creating objects (instances) from the class
dog1 = Dog("Buddy", 3, "Golden Retriever")
dog2 = Dog("Luna", 2, "Border Collie")

print(f"Dog 1: {dog1.describe()}")
print(f"Dog 2: {dog2.describe()}")
print(dog1.bark())
print(dog2.bark())
print(dog1.have_birthday())

# Accessing class attributes
print(f"Species: {Dog.species}")
print(f"Dog1 species: {dog1.species}")

print("\n" + "="*50 + "\n")

# Practice 2: Understanding self keyword
print("=== Practice 2: Understanding 'self' ===")

class Counter:
    def __init__(self, initial_value=0):
        self.value = initial_value
    
    def increment(self):
        # 'self' refers to the specific instance
        self.value += 1
        return self.value
    
    def decrement(self):
        self.value -= 1
        return self.value
    
    def get_value(self):
        return self.value

# Each instance maintains its own state
counter1 = Counter()
counter2 = Counter(10)

print(f"Counter1 initial: {counter1.get_value()}")
print(f"Counter2 initial: {counter2.get_value()}")

counter1.increment()
counter1.increment()
counter2.decrement()

print(f"Counter1 after increments: {counter1.get_value()}")
print(f"Counter2 after decrement: {counter2.get_value()}")

print("\n" + "="*50 + "\n")

# Practice 3: Class vs Instance attributes
print("=== Practice 3: Class vs Instance Attributes ===")

class BankAccount:
    # Class attribute - shared by all instances
    bank_name = "Python Bank"
    interest_rate = 0.02
    
    def __init__(self, account_holder, initial_balance=0):
        # Instance attributes - unique to each instance
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Insufficient funds or invalid amount"
    
    def get_account_info(self):
        return f"Account holder: {self.account_holder}\nBalance: ${self.balance}\nBank: {self.bank_name}"

# Creating accounts
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

print(account1.get_account_info())
print("\n")
print(account2.get_account_info())

print("\n")
print(account1.deposit(200))
print(account2.withdraw(100))

# Modifying class attribute affects all instances
BankAccount.interest_rate = 0.03
print(f"\nNew interest rate for all accounts: {BankAccount.interest_rate}")
print(f"Account1 interest rate: {account1.interest_rate}")
print(f"Account2 interest rate: {account2.interest_rate}")
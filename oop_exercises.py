# OOP Practical Exercises in Python
# These exercises will help you practice and understand OOP concepts

print("=== OOP Practice Exercises ===")
print("Try to solve these exercises step by step!")
print("\n" + "="*50 + "\n")

# Exercise 1: Library Management System
print("Exercise 1: Library Management System")
print("-" * 40)
print("""
Create a library management system with the following requirements:

1. Book class with attributes: title, author, isbn, available_copies
2. Member class with attributes: name, member_id, borrowed_books (list)
3. Library class that manages books and members
4. Implement methods for:
   - Adding books to library
   - Registering members
   - Borrowing books (decrease available copies)
   - Returning books (increase available copies)
   - Searching books by title or author
""")

# Solution for Exercise 1
class Book:
    def __init__(self, title, author, isbn, total_copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = total_copies
    
    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {self.available_copies}/{self.total_copies} available"
    
    def is_available(self):
        return self.available_copies > 0
    
    def borrow(self):
        if self.is_available():
            self.available_copies -= 1
            return True
        return False
    
    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id}) - {len(self.borrowed_books)} books borrowed"
    
    def borrow_book(self, book):
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
    
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
    
    def add_book(self, book):
        # Check if book already exists
        for existing_book in self.books:
            if existing_book.isbn == book.isbn:
                existing_book.total_copies += book.total_copies
                existing_book.available_copies += book.total_copies
                return f"Added {book.total_copies} more copies of '{book.title}'"
        
        self.books.append(book)
        return f"Added new book: '{book.title}'"
    
    def register_member(self, member):
        for existing_member in self.members:
            if existing_member.member_id == member.member_id:
                return f"Member with ID {member.member_id} already exists"
        
        self.members.append(member)
        return f"Registered new member: {member.name}"
    
    def find_book_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]
    
    def find_book_by_author(self, author):
        return [book for book in self.books if author.lower() in book.author.lower()]
    
    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
    
    def borrow_book(self, member_id, isbn):
        member = self.find_member(member_id)
        if not member:
            return "Member not found"
        
        book = None
        for b in self.books:
            if b.isbn == isbn:
                book = b
                break
        
        if not book:
            return "Book not found"
        
        if not book.is_available():
            return f"'{book.title}' is not available"
        
        if book.borrow():
            member.borrow_book(book)
            return f"{member.name} borrowed '{book.title}'"
        
        return "Failed to borrow book"
    
    def return_book(self, member_id, isbn):
        member = self.find_member(member_id)
        if not member:
            return "Member not found"
        
        book = None
        for b in self.books:
            if b.isbn == isbn:
                book = b
                break
        
        if not book:
            return "Book not found"
        
        if book in member.borrowed_books:
            book.return_book()
            member.return_book(book)
            return f"{member.name} returned '{book.title}'"
        
        return f"{member.name} hasn't borrowed this book"
    
    def display_available_books(self):
        available_books = [book for book in self.books if book.is_available()]
        if not available_books:
            return "No books available"
        
        result = f"Available books in {self.name}:\n"
        for book in available_books:
            result += f"  - {book}\n"
        return result

# Test the Library Management System
print("\nSolution demonstration:")
library = Library("City Central Library")

# Add books
book1 = Book("Python Programming", "John Smith", "978-1234567890", 3)
book2 = Book("Data Structures", "Jane Doe", "978-0987654321", 2)
book3 = Book("Web Development", "Bob Johnson", "978-1122334455", 1)

print(library.add_book(book1))
print(library.add_book(book2))
print(library.add_book(book3))

# Register members
member1 = Member("Alice Wilson", "M001")
member2 = Member("Charlie Brown", "M002")

print(library.register_member(member1))
print(library.register_member(member2))

# Display available books
print("\n" + library.display_available_books())

# Borrow books
print(library.borrow_book("M001", "978-1234567890"))
print(library.borrow_book("M002", "978-0987654321"))
print(library.borrow_book("M001", "978-1122334455"))

print("\nAfter borrowing:")
print(library.display_available_books())

# Return a book
print(library.return_book("M001", "978-1234567890"))

print("\nAfter returning:")
print(library.display_available_books())

print("\n" + "="*70 + "\n")

# Exercise 2: E-commerce System
print("Exercise 2: E-commerce System")
print("-" * 40)
print("""
Create an e-commerce system with:

1. Product class (name, price, stock_quantity)
2. Customer class (name, email, cart, order_history)
3. ShoppingCart class (items, total_price calculation)
4. Order class (customer, items, order_date, status)
5. Store class that manages everything

Implement polymorphism with different product types:
- ElectronicsProduct (warranty_period)
- ClothingProduct (size, color)
- BookProduct (author, pages)
""")

from datetime import datetime
from abc import ABC, abstractmethod

# Base Product class
class Product(ABC):
    def __init__(self, product_id, name, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
    
    @abstractmethod
    def get_details(self):
        pass
    
    def is_in_stock(self, quantity=1):
        return self.stock_quantity >= quantity
    
    def reduce_stock(self, quantity):
        if self.is_in_stock(quantity):
            self.stock_quantity -= quantity
            return True
        return False
    
    def increase_stock(self, quantity):
        self.stock_quantity += quantity
    
    def __str__(self):
        return f"{self.name} - ${self.price:.2f} (Stock: {self.stock_quantity})"

class ElectronicsProduct(Product):
    def __init__(self, product_id, name, price, stock_quantity, warranty_period):
        super().__init__(product_id, name, price, stock_quantity)
        self.warranty_period = warranty_period
    
    def get_details(self):
        return f"Electronics: {self.name} - ${self.price:.2f} ({self.warranty_period} year warranty)"

class ClothingProduct(Product):
    def __init__(self, product_id, name, price, stock_quantity, size, color):
        super().__init__(product_id, name, price, stock_quantity)
        self.size = size
        self.color = color
    
    def get_details(self):
        return f"Clothing: {self.name} - ${self.price:.2f} (Size: {self.size}, Color: {self.color})"

class BookProduct(Product):
    def __init__(self, product_id, name, price, stock_quantity, author, pages):
        super().__init__(product_id, name, price, stock_quantity)
        self.author = author
        self.pages = pages
    
    def get_details(self):
        return f"Book: {self.name} by {self.author} - ${self.price:.2f} ({self.pages} pages)"

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    
    def get_total_price(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.product.name} x{self.quantity} = ${self.get_total_price():.2f}"

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, product, quantity):
        # Check if product already in cart
        for item in self.items:
            if item.product.product_id == product.product_id:
                item.quantity += quantity
                return f"Updated {product.name} quantity to {item.quantity}"
        
        # Add new item
        self.items.append(CartItem(product, quantity))
        return f"Added {quantity} x {product.name} to cart"
    
    def remove_item(self, product_id):
        self.items = [item for item in self.items if item.product.product_id != product_id]
    
    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items)
    
    def get_total_items(self):
        return sum(item.quantity for item in self.items)
    
    def clear(self):
        self.items = []
    
    def __str__(self):
        if not self.items:
            return "Cart is empty"
        
        result = "Shopping Cart:\n"
        for item in self.items:
            result += f"  - {item}\n"
        result += f"Total: ${self.get_total_price():.2f} ({self.get_total_items()} items)"
        return result

class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.cart = ShoppingCart()
        self.order_history = []
    
    def add_to_cart(self, product, quantity):
        return self.cart.add_item(product, quantity)
    
    def view_cart(self):
        return str(self.cart)
    
    def __str__(self):
        return f"Customer: {self.name} ({self.email})"

class Order:
    def __init__(self, order_id, customer, cart_items):
        self.order_id = order_id
        self.customer = customer
        self.items = cart_items.copy()
        self.order_date = datetime.now()
        self.status = "Pending"
        self.total_amount = sum(item.get_total_price() for item in self.items)
    
    def update_status(self, new_status):
        self.status = new_status
    
    def __str__(self):
        result = f"Order #{self.order_id} - {self.customer.name}\n"
        result += f"Date: {self.order_date.strftime('%Y-%m-%d %H:%M')}\n"
        result += f"Status: {self.status}\n"
        result += "Items:\n"
        for item in self.items:
            result += f"  - {item}\n"
        result += f"Total: ${self.total_amount:.2f}"
        return result

class Store:
    def __init__(self, name):
        self.name = name
        self.products = {}
        self.customers = {}
        self.orders = {}
        self.next_order_id = 1
    
    def add_product(self, product):
        self.products[product.product_id] = product
        return f"Added product: {product.name}"
    
    def register_customer(self, customer):
        self.customers[customer.customer_id] = customer
        return f"Registered customer: {customer.name}"
    
    def find_product(self, product_id):
        return self.products.get(product_id)
    
    def find_customer(self, customer_id):
        return self.customers.get(customer_id)
    
    def add_to_customer_cart(self, customer_id, product_id, quantity):
        customer = self.find_customer(customer_id)
        product = self.find_product(product_id)
        
        if not customer:
            return "Customer not found"
        if not product:
            return "Product not found"
        if not product.is_in_stock(quantity):
            return f"Insufficient stock for {product.name}"
        
        return customer.add_to_cart(product, quantity)
    
    def create_order(self, customer_id):
        customer = self.find_customer(customer_id)
        if not customer:
            return "Customer not found"
        
        if not customer.cart.items:
            return "Cart is empty"
        
        # Check stock availability
        for item in customer.cart.items:
            if not item.product.is_in_stock(item.quantity):
                return f"Insufficient stock for {item.product.name}"
        
        # Reduce stock
        for item in customer.cart.items:
            item.product.reduce_stock(item.quantity)
        
        # Create order
        order = Order(self.next_order_id, customer, customer.cart.items)
        self.orders[self.next_order_id] = order
        customer.order_history.append(order)
        self.next_order_id += 1
        
        # Clear cart
        customer.cart.clear()
        
        return f"Order #{order.order_id} created successfully"
    
    def get_product_catalog(self):
        if not self.products:
            return "No products available"
        
        result = f"{self.name} Product Catalog:\n"
        for product in self.products.values():
            result += f"  - {product.get_details()}\n"
        return result

# Test the E-commerce System
print("\nSolution demonstration:")
store = Store("TechMart Online")

# Add products
laptop = ElectronicsProduct("E001", "Gaming Laptop", 1299.99, 5, 2)
tshirt = ClothingProduct("C001", "Cotton T-Shirt", 29.99, 20, "L", "Blue")
book = BookProduct("B001", "Python Mastery", 49.99, 10, "John Doe", 350)

print(store.add_product(laptop))
print(store.add_product(tshirt))
print(store.add_product(book))

# Register customers
customer1 = Customer("CUST001", "Alice Johnson", "alice@email.com")
customer2 = Customer("CUST002", "Bob Smith", "bob@email.com")

print(store.register_customer(customer1))
print(store.register_customer(customer2))

# Show catalog
print("\n" + store.get_product_catalog())

# Add items to cart
print(store.add_to_customer_cart("CUST001", "E001", 1))
print(store.add_to_customer_cart("CUST001", "B001", 2))
print(store.add_to_customer_cart("CUST002", "C001", 3))

# View carts
print(f"\n{customer1.view_cart()}")
print(f"\n{customer2.view_cart()}")

# Create orders
print(f"\n{store.create_order('CUST001')}")
print(f"{store.create_order('CUST002')}")

# View orders
if store.orders:
    print("\nRecent Orders:")
    for order in store.orders.values():
        print(order)
        print("-" * 40)

print("\n" + "="*70 + "\n")

# Exercise 3: Your Turn!
print("Exercise 3: Your Challenge!")
print("-" * 40)
print("""
Now it's your turn! Create a Vehicle Management System with:

1. Base Vehicle class with common attributes (make, model, year, mileage)
2. Inherited classes: Car, Motorcycle, Truck
3. Each vehicle type should have specific attributes and methods
4. Create a Garage class that can:
   - Store different types of vehicles
   - Calculate total value of all vehicles
   - Find vehicles by make or model
   - Service vehicles (increase mileage, update service history)

Requirements:
- Use inheritance and polymorphism
- Implement proper encapsulation
- Add validation for vehicle data
- Create methods to display vehicle information

Try to implement this yourself before looking at any solution!
""")

print("Good luck with your OOP journey! 🚀")
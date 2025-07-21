#!/usr/bin/env python3
"""
OOP Learning Hub - Interactive Python OOP Examples
Run this script to explore Object Oriented Programming concepts in Python
"""

import os
import sys
from pathlib import Path

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    """Display the main menu"""
    clear_screen()
    print("🐍 Python OOP Learning Hub 🐍")
    print("=" * 50)
    print()
    print("Choose a topic to explore:")
    print()
    print("1. 📚 OOP Basics (Classes, Objects, Methods)")
    print("2. 🧬 Inheritance (Parent-Child Classes, super())")
    print("3. 🔒 Encapsulation (Private/Protected, Properties)")
    print("4. 🎭 Polymorphism (Method Overriding, Duck Typing)")
    print("5. 💪 Practice Exercises (Library, E-commerce)")
    print("6. 📖 Quick Reference Guide")
    print("7. ❓ OOP Quiz")
    print("0. 🚪 Exit")
    print()
    print("=" * 50)

def run_oop_basics():
    """Run the OOP basics examples"""
    clear_screen()
    print("🏃‍♂️ Running OOP Basics Examples...")
    print("=" * 50)
    
    try:
        exec(open('oop_basics.py').read())
    except FileNotFoundError:
        print("❌ Error: oop_basics.py not found!")
    except Exception as e:
        print(f"❌ Error running examples: {e}")
    
    input("\n📚 Press Enter to return to menu...")

def run_inheritance():
    """Run the inheritance examples"""
    clear_screen()
    print("🏃‍♂️ Running Inheritance Examples...")
    print("=" * 50)
    
    try:
        exec(open('oop_inheritance.py').read())
    except FileNotFoundError:
        print("❌ Error: oop_inheritance.py not found!")
    except Exception as e:
        print(f"❌ Error running examples: {e}")
    
    input("\n🧬 Press Enter to return to menu...")

def run_encapsulation():
    """Run the encapsulation examples"""
    clear_screen()
    print("🏃‍♂️ Running Encapsulation Examples...")
    print("=" * 50)
    
    try:
        exec(open('oop_encapsulation.py').read())
    except FileNotFoundError:
        print("❌ Error: oop_encapsulation.py not found!")
    except Exception as e:
        print(f"❌ Error running examples: {e}")
    
    input("\n🔒 Press Enter to return to menu...")

def run_polymorphism():
    """Run the polymorphism examples"""
    clear_screen()
    print("🏃‍♂️ Running Polymorphism Examples...")
    print("=" * 50)
    
    try:
        exec(open('oop_polymorphism.py').read())
    except FileNotFoundError:
        print("❌ Error: oop_polymorphism.py not found!")
    except Exception as e:
        print(f"❌ Error running examples: {e}")
    
    input("\n🎭 Press Enter to return to menu...")

def run_exercises():
    """Run the practice exercises"""
    clear_screen()
    print("🏃‍♂️ Running Practice Exercises...")
    print("=" * 50)
    
    try:
        exec(open('oop_exercises.py').read())
    except FileNotFoundError:
        print("❌ Error: oop_exercises.py not found!")
    except Exception as e:
        print(f"❌ Error running examples: {e}")
    
    input("\n💪 Press Enter to return to menu...")

def show_reference_guide():
    """Show a quick reference guide for OOP concepts"""
    clear_screen()
    print("📖 Python OOP Quick Reference Guide")
    print("=" * 50)
    print()
    
    reference = """
🔸 CLASS DEFINITION:
    class MyClass:
        def __init__(self, param):
            self.attribute = param
        
        def method(self):
            return self.attribute

🔸 INHERITANCE:
    class Child(Parent):
        def __init__(self, param):
            super().__init__(param)
        
        def method(self):  # Override parent method
            return super().method() + " extended"

🔸 ENCAPSULATION:
    class MyClass:
        def __init__(self):
            self.public = "everyone can access"
            self._protected = "subclasses can access"
            self.__private = "only this class can access"
        
        @property
        def private(self):
            return self.__private
        
        @private.setter
        def private(self, value):
            self.__private = value

🔸 POLYMORPHISM:
    # Method overriding
    class Dog(Animal):
        def make_sound(self):
            return "Woof!"
    
    # Duck typing
    def make_noise(animal):
        return animal.make_sound()  # Works with any object having make_sound()

🔸 ABSTRACT CLASSES:
    from abc import ABC, abstractmethod
    
    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass

🔸 SPECIAL METHODS:
    def __str__(self):      # String representation
    def __len__(self):      # Length
    def __add__(self, other):  # Addition operator
    def __eq__(self, other):   # Equality operator

🔸 CLASS vs INSTANCE ATTRIBUTES:
    class MyClass:
        class_attr = "shared by all instances"
        
        def __init__(self):
            self.instance_attr = "unique to each instance"

🔸 COMPOSITION:
    class Car:
        def __init__(self):
            self.engine = Engine()  # Car "has-a" Engine
    """
    
    print(reference)
    input("\n📖 Press Enter to return to menu...")

def run_quiz():
    """Run an interactive OOP quiz"""
    clear_screen()
    print("❓ Python OOP Quiz")
    print("=" * 50)
    print()
    
    questions = [
        {
            "question": "What is the purpose of the __init__ method in Python?",
            "options": [
                "A) To delete an object",
                "B) To initialize object attributes",
                "C) To create a class",
                "D) To inherit from parent class"
            ],
            "correct": "B",
            "explanation": "__init__ is the constructor method that initializes object attributes when an instance is created."
        },
        {
            "question": "What does 'self' represent in a Python class method?",
            "options": [
                "A) The class itself",
                "B) The parent class",
                "C) The current instance of the class",
                "D) A static variable"
            ],
            "correct": "C",
            "explanation": "'self' refers to the current instance of the class, allowing access to instance attributes and methods."
        },
        {
            "question": "Which principle of OOP allows a subclass to provide a specific implementation of a method from its parent class?",
            "options": [
                "A) Encapsulation",
                "B) Inheritance",
                "C) Polymorphism",
                "D) Abstraction"
            ],
            "correct": "C",
            "explanation": "Polymorphism allows subclasses to override parent methods with their own specific implementations."
        },
        {
            "question": "What does a double underscore prefix (like __attribute) do in Python?",
            "options": [
                "A) Makes the attribute public",
                "B) Makes the attribute protected",
                "C) Triggers name mangling for privacy",
                "D) Creates a class attribute"
            ],
            "correct": "C",
            "explanation": "Double underscore prefix triggers name mangling, making the attribute harder to access from outside the class."
        },
        {
            "question": "What is the super() function used for?",
            "options": [
                "A) To create a superclass",
                "B) To access parent class methods and attributes",
                "C) To make a method static",
                "D) To delete a parent class"
            ],
            "correct": "B",
            "explanation": "super() is used to call methods from the parent class, especially useful in inheritance."
        }
    ]
    
    score = 0
    total_questions = len(questions)
    
    for i, q in enumerate(questions, 1):
        print(f"Question {i}/{total_questions}:")
        print(q["question"])
        print()
        
        for option in q["options"]:
            print(f"  {option}")
        print()
        
        while True:
            answer = input("Your answer (A/B/C/D): ").upper().strip()
            if answer in ['A', 'B', 'C', 'D']:
                break
            print("Please enter A, B, C, or D")
        
        if answer == q["correct"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer is {q['correct']}")
        
        print(f"💡 Explanation: {q['explanation']}")
        print()
        input("Press Enter for next question...")
        print("-" * 50)
    
    # Show final score
    percentage = (score / total_questions) * 100
    print(f"\n🎯 Quiz Complete!")
    print(f"Score: {score}/{total_questions} ({percentage:.1f}%)")
    
    if percentage >= 80:
        print("🏆 Excellent! You have a great understanding of OOP!")
    elif percentage >= 60:
        print("👍 Good job! Keep practicing to master OOP concepts.")
    else:
        print("📚 Keep studying! Review the examples and try again.")
    
    input("\n❓ Press Enter to return to menu...")

def main():
    """Main program loop"""
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (0-7): ").strip()
            
            if choice == '0':
                clear_screen()
                print("👋 Thanks for learning Python OOP!")
                print("Keep practicing and happy coding! 🚀")
                break
            elif choice == '1':
                run_oop_basics()
            elif choice == '2':
                run_inheritance()
            elif choice == '3':
                run_encapsulation()
            elif choice == '4':
                run_polymorphism()
            elif choice == '5':
                run_exercises()
            elif choice == '6':
                show_reference_guide()
            elif choice == '7':
                run_quiz()
            else:
                clear_screen()
                print("❌ Invalid choice! Please enter a number between 0-7.")
                input("Press Enter to continue...")
        
        except KeyboardInterrupt:
            clear_screen()
            print("\n👋 Thanks for learning Python OOP!")
            print("Keep practicing and happy coding! 🚀")
            break
        except Exception as e:
            clear_screen()
            print(f"❌ An error occurred: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
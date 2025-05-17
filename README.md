# 🧮 Python Assignments – OOP, Stack, and Calculator Projects

This repository contains coding assignments from an Object-Oriented Programming course. It includes a series of structured Python exercises focused on building class hierarchies, custom data structures, and practical applications like calculators and school databases. Each assignment builds progressively on Python's OOP principles, encapsulation, and method overloading.

---

## 📁 Contents

### ✅ `HW1.py`: Class and Method Fundamentals
- Implements basic Python classes with attributes and methods.
- Focuses on encapsulation and using `__str__`, `__repr__`, and equality methods.
- Prepares foundation for later, more advanced object interactions.

---

### ✅ `HW2.py` and [`HW2.pdf`](HW2.pdf): In-Memory School Database
- **8 interrelated classes**: `Course`, `Catalog`, `Semester`, `Loan`, `Person`, `Student`, `Staff`, `StudentAccount`.
- Simulates a school system where:
  - Staff can create students and apply/remove holds.
  - Students can enroll in courses, request loans, and manage balances.
- Uses:
  - Inheritance and method overriding
  - Operator overloading
  - Property methods and random loan ID generation

---

### ✅ `HW3.py` and [`HW3.pdf`](HW3.pdf): Stack + Calculator (Infix to Postfix)
- **`Stack` class**: Custom implementation using linked lists (no Python list).
- **`Calculator` class**:
  - Converts infix expressions (like `3 + 4 * 2`) into postfix
  - Evaluates postfix expressions using the custom stack
  - Handles PEMDAS, negative numbers, and invalid expressions
- **`AdvancedCalculator` class**:
  - Supports **multiple expressions** and **variables**
  - Parses and computes lines like:  
    `A = 1; B = A + 5; return B * 2`

---

### ✅ `HW4.py`: Expression Evaluation (Extended)
- Expands on the calculator from HW3.
- Introduces more robust handling for edge cases and multi-expression logic.
- May include:
  - More expression validation
  - Variable handling
  - Stateful evaluations

---

## 💡 Concepts Practiced

- Object-Oriented Programming (OOP)
- Inheritance and encapsulation
- Custom data structures (e.g., linked-list-based stacks)
- Expression parsing and evaluation
- Use of helper classes/methods for clean code design
- Test case validation and exception handling

---

## 🚀 How to Run

```bash
# Run any assignment file directly
python3 HW1.py
python3 HW3.py

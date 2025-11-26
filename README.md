# ✅ **Project Title:** University Registration System using OOP & Abstraction in Python

## 📌 **Project Overview**

This project demonstrates how Object-Oriented Programming (OOP) concepts can be used to build a simple university registration system. The system allows three types of users—Students, Professors, and Administration staff—to register their details, store them, and display the registered information. The project mainly focuses on **abstraction, inheritance, polymorphism, encapsulation, class methods, and static methods**.

---

## 🧩 **Core Concept**

At the heart of the project is the idea that different people in a university (Student, Professor, Administration) share some common properties like name and age, but each also has a different role. To represent this in a structured way, the project uses an **abstract base class** and multiple subclasses.

---

## 🏛️ **1. Abstract Class: `Person`**

* `Person` acts as a **blueprint** for all types of users.
* It stores common attributes:

  * Name
  * Age
* It contains:

  * One **abstract method**: `get_role()` which must be implemented by every subclass.
  * Concrete methods like:

    * `getbasicinfo()` → returns name and age
    * `getdetails()` → adds role information

✅ The abstract class ensures that no "Person" object can be created directly and every child class must define its role.

---

## 👥 **2. Inherited Subclasses**

There are three subclasses:

### ✅ `Student`

* Inherits from `Person`
* Adds:

  * Student ID
  * Course
* Overrides `get_role()` to return "Student"
* Provides a method `getstudentinfo()` for full details

### ✅ `Professor`

* Adds:

  * Professor ID
  * Department
* Overrides role as "Professor"
* Provides `getprofessorinfo()`

### ✅ `Administration`

* Adds:

  * Admin ID
  * Department
* Overrides role as "Administration"
* Provides `getadministrationinfo()`

✅ All three classes use **inheritance** and **polymorphism**, since `get_role()` behaves differently based on the object type.

---

## 🔐 **3. Encapsulation**

* All attributes like `__name`, `__age`, `__stuid`, etc., are private.
* This hides the internal data and prevents direct access from outside the class.
* Information is accessed only through methods.

---

## 🏫 **4. University Class**

* Maintains the list of registered people.
* Allows:

  * Adding new registrations
  * Displaying all registered users
* Uses:

  * **Class method** `getuniversityname()` — returns university name
  * **Static method** `welcomemessage()` — displays a welcome message

✅ This class acts as the system controller for storing all registered records.

---

## 🖥️ **5. User Interaction (Driver Code)**

* A simple menu-driven loop allows the user to:

  1. Register a student
  2. Register a professor
  3. Register administration staff
  4. Display all registered users
  5. Exit the application

✅ Based on the user’s choice, the program creates the appropriate object and stores it.

---

## 🎯 **Key OOP Concepts Demonstrated**

| Concept       | Where Used                                  |
| ------------- | ------------------------------------------- |
| Abstraction   | `Person` abstract class                     |
| Inheritance   | Student, Professor, Administration          |
| Polymorphism  | `get_role()` overridden in each subclass    |
| Encapsulation | Private variables (`__name`, `__age`, etc.) |
| Class Method  | `getuniversityname()`                       |
| Static Method | `welcomemessage()`                          |

---

## ✅ **Outcome**

This project successfully shows how OOP principles can be applied to design a real-world system. It provides a scalable structure where new roles can be added easily by creating new subclasses. It also demonstrates clean code organization, reusability, and modular design.


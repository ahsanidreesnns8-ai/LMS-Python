# LMS-Python
# Learning Management System (LMS) 🎓

A comprehensive, Object-Oriented Python application designed to simulate a University Learning Management System (LMS). This project manages student records, course content, attendance tracking, fee verification, hostel allotments, and GPA calculations.

## 🚀 Overview

Developed as a **1st Semester project**, this system demonstrates the use of Python **Classes and Objects** to create a modular and scalable management tool. It includes sophisticated logic for academic requirements, such as the 75% attendance rule for exam eligibility.

## ✨ Features

- **Student Authentication:** Secure login system with username and password verification.
- **Academic Management:**
  - **Course Tracking:** Manage 16 weeks of course content per subject.
  - **Attendance Monitoring:** Automated check for the 75% attendance threshold.
  - **Result Processing:** Detailed marks distribution (Mid-terms, Finals, Quizzes, Assignments, Projects, and Vivas).
- **Financial Module:**
  - Category-based fee structures (A1/A2 categories).
  - Multi-challan verification and fee status reporting.
- **Hostel Information System:** Verification of residence status, hall assignment, and room details using token authentication.
- **GPA Calculator:**
  - Support for variable credit hours (1, 2, or 3).
  - Automated conversion of letter grades to grade points (e.g., A+ = 4.0).
  - Detailed final transcript generation.

## 🛠️ Technical Deep Dive

- **Object-Oriented Programming:** The entire system is encapsulated within the `LMS` class.
- **Error Handling:** Uses `try-except` blocks to manage invalid inputs and prevent system crashes.
- **Data Encapsulation:** Student details (registration number, degree, etc.) are stored as instance attributes.
- **Visual Feedback:** Uses terminal-based progress bars and loading animations for an enhanced user experience.

## 📈 GPA Calculation Logic

The system calculates GPA based on the weighted average of credit hours:

$$GPA = \frac{\sum (Grade Points \times Credit Hours)}{Total Credit Hours}$$

## 🚀 How to Run

1. **Prerequisites:** Ensure you have Python 3.x installed.
2. **Setup:** Download `LMS(1st Semester) Project.py`.
3. **Execution:**
   ```bash
   python "LMS(1st Semester) Project.py"

## Author
M. Ahsan Idrees

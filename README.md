# Password Strength Analyzer

## Overview

The Password Strength Analyzer is a Python-based cybersecurity tool that evaluates the strength of user passwords using common security standards. The application analyzes passwords based on length, character diversity, and complexity requirements, then categorizes them as Weak, Medium, or Strong.
The project aims to promote awareness of secure password creation practices and demonstrate the implementation of fundamental cybersecurity concepts through Python programming.

## Project Objectives

* Evaluate password strength using predefined security criteria.
* Encourage the use of secure passwords.
* Provide recommendations for improving password security.
* Demonstrate the practical use of Python in cybersecurity-related tasks.

## Features

### Password Length Validation

Checks whether the password meets the recommended minimum length requirement.

### Character Complexity Analysis

Verifies the presence of:

* Uppercase letters (A–Z)
* Lowercase letters (a–z)
* Numeric characters (0–9)
* Special characters (!, @, #, $, %, &, *, etc.)

### Password Strength Classification

Classifies passwords into:

* Weak
* Medium
* Strong

### Improvement Suggestions

Provides actionable recommendations to help users strengthen weak or medium-strength passwords.

## Technologies Used

* Python 3
* Regular Expressions (re module)

## Working Principle

The application accepts a password from the user and evaluates it against multiple security parameters. Each satisfied criterion contributes to the overall score. Based on the final score, the password is categorized into a strength level and suggestions are generated when necessary.

## Project Structure

Password-Strength-Analyzer/

├── password_analyzer.py

├── README.md

└── screenshots/
└── password-strength-results.png

## Sample Execution

### Example 1 – Weak Password

**Input:**

pass1

**Output:**

Password Strength: Weak

Suggestions:

* Use at least 8 characters.
* Add an uppercase letter.
* Add a special character.

### Example 2 – Medium Password

**Input:**

password123

**Output:**

Password Strength: Medium

Suggestions:

* Add an uppercase letter.
* Add a special character.

### Example 3 – Strong Password

**Input:**

Rubix@3690

**Output:**

Password Strength: Strong

## Project Demonstration

The screenshot below demonstrates the successful execution of the Password Strength Analyzer and shows the classification of passwords as Weak, Medium, and Strong based on predefined security criteria.

## Learning Outcomes

Through the development of this project, the following concepts were explored:

* Password Security Fundamentals
* Input Validation Techniques
* Regular Expressions in Python
* Secure Authentication Practices
* Cybersecurity Best Practices

## Future Enhancements

Potential future improvements include:

* Graphical User Interface (GUI)
* Password Entropy Calculation
* Real-Time Password Strength Meter
* Password Breach Detection Integration
* Password History Validation

## Conclusion

The Password Strength Analyzer successfully evaluates password strength by analyzing various password characteristics and providing constructive feedback to users. The project highlights the importance of strong password practices and demonstrates fundamental cybersecurity concepts related to authentication and password security.

import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    # Number Check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add a number.")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add a special character.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions


password = input("Enter Password: ")

strength, suggestions = check_password_strength(password)

print(f"\nPassword Strength: {strength}")

if suggestions:
    print("\nSuggestions:")
    for item in suggestions:
        print("-", item)
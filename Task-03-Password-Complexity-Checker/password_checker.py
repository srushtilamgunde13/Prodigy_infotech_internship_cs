import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Criteria 1: Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long")

    # Criteria 2: Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one UPPERCASE letter (A-Z)")

    # Criteria 3: Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter (a-z)")

    # Criteria 4: Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9)")

    # Criteria 5: Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character (!@#$%^&*)")

    # Strength Rating
    if score == 5:
        strength = "VERY STRONG 🔒🔒🔒"
    elif score == 4:
        strength = "STRONG 🔒🔒"
    elif score == 3:
        strength = "MODERATE ⚠️"
    elif score == 2:
        strength = "WEAK ⚠️"
    else:
        strength = "VERY WEAK ❌"

    print("\n" + "="*40)
    print(f"Password: {password}")
    print(f"Strength: {strength} ({score}/5)")
    print("="*40)
    if feedback:
        print("\nSuggestions to improve:")
        for f in feedback:
            print(f)
    else:
        print("\n✅ Excellent! Your password meets all criteria.")
    print("="*40 + "\n")

def main():
    print("=== Password Complexity Checker - Task 03 ===")
    while True:
        pwd = input("Enter password (or 'q' to quit): ")
        if pwd.lower() == 'q':
            break
        check_password_strength(pwd)

if __name__ == "__main__":
    main()
    
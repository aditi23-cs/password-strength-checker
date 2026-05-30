import re

# List of common weak passwords
COMMON_PASSWORDS = [
    "password", "123456", "password123", "admin", "letmein",
    "qwerty", "abc123", "111111", "iloveyou", "welcome"
]

def check_password_strength(password):
    score = 0
    feedback = []

    # Check if it's a common password
    if password.lower() in COMMON_PASSWORDS:
        print("\n❌ This is a very common password. It would be cracked instantly!")
        return

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Use at least 8 characters")

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("💡 12+ characters makes it much stronger")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter (A-Z)")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter (a-z)")

    # Number check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9)")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character (!@#$...)")

    # Result
    print("\n--- Password Strength Result ---")
    if score <= 2:
        print("Strength: WEAK 🔴")
    elif score <= 4:
        print("Strength: MODERATE 🟡")
    elif score == 5:
        print("Strength: STRONG 🟢")
    else:
        print("Strength: VERY STRONG 💪🟢")

    print(f"Score: {score}/6")

    if feedback:
        print("\nSuggestions to improve:")
        for tip in feedback:
            print(" ", tip)
    else:
        print("✅ Great password! No suggestions.")

# Main program
print("=== Password Strength Checker ===")
while True:
    pwd = input("\nEnter a password to check (or type 'exit' to quit): ")
    if pwd.lower() == 'exit':
        print("Goodbye!")
        break
    check_password_strength(pwd)
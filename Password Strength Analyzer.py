import re
from termcolor import colored 

def evaluate_password_strength(password):
    strength_score = 0
    
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special_char": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }
    
    for key, met in criteria.items():
        if met:
            strength_score += 1
    
    feedback = []
    if strength_score == 5:
        feedback.append(colored("Your password is strong.", "green"))
    elif 3 <= strength_score < 5:
        feedback.append(colored("Your password is moderate.", "yellow"))
        feedback.append(colored("Suggestions to improve password strength:", "yellow"))
    else:
        feedback.append(colored("Your password is weak.", "red"))
        feedback.append(colored("Suggestions to improve password strength:", "red"))
    
    if not criteria["length"]:
        feedback.append("- Password should be at least 8 characters long.")
    if not criteria["uppercase"]:
        feedback.append("- Include at least one uppercase letter (A-Z).")
    if not criteria["lowercase"]:
        feedback.append("- Include at least one lowercase letter (a-z).")
    if not criteria["digit"]:
        feedback.append("- Include at least one number (0-9).")
    if not criteria["special_char"]:
        feedback.append("- Include at least one special character (!@#$%^&*(), etc.).")
    
    return feedback, strength_score

def main():
    print("Password Strength Checker Tool")
    
    while True:
        password = input("\nEnter a password to check its strength (or 'q' to quit): ")
        if password.lower() == 'q':
            print("Exiting the tool.")
            break
        
        feedback, score = evaluate_password_strength(password)
        
        print("\nPassword Strength Feedback:")
        for line in feedback:
            print(line)
        
        print(colored(f"\nStrength Score: {score}/5\n", "cyan"))

if __name__ == "__main__":
    main()

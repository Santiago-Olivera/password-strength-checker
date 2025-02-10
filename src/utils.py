import re

def evaluate_password(password):
    """Evaluates password strength based on length, uppercase, lowercase, numbers, and special characters."""
    criteria = {
        "length": len(password) >= 12,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "numbers": bool(re.search(r"\d", password)),
        "special_chars": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }
    
    score = sum(criteria.values())  # Count the number of criteria met
    return score, criteria  # Return both the score and which criteria passed

def is_common_password(password):
    """Checks if the password is in a common passwords list."""
    common_passwords = {
        "123456", "password", "123456789", "12345", "12345678", "qwerty", "abc123", "password1",
        "1234567", "iloveyou", "admin", "welcome", "monkey", "123123", "sunshine", "football",
        "letmein", "access", "shadow", "master", "696969", "superman", "987654321", "qazwsx",
        "michael", "qwertyuiop", "1qaz2wsx", "trustno1", "123qwe", "dragon", "baseball",
        "jennifer", "hunter", "freedom", "password123", "secret", "whatever", "mustang",
        "buster", "soccer", "charlie", "qwerty123", "monkey123", "batman", "thomas", "jordan",
        "harley", "ranger", "tigger", "maggie", "pokemon", "liverpool", "starwars", "nintendo"
    }
    return password in common_passwords


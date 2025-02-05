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

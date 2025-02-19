import re
import hashlib
import requests
import math
import string

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

def check_password_breach(password):
    """Checks if the password has been exposed in data breaches using Have I Been Pwned API."""
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        return "Error: Could not check password breach status."

    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return f"⚠️ Your password has been leaked **{count} times**! Consider using a different one."

    return "✅ Your password has not been found in breaches."

def calculate_entropy(password):
    """Calculates password entropy based on its length and character diversity."""
    if not password:
        return 0, "⚠️ Password is empty."

    charset_size = 0
    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(c in string.punctuation for c in password):
        charset_size += len(string.punctuation)

    entropy = len(password) * math.log2(charset_size)

    # Provide feedback
    if entropy < 28:
        strength = "❌ Very Weak (Easy to crack)"
    elif entropy < 36:
        strength = "⚠️ Weak (Crackable in seconds)"
    elif entropy < 60:
        strength = "🔸 Moderate (Better, but still risky)"
    elif entropy < 80:
        strength = "✅ Strong (Difficult to crack)"
    else:
        strength = "💪 Very Strong (Highly secure)"

    return round(entropy, 2), strength

def provide_password_feedback(password):
    """Provides detailed feedback on how to improve password security."""
    feedback = []
    
    if len(password) < 12:
        feedback.append("🔹 Consider using **at least 12 characters** for better security.")
    if not any(c.isupper() for c in password):
        feedback.append("🔹 Add **uppercase letters** to strengthen your password.")
    if not any(c.islower() for c in password):
        feedback.append("🔹 Include **lowercase letters** for a more diverse character set.")
    if not any(c.isdigit() for c in password):
        feedback.append("🔹 Use **numbers** to increase complexity.")
    if not any(c in string.punctuation for c in password):
        feedback.append("🔹 Add **special characters** (e.g., @, #, $) to make it harder to guess.")
    if is_common_password(password):
        feedback.append("🚨 Avoid using **common passwords** that attackers can easily guess.")
    if "leaked" in check_password_breach(password):
        feedback.append("⚠️ This password has been found in breaches! **Change it immediately.**")
    
    if not feedback:
        return "✅ Your password meets **all** recommended security criteria!"
    return feedback

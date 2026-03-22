import math
import string


def calculate_entropy(password):
    pool_size = 0

    if any(c in string.ascii_lowercase for c in password):
        pool_size += 26
    if any(c in string.ascii_uppercase for c in password):
        pool_size += 26
    if any(c in string.digits for c in password):
        pool_size += 10
    if any(c in string.punctuation for c in password):
        pool_size += 32

    if pool_size == 0:
        return 0

    entropy = math.log2(pool_size) * len(password)
    return round(entropy, 2)


def score_password(password):
    entropy = calculate_entropy(password)
    length = len(password)
    reasons = []

    if length < 8:
        reasons.append("too short (minimum 8 characters)")
    if not any(c in string.ascii_uppercase for c in password):
        reasons.append("no uppercase letters")
    if not any(c in string.digits for c in password):
        reasons.append("no digits")
    if not any(c in string.punctuation for c in password):
        reasons.append("no symbols")

    if entropy < 28:
        rating = "Weak"
    elif entropy < 36:
        rating = "Fair"
    elif entropy < 60:
        rating = "Strong"
    else:
        rating = "Very Strong"

    return {
        "rating": rating,
        "entropy": entropy,
        "reasons": reasons
    }
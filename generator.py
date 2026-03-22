import random
import string


def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    pool = ""

    if use_upper:
        pool += string.ascii_uppercase
    if use_lower:
        pool += string.ascii_lowercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation

    if not pool:
        raise ValueError("At least one character set must be selected.")

    password = "".join(random.choice(pool) for _ in range(length))
    return password
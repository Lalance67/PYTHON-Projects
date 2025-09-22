password = "Password123"
condition = [
    len(password) >= 8,
    any(c.isdigit() for c in password),
    any(c.isupper() for c in password),
]
print("valid password" if all(condition) else "invalid password")
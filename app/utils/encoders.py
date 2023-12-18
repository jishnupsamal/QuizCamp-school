from argon2 import PasswordHasher
import logging as log
from .validators import password

def hash_password(password1):
    ph = PasswordHasher()
    if password(password1):
        hash = ph.hash(password1)
        return hash
    else:
        return None
        
from argon2 import PasswordHasher
from database.get import fetchoneuser, fetchall

def login(cur, email, password):
    role_options = {}
    for role in fetchall(cur, '*', 'ROLES'):
        role_options[role[0]] = role[1]

    ph = PasswordHasher()
    user = fetchoneuser(cur, email)
    user = {
        'ID': user[0],
        'first_name': user[1],
        'last_name': user[2],
        'email': user[3],
        'password': user[4],
        'role': role_options[user[5]]
    }
    pass_correct = ph.verify(user['password'], password)
    return user, pass_correct
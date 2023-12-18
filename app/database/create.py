from utils.validators import email, required_input
from .get import fetchall
from utils.encoders import hash_password

def add_roles(cur):
    roles = fetchall(cur, '*', 'ROLES')
    comm = "INSERT INTO ROLES (TITLE) VALUES (%s)"
    
    if roles == ():
        print('Adding Roles')
        cur.executemany(comm, [('Quizmaster'), ('Quizzer')])

def add_user(cur):
    first_name = required_input('First Name')
    last_name = input('Last Name: ') or None
    email1 = email(required_input('Email'))
    password = hash_password(required_input('Password'))
    role_options = {}
    for role in fetchall(cur, '*', 'ROLES'):
        role_options[role[0]] = role[1]
        print('{}. {}'.format(role[0], role[1]))
    role = int(required_input('Role'))
    
    comm = 'INSERT INTO USERS(FIRST_NAME, LAST_NAME, EMAIL, PASSWORD, ROLE) VALUES (%s, %s, %s, %s, %s)'
    
    print('Creating your {} account'.format(role_options[role]))
    cur.execute(comm, (first_name, last_name, email1, password, role))
    
def add_quiz(cur, user):
    title = required_input('First Name')
    comm = 'INSERT INTO QUIZZES(TITLE, DATE_CREATED, CREATED_BY) VALUES (%s, %s, %s)'
    if user.role == 'Quizmaster':
        cur.execute(comm, (title, 'CURDATE()', user.ID))
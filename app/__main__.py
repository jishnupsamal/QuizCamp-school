import logging as log
import pickle
from database import create_tables, connect, create_db
from database.create import add_roles, add_user
from utils.validators import required_input
from auth import login
from quizmaster import quizmaster
from quizzer import quizzer

log.basicConfig(filename="debug.log", level=log.DEBUG)

con = connect()
cur = create_db(con)
create_tables(cur)

add_roles(cur)

try:
    with open('user.dat', 'rb') as f:
        user = pickle.load(f)
except:
    user = None
        
    
c = 'y'

while c in 'yY':
    print('''
1. Register
2. Login
3. Profile
4. Go to App
5. Logout
    ''')
    option = int(required_input('Option'))
    
    if option == 1:
        print('Register', '-'*50, sep='\n')
        if user is None:
            add_user(cur)
        else:
            print("You're already logged in.")
    elif option == 2:
        print('Login', '-'*50, sep='\n')
        if user is None:
            email = required_input('Email')
            password = required_input('Password')
            user, verified = login(cur, email, password)
            if verified:
                with open('user.dat', 'wb') as f:
                    pickle.dump(user, f)
                print('Welcome, {}'.format(user['first_name']))
            else:
                raise Exception('Either username or password is wrong.')
        else:
            print('You\'re already logged in.')
    
    elif option == 3:
        print('Profile', '-'*50, sep='\n')
        if user is None:
            print("You're not logged in.")
        else:
            for k, v in user.items():
                if k == 'password':
                    continue
                print('{}: {}'.format(k, v))
    elif option == 4:
        if user is not None:
            if user['role'] == 'Quizmaster':
                quizmaster(cur, user)
            elif user['role'] == 'Quizzer':
                quizzer(cur)
        else:
            print("You're not logged in.")
    elif option == 5:
        print('Logout', '-'*50, sep='\n')
        if user is None:
            print("You're not logged in.")
        else:
            user = None
            with open('user.dat', 'wb') as f:
                f.truncate(0)
    else:
        print('Invalid Option')
    c = required_input('Do you want to continue? [y/n]')

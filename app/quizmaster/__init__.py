from utils.validators import required_input
from .create_quiz import add_quiz
from database.get import fetchallquizzes
from tabulate import tabulate

def quizmaster(cur, user):
    c = 'y'

    while c in 'yY':
        print('''
    1. Create New Quiz
    2. My Quizzes
    3. Back
        ''')
        
        option = int(required_input('Option'))
        
        if option == 1:
            print('Create New Quiz', '-'*50, sep='\n')
            add_quiz(cur, user)
            
        elif option == 2:
            print('My Quizzes', '-'*50, sep='\n')
            myquizzes = fetchallquizzes(cur, user['ID'])
            head = ['ID', 'Title', 'Date']
            print(tabulate(myquizzes, headers=head, tablefmt="grid"))
        
        elif option == 3:
            break
        
        else:
            print('Invalid Option')
        c = required_input('Do you want to continue? [y/n]')
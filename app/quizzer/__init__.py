from utils.validators import required_input
from database.get import fetchall_quizzes
from tabulate import tabulate
from .attempt import attempt_quiz

def quizzer(cur, user):
    c = 'y'

    while c in 'yY':
        print('''
    1. Attempt Quiz
    2. Back
        ''')
        
        option = int(required_input('Option'))
        
        if option == 1:
            print('Attempt Quiz', '-'*50, sep='\n')
            quizzes = fetchall_quizzes(cur)
            head = ['ID', 'Title', 'Date']
            print(tabulate(quizzes, headers=head, tablefmt="grid"))
            attempt_quiz(cur)
            
        
        elif option == 2:
            break
        
        else:
            print('Invalid Option')
        c = required_input('Do you want to continue? [y/n]')
from utils.validators import required_input
from database.get import fetchallquizzes
from tabulate import tabulate

def quizmaster(cur, user):
    c = 'y'

    while c in 'yY':
        print('''
    1. Attempt Quiz
    3. Back
        ''')
        
        option = int(required_input('Option'))
        
        if option == 1:
            print('Attempt Quiz', '-'*50, sep='\n')
        
        elif option == 3:
            break
        
        else:
            print('Invalid Option')
        c = required_input('Do you want to exit \'Quizcamp\'? [y/n]')
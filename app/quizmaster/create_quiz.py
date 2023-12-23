from datetime import datetime
import re
from utils.validators import required_input, option_validator
from database.get import fetchall, fetchonequiz

def add_quiz(cur, user):
    title = required_input('Title')
    curdate = datetime.now().strftime("%Y-%m-%d")
    comm = 'INSERT INTO QUIZZES(TITLE, DATE_CREATED, CREATED_BY) VALUES (%s, %s, %s)'
    cur.execute(comm, (title, curdate , user["ID"]))
    
    add_questions(cur, title)
    
def add_question(cur, title):
    quiz = fetchonequiz(cur, title)
    question = required_input('Question')
    print('Add options:-')
    options = []
    i = 1
    while True:
        option = input(f"Option {i} : ")
        if option == '':
            break
        else:
            options.append(option_validator(options, option))
        i += 1
    for j in options:
        print("{}. {}".format(options.index(j)+1, j))
    correct = int(required_input('Correct Option: ')) - 1
    return [quiz[0], question, str(options), correct]
    
def add_questions(cur, title):
    c = 'y'
    questions = []
    
    while c in 'yY':
        question = add_question(cur, title)
        questions.append(question)
        c = required_input('Do you want to add more questions? [y/n]')
    
    print(questions)
    comm = 'INSERT INTO QUESTIONS(QUIZ, QUESTION, CHOICES, CORRECT_CHOICE) VALUES (%s, %s, %s, %s)'
    cur.executemany(comm, questions)
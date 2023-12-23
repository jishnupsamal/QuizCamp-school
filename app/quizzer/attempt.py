from utils.validators import required_input
from database.get import fetchquestionsbyquizid

def attempt_quiz(cur):
    quiz = int(required_input('Enter ID of the quiz you want to attempt'))
    questions = fetchquestionsbyquizid(cur, quiz)
    questions_dict = dict(list(zip(range(len(questions)+1), questions)))
    marks = len(questions_dict)
    score = 0
    for sno, question in questions_dict.items():
        print("{}. {}".format(sno+1, question[0]))
        options = dict(zip(range(len(eval(question[1]))), eval(question[1])))
        for option in options:
            print("    {}. {}".format(chr(65+option), options[option]))
        choice = required_input('Your Choice')
        try:
            if question[2] == (ord(choice) - 65):
                print("✔ Well done.")
                score += 1
            else:
                print("❌ Oops, better luck next time.")
        except:
            print("Invalid option!!")
    
    print('Your Score: {}/{}'.format(score, marks))
    
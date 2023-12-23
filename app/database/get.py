

def fetchall(cur, columns, table):
    cur.execute("SELECT {} FROM {}".format(columns, table))
    res = cur.fetchall()
    return res

def fetchoneuser(cur, field):
    comm = "SELECT * FROM USERS WHERE email = %s"
    cur.execute(comm, (field))
    res = cur.fetchone()
    return res

def fetchonequiz(cur, title):
    comm = "SELECT * FROM QUIZZES WHERE TITLE = %s"
    cur.execute(comm, (title))
    res = cur.fetchone()
    return res

def fetchallquizzes(cur, ID):
    comm = "SELECT ID, TITLE, DATE_CREATED FROM QUIZZES WHERE CREATED_BY = %s ORDER BY ID DESC"
    cur.execute(comm, (ID))
    res = cur.fetchall()
    return res

def fetchall_quizzes(cur):
    comm = "SELECT ID, TITLE, DATE_CREATED FROM QUIZZES"
    cur.execute(comm)
    res = cur.fetchall()
    return res

def fetchquestionsbyquizid(cur, quiz):
    comm = "SELECT QUESTION, CHOICES, CORRECT_CHOICE FROM QUESTIONS WHERE QUIZ = %s ORDER BY ID ASC"
    cur.execute(comm, (quiz))
    res = cur.fetchall()
    return res
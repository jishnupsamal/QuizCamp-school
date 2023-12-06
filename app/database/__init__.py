import pymysql as sql

def connect(password: str = "12345678"):
    try:
        con = sql.connect(
            host="localhost",
            port=3306,
            user="root",
            password=password,
        )
        return True, con
    except:
        raise ConnectionRefusedError("Failed to connect")


def create_db():
    isCon, con = connect()
    db = 'quizcamp'
    if isCon:
        cur = con.cursor()
        cur.execute('SHOW DATABASES')
        dbs = [db[0] for db in cur.fetchall()]
    
    if db not in dbs:
        try:
            cur.execute('CREATE DATABASE quizcamp')
            return cur
        except:
            raise Exception('Failed to create DB')
    else:
        return cur
    
def create_tables():
    cur = create_db()
    cur.execute('USE QUIZCAMP')
    cur.execute('SHOW TABLES')
    tables = [table[0] for table in cur.fetchall()]
    
    #### Users Table
    if 'users' not in tables:
        try:
            cur.execute('''CREATE TABLE USERS (
                ID INT(10) NOT NULL AUTO_INCREMENT, 
                FIRST_NAME VARCHAR(50) NOT NULL,
                LAST_NAME VARCHAR(50),
                EMAIL VARCHAR(100) NOT NULL UNIQUE,
                PASSWORD VARCHAR(30) NOT NULL,
                ROLE VARCHAR(50) NOT NULL,
                PRIMARY KEY(ID)
                )''')
        except:
            raise Exception('Failed to create table Quizzes')
    else:
        print('Table Users exists')
    
    #### Quizzes Table
    if 'quizzes' not in tables:
        try:
            cur.execute('''CREATE TABLE Quizzes (
                ID INT(10) NOT NULL AUTO_INCREMENT, 
                TITLE VARCHAR(50) NOT NULL,
                DATE_CREATED DATE NOT NULL,
                CREATED_BY INT NOT NULL,
                PRIMARY KEY(ID),
                FOREIGN KEY(CREATED_BY) REFERENCES USERS(ID)
                )''')
        except:
            raise Exception('Failed to create table Quizzes')
    else:
        print('Table Quizzes exists')
    
    #### Questions Table
    if 'questions' not in tables:
        try:
            cur.execute('''CREATE TABLE Questions (
                ID INT(10) NOT NULL AUTO_INCREMENT, 
                QUIZ INT NOT NULL,
                QUESTION VARCHAR(50) NOT NULL,
                DATE_CREATED DATE NOT NULL,
                PRIMARY KEY(ID),
                FOREIGN KEY(QUIZ) REFERENCES QUIZZES(ID)
                )''')
        except:
            raise Exception('Failed to create table Questions')
    else:
        print('Table Questions exists')
    
    return 'Success'

# CREATE TABLE Quizzes (
# ID INT(10) NOT NULL AUTO_INCREMENT, 
# TITLE VARCHAR(50) NOT NULL,
# DATE_CREATED DATE NOT NULL,
# CREATED_BY INT NOT NULL,
# PRIMARY KEY(ID),
# FOREIGN KEY(CREATED_BY) REFERENCES USERS(ID),
# )
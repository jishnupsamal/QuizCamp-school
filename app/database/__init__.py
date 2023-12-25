import logging as log
import pymysql as sql

def connect(password: str = "12345678"):
    try:
        con = sql.connect(
            host="localhost",
            port=3306,
            user="root",
            password=password,
            autocommit=True,
        )
        return True, con
    except:
        log.error('Failed to connect')
        raise ConnectionRefusedError("Failed to connect")


def create_db(connect):
    isCon, con = connect
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
            log.error('Failed to create DB')
            raise Exception('Failed to create DB')
    else:
        return cur
    
def create_tables(cur):
    cur.execute('USE QUIZCAMP')
    cur.execute('SHOW TABLES')
    tables = [table[0] for table in cur.fetchall()]
    
    if 'roles' not in tables:
        try:
            cur.execute('''CREATE TABLE ROLES (
                ID INT(10) NOT NULL AUTO_INCREMENT, 
                TITLE VARCHAR(50) NOT NULL,
                PRIMARY KEY(ID)
                )''')
        except:
            log.error('Failed to create table Roles')
            raise Exception('Failed to create table Roles')
    else:
        log.info('Table Roles exists')
    
    #### Users Table
    if 'users' not in tables:
        try:
            cur.execute('''CREATE TABLE USERS (
                ID INT(10) NOT NULL AUTO_INCREMENT, 
                FIRST_NAME VARCHAR(50) NOT NULL,
                LAST_NAME VARCHAR(50),
                EMAIL VARCHAR(100) NOT NULL UNIQUE,
                PASSWORD VARCHAR(100) NOT NULL,
                ROLE INT NOT NULL,
                FOREIGN KEY(ROLE) REFERENCES ROLES(ID),
                PRIMARY KEY(ID)
                )''')
        except:
            log.error('Failed to create table Quizzes')
            raise Exception('Failed to create table Quizzes')
    else:
        log.info('Table Users exists')
    
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
            log.error('Failed to create table Quizzes')
            raise Exception('Failed to create table Quizzes')
    else:
        log.info('Table Quizzes exists')
    
    #### Questions Table
    if 'questions' not in tables:
        try:
            cur.execute('''CREATE TABLE Questions (
                ID INT(10) NOT NULL AUTO_INCREMENT, 
                QUIZ INT NOT NULL,
                QUESTION TEXT NOT NULL,
                CHOICES VARCHAR(100) NOT NULL,
                CORRECT_CHOICE INT(11) NOT NULL,
                PRIMARY KEY(ID),
                FOREIGN KEY(QUIZ) REFERENCES QUIZZES(ID)
                )''')
        except:
            log.error('Failed to create table Questions')
            raise Exception('Failed to create table Questions')
    else:
        log.info('Table Questions exists')
    
    return 'Success'

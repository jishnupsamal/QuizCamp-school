

def fetchall(cur, columns, table):
    cur.execute("SELECT {} FROM {}".format(columns, table))
    res = cur.fetchall()
    return res

def fetchoneuser(cur, field):
    comm = "SELECT * FROM USERS WHERE email = %s"
    cur.execute(comm, (field))
    res = cur.fetchone()
    return res
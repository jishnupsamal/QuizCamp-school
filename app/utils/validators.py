import logging as log

def required_input(field: str):
    val = input('{} * : '.format(field))
    if val == '' or val == None:
        raise Exception('Input is required.')
    else:
        return val
    

def email(email: str) -> bool:
    comp = email.partition('@')
    if comp[0] != '' and comp[1] != '' and comp[2] != '':
        return email
    else:
        log.error('Email validation failed.')
        raise Exception('Email validation failed.')

def password(password: str) -> bool:
    if len(password) > 8:
        return True
    else:
        log.error('Password validation failed.')
        raise Exception('Password validation failed.')
    
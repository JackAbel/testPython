#! /usr/bin/env python

import time

db = {}


def newuser():
    prompt = 'login desired by ignore case: '
    while True:
        name = raw_input(prompt).lower()
        if name in db.keys():
            prompt = 'name taken, try again'
        elif name.isalnum() and ' ' not in name:
            break
        else:
            prompt = 'name has character or space, try again'
    pwd = raw_input('passwd:')
    timestamp_login = time.mktime(time.localtime())
    db[name] = [pwd, timestamp_login]


def olduser():
    name = raw_input('login:').lower()
    pwd = raw_input('passwd:')
    passwd = db[name][0]
    timestamp_login = time.mktime(time.localtime())
    while name in db.keys():
        if passwd == pwd:
            if timestamp_login - db.get(name)[1] <= 14400:
                print 'You already logged in at: %s' % time.ctime(db.get(name)[1])
                break
            else:
                print 'Welcome you back!'
                break
        else:
            print 'pwd is error'
            break
    while name not in db.keys():
        answer = raw_input('Are you new user?')
        if answer.upper() == 'Y' and not name.isalnum() and ' ' not in name:
            db[name] = [pwd, timestamp_login]
            break
        else:
            print 'You user name is mistake, Please correct'
            olduser()
            break


def deluser():
    name =raw_input('username: ')
    del db[name]


def showusers():
    for keys in db.keys():
        print keys, db[keys][0]


def showmenu():
    prompt = """
    (N)ew User Login
    (E)xisting User Login
    (D)el User
    (S)how Users
    (Q)uit
    Enter choice: """
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
            if choice not in 'nedsq':
                print 'invalid optionm try again'
            else:
                chosen = True
        if choice == 'q':
            done = True
        if choice == 'n':
            newuser()
        if choice == 'e':
            olduser()
        if choice == 'd':
            deluser()
        if choice == 's':
            showusers()

if __name__ == '__main__':
    showmenu()





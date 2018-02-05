#! /usr/bin/env python

queue = []


def pushit():
    queue.append(raw_input('Enter a string;').strip())


def popit():
    if len(queue) == 0:
        print 'cannot pop it from empty queue'
    else:
        print 'Removed [', `queue.pop(-1)`, ']'


def viewqueue():
    print queue

CMDs = {'u': pushit, 'o': popit, 'v': viewqueue}


def showmenu():
    pr = """
    p(U)sh
    p(O)p
    (V)iew
    (Q)uit

    Enter choice:"""

    while True:
        while True:
            try:
                choice = raw_input(pr).strip().lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
            if choice not in 'uovq':
                print 'Invalid options: try again'
            else:
                break

        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    showmenu()

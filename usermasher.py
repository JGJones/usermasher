#!/usr/bin/env python3
import argparse


def command_args():
    # get args (ie username text file and display help text)
    parser = argparse.ArgumentParser(description='Take a text file of names as input to generate potential usernames')
    parser.add_argument('-d', '--domain', help='include a domain for an email style username like johndoe@domain.com',default='')
    parser.add_argument('filename', help='text list with list of names')
    return parser.parse_args()


def selectmash():
    '''
    Provide a list of username format using a userfriendly curses based menu
    make use of the pick module (from https://github.com/wong2/pick)
    '''
    from pick import pick
    title = 'Please choose your username format: '
    options = ['john.doe', 'johndoe', 'j.doe', 'jdoe', 'john', 'johnd', 'doe.john', 'doejohn', 'doe.j', 'doej',
               'd.john', 'djohn', 'doe', 'all format']
    selected = pick(options, title, multiselect=False)
    return selected


def mash(namelist,domain, mashtype):
    mashed = []
    for line in open(namelist):
        name = ''.join([c for c in line if c == ' ' or c.isalpha()])

        tokens = name.lower().split()
        fname = tokens[0]
        lname = tokens[-1]

        if mashtype == 0:  # john.doe
            mashed += [fname + '.' + lname]
        elif mashtype == 1:  # johndoe
            mashed += [fname + lname]
        elif mashtype == 2:  # j.doe
            mashed += [fname[0] + '.' + lname]
        elif mashtype == 3:  # jdoe
            mashed += [fname[0] + lname]
        elif mashtype == 4:  # john
            mashed += [fname]
        elif mashtype == 5:  # johnd
            mashed += [fname + lname[0]]
        elif mashtype == 6:  # doe.john
            mashed += [lname + '.' + fname]
        elif mashtype == 7:  # doejohn
            mashed += [lname + fname]
        elif mashtype == 8:  # doe.j
            mashed += [lname + '.' + fname[0]]
        elif mashtype == 9:  # doej
            mashed += [lname + fname[0]]
        elif mashtype == 10:  # d.john
            mashed += [lname[0] + '.' + fname]
        elif mashtype == 11:  # djohn
            mashed += [lname[0] + fname]
        elif mashtype == 12:  # doe
            mashed += [lname]
        elif mashtype == 13:  # all formats
            mashed += [fname + '.' + lname]
            mashed += [fname + lname]
            mashed += [fname[0] + '.' + lname]
            mashed += [fname[0] + lname]
            mashed += [fname]
            mashed += [fname + lname[0]]
            mashed += [lname + '.' + fname]
            mashed += [lname + fname]
            mashed += [lname + '.' + fname[0]]
            mashed += [lname + fname[0]]
            mashed += [lname[0] + '.' + fname]
            mashed += [lname[0] + fname]
            mashed += [lname]
        else:
            print(mashtype)

        if domain:
            domain = '@' + domain
            for i in mashed:
                print(i + domain)
        else:
            for i in mashed:
                print(i)


def main():
    # Get the args
    args = command_args()
    mashtype = selectmash()
    mash(args.filename,args.domain, mashtype[1])


main()

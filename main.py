#!/usr/bin/python
# -*- coding: utf-8 -*-
#; Copyright 2016 <Benne>
#; https://github.com/Ro0x2A/
#; Creation date [11.06.2016]

from Mailer  import Mailer
from getpass import getpass

def prompt(text, default):
    m = input(text + ' [' + default + ']: ')
    if (m == ''):
        return default
    else:
        return m

def main():
    server   = prompt('Enter server', 'klimlive.de')
    port     = int(prompt('Enter port', '587'))
    user     = input("Account: ")
    pwd      = getpass("Password: ")
    fromaddr = user
    toaddr   = input("Mail to: ")
    title    = input("Title: ")
    MyMail = Mailer(server, port, user, pwd)
    MyMail.head(toaddr, fromaddr, title)

    print ('To send double press >> Enter')

    while True:
        try:
            line = input()
        except EOFError:
            break
        if not line:
            break
        MyMail.message(line)

    print ('Message length is ' + str(len(line)))

    MyMail.connect()
    if (MyMail.send()):
        print ("Success!")
    else :
        print ("Failed!")

    del MyMail

if __name__ == "__main__":
    try:
        input = raw_input
    except NameError:
        pass

    main()

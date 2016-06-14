#!/usr/bin/python
# -*- coding: utf-8 -*-
#; Copyright 2016 <Benne>
#; https://github.com/Ro0x2A/
#; Creation date [11.06.2016]

import smtplib

class Mailer(object):
    def __init__(self, server, port, usr, pwd='', debug=False):
        self.smtp     = None
        self.server   = server
        self.port     = int(port)
        self.usr      = usr
        self.pwd      = pwd
        self.debug    = debug
        self.header   = ""
        self.msg      = ""
        self.fromaddr = ""
        self.toaddr   = ""

    def connect(self):
        self.smtp = smtplib.SMTP(self.server, self.port)
        self.smtp.ehlo()
        self.smtp.starttls()
        self.smtp.ehlo
        self.smtp.set_debuglevel(self.debug)
        self.smtp.login(self.usr, self.pwd)

    def send(self):
        if (self.toaddr == ""):
            return False
        self.smtp.sendmail(self.fromaddr, self.toaddr,self.header + self.msg)
        return True

    def head(self, toaddr, fromaddr, title):
        self.header = ('To:' + toaddr + '\n' + 'From: '
                   + fromaddr + '\n' + 'Subject: ' + title + '\n')
        self.fromaddr = fromaddr
        self.toaddr   = toaddr

    def message(self, msg):
        self.msg = msg

    def __del__(self):
        if (self.smtp):
            self.smtp.quit()

if __name__ == "__main__":
    exit()

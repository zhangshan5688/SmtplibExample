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

    def connect(self):
        self.smtp = smtplib.SMTP(self.server, self.port)
        self.smtp.ehlo()
        self.smtp.starttls()
        self.smtp.ehlo
        self.smtp.set_debuglevel(self.debug)
        self.smtp.login(self.usr, self.pwd)

    def send(self, fromaddr, toaddr, msg):
        self.smtp.sendmail(fromaddr, toaddr, msg)

    def __del__(self):
        if (self.smtp):
            self.smtp.quit()

if __name__ == "__main__":
    exit()

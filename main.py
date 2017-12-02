#!/bin/python
import smtplib

class mailbomb():
    print("You may need to enable 'Access for less secure apps' option in your Google account security section.")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    email = input("Enter your gmail login: ")
    password = input("Enter your gmail password: ")
    targets = open(input("Targets list (.txt): "))
    targets = targets.read().splitlines()
    email_txt = open(input("E-Mail' s message path (.txt): "))
    email_txt = email_txt.read()

    def login(self, login, password):
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login(login, password)

    def send(self, target, msg):
        for x in target:
            self.server.sendmail(self.email, x, msg)
            print("E-Mail sended to %s" % x)

mailbomb.login(mailbomb, mailbomb.email, mailbomb.password)
mailbomb.send(mailbomb, mailbomb.targets, mailbomb.email_txt)

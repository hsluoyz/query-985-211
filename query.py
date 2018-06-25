# coding=utf8

import re

list_985 = set()
list_211 = set()
input = []


def read_985():
    file = open("data/985.txt")
    while 1:
        line = file.readline()
        if len(line) > 0:
            list_985.add(line.strip("\n"))
        if not line:
            break
    file.close()

    print "************************************************************"
    print "985:"
    for s in list_985:
        print s
    print "************************************************************"


def read_211():
    file = open("data/211.txt")
    while 1:
        line = file.readline()
        if len(line) > 0:
            s = line.strip("\n")
            s = re.sub("\(.*\)", '', s)
            list_211.add(s)
        if not line:
            break
    file.close()

    print "************************************************************"
    print "211:"
    for s in list_211:
        print s
    print "************************************************************"


def read_input():
    file = open("input.txt")
    while 1:
        line = file.readline()
        if len(line) > 0:
            s = line.strip("\n")
            s = re.sub("\(.*\)", '', s)
            input.append(s)
        if not line:
            break
    file.close()

    print "************************************************************"
    print "input:"
    for s in input:
        print s
    print "************************************************************"


def calculate():
    for s in input:
        if s in list_985:
            print "985"
        elif s in list_211:
            print "211"
        else:
            print ""


read_985()
read_211()
read_input()

print "************************************************************"
print "output:"
calculate()
print "************************************************************"


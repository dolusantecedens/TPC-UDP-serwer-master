import argparsei
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

def execute(cmd):
    cmd=cmd.strip()
    if not cmd:
        return
    output=subprocess.check_output(shlex.split(cmd),
                                    strerr=subprocess.STDOUT)
    return output.decode() 
if __name__=='__main__':
    parser = agrprase.ArgumentParser(
        description='bhp tool',
        formatter_class=argprase.RawDescriptionHelpFormatter,
        epilog=textwrap.decent('''example:
        netcat.py -t 192.168.1.108 -p 5555 -l -c # powloka systemu)
        netcat.py -t 192.168.1.108 -p 5555 -l -u-mytest.whatisup
        netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\"

        echo 'ABCDEFGHI' | ./netcat.py -t 192.168.1.108 -p 135 

        netcat.py -y 192.168.1.108 -p 5555 
        '''))
    parser.add_argument('-c' '--comand', action='store_true',help='otwarcie powloki')
    parser.add_argument()
    parser.add_argument
    parser.add_argument
    parser.add_argument
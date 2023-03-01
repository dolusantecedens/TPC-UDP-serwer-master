import argparse
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
    parser = argparse.ArgumentParser(
        description='bhp tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''example:
        netcat.py -t 192.168.1.108 -p 5555 -l -c 
        netcat.py -t 192.168.1.108 -p 5555 -l -u-mytest.whatisup
        netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\"

        echo 'ABCDEFGHI' | ./netcat.py -t 192.168.1.108 -p 135 

        netcat.py -y 192.168.1.108 -p 5555 
        '''))
    parser.add_argument('-c' '--comand', action='store_true',help='otwarcie powloki')
    parser.add_argument('-l' '--listen', action='store_true',help='nasluch')
    parser.add_argument('-p' '--port', type=int, default=5555,help='docelowy port')
    parser.add_argument('-t' '--target', default='192.168.1.203',help='docelowy')
    parser.add_argument('-u','--upload',help='zaladowanie pliku')
    args=parser.parse_args()
    if args.l_listen:
        buffer=''
    else:
        buffer=sys.stdin.read()
    nc=NetCat(args,buffer.encode('utf-8'))
    nc.run()
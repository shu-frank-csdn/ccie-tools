
HOST_IP = '192.168.159.11'
PORT_BASE = 2000
N = 42

PASSWORD = "cisco"

import pexpect


def get_running(n):    
    t = pexpect.spawn('telnet ' + HOST_IP + ' ' + str(PORT_BASE + i))

    t.sendline("\r\n\r\n\r\n")
    t.expect(">")
    t.sendline('enable')
    t.expect("Password:")
    t.sendline(PASSWORD)
    t.expect("#")
    #m =t.expect([">", "#"])
    #if m == 0:
    #    t.sendline('enable')
    #    t.expect("Password:")
    #    t.sendline(PASSWORD)
    t.sendline('term len 0')
    t.expect("#")
    t.sendline("show run")
    t.expect("#")
    data = t.before
    t.sendline("exit")
    print data

    hostname = data.split('\n')[-1]

    f = open(hostname + '.txt', "w")
    f.write(data)
    f.close()

for i in range(1, N+1):
#for i in range(31, N+1):
    get_running(i)


import threading
import time
import os

class myThread (threading.Thread):
    def __init__(self,ip):
        threading.Thread.__init__(self)
        self.ip = ip

    def run(self):        
        status = "Down"
        outx = None
        ipx = ip.strip()

        cmd = "ping -q -c3 %s" %(ipx)
        fp = os.popen(cmd)
        outx = fp.read()

        if outx.find(pattern) > -1 :
            status = "Up"

        cmd1 = "date +'%F %X'"    
        fp1 = os.popen(cmd1)
        outx1 = fp1.read()
        outx1 = outx1.strip()
        
        print("Host %s is %s" %(ipx, status))
        fd1.write("%s;%s;%s\n" %(outx1, ipx, status))    

fname = "ip.txt"
fd = open(fname)

fname1 = "status.csv"
fd1 = open(fname1, "a")

pattern = "3 received"

for ip in fd.readlines() :    
    thread = myThread(ip)
    thread.start()
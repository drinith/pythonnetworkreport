from threading import Thread
from os import system

class PingThread (Thread):
    def __init__(self,ip,host):
        Thread.__init__(self)
        self.ip = ip
        self.host=host
        
        
    def run(self):        
        self.processo()

    def processo(self):
        hostname = self.ip #example
        response = system("ping -c 1 " + hostname)

        #and then check the response...
        if response == 0:
            print (hostname, 'is up!')
            self.host.listHostUp.append(hostname)
        else:
            print (hostname, 'is down!')
            
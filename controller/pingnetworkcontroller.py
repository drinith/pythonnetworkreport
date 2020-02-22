from model.host import Host
from infra.pingthread import PingThread


class PingNetworkController():
    
    

    def __init__(self,ip,mask):
        self.host = Host(ip,mask)
    
#def testAliveRange(self,ip,mask):list

    def pingAllNetworkThreads(self):
        # Criando as threads
        threads = []
        #passa uma lista de ips compreendidos na rede do host
        for ip in self.host.listIpRange():
            thread = PingThread(ip,self.host)
            threads.append(thread)    
        
        # Comecando novas Threads
        for ip in threads:
            ip.start()

        
        for t in threads:
            t.join()
        
        for ip in self.host.listHostUp:
            print(f"Este host está ligado {ip} ")
        print("terminou")

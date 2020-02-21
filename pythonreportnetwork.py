import threading
 
class pingThread (threading.Thread):
    def __init__(self, ip, name):
        threading.Thread.__init__(self)
        self.ip = ip
        self.name = name
        
    def run(self):        
        self.processo(self.nome, self.ip)
 
    def processo(self,ip, name):
        print(self.ip+" "+self.name)


class pingNetwork():
    
    def __init__(self,host):
        self.host = host
        
    #def testAliveRange(self,ip,mask):list
    
    def findRangeNetwork(self,ip,mask):(int,int)


class host():

    def __init__(self,ip,mask):
        self.id = None
        self.ip = ip
        self.mask= mask
        self.nameReal = None
        self.ipSplit = self.splitIP(ip)
        self.maskSplit = self.splitIP(mask)
        self.network =([],[],[]) #(ipNetwork,ipSalto,ipBroadcast)
        self.findNetwork()
        
    def findNetwork(self):
        #calculos de rede
        ipNetWork=[]
        ipNetwork = [self.ipSplit[0]&self.maskSplit[0],self.ipSplit[1]&self.maskSplit[1],self.ipSplit[2]&self.maskSplit[2],self.ipSplit[3]&self.maskSplit[3]]
        ipSalto = [255-self.maskSplit[0],255-self.maskSplit[1],255-self.maskSplit[2],255-self.maskSplit[3]]
        ipBroadcast = [ipSalto[0]+ipNetwork[0],ipSalto[1]+ipNetwork[1],ipSalto[2]+ipNetwork[2],ipSalto[3]+ipNetwork[3]]
        self.network=(ipNetwork,ipSalto,ipBroadcast)
    def splitIP(self,num):
        listNum=[]
        for nume in num.split('.'):
            listNum.append(int(nume))

        return listNum

    def listIpRange(self):

        listaIp=[]
        lenA,lenB,lenC,lenD = self.network[1][0]+1,self.network[1][1]+1,self.network[1][2]+1,self.network[1][3]+1
        print(self.network[1][3])
        for a in range(lenA):
            
            for b in range(lenB):
                
                for c in range(lenC):
                    
                    for d in range(lenD):
                        listaIp.append(str(self.network[0][0]+a)+"."+str(self.network[0][1]+b)+"."+str(self.network[0][2]+c)+"."+str(self.network[0][3]+d))
          
       
        return listaIp


if __name__=="__main__":

    host1 = host("192.168.0.3","255.255.0.0")
    print(host1)
    print(host1.listIpRange())

    """
    # Criando as threads
    threads = []
    for i in range (255):
        thread = pingThread("192.168.0"+str(i), "Máquina "+str(i))
        threads.append(thread)    
    
    # Comecando novas Threads
    for ip in threads:
        ip.start()

    
    for t in threads:
        t.join()
    
    print ("Saindo da main")"""
class Host():

    listHostUp=[]
    
    def __init__(self,ip,mask):
        self.id = None
        self.ip = ip #ip formato de string
        self.mask= mask #ip formato de string
        self.nameReal = None
        self.ipSplit = self.splitIP(ip) #ip como lista
        self.maskSplit = self.splitIP(mask) #ip como lista
        self.network =([],[],[]) #(ipNetwork,ipSalto,ipBroadcast)
        self.findNetwork()
        
    #Encontra rede que o host está compreendido e retirna nome da rede, salto e broadcast
    def findNetwork(self):
        #calculos de rede
        ipNetWork=[]
        ipNetwork = [self.ipSplit[0]&self.maskSplit[0],self.ipSplit[1]&self.maskSplit[1],self.ipSplit[2]&self.maskSplit[2],self.ipSplit[3]&self.maskSplit[3]]
        ipSalto = [255-self.maskSplit[0],255-self.maskSplit[1],255-self.maskSplit[2],255-self.maskSplit[3]]
        ipBroadcast = [ipSalto[0]+ipNetwork[0],ipSalto[1]+ipNetwork[1],ipSalto[2]+ipNetwork[2],ipSalto[3]+ipNetwork[3]]
        self.network=(ipNetwork,ipSalto,ipBroadcast)
    #Transforma os ips como string em lista
    def splitIP(self,num):
        listNum=[]
        for nume in num.split('.'):
            listNum.append(int(nume))

        return listNum
    #lista todos os ips compreendidos no range
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
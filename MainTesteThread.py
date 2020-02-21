from pythonnetworkreport import Host,PingNetwork
 


if __name__=="__main__":

    host1 = Host("192.168.10.1","255.255.255.0")
        
    pNet = PingNetwork(host1)
    pNet.pingAllNetwork()
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
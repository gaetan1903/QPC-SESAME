import socket
import threading
import optparse
def scan(host,ports):
    try:
        ip=socket.gethostbyname(host);
    except Exceptione:
        print(str(e))
        exit(0)
    try:
        hostname= socket.gethostbyaddr(ip);
        print ("Resultats pour %s"%hostname)
    except:
        print ("Resultats pour %s"%ip)

    for port in ports:
        t=Thread(target=isPortOpen,args=(ip,int(port)));
        t.start()
def main():
    parser= optparse.OptionParser();
    parser.add_option("-p","--ports",dest="ports",default="42,23,22,21,12345",help="Ports a scanner",type="string")
    (options,args)=parser.parse_args();
    ports=options.ports.split(",");
    if(len(args)<1):
        print ("Il faut un hostname")
        exit(0);

    host=args[0];
    scan(host,ports);

if __name__=="__main__":
    main();

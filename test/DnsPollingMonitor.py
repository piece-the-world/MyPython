import dns.resolver
import httplib
iplist=[]
domain='www.baidu.com'
def get_iplist(domian=""):
    try:
        A=dns.resolver.query(domain,'A')
    except Exception,e:
        print "dns resolver error:"+str(e)
        return
    for i in A.response.answer:
        for j in i.items:
            try:
                iplist.append(j.address)
            except Exception as e:
                print e

    return True
def checkip(ip):
    checkurl=ip+":80"
    getcontent=""
    httplib.socket.setdefaulttimeout(50)
    conn=httplib.HTTPConnection(checkurl)
    try:
        conn.request("GET","/",headers={"Host":domain})
        r=conn.getresponse()
        getcontent=r.read(15)
    finally:
        if getcontent=="<!doctype html>":
            print ip+"[OK]"
        else:
            print ip+"[Error]"
if __name__=="__main__":
    if get_iplist(domain) and len(iplist)>0:
        for ip in iplist:
            checkip(ip)
    else:
        print "dns resolver error."
# @BEG@ 5 6 RPCProxy
# une troisi�me impl�mentation de RPCProxy

class Forwarder(object):
    """
    Une instance de la classe Forwarder est un callable
    qui peut �tre utilis�e comme une m�thode sur l
    class RPCProxy
    """
    def __init__(self, rpc_proxy, methodname):
        """
        le constructeur  m�morise l'instance de RPCProxy
        et le nom de la m�thode qui a �t� appel�e
        """
        self.methodname = methodname
        self.rpc_proxy = rpc_proxy

    def __call__(self, *args):
        """
        en rendant cet objet callable, on peut l'utiliser
        comme une m�thode de RPCProxy
        """
        print "Envoi � {}\nde la fonction {} -- args= {}".\
            format(self.rpc_proxy.url, self.methodname, args)
        return "retour de la fonction " + self.methodname

class RPCProxy(object):
    """
    Une troisi�me impl�mentation de RPCProxy qui sous-traite
    � une classe annexe `Forwarder` qui se comporte comme
    une *factory* de m�thodes
    """
    def __init__(self, url, login, password):
        self.url = url
        self.login = login
        self.password = password
        
    def __getattr__ (self, methodname):
        """
        Cr�e � la vol�e une instance de Forwarder
        correspondant � 'methodname'
        """
        return Forwarder(self, methodname)
# @END@

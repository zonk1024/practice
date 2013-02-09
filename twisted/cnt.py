#!/usr/bin/env python

from twisted.internet import reactor, protocol, endpoints

class CntProtocol(protocol.Protocol):

    def connectionMade(self):
        self.factory.cnt += 1
        self.transport.write('There are currently %d connections.\n' % self.factory.cnt)

    def connectionLost(self, reason):
        self.factory.cnt -= 1

    def dataReceived(self, data):
        self.transport.loseConnection()


class CntFactory(protocol.ServerFactory):

    cnt = 0
    protocol = CntProtocol


endpoints.serverFromString(reactor, "tcp:8090").listen(CntFactory())
reactor.run()

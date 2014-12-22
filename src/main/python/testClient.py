from isoblockprojector import IsoBlockProjectorService

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    transport = TSocket.TSocket('localhost',9090)
    transport = TTransport.TFramedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = IsoBlockProjectorService.Client(protocol)
    transport.open()
    print client.getVersion()
except Thrift.TException, tx:
    print '%s' % (tx.message)
